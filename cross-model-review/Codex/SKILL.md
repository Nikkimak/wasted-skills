---
name: cross-model-review
description: Run a bounded live cross-family review of a complete review-ready PRD, security-aware implementation design, explicitly requested task plan, or approved-feature revision bundle. Use when the human wants Claude to challenge complete artifacts, reconcile evidence-backed findings, and recheck the corrected artifact set. Implementation and revision reviews include security and execution-prerequisite coverage. Do not use during discovery or partial drafting, and do not create review ledgers or durable findings artifacts.
---

# Cross-Model Review

Keep Codex/GPT as sole author and editor. Use one resumable, read-only Claude session and preserve only the approved artifact set.

Read `references/review-profiles.md`, select `prd`, `implementation`, `task-plan`, or `revision`, and use `scripts/claude_review.py`. `task-plan` is explicit-request only. Unless the human chooses otherwise, use `claude-opus-4-8` with `xhigh` effort for probe, review, and recheck; never change reviewer model or effort mid-session.

## Readiness Gate

- Read repository instructions and resolve exact artifact paths, versions/hashes, profile, and minimal canonical context.
- Require complete, self-contained `draft` or `proposed` targets with no placeholders or decisions hidden only in chat. For `revision`, also require accepted baselines, change intent, and baseline-to-proposal diff.
- Require human confirmation of full review; an earlier clear request counts. Name every unresolved human decision explicitly.
- Keep canonical documents unchanged. If the initial review, corrections, human decisions, and full recheck cannot fit safely, use `$feature-context-handoff` before review.

Return incomplete inputs to their authoring skill.

## Reviewer Probe

Run one real minimal probe immediately before the first full call:

```bash
REVIEW_HELPER="${CODEX_HOME:-$HOME/.codex}/skills/cross-model-review/scripts/claude_review.py"
python3 "$REVIEW_HELPER" probe --cwd "$PWD"
```

On failure, report the exact error and stop. Do not retry, change models, or bypass review without explicit human direction.

## Review Loop

1. Create an owner-only scratch directory outside canonical truth, copy mutable targets into it, and pass it as `--scratch-root`.
2. Start one reviewer session with the selected profile, scratch artifacts, and minimal context. Keep its `session_id` only in the live conversation. For `revision`, repeat `--artifact` for proposed documents and `--context` for baselines, intent, diff, and unchanged related documents.

   ```bash
   python3 "$REVIEW_HELPER" start --cwd "$PWD" --profile implementation \
     --artifact "$REVIEW_SCRATCH/implementation.md" \
     --scratch-root "$REVIEW_SCRATCH" --context "$PWD/AGENTS.md"
   ```
3. Poll the long provider call at roughly 60-second intervals without status-only model turns.
4. Keep an ephemeral inventory of every finding's ID, original severity, summary, and disposition: `corrected`, `rejected`, `awaiting-human`, or `accepted-as-is`. Verify each finding against repository evidence. If Claude omits findings it claims to have raised, resume once for a self-contained restatement before editing.
5. Prepare confirmed corrections in scratch. Stop for human resolution when scope, material architecture, risk acceptance, or irreversible commitments change.
6. Resume the same session once for a full recheck of every corrected artifact.

   ```bash
   python3 "$REVIEW_HELPER" resume --cwd "$PWD" --session-id SESSION_UUID \
     --profile implementation --artifact "$REVIEW_SCRATCH/implementation.md" \
     --scratch-root "$REVIEW_SCRATCH" \
     --change-summary "Applied confirmed findings; recheck the whole draft."
   ```
7. Permit another focused round only for a new blocking or material finding. Return new minor findings to the human without another required call.
8. After human resolution, apply one canonical patch and remove scratch state. Disclose a human-approved post-recheck minor edit as unrechecked instead of forcing another full pass.

## Completion And Safety

Complete only when Codex evaluated every finding, no confirmed blocking/material issue remains, Claude completed the full corrected-set recheck in the same session, and the human resolved every remaining minor or optional disagreement.

Use `CLEAN` only when the recheck found no remaining issue. Otherwise report `review_complete_with_human_resolved_minors` and identify any post-recheck minor edit.

- Claude may read/search only; it must not edit, mutate git, run arbitrary shell commands, or access trackers.
- Do not persist raw output, finding ledgers, transcripts, or reviewer session IDs.
- Keep every input outside `--cwd` under the private `--scratch-root`.
- On rate limit, timeout, authentication/model error, malformed output, or resume failure, preserve scratch state, report the exact error, and stop until explicit human direction.

## Completion Report

List every finding across all rounds with original severity, one-line meaning, final disposition, and repository evidence for rejection. State totals, remaining human choices, recheck result, any disclosed post-recheck minor edit, and whether the final patch was applied.
