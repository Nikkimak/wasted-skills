---
name: implementation-design
description: Create or revise the smallest sufficient security-aware technical design from an approved PRD, or conclude that no document or accepted-contract change is needed. Use after PRD approval to define shared architecture, contracts, failure/recovery, verification, prerequisites, and only new or changed security obligations. Classify security from the material delta, not the feature domain; create a document only when shared meaning changes, and run cross-model review only with explicit approval. Do not create tasks, issues, or code.
---

# Implementation Design

Read the target repository's instructions, accepted PRD, current architecture, runtime map, and relevant decisions. Read `${KIMI_SKILL_DIR}/references/implementation-contract.md` completely.

For unfinished named work, use the `feature-context-handoff` skill (via the Skill tool, `/skill:feature-context-handoff`); canonical artifacts override it.

## Workflow

1. Bind to the exact accepted PRD and any accepted implementation baseline; identify the requested technical and security delta before choosing an artifact.
2. Return `implementation_change_not_required` when the accepted design or no-document result remains valid and no shared technical/security contract changes. Cite the baseline, report affected delivery artifacts, route to existing remediation or the `feature-delivery-plan` skill (`/skill:feature-delivery-plan`), and do not edit, review, or reapprove the implementation artifact. If this distinction is materially ambiguous, ask the human one focused question instead of defaulting to a document.
3. Return `implementation_doc_not_required` when one bounded task can own all notes and no new or changed shared contract/security decision exists. Present its reason and planning constraints for explicit human approval, then hand off to the `feature-delivery-plan` skill (`/skill:feature-delivery-plan`); do not offer cross-model review.
4. Otherwise create or amend the smallest design needed for shared contracts, data/migrations, integrations, recovery/rollout, material trust boundaries, or whole-feature verification. Cover only affected meaning, reference unchanged baseline once, and use `${KIMI_SKILL_DIR}/references/implementation-contract.md`.
5. Classify security depth from the delta as `quick`, `standard`, or `deep`; existing payment, identity, sensitive-data, privilege, tenant, or destructive behavior alone does not make a change `deep`. Add stable IDs only for new or changed controls and verification. Never record secret values or sensitive payloads.
6. Ask only about material unsupported technical or risk decisions; return product changes to the `feature-design` skill (`/skill:feature-design`). For a `deep` delta or an explicit human request, invoke the `feature-security-review` skill (`/skill:feature-security-review`) and incorporate confirmed requirements; it is not a later delivery gate.
7. Make any document self-contained and `draft` or `proposed`, with every open human decision explicit. Recommend cross-model review only for material uncertainty, broad impact, or complex revision; ask the human before invoking the `cross-model-review` skill (`/skill:cross-model-review`) with the `implementation` profile, and check `/usage` and invoke the `feature-context-handoff` skill (`/skill:feature-context-handoff`) first if the full review-and-recheck loop cannot fit safely. Never invoke review before explicit approval; an earlier clear request for this document counts.
8. After the review decision and any approved review, obtain explicit human approval of the technical and security posture, close obsolete handoff state, and hand off to the `feature-delivery-plan` skill (`/skill:feature-delivery-plan`).

## Boundaries

- Do not change accepted business scope, create task graphs, choose executors, publish issues, or implement code.
- Keep durable security controls in the implementation design, not a separate report.

## Completion

Report `implementation_change_not_required`, `implementation_doc_not_required`, or the accepted design path; the bound PRD/baseline, material delta, security depth, changed decisions and control IDs, affected delivery artifacts, known execution prerequisites, remaining human decisions, cross-model review outcome when applicable, and readiness for the `feature-delivery-plan` skill.
