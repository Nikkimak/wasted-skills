#!/usr/bin/env python3
"""Start or resume a read-only Claude document-review session."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import uuid


PROFILE_FOCUS = {
    "prd": "business outcome, scenarios, scope, non-goals, assumptions, acceptance criteria, and unresolved product decisions",
    "implementation": "PRD fidelity, architecture and ownership, contracts, data/migrations, failure and recovery, security, and verification",
    "task-plan": "requirement coverage, vertical slices, bounded task scope, dependencies, routing, validation, merge targets, and parent acceptance",
    "security": "assets, actors, trust boundaries, authorization, secrets, external inputs, abuse cases, data lifecycle, recovery, and task-level mitigations",
}


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)

    for name in ("start", "resume"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--cwd", required=True, type=Path)
        cmd.add_argument("--profile", required=True, choices=sorted(PROFILE_FOCUS))
        cmd.add_argument("--artifact", action="append", required=True, type=Path)
        cmd.add_argument("--context", action="append", default=[], type=Path)
        cmd.add_argument("--model", default="claude-opus-4-8")
        cmd.add_argument("--effort", default="xhigh", choices=("low", "medium", "high", "xhigh", "max"))

    sub.choices["start"].add_argument("--session-id")
    sub.choices["resume"].add_argument("--session-id", required=True)
    sub.choices["resume"].add_argument("--change-summary", default="The author applied the supported findings.")
    return root


def validated_paths(args: argparse.Namespace) -> tuple[Path, list[Path], list[Path]]:
    cwd = args.cwd.expanduser().resolve()
    if not cwd.is_dir():
        raise ValueError(f"cwd is not a directory: {cwd}")

    artifacts = [path.expanduser().resolve() for path in args.artifact]
    contexts = [path.expanduser().resolve() for path in args.context]
    missing = [str(path) for path in artifacts + contexts if not path.is_file()]
    if missing:
        raise ValueError("missing input file(s): " + ", ".join(missing))
    return cwd, artifacts, contexts


def prompt(args: argparse.Namespace, artifacts: list[Path], contexts: list[Path]) -> str:
    paths = "\n".join(f"- {path}" for path in artifacts)
    context_paths = "\n".join(f"- {path}" for path in contexts) or "- none supplied"
    focus = PROFILE_FOCUS[args.profile]

    if args.command == "start":
        phase = "Perform an independent full review."
    else:
        phase = (
            "This is a recheck in the same review session. Re-read every revised artifact, "
            "verify prior findings, and inspect the whole draft for regressions or new issues.\n"
            f"Author change summary: {args.change_summary}"
        )

    return f"""You are the independent Claude reviewer in a bounded cross-model document review.
You are read-only. Do not edit files, mutate git, call external services, or create artifacts.

Profile: {args.profile}
Primary focus: {focus}

Artifacts:
{paths}

Canonical context:
{context_paths}

{phase}

For every finding, use:
[ID] [blocking|material|minor] Summary
Evidence: exact path/section and the contradiction or missing contract
Impact: why it matters
Recommendation: smallest correction preserving the intended outcome
Human decision: yes/no; include the exact question when yes

Do not omit minor findings. Do not approve by politeness. On a recheck, say which prior
findings are resolved and list every remaining or new issue. Say CLEAN only when no
blocking, material, or minor finding remains.
"""


def claude_command(args: argparse.Namespace, session_id: str, extra_dirs: list[Path]) -> list[str]:
    binary = os.environ.get("CLAUDE_BIN", "claude")
    command = [
        binary,
        "--print",
        "--output-format",
        "json",
        "--safe-mode",
        "--permission-mode",
        "plan",
        "--tools",
        "Read,Glob,Grep",
        "--model",
        args.model,
        "--effort",
        args.effort,
    ]
    for directory in extra_dirs:
        command.extend(["--add-dir", str(directory)])
    if args.command == "start":
        command.extend(["--session-id", session_id])
    else:
        command.extend(["--resume", session_id])
    return command


def normalize(stdout: str, fallback_session_id: str) -> dict[str, object]:
    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Claude returned invalid JSON: {exc}") from exc

    if not isinstance(payload, dict):
        raise ValueError("Claude JSON result must be an object")
    result = payload.get("result")
    if not isinstance(result, str):
        result = payload.get("message")
    if not isinstance(result, str):
        raise ValueError("Claude JSON result did not contain text in 'result' or 'message'")

    session_id = payload.get("session_id") or fallback_session_id
    return {
        "session_id": session_id,
        "result": result,
        "is_error": bool(payload.get("is_error", False)),
    }


def main() -> int:
    args = parser().parse_args()
    try:
        cwd, artifacts, contexts = validated_paths(args)
        session_id = args.session_id or str(uuid.uuid4())
        extra_dirs = sorted({path.parent for path in artifacts + contexts if cwd not in path.parents})
        completed = subprocess.run(
            claude_command(args, session_id, extra_dirs),
            cwd=cwd,
            input=prompt(args, artifacts, contexts),
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode != 0:
            error = completed.stderr.strip() or completed.stdout.strip() or "unknown Claude failure"
            print(json.dumps({"session_id": session_id, "error": error}), file=sys.stderr)
            return completed.returncode
        print(json.dumps(normalize(completed.stdout, session_id), ensure_ascii=False))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
