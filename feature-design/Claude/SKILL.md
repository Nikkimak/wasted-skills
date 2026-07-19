---
name: feature-design
description: Triage product changes and create or revise a human-approved business-led PRD only when product meaning changes. Use when the user wants to define, explore, or update a feature or version; when Claude must clarify users, outcomes, scenarios, scope, non-goals, MVP, acceptance criteria, assumptions, architecture horizon, and open product decisions; or when deciding whether requested work is a feature, a fix restoring accepted behavior, or a non-product correction. Keep fixes lightweight, ask the human one focused question when classification is materially ambiguous, and run cross-model review only for a complete PRD with explicit approval. Do not create implementation design, task decomposition, dependencies, execution profiles, tracker issues, or code.
---

# Feature Design

Turn a product idea into an approved PRD through an adaptive human-guided conversation. Preserve business meaning; defer technical design and delivery to later skills.

Read the target repository's instructions and canonical context before asking questions. Read `references/prd-contract.md` completely before drafting.

## Session Continuity

For an existing named feature, use the `feature-context-handoff` skill (via the Skill tool, `/feature-context-handoff`) to locate unfinished work and the next question; canonical documents remain authoritative. That skill also owns context-capacity judgment and checkpointing before an atomic review loop.

## Workflow

1. Absorb what the human and canonical docs already establish. Summarize only what is useful for deciding whether product meaning changes; do not force feature discovery onto an apparent correction.
2. Triage before drafting or asking broad questions:
   - Return `prd_not_applicable` when the work changes no observable product behavior or accepted requirement, such as internal cleanup or repository-document formatting and spelling that preserve accepted meaning. Do not create or edit a PRD, ask about review, or request PRD approval; identify the appropriate repository workflow and stop.
   - Classify as `fix` only when canonical accepted evidence establishes the intended behavior and the request restores it. Return `prd_change_not_required`, cite that evidence, identify affected downstream artifacts, and do not create or edit a PRD, ask about review, or request PRD reapproval. Route to existing remediation or the `feature-delivery-plan` skill (via the Skill tool, `/feature-delivery-plan`) when accepted upstream inputs remain valid; route to the `implementation-design` skill only when a shared technical/security contract may change or its required accepted input is missing.
   - Continue with PRD discovery when observable product meaning, scope, acceptance, or failure behavior changes, classifying it provisionally as `large_feature` or `small_feature`.
   - If the available evidence cannot distinguish these outcomes and the distinction changes the workflow, ask the human one concise, focused question. Continue from the answer; do not default to the full PRD path.
3. For PRD work, summarize the intended user, problem, desired outcome, likely current-version boundary, and known constraints without asking the human to repeat it. Then ask only the highest-value unanswered questions, one focused question (or a small related group) at a time, adapting each to prior answers. Do not run a fixed questionnaire; record unanswered material choices as open decisions. Prioritize who has the problem and who receives value, current vs desired behavior and observable outcomes, MVP scope and non-goals, acceptance and failure behavior, product-affecting constraints and assumptions, owner-supplied dependencies (assets, data, access, approvals, budgets, validation), architecture horizon, and unresolved product decisions.
4. Keep business requirements separate from implementation suggestions; record useful technical ideas as constraints or assumptions, not architecture. Draft one complete proposed PRD using `references/prd-contract.md`. Remove placeholders, record known human/external dependencies as product constraints without designing their handling, and show a concise summary of inferred decisions and remaining gaps. When revising an accepted PRD, preserve its baseline, change only the affected product meaning, identify existing downstream artifacts affected by the change, and report which require reassessment; do not edit them in this skill.
5. Once the PRD is self-contained and `draft` or `proposed`, assess whether cross-model review is worth the added cost. Ask the human whether to run it and give a concise recommendation with reasons. Recommend it for material ambiguity, broad or risky scope, or complex changes to an accepted PRD; recommend skipping it for a small, clear, low-risk PRD change. Never invoke review before explicit human approval; an earlier clear request for this PRD counts.
6. If approved, invoke the `cross-model-review` skill (via the Skill tool, `/cross-model-review`) with the `prd` profile, verify findings, prepare supported corrections, and surface remaining disagreements. If declined, proceed without it. Before an approved review, use the `feature-context-handoff` skill if the full review-and-recheck loop cannot fit safely.
7. After the review decision and any approved review, obtain explicit human approval of the PRD before marking or applying it as accepted. Close any obsolete `WORK-HANDOFF.md` through the `feature-context-handoff` skill and end with readiness for the `implementation-design` skill (via the Skill tool, `/implementation-design`).

## PRD Output

For a triage result, produce no PRD artifact. Otherwise produce one canonical Markdown draft in the repository's existing feature-document structure and naming (not JSON, not only chat prose), preserving the semantic contract in `references/prd-contract.md`. Keep findings and transcripts ephemeral; keep implementation or task detail out of the PRD.

## Boundaries

- Do not create implementation/security design, tasks, dependencies, execution or validation choices, branches, merge strategy, tracker changes, or code.
- Do not let technical suggestions silently change product scope; the `implementation-design` skill owns the technical and security contract.

## Completion

For `prd_not_applicable`, report why no product artifact changes and the next repository workflow. For `prd_change_not_required`, report the accepted-behavior evidence, affected downstream artifacts, and the lightest valid next stage. For PRD work, report the accepted PRD path, feature classification, resolved product decisions, affected downstream artifacts, remaining explicitly deferred questions, cross-model review decision and outcome, and readiness for the `implementation-design` skill.
