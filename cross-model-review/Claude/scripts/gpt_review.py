#!/usr/bin/env python3
"""Start or resume a read-only GPT (Codex CLI) document-review session.

Claude is the author/editor in this cross-model loop. This helper drives an
independent GPT reviewer through the `codex exec` CLI, kept read-only and
resumable so the same reviewer session can recheck the corrected draft.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


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
        cmd.add_argument("--model", default="gpt-5.6-sol", help="Reviewer model id.")
        cmd.add_argument("--effort", default="high", choices=("minimal", "low", "medium", "high"))

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

    return f"""You are the independent GPT reviewer in a bounded cross-model document review.
Claude is the author and sole editor. You are read-only: do not edit files, mutate git,
call external services, or create artifacts. Read the listed files with shell commands.

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


def codex_command(args: argparse.Namespace, last_message: Path) -> list[str]:
    binary = os.environ.get("CODEX_BIN", "codex")
    command = [binary, "exec"]

    if args.command == "resume":
        command.append("resume")

    command += ["--json", "--skip-git-repo-check", "-o", str(last_message)]

    if args.command == "start":
        command += ["--sandbox", "read-only", "-C", str(args.cwd.expanduser().resolve())]
    else:
        # `resume` has no --sandbox/-C flags; enforce read-only via config override.
        command += ["-c", "sandbox_mode=read-only"]

    # Let the reviewer read the scratch draft and context wherever they live,
    # while writes and networked commands stay blocked by the read-only sandbox.
    command += ["-c", 'sandbox_permissions=["disk-full-read-access"]']

    if args.model:
        command += ["-m", args.model]
    command += ["-c", f"model_reasoning_effort={args.effort}"]

    if args.command == "resume":
        command.append(args.session_id)

    command.append("-")  # prompt is read from stdin
    return command


def extract(stdout: str, last_message: Path, fallback_session_id: str | None) -> dict[str, object]:
    session_id = fallback_session_id
    message = ""
    is_error = False

    for line in stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            continue
        etype = event.get("type")
        if etype == "thread.started" and event.get("thread_id"):
            session_id = str(event["thread_id"])
        elif etype == "item.completed":
            item = event.get("item") or {}
            if item.get("type") == "agent_message" and isinstance(item.get("text"), str):
                message = item["text"]
        elif etype == "error" or event.get("error"):
            is_error = True

    if last_message.is_file():
        file_text = last_message.read_text(encoding="utf-8", errors="replace").strip()
        if file_text:
            message = file_text

    if not message:
        is_error = True
        message = "GPT reviewer returned no final message."

    return {"session_id": session_id, "result": message, "is_error": is_error}


def main() -> int:
    args = parser().parse_args()
    try:
        cwd, artifacts, contexts = validated_paths(args)
        args.cwd = cwd
        fallback_session_id = getattr(args, "session_id", None)

        with tempfile.NamedTemporaryFile("r", suffix=".txt", delete=False) as handle:
            last_message = Path(handle.name)
        try:
            completed = subprocess.run(
                codex_command(args, last_message),
                cwd=cwd,
                input=prompt(args, artifacts, contexts),
                text=True,
                capture_output=True,
                check=False,
            )
            if completed.returncode != 0:
                error = completed.stderr.strip() or completed.stdout.strip() or "unknown Codex failure"
                print(json.dumps({"session_id": fallback_session_id, "error": error}), file=sys.stderr)
                return completed.returncode
            payload = extract(completed.stdout, last_message, fallback_session_id)
        finally:
            last_message.unlink(missing_ok=True)

        print(json.dumps(payload, ensure_ascii=False))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
