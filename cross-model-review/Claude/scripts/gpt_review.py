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
import stat
import subprocess
import sys
import tempfile


PROFILE_FOCUS = {
    "prd": "business outcome, scenarios, scope, non-goals, assumptions, acceptance criteria, and unresolved product decisions",
    "implementation": "PRD fidelity, architecture and ownership, contracts, data/migrations, failure and recovery, security, and verification",
    "task-plan": "requirement coverage, vertical slices, bounded task scope, dependencies, routing, validation, merge targets, and parent acceptance",
    "security": "assets, actors, trust boundaries, authorization, secrets, external inputs, abuse cases, data lifecycle, recovery, and task-level mitigations",
}


def add_runtime_arguments(command: argparse.ArgumentParser) -> None:
    command.add_argument("--cwd", required=True, type=Path)
    command.add_argument("--model", default="gpt-5.6-sol", help="Reviewer model id.")
    command.add_argument("--effort", default="high", choices=("minimal", "low", "medium", "high"))


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)

    probe = sub.add_parser(
        "probe",
        help="Verify the codex CLI login and configured reviewer model access.",
    )
    add_runtime_arguments(probe)

    for name in ("start", "resume"):
        cmd = sub.add_parser(name)
        add_runtime_arguments(cmd)
        cmd.add_argument("--profile", required=True, choices=sorted(PROFILE_FOCUS))
        cmd.add_argument("--artifact", action="append", required=True, type=Path)
        cmd.add_argument("--context", action="append", default=[], type=Path)
        cmd.add_argument("--scratch-root", type=Path)

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


def codex_command(
    args: argparse.Namespace, last_message: Path, needs_full_read: bool
) -> list[str]:
    binary = os.environ.get("CODEX_BIN", "codex")
    command = [binary, "exec"]
    cwd = str(args.cwd.expanduser().resolve())

    if args.command == "probe":
        # --ephemeral keeps the probe from persisting a resumable session; the
        # prompt never references project artifacts, so nothing is loaded.
        command += ["--json", "--skip-git-repo-check", "--ephemeral", "-o", str(last_message)]
        command += ["--sandbox", "read-only", "-C", cwd]
        command += ["-m", args.model, "-c", f"model_reasoning_effort={args.effort}"]
        command.append("-")  # prompt is read from stdin
        return command

    if args.command == "resume":
        command.append("resume")

    command += ["--json", "--skip-git-repo-check", "-o", str(last_message)]

    if args.command == "start":
        command += ["--sandbox", "read-only", "-C", cwd]
    else:
        # `resume` has no --sandbox/-C flags; enforce read-only via config override.
        command += ["-c", "sandbox_mode=read-only"]

    if needs_full_read:
        # `codex exec` exposes no scoped read-root flag, so this is the only lever
        # that lets the reviewer read the private scratch draft living outside
        # --cwd (validated to sit under --scratch-root). It grants reads only;
        # writes and networked commands stay blocked by the read-only sandbox.
        # When every input is under --cwd it is omitted entirely.
        command += ["-c", 'sandbox_permissions=["disk-full-read-access"]']

    if args.model:
        command += ["-m", args.model]
    command += ["-c", f"model_reasoning_effort={args.effort}"]

    if args.command == "resume":
        command.append(args.session_id)

    command.append("-")  # prompt is read from stdin
    return command


def extract(stdout: str, last_message: Path, fallback_session_id: str | None) -> dict[str, object]:
    observed_session_id: str | None = None
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
            observed_session_id = str(event["thread_id"])
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

    return {
        "session_id": observed_session_id or fallback_session_id,
        "observed_session_id": observed_session_id,
        "result": message,
        "is_error": is_error,
    }


def main() -> int:
    args = parser().parse_args()
    try:
        cwd, artifacts, contexts, _scratch_root = validated_paths(args)
        args.cwd = cwd
        fallback_session_id = getattr(args, "session_id", None)
        needs_full_read = any(cwd not in path.parents for path in artifacts + contexts)

        with tempfile.NamedTemporaryFile("r", suffix=".txt", delete=False) as handle:
            last_message = Path(handle.name)
        try:
            completed = subprocess.run(
                codex_command(args, last_message, needs_full_read),
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

        if payload["is_error"]:
            raise ValueError(f"GPT reviewer reported an error: {payload['result']}")
        if args.command == "probe":
            if str(payload["result"]).strip() != "READY":
                raise ValueError(
                    "GPT probe returned an unexpected response: "
                    + str(payload["result"]).strip()
                )
            print(
                json.dumps(
                    {"status": "ready", "model": args.model, "effort": args.effort},
                    ensure_ascii=False,
                )
            )
            return 0

        if args.command == "start":
            if not payload["session_id"]:
                raise ValueError(
                    "GPT reviewer did not return a session id; the review session "
                    "cannot be resumed."
                )
        else:  # resume
            observed = payload["observed_session_id"]
            if observed and observed != args.session_id:
                raise ValueError(
                    "GPT reviewer resumed a different session than requested; "
                    "reviewer continuity is broken."
                )
            payload["session_id"] = args.session_id

        payload.pop("observed_session_id", None)
        print(json.dumps(payload, ensure_ascii=False))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
