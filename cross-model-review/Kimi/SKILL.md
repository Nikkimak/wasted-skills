---
name: cross-model-review
description: Run a bounded live cross-family review of a PRD, feature document, implementation design, or delivery/task plan while keeping the current Kimi session as author and editor and one resumable Claude session as a read-only reviewer. Use when the user asks Claude to challenge or audit the current draft, wants Kimi and Claude to reach evidence-based consensus, wants corrections rechecked in the same reviewer session, or wants remaining material and minor disagreements surfaced before canonical docs are finalized. Do not create review ledgers or durable findings artifacts.
---

# Cross-Model Review

Keep the current Kimi conversation as the authoring session. Use one resumable Claude session as the independent reviewer. Relay findings and corrections in the live turn; preserve only the final approved document.

Read `${KIMI_SKILL_DIR}/references/review-profiles.md` and select `prd`, `implementation`, or `task-plan`. Use `security` only when the `feature-security-review` skill (via the Skill tool, `/skill:feature-security-review`) invokes this skill as its cross-family challenger. Use `${KIMI_SKILL_DIR}/scripts/claude_review.py` to start and resume Claude.

Use `claude-opus-4-8` with `xhigh` effort for both the initial review and every resumed recheck. These are explicit skill defaults and must not inherit the user's interactive Claude CLI model selection. Override them only when the human explicitly requests another reviewer model/effort, and pass the same override on start and resume.

## Preconditions

- Identify the exact draft artifacts and required canonical context.
- Read the target repository's instructions first.
- Keep Claude read-only.
- Confirm the `claude` CLI is available and authenticated. Confirm access to the configured reviewer model; if either prerequisite is missing, tell the user and stop instead of skipping the cross-family challenge.
- Do not mutate canonical documents until the review/recheck loop and human decisions are complete.

## Live Review Loop

1. Create an ephemeral scratch copy of the target draft outside canonical project truth. Keep source-to-scratch paths clear. Do not create a committed review directory or findings file.
2. Start one Claude session:

   ```bash
   python3 "${KIMI_SKILL_DIR}/scripts/claude_review.py" start \
     --cwd "$PWD" \
     --profile implementation \
     --artifact "${TMPDIR:-/tmp}/implementation.md" \
     --context "$PWD/AGENTS.md"
   ```

3. Retain the returned `session_id` in the active conversation. Do not persist raw Claude output as a project artifact.
4. Keep an ephemeral finding inventory in the live conversation. For every reviewer finding, retain its ID, original severity, one-line summary, and current disposition: `corrected`, `rejected`, `awaiting-human`, or `accepted-as-is`. Verify every finding against the draft, repository, and canonical context. Reject unsupported findings with evidence; never accept by model authority. Do not write the inventory to a project file.
   - If reviewer output only gives counts, references missing text such as "the review above", or otherwise omits a finding it claims to have raised, resume the same reviewer session and request one self-contained restatement of every finding before editing or reporting results.
5. Prepare confirmed corrections in the scratch draft. Stop and ask the human when a finding changes business scope, selects between material architecture alternatives, accepts risk, or makes an irreversible choice.
6. Resume the same Claude session with the corrected scratch artifact:

   ```bash
   python3 "${KIMI_SKILL_DIR}/scripts/claude_review.py" resume \
     --cwd "$PWD" \
     --session-id SESSION_UUID \
     --profile implementation \
     --artifact "${TMPDIR:-/tmp}/implementation.md" \
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
- The current Kimi session is the sole editor.
- Do not let the helper apply canonical changes automatically.
- Do not create review ledgers, report JSON, or transcript archives.
- If Claude resume fails, start one replacement review from the latest scratch draft and disclose that reviewer continuity was lost.
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
