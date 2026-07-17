---
name: feature-context-handoff
description: Preserve or restore the minimal working state of one unfinished feature across fresh Claude sessions. Use when the user asks to pause, end, hand off, or continue a named feature; when a product, implementation, delivery, or security phase cannot safely finish in the remaining context; when a blocker pauses incomplete feature work; or when Claude must create, refresh, read, or remove a feature-local WORK-HANDOFF.md. Do not use for completed work, routine turn summaries, or durable product and technical decisions that belong in canonical documents.
---

# Feature Context Handoff

Carry one unfinished feature into a fresh Claude session without replaying its full conversation history. Keep durable truth in canonical feature documents; use `WORK-HANDOFF.md` only as a short-lived navigation and process-state pointer.

## Resolve The Feature Workspace

1. Read the target repository's instructions first.
2. Resolve the named feature and its canonical feature folder from the user's request, work plan, or repository conventions. Do not guess between multiple plausible folders.
3. Use `<feature-folder>/WORK-HANDOFF.md` unless the repository defines an equivalent feature-local name.
4. Respect every mandatory repository read rule. When those rules permit selective loading, read the handoff before broader feature history, then read only its `Read first` paths and the evidence needed for the current phase.

## Choose The Operation

### Resume

Use this path when the user says to continue or resume a named feature.

1. Check whether the feature-local handoff exists. If it does not, report that no handoff was saved and continue through the active authoring skill from canonical documents and the project work plan. Do not invent a retrospective handoff.
2. Read the existing handoff when present.
3. Verify that every referenced path still exists and that its stated phase agrees with canonical documents and the work plan.
4. Treat canonical documents as authoritative when they conflict with the handoff. Repair the stale handoff before relying on it.
5. Read the listed inputs in order, inspect relevant working-tree state, and continue from `Exact next step`.
6. Do not reread raw transcripts or the entire feature history unless the handoff or current evidence shows that it is necessary.

### Pause Or Refresh

Create or update the handoff only when at least one condition holds:

- the human explicitly ends or pauses the session while feature work is incomplete;
- the current phase cannot safely reach its next atomic checkpoint in the remaining context;
- a blocker pauses incomplete work;
- the human and Claude intentionally move an unfinished phase or its review loop to a fresh session.

Do not create or refresh it after every turn. Do not create one merely to announce the next normal phase when accepted canonical documents and the work plan already make that phase obvious.

Before stopping, finish the nearest safe atomic action: persist an internally consistent draft, leave any active external process finished or safely resumable within current authority, and make the working tree understandable. Never stretch into a new review, migration, or mutation just to use the remaining context.

### Close

Remove the handoff when the paused phase is complete and canonical documents plus the project work plan make the next action unambiguous. Also remove it when the feature itself is complete. Report the removal; do not retain an archival copy or move it into project knowledge.

## Context Capacity

Use only a host-provided context indicator as numerical evidence. In Claude Code, inspect the available context/token display when accessible — the `/context` view or the configured status line; when only the human can see it, ask them to check it. Never invent a remaining-token count or percentage from conversation length.

At a major boundary, especially before a complete cross-model review, decide whether the next atomic phase can finish with comfortable margin. A review includes the initial reviewer call, author corrections, human decisions, and a full reviewer recheck. If capacity is doubtful, create or refresh the handoff and recommend a fresh Claude session in the same repository. A fresh session is preferable to resume/fork when the purpose is to discard old conversational context.

This skill does not install hooks, plugins, timers, or automatic session termination.

## Handoff Contract

Keep the file direct and normally within roughly 1,000-2,000 tokens. Use this structure, omitting empty optional fields:

```markdown
# Work handoff: <feature>

Updated: <date/time or date>
Phase: <feature-design|implementation-design|delivery-plan|security-review|other>
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

## Content Boundaries

- Link to the PRD, implementation design, delivery plan, decisions, and work plan; do not duplicate their contents.
- Record accepted inputs and exact continuation state, not a narrative session summary.
- Never store raw model transcripts, cross-model finding inventories, chain-of-thought, credentials, tokens, or generated authentication state.
- Keep the handoff local and ephemeral. Do not stage, commit, publish, or archive it; do not edit ignore rules merely to hide it.
- Preserve relevant user changes and distinguish them from Claude changes.
- Keep unresolved human decisions explicit. Do not convert them into assumptions for the next session.
- Replace stale content instead of appending a chronological journal.

## Completion

For `resume`, report the verified phase and exact action being continued. For `pause`, report the handoff path and tell the human that the safe continuation is a fresh Claude session in the same repository followed by "continue <feature>". For `close`, report that the ephemeral handoff was removed and name the canonical source that now carries the next state.
</content>
</invoke>
