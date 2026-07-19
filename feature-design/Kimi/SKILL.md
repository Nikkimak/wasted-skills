---
name: feature-design
description: Create or revise a human-approved business-led PRD through an adaptive guided conversation. Use when the user wants to define, explore, or update a feature or version; when Kimi must clarify users, outcomes, scenarios, scope, non-goals, MVP, acceptance criteria, assumptions, architecture horizon, and open product decisions; or when deciding whether requested work is a feature versus a fix. Once the PRD is complete, recommend for or against cross-model review, ask the human, and invoke it only with explicit approval. Do not create implementation design, task decomposition, dependencies, execution profiles, or tracker issues.
---

# Feature Design

Read the target repository's instructions and canonical context before asking questions. Read `${KIMI_SKILL_DIR}/references/prd-contract.md` completely before drafting.

For an existing named feature, use the `feature-context-handoff` skill (via the Skill tool, `/skill:feature-context-handoff`) to locate unfinished work; canonical documents remain authoritative.

## Workflow

1. Absorb what the human and canonical docs already establish. Summarize the intended user, problem, desired outcome, likely current-version boundary, and known constraints.
2. Ask one focused question at a time, adapting each to prior answers; do not repeat known information or use a fixed questionnaire. Prioritize users and value, current-behavior gaps, scenarios and outcomes, MVP scope and non-goals, acceptance and failure behavior, constraints and assumptions, owner-supplied dependencies, the architecture horizon, and unresolved product decisions; record unanswerable choices as open decisions instead of inventing them.
3. Keep business requirements separate from implementation suggestions, recording technical ideas as constraints or open assumptions rather than architecture. Classify provisionally as `large_feature`, `small_feature`, or `fix`, asking the human only when the distinction changes scope or workflow.
4. Draft one complete proposed PRD using `${KIMI_SKILL_DIR}/references/prd-contract.md`: remove placeholders, record known human/external dependencies without designing their technical handling, and summarize inferred decisions and remaining gaps. When revising an accepted PRD, preserve its baseline, identify existing downstream artifacts affected by the change, and report which require reassessment; do not edit them in this skill.
5. Once the PRD is self-contained and `draft` or `proposed`, assess whether cross-model review is worth the added cost. Ask the human whether to run it and give a concise recommendation with reasons. Recommend it for material ambiguity, broad or risky scope, or complex changes to an accepted PRD; a small feature may receive a recommendation to skip. Never invoke review before explicit human approval; an earlier clear request for this PRD counts.
6. If approved, invoke the `cross-model-review` skill (via the Skill tool, `/skill:cross-model-review`) with the `prd` profile, evaluate every finding, prepare supported corrections, and surface remaining disagreements. If declined, proceed without it. Before an approved review, check `/usage` and invoke the `feature-context-handoff` skill (`/skill:feature-context-handoff`) if the full review-and-recheck loop cannot fit safely.
7. After the review decision and any approved review, obtain explicit human approval of the PRD before marking or applying it as accepted. Close any obsolete `WORK-HANDOFF.md` through the `feature-context-handoff` skill (`/skill:feature-context-handoff`) and end with a handoff to the `implementation-design` skill (`/skill:implementation-design`).

## PRD Output

Produce one canonical Markdown document in the repository's existing feature-document location, naming, and section conventions. Keep findings and transcripts ephemeral and implementation or task detail out of the PRD.

## Boundaries

- Do not create implementation/security design, tasks, dependencies, execution choices, branches, merge strategy, tracker issues, or code; the `implementation-design` skill owns the technical and security contract.
- Do not let technical suggestions silently change product scope.

## Completion

Report the accepted PRD path, feature/fix classification, resolved product decisions, affected downstream artifacts, remaining explicitly deferred questions, cross-model review decision and outcome, and readiness for the `implementation-design` skill.
