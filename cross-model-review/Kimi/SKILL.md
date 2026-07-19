---
name: cross-model-review
description: Run a bounded live cross-family review of a complete review-ready PRD, security-aware implementation design, or explicitly requested task plan, keeping the current Kimi session as author and one resumable Claude session as a read-only reviewer. Use only after the human explicitly asks for or approves review of the specific complete artifact. Reconcile evidence-backed findings and recheck the corrected artifact. Implementation review includes security and execution-prerequisite coverage. Do not infer consent from complexity or risk, use during partial drafting, or create durable review artifacts.
---

# Cross-Model Review

Keep the current Kimi session as author and sole editor. Use one resumable Claude session as the read-only reviewer; preserve only the final approved artifact.

Read `${KIMI_SKILL_DIR}/references/review-profiles.md` and select `prd`, `implementation`, or `task-plan` (`implementation` includes security; `task-plan` is explicit-request only and authoring skills must not offer it routinely). Use `${KIMI_SKILL_DIR}/scripts/claude_review.py` to probe, start, and resume Claude. Unless the human explicitly requests otherwise, use `claude-opus-4-8` with `xhigh` effort for probe, initial review, and recheck; keep one reviewer model and effort throughout the session.

## Readiness Gate

- Read repository instructions and resolve exact artifact paths, version/hash, profile, and minimal canonical context.
- Require the mutable target complete, self-contained, substantive, and `draft` or `proposed`, with no placeholders or decisions hidden only in chat. For changes to an accepted artifact, include the accepted baseline and intended delta as context when available.
- Require explicit human approval for review of this artifact and profile; an earlier clear request counts. An authoring skill's recommendation, complexity assessment, risk classification, or generic permission to continue does not count. Name every unresolved human decision explicitly.
- Keep canonical documents unchanged. If initial review, corrections, human decisions, and one full recheck cannot fit safely in the session (check capacity with `/usage`), invoke the `feature-context-handoff` skill (via the Skill tool, `/skill:feature-context-handoff`) and move the atomic loop to a fresh session.

Return incomplete artifacts to their authoring skill.

## Reviewer Probe

Run one real minimal probe immediately before the first full call:

```bash
REVIEW_HELPER="${KIMI_SKILL_DIR}/scripts/claude_review.py"
python3 "$REVIEW_HELPER" probe --cwd "$PWD"
```

On failure, report the exact error and stop. Do not retry, change models, or bypass the review without explicit human direction.

## Review Loop

1. Create an owner-only scratch directory outside canonical project truth, copy mutable targets into it, and pass it as `--scratch-root`.
2. Start one reviewer session with the selected profile, scratch artifact, and minimal canonical context; retain the returned `session_id` only in the live conversation. For an update to an accepted artifact, pass its baseline and intended delta as context when available.

   ```bash
   python3 "$REVIEW_HELPER" start --cwd "$PWD" --profile implementation \
     --artifact "$REVIEW_SCRATCH/implementation.md" \
     --scratch-root "$REVIEW_SCRATCH" --context "$PWD/AGENTS.md"
   ```
3. Poll the long provider call at roughly 60-second intervals without status-only model turns.
4. Keep an ephemeral inventory of each finding's ID, original severity, summary, and disposition: `corrected`, `rejected`, `awaiting-human`, or `accepted-as-is`. Verify findings against repository evidence. If the output omits findings it claims to have raised, resume once for a self-contained restatement before editing.
5. Prepare confirmed corrections in scratch. Stop for human resolution when scope, material architecture, risk acceptance, or irreversible commitments change.
6. Resume the same Claude session once for a full-document recheck of the corrected artifact.

   ```bash
   python3 "$REVIEW_HELPER" resume --cwd "$PWD" --session-id SESSION_UUID \
     --profile implementation --artifact "$REVIEW_SCRATCH/implementation.md" \
     --scratch-root "$REVIEW_SCRATCH" \
     --change-summary "Applied confirmed findings; recheck the whole draft."
   ```
7. Permit an additional focused round only for a new blocking or material finding. New minor findings return to the human without another required reviewer call.
8. After human resolution, apply one canonical patch and remove scratch state. Disclose a human-approved post-recheck minor edit as unrechecked instead of forcing another full pass.

## Completion And Safety

Complete only when Kimi evaluated every finding, no confirmed blocking or material finding remains, Claude completed one full corrected-document recheck in the same session, no material product, architecture, security, or irreversible decision is hidden, and the human decided every remaining minor or optional disagreement.

Use `CLEAN` only when the recheck found no remaining issue. Otherwise report `review_complete_with_human_resolved_minors` and identify any post-recheck minor edit.

- Claude may read/search only; it must not edit, mutate git, run arbitrary shell commands, or access trackers.
- Do not persist raw output, finding ledgers, transcripts, or reviewer session IDs.
- Keep every input outside `--cwd` under the private `--scratch-root`.
- On rate limit, timeout, authentication/model error, malformed output, or resume failure, preserve scratch state, report the exact error, and stop until explicit human direction.

## Completion Report

List every finding across all rounds with original severity, one-line meaning, final disposition, and repository evidence for rejection. State totals, remaining human choices, recheck result, any disclosed post-recheck minor edit, and whether the final patch was applied.
