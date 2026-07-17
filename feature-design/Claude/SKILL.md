---
name: feature-design
description: Turn an initial product idea, requested capability, or change into a human-approved business-led PRD through an adaptive guided conversation. Use when the user says they want to create, define, explore, or update a feature or version; when Claude must clarify users, outcomes, scenarios, scope, non-goals, MVP, acceptance criteria, assumptions, architecture horizon, and open product decisions; or when deciding whether requested work is a feature versus a fix. Stop after cross-model PRD review and human approval. Do not create implementation design, task decomposition, dependencies, execution profiles, or tracker issues.
---

# Feature Design

Create an approved PRD through a natural human-guided conversation. Preserve business meaning and defer technical design and delivery planning to later skills.

Read the target repository's instructions and canonical context before asking questions. Read `references/prd-contract.md` completely before drafting.

## Session Continuity

When continuing an existing named feature, check for a feature-local `WORK-HANDOFF.md` through the `feature-context-handoff` skill (invoked via the Skill tool as `/feature-context-handoff`) after reading mandatory repository instructions. Use it to locate the active draft and exact next question; do not use it as product truth.

At a major phase boundary, use only the host-provided context indicator (the Claude Code `/context` view or status line) when available. If the PRD phase or its complete review loop cannot safely finish in the remaining context, invoke the `feature-context-handoff` skill, stop at the nearest coherent checkpoint, and recommend a fresh session. Do not estimate a percentage and do not install automatic monitoring.

## Conversation Workflow

1. Absorb everything the human has already said. Do not ask them to repeat it.
2. Summarize the feature in plain language: intended user, problem, desired outcome, likely current-version boundary, and known constraints.
3. Identify only the highest-impact unknowns. Ask one focused question at a time unless a small tightly related group is easier to answer together.
4. Adapt the next question to the previous answer. Do not run a fixed questionnaire or expose a template as an interrogation checklist.
5. Distinguish business requirements from implementation suggestions. Record useful technical ideas as constraints or open assumptions without turning them into architecture.
6. Classify the request provisionally as `large_feature`, `small_feature`, or `fix`. Ask the human when the distinction changes workflow or scope.
7. Draft the complete PRD once enough meaning is known. Resolve every required section, remove placeholders, and record every known unresolved human decision in the document. Show the human a concise summary of inferred decisions and remaining gaps.
8. Treat the PRD as review-ready only when the full artifact is self-contained and marked `draft` or `proposed`. Confirm that the human wants the complete draft reviewed; an explicit review request already made in the current conversation counts. Check that enough session context remains for the initial review, corrections, human resolution, and full recheck. Otherwise invoke the `feature-context-handoff` skill (via the Skill tool as `/feature-context-handoff`) and move the review to a fresh session.
9. Invoke the `cross-model-review` skill (via the Skill tool, `/cross-model-review`) with the `prd` profile. Keep the current session as author, let GPT challenge the full draft, prepare supported corrections, and recheck the whole corrected document in the same GPT reviewer session.
10. Surface every remaining material and minor disagreement to the human. Apply the final consolidated patch only after the human chooses what to fix or accept as-is.
11. Mark the PRD accepted only after explicit human approval. Remove any obsolete `WORK-HANDOFF.md` through the `feature-context-handoff` skill when canonical documents and the work plan make the next phase clear. End with a handoff to the `implementation-design` skill (via the Skill tool, `/implementation-design`); do not continue into implementation or task planning in this skill.

## Question Priorities

Prefer questions that resolve:

- who experiences the problem and who receives value;
- current behavior and why it is insufficient;
- desired scenarios and observable outcomes;
- current-version/MVP scope and explicit non-goals;
- acceptance and failure behavior;
- constraints and assumptions that affect product meaning;
- architecture horizon that today's work must not block;
- unresolved product decisions.

Skip questions already answered by the conversation or canonical docs. If the human cannot answer yet, record an open decision instead of inventing one.

## PRD Output

Produce one canonical Markdown draft in the target repository's existing feature-document location and naming scheme, not JSON and not only chat prose. Adapt headings when equivalent canonical sections already exist, while preserving the semantic contract in `references/prd-contract.md`.

Mark the document draft/proposed until cross-model review and human approval complete. Do not put model findings, review transcripts, technical task breakdowns, or speculative implementation plans in the PRD.

## Boundaries

- Do not create an implementation document.
- Do not decompose into tasks or dependencies.
- Do not choose executors, models, validation profiles, branches, or merge strategy.
- Do not run security approval; security review follows technical design and task planning.
- Do not publish or update tracker issues.
- Do not implement code.

## Completion

Report the accepted PRD path, feature/fix classification, resolved product decisions, remaining explicitly deferred questions, cross-model review outcome, and readiness for the `implementation-design` skill.
