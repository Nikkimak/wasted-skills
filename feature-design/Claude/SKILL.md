---
name: feature-design
description: Create or revise a human-approved business-led PRD through an adaptive guided conversation. Use when the user wants to define, explore, or update a feature or version; when Claude must clarify users, outcomes, scenarios, scope, non-goals, MVP, acceptance criteria, assumptions, architecture horizon, and open product decisions; or when deciding whether requested work is a feature versus a fix. Once the PRD is complete, recommend for or against cross-model review, ask the human, and invoke it only with explicit approval. Do not create implementation design, task decomposition, dependencies, execution profiles, or tracker issues.
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
4. Draft one complete proposed PRD using `references/prd-contract.md`. Remove placeholders, record known human/external dependencies as product constraints without designing their handling, and show a concise summary of inferred decisions and remaining gaps. When revising an accepted PRD, preserve its baseline, identify existing downstream artifacts affected by the change, and report which require reassessment; do not edit them in this skill.
5. Once the PRD is self-contained and `draft` or `proposed`, assess whether cross-model review is worth the added cost. Ask the human whether to run it and give a concise recommendation with reasons. Recommend it for material ambiguity, broad or risky scope, or complex changes to an accepted PRD; a small feature may receive a recommendation to skip. Never invoke review before explicit human approval; an earlier clear request for this PRD counts.
6. If approved, invoke the `cross-model-review` skill (via the Skill tool, `/cross-model-review`) with the `prd` profile, verify findings, prepare supported corrections, and surface remaining disagreements. If declined, proceed without it. Before an approved review, use the `feature-context-handoff` skill if the full review-and-recheck loop cannot fit safely.
7. After the review decision and any approved review, obtain explicit human approval of the PRD before marking or applying it as accepted. Close any obsolete `WORK-HANDOFF.md` through the `feature-context-handoff` skill and end with readiness for the `implementation-design` skill (via the Skill tool, `/implementation-design`).

## PRD Output

Produce one canonical Markdown draft in the repository's existing feature-document structure and naming (not JSON, not only chat prose), preserving the semantic contract in `references/prd-contract.md`. Keep findings and transcripts ephemeral; keep implementation or task detail out of the PRD.

## Boundaries

- Do not create implementation/security design, tasks, dependencies, execution or validation choices, branches, merge strategy, tracker changes, or code.
- Do not let technical suggestions silently change product scope; the `implementation-design` skill owns the technical and security contract.

## Completion

Report the accepted PRD path, feature/fix classification, resolved product decisions, affected downstream artifacts, remaining explicitly deferred questions, cross-model review decision and outcome, and readiness for the `implementation-design` skill.
