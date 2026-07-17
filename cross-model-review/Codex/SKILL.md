---
name: cross-model-review
description: Run a bounded live cross-family review of a complete, self-contained PRD, implementation design, delivery/task plan, or security-relevant artifact set already in review-ready draft/proposed state. Use when the human asks Claude to challenge the full draft, wants GPT and Claude to reach evidence-based consensus, wants supported corrections rechecked in the same reviewer session, or wants every remaining disagreement surfaced before approval. Do not use during discovery, question gathering, outlining, or partial drafting, and do not create review ledgers or durable findings artifacts.
---

# Cross-Model Review

Keep the current Codex/GPT conversation as the authoring session. Use one resumable Claude session as the independent reviewer. Relay findings and corrections in the live turn; preserve only the final approved document.

This skill reviews a finished draft; it does not co-author an unfinished one. Return partial artifacts to their authoring skill.

Read `references/review-profiles.md` and select `prd`, `implementation`, or `task-plan`. Use `security` only when `$feature-security-review` invokes this skill as its cross-family challenger. Use `scripts/claude_review.py` to probe, start, and resume Claude.

Use `claude-opus-4-8` with `xhigh` effort for the probe, initial review, and every resumed recheck. These are explicit skill defaults and must not inherit the user's interactive Claude CLI model selection. Override them only when the human explicitly requests another reviewer model/effort, and pass the same override to every command.

## Review Readiness Gate

Pass every gate before invoking Claude:

- Read the target repository's instructions first.
- Identify the exact artifact path or paths, version/commit/hash when relevant, review profile, and minimal canonical context.
- Require every artifact being revised in the current review stage to be complete, self-contained, and marked `draft` or `proposed`. Accepted upstream inputs may be supplied as immutable context without changing status. Every required section in the review target must be substantive; no placeholders, TODOs, unfinished task contracts, or known decisions hidden only in chat may remain.
- Require every known unresolved human decision to be resolved or explicitly named in the draft. Review may challenge an explicit open decision but may not silently decide it.
- Require the human to have requested or confirmed review of the full draft. A clear request earlier in the current conversation counts; do not ask twice.
- Verify that the current Codex session has comfortable context capacity for the initial review, author evaluation and corrections, human decisions, and a full-document recheck. Use only the host-provided context/status indicator; never invent a percentage. If capacity is doubtful, invoke `$feature-context-handoff` and move the atomic review loop to a fresh session.
- Keep Claude read-only and leave canonical documents unchanged until review, recheck, and human decisions are complete.

Stop and return to the authoring skill when any readiness gate fails. Do not invoke Claude on discovery notes, question collections, outlines, isolated sections, or knowingly incomplete drafts.

## Reviewer CLI Probe

Resolve the helper from the installed skill package, then run one real minimal probe immediately before the first full-artifact call:

```bash
REVIEW_HELPER="${CODEX_HOME:-$HOME/.codex}/skills/cross-model-review/scripts/claude_review.py"
python3 "$REVIEW_HELPER" probe \
  --cwd "$PWD"
```

The probe must verify executable availability, authentication, and access to `claude-opus-4-8` with `xhigh` effort without loading project artifacts or creating a resumable session. If the probe fails, report the exact error and stop. Do not fall back to another model, skip the cross-family review, or retry automatically. Retry only after an explicit human request.

## Live Review Loop

1. Create one private ephemeral scratch directory outside canonical project truth and copy every mutable review target into it. Keep source-to-scratch paths clear. Do not use a shared directory such as `/tmp` itself, and do not create a committed review directory or findings file.

   ```bash
   REVIEW_SCRATCH="$(mktemp -d "${TMPDIR:-/tmp}/cross-model-review.XXXXXX")"
   chmod 700 "$REVIEW_SCRATCH"
   cp "$PWD/path/to/implementation.md" "$REVIEW_SCRATCH/implementation.md"
   ```

2. Start one Claude session with the same helper and defaults used by the successful probe:

   ```bash
   python3 "$REVIEW_HELPER" start \
     --cwd "$PWD" \
     --profile implementation \
     --artifact "$REVIEW_SCRATCH/implementation.md" \
     --scratch-root "$REVIEW_SCRATCH" \
     --context "$PWD/AGENTS.md"
   ```

3. Retain the returned `session_id` in the active conversation. Do not persist raw Claude output as a project artifact.
   - Treat the provider call as one long-running operation. Use the longest supported wait and poll at roughly 60-second intervals. Do not create repeated model/status turns merely to poll an unchanged process.
4. Keep an ephemeral finding inventory in the live conversation. For every reviewer finding, retain its ID, original severity, one-line summary, and current disposition: `corrected`, `rejected`, `awaiting-human`, or `accepted-as-is`. Verify every finding against the draft, repository, and canonical context. Reject unsupported findings with evidence; never accept by model authority. Do not write the inventory to a project file.
   - If reviewer output only gives counts, references missing text such as "the review above", or otherwise omits a finding it claims to have raised, resume the same reviewer session and request one self-contained restatement of every finding before editing or reporting results.
5. Prepare confirmed corrections in the scratch draft. Stop and ask the human when a finding changes business scope, selects between material architecture alternatives, accepts risk, or makes an irreversible choice.
6. Resume the same Claude session with the corrected scratch artifact:

   ```bash
   python3 "$REVIEW_HELPER" resume \
     --cwd "$PWD" \
     --session-id SESSION_UUID \
     --profile implementation \
     --artifact "$REVIEW_SCRATCH/implementation.md" \
     --scratch-root "$REVIEW_SCRATCH" \
     --change-summary "Applied confirmed findings; recheck the whole draft."
   ```

7. Require a full-document recheck, not only confirmation of the author's summary. Permit one additional focused round only for a new material finding.
8. Surface every remaining disagreement, including minor or optional edits, to the human. The human chooses to apply it or accept the draft as-is.
9. After human resolution and a clean recheck, apply one consolidated patch from scratch to canonical documentation. Delete scratch state.

## Consensus Contract

Consensus requires all of the following:

- no confirmed blocking finding remains;
- the author evaluated every reviewer finding;
- Claude re-read the corrected whole draft in the same reviewer session;
- no product, architecture, security, or irreversible decision is hidden;
- the human decided every remaining minor or optional disagreement.

Consensus is not model voting. If evidence remains ambiguous after the bounded loop, stop and ask the human.

## Mutation And Safety

- Claude may use only read/search tools and must not edit files, run arbitrary shell commands, mutate git, or access Linear.
- The current GPT/Codex session is the sole editor.
- Do not let the helper apply canonical changes automatically.
- Do not create review ledgers, report JSON, or transcript archives.
- Require every input outside `--cwd` to live under the private `--scratch-root`; never grant the reviewer a shared parent directory merely to expose one file.
- On rate limits, overload, timeouts, authentication/model-access errors, malformed output, or resume failure, preserve scratch state, report the exact error, and stop. Do not retry, replace the reviewer session, or change models automatically. Continue only after an explicit human request; disclose lost reviewer continuity if the human chooses a replacement review.
- Do not silently drop provider failures or pretend consensus was reached.

## Completion

Report a concise but complete live finding inventory. A count-only summary is
not sufficient. List every finding raised across all rounds, including findings
already corrected or rejected, with:

- finding ID and original severity;
- one-line summary;
- final disposition: `corrected`, `rejected`, `accepted-as-is`, or
  `still-open`;
- concise repository evidence for every rejection.

Then state the total count, every remaining human choice, whether Claude's full
recheck is clean, and whether the final patch was applied. Do not reproduce the
raw reviewer transcript or create a durable findings artifact.
