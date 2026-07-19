---
name: implementation-design
description: Create or revise the smallest sufficient security-aware technical design from an approved PRD, or conclude that no document or accepted-contract change is needed. Use after PRD approval to define shared architecture, contracts, failure/recovery, verification, prerequisites, and only new or changed security obligations. Classify security from the material delta, not the feature domain; create a document only when shared meaning changes, and run cross-model review only with explicit approval. Do not create tasks, issues, or code.
---

# Implementation Design

Read the target repository's instructions, accepted PRD, current architecture, runtime map, and relevant decisions. Read `references/implementation-contract.md` completely.

For unfinished named work, use `$feature-context-handoff`; canonical artifacts override it.

## Workflow

1. Bind to the exact accepted PRD and any accepted implementation baseline; identify the requested technical and security delta before choosing an artifact.
2. Return `implementation_change_not_required` when the accepted design or no-document result remains valid and no shared technical/security contract changes. Cite the baseline, report affected delivery artifacts, route to existing remediation or `$feature-delivery-plan`, and do not edit, review, or reapprove the implementation artifact. If this distinction is materially ambiguous, ask the human one focused question instead of defaulting to a document.
3. Return `implementation_doc_not_required` when one bounded task can own all notes and no new or changed shared contract/security decision exists. Present its reason and planning constraints for explicit approval, then hand off to `$feature-delivery-plan`; do not offer review.
4. Otherwise create or amend the smallest design needed for shared contracts, data/migrations, integrations, recovery/rollout, material trust boundaries, or whole-feature verification. Cover only affected meaning, reference unchanged baseline once, and use `references/implementation-contract.md`.
5. Classify security depth from the delta as `quick`, `standard`, or `deep`; existing payment, identity, sensitive-data, privilege, tenant, or destructive behavior alone does not make a change `deep`. Add stable IDs only for new or changed controls and verification. Never record secrets or sensitive payloads.
6. Ask only about material unsupported technical or risk decisions; return product changes to `$feature-design`. For `deep` delta or explicit human request, invoke `$feature-security-review`.
7. Make any document self-contained and `draft` or `proposed`. Recommend review only for material uncertainty, broad impact, or complex revision; ask before `$cross-model-review`, and use `$feature-context-handoff` first if the full loop cannot fit.
8. After the review decision and any approved review, obtain explicit human approval, close obsolete handoff state, and hand off to `$feature-delivery-plan`.

## Boundaries

- Do not change accepted business scope, create task graphs, choose executors, publish issues, or implement code.
- Keep durable security controls in the implementation design, not a separate report.

## Completion

Report `implementation_change_not_required`, `implementation_doc_not_required`, or the accepted design path; the bound PRD/baseline, material delta, security depth, changed decisions/controls, affected delivery artifacts, prerequisites, remaining human decisions, review outcome when applicable, and readiness for `$feature-delivery-plan`.
