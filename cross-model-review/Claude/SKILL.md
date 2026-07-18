---
name: cross-model-review
description: Run a bounded live cross-family review of a complete review-ready PRD, security-aware implementation design, or explicitly requested task plan. Use when the human wants GPT to challenge the full draft, reconcile evidence-backed findings, and recheck the corrected artifact. Implementation review includes security and execution-prerequisite coverage. Do not use during discovery or partial drafting, and do not create review ledgers or durable findings artifacts.
---

# Cross-Model Review

Keep the current Claude conversation as author and sole editor. Use one resumable GPT/Codex session as the read-only reviewer; preserve only the final approved artifact.

Read `${CLAUDE_SKILL_DIR}/references/review-profiles.md` and select `prd`, `implementation`, or `task-plan`. `implementation` includes security. `task-plan` is available only on explicit human request and is not part of the default feature workflow. Use `${CLAUDE_SKILL_DIR}/scripts/gpt_review.py` to probe, start, and resume the GPT reviewer through the local `codex exec` CLI (read-only sandbox, resumable session).

Use `gpt-5.6-sol` with `high` reasoning effort for the probe, initial review, and recheck unless the human explicitly requests another reviewer model/effort. Keep one reviewer model and effort throughout the session.

## Readiness Gate

Before invoking the GPT reviewer:

- Read target repository instructions.
- Resolve exact artifact paths, version/hash, profile, and minimal canonical context.
- Require each mutable target to be complete, self-contained, substantive, and `draft` or `proposed`, with no placeholders or decisions hidden only in chat.
- Require every unresolved human decision to be resolved or named explicitly.
- Require human confirmation of full review; an earlier clear request in the conversation counts.
- Ensure the Claude session can safely hold the initial review, corrections, human decisions, and one full recheck. Otherwise use the `feature-context-handoff` skill (invoked via the Skill tool as `/feature-context-handoff`) and move the atomic loop to a fresh session.
- Keep canonical documents unchanged until review resolution completes.

Return incomplete artifacts to their authoring skill.

## Reviewer Probe

Confirm the `codex` CLI is available and logged in (`codex login status`). Run one real minimal probe immediately before the first full call:

```bash
REVIEW_HELPER="${CLAUDE_SKILL_DIR}/scripts/gpt_review.py"
python3 "$REVIEW_HELPER" probe --cwd "$PWD"
```

The probe verifies executable availability, login, and access to `gpt-5.6-sol` with `high` effort under a read-only, ephemeral sandbox without loading project artifacts or creating a resumable session. On failure, report the exact error and stop. Do not retry, change models, or bypass the review without explicit human direction.

## Review Loop

1. Create an owner-only scratch directory outside canonical project truth and copy mutable targets into it. Pass it as `--scratch-root`.

   ```bash
   REVIEW_SCRATCH="$(mktemp -d "${TMPDIR:-/tmp}/cross-model-review.XXXXXX")"
   chmod 700 "$REVIEW_SCRATCH"
   cp "$PWD/path/to/implementation.md" "$REVIEW_SCRATCH/implementation.md"
   ```

2. Start one GPT reviewer session with the selected profile, scratch artifact, and minimal canonical context; retain the returned `session_id` only in the live conversation.

   ```bash
   python3 "$REVIEW_HELPER" start --cwd "$PWD" --profile implementation \
     --artifact "$REVIEW_SCRATCH/implementation.md" \
     --scratch-root "$REVIEW_SCRATCH" --context "$PWD/CLAUDE.md"
   ```

3. Treat the provider call as one long operation. Poll at roughly 60-second intervals without creating status-only turns.
4. Maintain an ephemeral inventory containing each finding ID, original severity, summary, and disposition: `corrected`, `rejected`, `awaiting-human`, or `accepted-as-is`. Verify findings against repository evidence; never accept by model authority.
5. If output omits findings it claims to have raised, resume once for a self-contained restatement before editing.
6. Prepare confirmed corrections in scratch. Stop for human resolution when scope, material architecture, risk acceptance, or irreversible commitments change.
7. Resume the same GPT session once for a full-document recheck of the corrected artifact.

   ```bash
   python3 "$REVIEW_HELPER" resume --cwd "$PWD" --session-id SESSION_UUID \
     --profile implementation --artifact "$REVIEW_SCRATCH/implementation.md" \
     --scratch-root "$REVIEW_SCRATCH" \
     --change-summary "Applied confirmed findings; recheck the whole draft."
   ```

8. Permit an additional focused round only for a new blocking or material finding. New minor findings return to the human without another required reviewer call.
9. After human resolution, apply one consolidated patch from scratch to canonical documentation and remove scratch state. A human-approved minor edit made after recheck may remain explicitly disclosed as unrechecked rather than forcing another full pass.

## Completion Standard

Review is complete when:

- no confirmed blocking or material finding remains;
- the Claude author evaluated every finding;
- the GPT reviewer completed one full corrected-document recheck in the same session;
- no material product, architecture, security, or irreversible decision is hidden;
- the human decided every remaining minor or optional disagreement.

Use `CLEAN` only when the recheck found no remaining issue. Otherwise report `review_complete_with_human_resolved_minors` and identify any post-recheck minor edit.

## Safety

- The GPT reviewer runs under a read-only sandbox: it may only read/search and must not edit files, mutate git, run mutating or networked commands, or access external services.
- Do not persist raw output, finding ledgers, transcripts, or reviewer session IDs.
- Keep every input outside `--cwd` under the private `--scratch-root`; the helper adds whole-disk read access only when an input sits outside `--cwd`, and never grants write or network access.
- On rate limit, timeout, login/model-access error, malformed output, or resume failure, preserve scratch state, report the exact error, and stop until explicit human direction.

## Completion Report

List every finding across all rounds with original severity, one-line meaning, final disposition, and repository evidence for rejection. State totals, remaining human choices, recheck result, any disclosed post-recheck minor edit, and whether the final patch was applied. Do not reproduce the raw reviewer transcript or create a durable findings artifact.
