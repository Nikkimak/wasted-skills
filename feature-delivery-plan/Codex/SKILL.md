---
name: feature-delivery-plan
description: Create or revise the smallest executable vertical task graph from an approved PRD and accepted implementation design, no-document result, or no-change result. Map only applicable product, technical, security, verification, dependency, routing, merge, and prerequisite obligations; create execution readiness only when needed; run local checks and obtain human approval. Do not offer routine cross-model review, change upstream decisions, publish issues, or implement code.
---

# Feature Delivery Plan

Read the target repository's instructions, accepted PRD, accepted implementation design or `implementation_doc_not_required`/`implementation_change_not_required` result, and current task/intake contracts. Read `references/delivery-plan-contract.md` completely. If any human or external execution dependency exists, also read `references/execution-readiness-contract.md` completely.

For unfinished named work, use `$feature-context-handoff`; canonical artifacts override it.

## Workflow

1. Verify the exact accepted inputs. When revising a plan, preserve its accepted baseline and update only the tasks, dependencies, and readiness state affected by those inputs. Return product gaps to `$feature-design` and shared technical/security gaps to `$implementation-design`.
2. Choose the smallest supported delivery shape and decompose only into observable vertical increments with runnable verification. Group tightly coupled work and split only at real size, repository, dependency, provider, or security boundaries.
3. Define parent relations, acyclic dependencies, committed/deferred scope, execution and validation profiles, merge targets, and parent acceptance using `references/delivery-plan-contract.md`.
4. Map every committed acceptance criterion and every implementation, `SEC-*`, or `VER-*` obligation applicable to this delivery delta; do not create tasks for unchanged baseline controls.
5. When human or external dependencies exist, create one feature-local `EXECUTION-READINESS.md` under its contract, assign `HIN-*` IDs, and reference them from consuming tasks. Never record secret values or sensitive payloads.
6. Run local checks for coverage, unauthorized or duplicate work, bounded scope, dependencies, verification, merge targets, control mapping, and readiness.
7. Present the complete plan and one `needed now` / `needed later` human-input summary. Do not offer cross-model review routinely. Run it only if the human independently requests task-plan review; then obtain explicit approval of the resulting task graph and readiness posture. Otherwise obtain explicit human approval directly, close any obsolete handoff, and finish with a tracker-ready plan; publication remains a later explicit action.

## Boundaries

- Do not redesign accepted product, architecture, or security. Return gaps upstream.
- Do not run routine cross-model/security review, publish tasks, create runtime worktrees, provision credentials, or implement code. Use `$cross-model-review` only on explicit human request.

## Completion

Report delivery shape, tasks and dependencies, committed/deferred scope, acceptance/control coverage, execution/validation profiles, merge targets, readiness result (`ready`, `ready_with_scheduled_inputs`, `ready_with_reduced_scope`, or `blocked`), all `needed now` and `needed later` human inputs, remaining decisions, any explicitly requested cross-model review outcome, and tracker readiness.
