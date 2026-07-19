---
name: feature-design
description: Triage product changes and create or revise a human-approved business-led PRD only when product meaning changes. Use when the user wants to define, explore, or update a feature or version; when Kimi must clarify users, outcomes, scenarios, scope, non-goals, MVP, acceptance criteria, assumptions, architecture horizon, and open product decisions; or when deciding whether requested work is a feature, a fix restoring accepted behavior, or a non-product correction. Keep fixes lightweight, ask the human one focused question when classification is materially ambiguous, and run cross-model review only for a complete PRD with explicit approval. Do not create implementation design, task decomposition, dependencies, execution profiles, tracker issues, or code.
---

# Feature Design

Read the target repository's instructions and canonical context before asking questions. Read `${KIMI_SKILL_DIR}/references/prd-contract.md` completely before drafting.

For an existing named feature, use the `feature-context-handoff` skill (via the Skill tool, `/skill:feature-context-handoff`) to locate unfinished work; canonical documents remain authoritative.

## Workflow

1. Absorb what the human and canonical docs already establish. Summarize only what is useful for deciding whether product meaning changes; do not force feature discovery onto an apparent correction.
2. Triage before drafting or asking broad questions:
   - Return `prd_not_applicable` when the work changes no observable product behavior or accepted requirement, such as internal cleanup or repository-document formatting and spelling that preserve accepted meaning. Do not create or edit a PRD, ask about review, or request PRD approval; identify the appropriate repository workflow and stop.
   - Classify as `fix` only when canonical accepted evidence establishes the intended behavior and the request restores it. Return `prd_change_not_required`, cite that evidence, identify affected downstream artifacts, and do not create or edit a PRD, ask about review, or request PRD reapproval. Route to existing remediation or the `feature-delivery-plan` skill (via the Skill tool, `/skill:feature-delivery-plan`) when accepted upstream inputs remain valid; route to the `implementation-design` skill only when a shared technical/security contract may change or its required accepted input is missing.
   - Continue with PRD discovery when observable product meaning, scope, acceptance, or failure behavior changes, classifying it provisionally as `large_feature` or `small_feature`.
   - If the available evidence cannot distinguish these outcomes and the distinction changes the workflow, ask the human one concise, focused question. Continue from the answer; do not default to the full PRD path.
3. For PRD work, summarize the intended user, problem, desired outcome, likely current-version boundary, and known constraints without asking the human to repeat it. Then ask one focused question at a time, adapting each to prior answers; do not repeat known information or use a fixed questionnaire. Prioritize users and value, current-behavior gaps, scenarios and outcomes, MVP scope and non-goals, acceptance and failure behavior, constraints and assumptions, owner-supplied dependencies, the architecture horizon, and unresolved product decisions; record unanswerable choices as open decisions instead of inventing them.
4. Keep business requirements separate from implementation suggestions, recording technical ideas as constraints or open assumptions rather than architecture. Draft one complete proposed PRD using `${KIMI_SKILL_DIR}/references/prd-contract.md`: remove placeholders, record known human/external dependencies without designing their technical handling, and summarize inferred decisions and remaining gaps. When revising an accepted PRD, preserve its baseline, change only the affected product meaning, identify existing downstream artifacts affected by the change, and report which require reassessment; do not edit them in this skill.
5. Once the PRD is self-contained and `draft` or `proposed`, assess whether cross-model review is worth the added cost. Ask the human whether to run it and give a concise recommendation with reasons. Recommend it for material ambiguity, broad or risky scope, or complex changes to an accepted PRD; recommend skipping it for a small, clear, low-risk PRD change. Never invoke review before explicit human approval; an earlier clear request for this PRD counts.
6. If approved, invoke the `cross-model-review` skill (via the Skill tool, `/skill:cross-model-review`) with the `prd` profile, evaluate every finding, prepare supported corrections, and surface remaining disagreements. If declined, proceed without it. Before an approved review, check `/usage` and invoke the `feature-context-handoff` skill (`/skill:feature-context-handoff`) if the full review-and-recheck loop cannot fit safely.
7. After the review decision and any approved review, obtain explicit human approval of the PRD before marking or applying it as accepted. Close any obsolete `WORK-HANDOFF.md` through the `feature-context-handoff` skill (`/skill:feature-context-handoff`) and end with a handoff to the `implementation-design` skill (`/skill:implementation-design`).

## PRD Output

For a triage result, produce no PRD artifact. Otherwise produce one canonical Markdown document in the repository's existing feature-document location, naming, and section conventions. Keep findings and transcripts ephemeral and implementation or task detail out of the PRD.

## Boundaries

- Do not create implementation/security design, tasks, dependencies, execution choices, branches, merge strategy, tracker issues, or code; the `implementation-design` skill owns the technical and security contract.
- Do not let technical suggestions silently change product scope.

## Completion

For `prd_not_applicable`, report why no product artifact changes and the next repository workflow. For `prd_change_not_required`, report the accepted-behavior evidence, affected downstream artifacts, and the lightest valid next stage. For PRD work, report the accepted PRD path, feature classification, resolved product decisions, affected downstream artifacts, remaining explicitly deferred questions, cross-model review decision and outcome, and readiness for the `implementation-design` skill.
