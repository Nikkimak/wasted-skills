---
name: feature-design
description: Turn an initial product idea, requested capability, or change into a human-approved business-led PRD through an adaptive guided conversation. Use when the user says they want to create, define, explore, or update a feature or version; when Kimi must clarify users, outcomes, scenarios, scope, non-goals, MVP, acceptance criteria, assumptions, architecture horizon, and open product decisions; or when deciding whether requested work is a feature versus a fix. Stop after cross-model PRD review and human approval. Do not create implementation design, task decomposition, dependencies, execution profiles, or tracker issues.
---

# Feature Design

Read the target repository's instructions and canonical context before asking questions. Read `${KIMI_SKILL_DIR}/references/prd-contract.md` completely before drafting.

For an existing named feature, use the `feature-context-handoff` skill (via the Skill tool, `/skill:feature-context-handoff`) to locate unfinished work; canonical documents remain authoritative.

## Workflow

1. Absorb what the human and canonical docs already establish. Summarize the intended user, problem, desired outcome, likely current-version boundary, and known constraints.
2. Ask one focused question at a time, adapting each to prior answers; do not repeat known information or use a fixed questionnaire. Prioritize users and value, current-behavior gaps, scenarios and outcomes, MVP scope and non-goals, acceptance and failure behavior, constraints and assumptions, owner-supplied dependencies, the architecture horizon, and unresolved product decisions; record unanswerable choices as open decisions instead of inventing them.
3. Keep business requirements separate from implementation suggestions, recording technical ideas as constraints or open assumptions rather than architecture. Classify provisionally as `large_feature`, `small_feature`, or `fix`, asking the human only when the distinction changes scope or workflow.
4. Draft one complete canonical PRD using `${KIMI_SKILL_DIR}/references/prd-contract.md`: remove placeholders, record known human/external dependencies without designing their technical handling, and summarize inferred decisions and remaining gaps.
5. Confirm full review once the artifact is self-contained and marked `draft` or `proposed`. Check with `/usage`, not estimates or monitoring, that review, corrections, human decisions, and full recheck fit safely; otherwise invoke the `feature-context-handoff` skill (`/skill:feature-context-handoff`) and continue in a fresh session.
6. Invoke the `cross-model-review` skill (via the Skill tool, `/skill:cross-model-review`) with the `prd` profile. Evaluate every finding, prepare supported corrections, surface remaining material or minor disagreements, and apply one consolidated patch after the human resolves them.
7. Mark the PRD accepted only after explicit human approval. Close any obsolete `WORK-HANDOFF.md` through the `feature-context-handoff` skill (`/skill:feature-context-handoff`) and end with a handoff to the `implementation-design` skill (`/skill:implementation-design`).

## PRD Output

Produce one canonical Markdown document in the repository's existing feature-document location, naming, and section conventions. Keep findings and transcripts ephemeral and implementation or task detail out of the PRD.

## Boundaries

- Do not create implementation/security design, tasks, dependencies, execution choices, branches, merge strategy, tracker issues, or code; the `implementation-design` skill owns the technical and security contract.
- Do not let technical suggestions silently change product scope.

## Completion

Report the accepted PRD path, feature/fix classification, resolved product decisions, remaining explicitly deferred questions, cross-model review outcome, and readiness for the `implementation-design` skill.
