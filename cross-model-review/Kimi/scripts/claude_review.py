#!/usr/bin/env python3
"""Probe, start, or resume a read-only Claude document-review session."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import uuid


PROFILE_FOCUS = {
    "prd": "business outcome, scenarios, scope, non-goals, assumptions, acceptance criteria, and unresolved product decisions",
    "implementation": "PRD fidelity, architecture and ownership, contracts, data/migrations, failure and recovery, security, and verification",
    "task-plan": "requirement coverage, vertical slices, bounded task scope, dependencies, routing, validation, merge targets, and parent acceptance",
    "security": "assets, actors, trust boundaries, authorization, secrets, external inputs, abuse cases, data lifecycle, recovery, and task-level mitigations",
}


def add_runtime_arguments(command: argparse.ArgumentParser) -> None:
    command.add_argument("--cwd", required=True, type=Path)
    command.add_argument("--model", default="claude-opus-4-8")
    command.add_argument(
        "--effort",
        default="xhigh",
        choices=("low", "medium", "high", "xhigh", "max"),
    )


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)

    probe = sub.add_parser(
        "probe",
        help="Verify Claude CLI authentication and configured model access.",
    )
    add_runtime_arguments(probe)

    for name in ("start", "resume"):
        cmd = sub.add_parser(name)
        add_runtime_arguments(cmd)
        cmd.add_argument("--profile", required=True, choices=sorted(PROFILE_FOCUS))
        cmd.add_argument("--artifact", action="append", required=True, type=Path)
        cmd.add_argument("--context", action="append", default=[], type=Path)
        cmd.add_argument("--scratch-root", type=Path)

    sub.choices["start"].add_argument("--session-id")
    sub.choices["resume"].add_argument("--session-id", required=True)
    sub.choices["resume"].add_argument("--change-summary", default="The author applied the supported findings.")
    return root


def validated_paths(
    args: argparse.Namespace,
) -> tuple[Path, list[Path], list[Path], Path | None]:
    cwd = args.cwd.expanduser().resolve()
    if not cwd.is_dir():
        raise ValueError(f"cwd is not a directory: {cwd}")

    if args.command == "probe":
        return cwd, [], [], None

    artifacts = [path.expanduser().resolve() for path in args.artifact]
    contexts = [path.expanduser().resolve() for path in args.context]
    missing = [str(path) for path in artifacts + contexts if not path.is_file()]
    if missing:
        raise ValueError("missing input file(s): " + ", ".join(missing))

    scratch_root = (
        args.scratch_root.expanduser().resolve() if args.scratch_root else None
    )
    external = [path for path in artifacts + contexts if cwd not in path.parents]
    if external and scratch_root is None:
        raise ValueError(
            "--scratch-root is required when an artifact or context is outside --cwd"
        )
    if scratch_root is not None:
        if not scratch_root.is_dir():
            raise ValueError(f"scratch root is not a directory: {scratch_root}")
        root_stat = scratch_root.stat()
        if os.name == "posix":
            if root_stat.st_uid != os.geteuid():
                raise ValueError(
                    f"scratch root is not owned by the current user: {scratch_root}"
                )
            if stat.S_IMODE(root_stat.st_mode) & 0o077:
                raise ValueError(
                    f"scratch root must not grant group/other access: {scratch_root}"
                )
        outside = [path for path in external if scratch_root not in path.parents]
        if outside:
            raise ValueError(
                "external input is outside --scratch-root: "
                + ", ".join(str(path) for path in outside)
            )
    return cwd, artifacts, contexts, scratch_root


def prompt(args: argparse.Namespace, artifacts: list[Path], contexts: list[Path]) -> str:
    if args.command == "probe":
        return "Reply with exactly READY and no other text."

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
        "" if args.command == "probe" else "Read,Glob,Grep",
        "--model",
        args.model,
        "--effort",
        args.effort,
    ]
    if args.command == "probe":
        command.append("--no-session-persistence")
        return command

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
    if not isinstance(session_id, str):
        raise ValueError("Claude JSON result contained a non-string session_id")
    return {
        "session_id": session_id,
        "result": result,
        "is_error": bool(payload.get("is_error", False)),
    }


def main() -> int:
    args = parser().parse_args()
    try:
        cwd, artifacts, contexts, scratch_root = validated_paths(args)
        session_id = (
            ""
            if args.command == "probe"
            else getattr(args, "session_id", None) or str(uuid.uuid4())
        )
        extra_dirs = [scratch_root] if scratch_root is not None else []
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
            failure = {"error": error}
            if session_id:
                failure["session_id"] = session_id
            print(json.dumps(failure), file=sys.stderr)
            return completed.returncode
        payload = normalize(completed.stdout, session_id)
        if payload["is_error"]:
            raise ValueError(f"Claude reported an error: {payload['result']}")
        if args.command == "probe":
            if str(payload["result"]).strip() != "READY":
                raise ValueError(
                    "Claude probe returned an unexpected response: "
                    + str(payload["result"]).strip()
                )
            print(
                json.dumps(
                    {"status": "ready", "model": args.model, "effort": args.effort},
                    ensure_ascii=False,
                )
            )
            return 0
        if payload["session_id"] != session_id:
            raise ValueError(
                "Claude returned a different session_id than the requested review session"
            )
        print(json.dumps(payload, ensure_ascii=False))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
