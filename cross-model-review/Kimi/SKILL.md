---
name: cross-model-review
description: Run a bounded live cross-family review of a complete review-ready PRD, security-aware implementation design, or explicitly requested task plan, keeping the current Kimi session as author and editor and one resumable Claude session as a read-only reviewer. Use when the human wants Claude to challenge the full draft, reconcile evidence-backed findings, and recheck the corrected artifact. Implementation review includes security and execution-prerequisite coverage. Do not use during discovery or partial drafting, and do not create review ledgers or durable findings artifacts.
---

# Cross-Model Review

Keep the current Kimi session as author and sole editor. Use one resumable Claude session as the read-only reviewer; preserve only the final approved artifact.

Read `${KIMI_SKILL_DIR}/references/review-profiles.md` and select `prd`, `implementation`, or `task-plan`. `implementation` includes security. `task-plan` is available only on explicit human request and is not part of the default feature workflow. Use `${KIMI_SKILL_DIR}/scripts/claude_review.py` to probe, start, and resume Claude.

Use `claude-opus-4-8` with `xhigh` effort for probe, initial review, and recheck unless the human explicitly requests another model/effort. Keep one reviewer model and effort throughout the session.

## Readiness Gate

Before invoking Claude:

- Read target repository instructions.
- Resolve exact artifact paths, version/hash, profile, and minimal canonical context.
- Require each mutable target to be complete, self-contained, substantive, and `draft` or `proposed`, with no placeholders or decisions hidden only in chat.
- Require every unresolved human decision to be resolved or named explicitly.
- Require human confirmation of full review; an earlier clear request in the conversation counts.
- Ensure the Kimi session can safely hold initial review, corrections, human decisions, and one full recheck (check capacity with `/usage`). Otherwise invoke the `feature-context-handoff` skill (via the Skill tool, `/skill:feature-context-handoff`) and move the atomic loop to a fresh session.
- Keep canonical documents unchanged until review resolution completes.

Return incomplete artifacts to their authoring skill.

## Reviewer Probe

Run one real minimal probe immediately before the first full call:

```bash
REVIEW_HELPER="${KIMI_SKILL_DIR}/scripts/claude_review.py"
python3 "$REVIEW_HELPER" probe --cwd "$PWD"
```

On failure, report the exact error and stop. Do not retry, change models, or bypass the review without explicit human direction.

## Review Loop

1. Create an owner-only scratch directory outside canonical project truth and copy mutable targets into it. Pass it as `--scratch-root`.
2. Start one reviewer session with the selected profile, scratch artifact, and minimal canonical context; retain the returned `session_id` only in the live conversation.

   ```bash
   python3 "$REVIEW_HELPER" start --cwd "$PWD" --profile implementation \
     --artifact "$REVIEW_SCRATCH/implementation.md" \
     --scratch-root "$REVIEW_SCRATCH" --context "$PWD/AGENTS.md"
   ```
3. Treat the provider call as one long operation. Poll at roughly 60-second intervals without creating status-only model turns.
4. Maintain an ephemeral inventory containing each finding ID, original severity, summary, and disposition: `corrected`, `rejected`, `awaiting-human`, or `accepted-as-is`. Verify findings against repository evidence.
5. If output omits findings it claims to have raised, resume once for a self-contained restatement before editing.
6. Prepare confirmed corrections in scratch. Stop for human resolution when scope, material architecture, risk acceptance, or irreversible commitments change.
7. Resume the same Claude session once for a full-document recheck of the corrected artifact.

   ```bash
   python3 "$REVIEW_HELPER" resume --cwd "$PWD" --session-id SESSION_UUID \
     --profile implementation --artifact "$REVIEW_SCRATCH/implementation.md" \
     --scratch-root "$REVIEW_SCRATCH" \
     --change-summary "Applied confirmed findings; recheck the whole draft."
   ```
8. Permit an additional focused round only for a new blocking or material finding. New minor findings return to the human without another required reviewer call.
9. After human resolution, apply one consolidated canonical patch and remove scratch state. A human-approved minor edit made after recheck may remain explicitly disclosed as unrechecked rather than forcing another full pass.

## Completion Standard

Review is complete when:

- no confirmed blocking or material finding remains;
- Kimi evaluated every finding;
- Claude completed one full corrected-document recheck in the same session;
- no material product, architecture, security, or irreversible decision is hidden;
- the human decided every remaining minor or optional disagreement.

Use `CLEAN` only when the recheck found no remaining issue. Otherwise report `review_complete_with_human_resolved_minors` and identify any post-recheck minor edit.

## Safety

- Claude may read/search only; it must not edit, mutate git, run arbitrary shell commands, or access trackers.
- Do not persist raw output, finding ledgers, transcripts, or reviewer session IDs.
- Keep every input outside `--cwd` under the private `--scratch-root`.
- On rate limit, timeout, authentication/model error, malformed output, or resume failure, preserve scratch state, report the exact error, and stop until explicit human direction.

## Completion Report

List every finding across all rounds with original severity, one-line meaning, final disposition, and repository evidence for rejection. State totals, remaining human choices, recheck result, any disclosed post-recheck minor edit, and whether the final patch was applied.
