---
name: cross-model-review
description: Run a bounded live cross-family review of a PRD, feature document, implementation design, or delivery/task plan while keeping the current GPT/Codex session as author and editor and one resumable Claude session as a read-only reviewer. Use when the user asks Claude to challenge or audit the current draft, wants GPT and Claude to reach evidence-based consensus, wants corrections rechecked in the same reviewer session, or wants remaining material and minor disagreements surfaced before canonical docs are finalized. Do not create review ledgers or durable findings artifacts.
---

# Cross-Model Review

Keep the current Codex/GPT conversation as the authoring session. Use one resumable Claude session as the independent reviewer. Relay findings and corrections in the live turn; preserve only the final approved document.

Read `references/review-profiles.md` and select `prd`, `implementation`, or `task-plan`. Use `security` only when `$feature-security-review` invokes this skill as its cross-family challenger. Use `scripts/claude_review.py` to start and resume Claude.

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
   python3 scripts/claude_review.py start \
     --cwd "$PWD" \
     --profile implementation \
     --artifact "${TMPDIR:-/tmp}/implementation.md" \
     --context "$PWD/AGENTS.md"
   ```

3. Retain the returned `session_id` in the active conversation. Do not persist raw Claude output as a project artifact.
4. Verify every finding against the draft, repository, and canonical context. Reject unsupported findings with evidence; never accept by model authority.
5. Prepare confirmed corrections in the scratch draft. Stop and ask the human when a finding changes business scope, selects between material architecture alternatives, accepts risk, or makes an irreversible choice.
6. Resume the same Claude session with the corrected scratch artifact:

   ```bash
   python3 scripts/claude_review.py resume \
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
- The current GPT/Codex session is the sole editor.
- Do not let the helper apply canonical changes automatically.
- Do not create review ledgers, report JSON, or transcript archives.
- If Claude resume fails, start one replacement review from the latest scratch draft and disclose that reviewer continuity was lost.
- Do not silently drop provider failures or pretend consensus was reached.

## Completion

Report only a concise live summary:

- number of findings raised;
- which were confirmed and corrected;
- which were rejected with evidence;
- every remaining material/minor human choice;
- whether Claude's full recheck is clean;
- whether the final patch was applied.
