---
name: feature-design
description: Turn an initial product idea, requested capability, or change into a human-approved business-led PRD through an adaptive guided conversation. Use when the user says they want to create, define, explore, or update a feature or version; when Claude must clarify users, outcomes, scenarios, scope, non-goals, MVP, acceptance criteria, assumptions, architecture horizon, and open product decisions; or when deciding whether requested work is a feature versus a fix. Stop after cross-model PRD review and human approval. Do not create implementation design, task decomposition, dependencies, execution profiles, or tracker issues.
---

# Feature Design

Turn a product idea into an approved PRD through an adaptive human-guided conversation. Preserve business meaning; defer technical design and delivery to later skills.

Read the target repository's instructions and canonical context before asking questions. Read `references/prd-contract.md` completely before drafting.

## Session Continuity

For an existing named feature, use the `feature-context-handoff` skill (via the Skill tool, `/feature-context-handoff`) to locate unfinished work and the next question; canonical documents remain authoritative. That skill also owns context-capacity judgment and checkpointing before an atomic review loop.

## Workflow

1. Absorb what the human and canonical docs already establish. Summarize the intended user, problem, desired outcome, likely current-version boundary, and known constraints without asking them to repeat it.
2. Ask only the highest-value unanswered questions, one focused question (or a small related group) at a time, adapting each to prior answers. Do not run a fixed questionnaire; record unanswered material choices as open decisions. Prioritize who has the problem and who receives value, current vs desired behavior and observable outcomes, MVP scope and non-goals, acceptance and failure behavior, product-affecting constraints and assumptions, owner-supplied dependencies (assets, data, access, approvals, budgets, validation), architecture horizon, and unresolved product decisions.
3. Keep business requirements separate from implementation suggestions; record useful technical ideas as constraints or assumptions, not architecture. Classify the work provisionally as `large_feature`, `small_feature`, or `fix`, asking the human only when the distinction changes scope or workflow.
4. Draft one complete canonical PRD using `references/prd-contract.md`. Remove placeholders, record known human/external dependencies as product constraints without designing their handling, and show a concise summary of inferred decisions and remaining gaps.
5. Treat the PRD as review-ready only when the self-contained artifact is `draft` or `proposed` and the human has confirmed full review (an explicit request already made in this conversation counts). If the initial review, corrections, human decisions, and full recheck cannot fit safely, invoke the `feature-context-handoff` skill before review and continue in a fresh session.
6. Invoke the `cross-model-review` skill (via the Skill tool, `/cross-model-review`) with the `prd` profile. Keep this session as author; let GPT challenge the full draft; prepare supported corrections and recheck the whole corrected document in the same reviewer session.
7. Surface every remaining material and minor disagreement; apply one consolidated patch only after the human resolves them.
8. Mark the PRD accepted only after explicit human approval. Close any obsolete `WORK-HANDOFF.md` through the `feature-context-handoff` skill and end with readiness for the `implementation-design` skill (via the Skill tool, `/implementation-design`).

## PRD Output

Produce one canonical Markdown draft in the repository's existing feature-document structure and naming (not JSON, not only chat prose), preserving the semantic contract in `references/prd-contract.md`. Keep findings and transcripts ephemeral; keep implementation or task detail out of the PRD.

## Boundaries

- Do not create implementation/security design, tasks, dependencies, execution or validation choices, branches, merge strategy, tracker changes, or code.
- Do not let technical suggestions silently change product scope; the `implementation-design` skill owns the technical and security contract.

## Completion

Report the accepted PRD path, feature/fix classification, resolved product decisions, remaining explicitly deferred questions, cross-model review outcome, and readiness for the `implementation-design` skill.
