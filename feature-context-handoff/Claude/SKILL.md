---
name: feature-context-handoff
description: Preserve or restore the minimal working state of one unfinished feature across fresh Claude sessions. Use when the user asks to pause, end, hand off, or continue a named feature; when product, implementation/security design, delivery, or execution-readiness work cannot safely finish in the remaining context; when a blocker pauses incomplete feature work; or when Claude must create, refresh, read, or remove a feature-local WORK-HANDOFF.md. Do not use for completed work, routine turn summaries, or durable decisions that belong in canonical documents.
---

# Feature Context Handoff

Carry one unfinished feature across sessions with a short-lived `WORK-HANDOFF.md`. Canonical documents remain the durable truth.

## Resolve The Feature Workspace

Read repository instructions, resolve the named canonical feature folder without guessing between plausible locations, and use `<feature-folder>/WORK-HANDOFF.md` unless the repository defines an equivalent. When permitted, read the handoff before broader history, then load only its `Read first` paths and the phase evidence needed now.

## Choose The Operation

### Resume

1. If no handoff exists, report that and continue through the active authoring skill from canonical documents and the work plan; do not invent one retrospectively.
2. Verify referenced paths, phase, canonical state, work plan, and relevant working tree. Repair a stale handoff, with canonical truth taking precedence.
3. Read the listed inputs in order and continue from `Exact next step`; do not reread transcripts or full history without evidence that it is needed.

### Pause Or Refresh

Create or refresh only when the human pauses incomplete work, a blocker stops it, or the next atomic checkpoint/review loop cannot safely finish in this session. Do not create routine per-turn handoffs when canonical state already makes the next phase obvious.

Before stopping, finish the nearest safe atomic action, persist a coherent draft, leave external work finished or safely resumable within current authority, and make the working tree understandable. Do not start a new review, migration, or mutation merely to consume remaining context.

### Close

Remove and report the handoff when the phase or feature is complete and canonical state makes the next action clear. Do not archive or relocate it into project knowledge.

## Context Capacity

Use only a host-provided context indicator as numerical evidence — in Claude Code the `/context` view or configured status line; when only the human can see it, ask them to check it. Never infer a token count or percentage from conversation length. At a major boundary, especially before a complete cross-model review (initial reviewer call, corrections, human decisions, and full recheck), create or refresh the handoff and recommend a fresh Claude session when capacity is doubtful. This skill installs no hooks, timers, plugins, or automatic termination.

## Handoff Contract

Keep the file direct and normally within roughly 1,000-2,000 tokens. Use this structure, omitting empty optional fields:

```markdown
# Work handoff: <feature>

Updated: <date/time or date>
Phase: <feature-design|implementation-design|deep-security-design|delivery-plan|execution-readiness|other>
Status: <precise incomplete state>

## Read first
1. <canonical path and why>
2. <canonical path and why>

## Accepted inputs
- <approved artifact path plus version, commit, or hash when relevant>

## Last completed checkpoint
- <what is durably complete>

## Exact next step
1. <the first bounded action in the fresh session>

## Open human decisions
- <question that must not be guessed>

## Hard gates and permissions
- <approval, provider, security, or mutation gate still in force>

## Working state
- Git: <branch and relevant modified/untracked paths>
- External process: <none, stopped, or resumable identifier without secrets>
```

## Boundaries

- Link to canonical artifacts instead of duplicating them. Record accepted inputs, exact continuation state, explicit human decisions, and relevant user changes distinguished from Claude changes — not a narrative journal.
- Never store transcripts, finding inventories, chain-of-thought, credentials, tokens, or authentication state.
- Keep the handoff local and ephemeral: do not stage, commit, publish, archive, or change ignore rules merely to hide it. Replace stale content instead of appending history.

## Completion

For `resume`, report the verified phase and exact action being continued. For `pause`, report the handoff path and tell the human that the safe continuation is a fresh Claude session in the same repository followed by "continue <feature>". For `close`, report that the ephemeral handoff was removed and name the canonical source that now carries the next state.
