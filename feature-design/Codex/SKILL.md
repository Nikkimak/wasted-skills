---
name: feature-design
description: Turn an initial product idea, requested capability, or change into a human-approved business-led PRD through an adaptive guided conversation. Use when the user says they want to create, define, explore, or update a feature or version; when Codex must clarify users, outcomes, scenarios, scope, non-goals, MVP, acceptance criteria, assumptions, architecture horizon, and open product decisions; or when deciding whether requested work is a feature versus a fix. Stop after cross-model PRD review and human approval. Do not create implementation design, task decomposition, dependencies, execution profiles, or tracker issues.
---

# Feature Design

Read the target repository's instructions and canonical context before asking questions. Read `references/prd-contract.md` completely before drafting.

For an existing named feature, use `$feature-context-handoff` to locate unfinished work; canonical documents remain authoritative.

## Workflow

1. Absorb what the human and canonical docs already establish. Summarize the intended user, problem, desired outcome, likely current-version boundary, and known constraints.
2. Ask only the highest-value unanswered questions, adapting each to prior answers. Do not repeat known information or use a fixed questionnaire; record unanswered material choices as open decisions.
3. Keep business requirements separate from implementation suggestions. Classify the work provisionally as `large_feature`, `small_feature`, or `fix`, asking the human only when the distinction changes scope or workflow.
4. Draft one complete canonical PRD using `references/prd-contract.md`. Remove placeholders, include known human/external dependencies without designing their technical handling, and summarize inferred decisions and remaining gaps.
5. Confirm full review when the self-contained artifact is `draft` or `proposed`. If the initial review, corrections, human decisions, and full recheck cannot fit safely, use `$feature-context-handoff` before review and continue in a fresh session.
6. Invoke `$cross-model-review` with the `prd` profile. Evaluate every finding, prepare supported corrections, and surface remaining material or minor disagreements. Apply one consolidated patch after the human resolves them.
7. Mark the PRD accepted only after explicit human approval. Close any obsolete handoff and end with readiness for `$implementation-design`.

## PRD Output

Produce one canonical Markdown document in the repository's existing feature-document structure. Keep findings and transcripts ephemeral and keep implementation or task detail out of the PRD.

## Boundaries

- Do not create implementation/security design, tasks, execution choices, branches, merge strategy, tracker changes, or code.
- Do not let technical suggestions silently change product scope.

## Completion

Report the accepted PRD path, feature/fix classification, resolved product decisions, remaining explicitly deferred questions, cross-model review outcome, and readiness for `$implementation-design`.
