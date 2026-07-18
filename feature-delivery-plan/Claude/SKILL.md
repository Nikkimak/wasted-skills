---
name: feature-delivery-plan
description: Turn an approved PRD and approved security-aware implementation design, or an explicit no-document result, into the smallest executable vertical task graph. Map product criteria, technical invariants, security controls, verification, dependencies, routing, merge targets, and human/external prerequisites; create a conditional feature-local execution-readiness manifest; run deterministic local checks and obtain human approval. Do not run a routine cross-model or separate security review, change upstream decisions, publish issues, or implement code.
---

# Feature Delivery Plan

Convert accepted meaning into the smallest executable task graph. Do not redesign product, architecture, or security during decomposition.

Read the target repository's instructions, accepted PRD, accepted implementation design or `implementation_doc_not_required`, and current task/intake contracts. Read `references/delivery-plan-contract.md` completely. If any human or external execution dependency exists, also read `references/execution-readiness-contract.md` completely.

## Session Continuity

For unfinished named work, use the `feature-context-handoff` skill (via the Skill tool, `/feature-context-handoff`) to read any feature-local `WORK-HANDOFF.md` after mandatory repository instructions; canonical artifacts override it.

## Workflow

1. Verify the exact accepted inputs. Return product gaps to the `feature-design` skill (via the Skill tool, `/feature-design`) and shared technical/security gaps to the `implementation-design` skill (via the Skill tool, `/implementation-design`).
2. Choose the smallest supported delivery shape (one bounded feature/task, one parent with substantial child slices, or one standalone fix) and decompose only into observable vertical increments with runnable verification. Group tightly coupled work; do not create one task per technical step. Split only at real size, repository, dependency, provider, or security boundaries.
3. Define parent relations, acyclic dependencies, committed/deferred scope, execution and validation profiles, merge targets, and parent acceptance using `references/delivery-plan-contract.md`. For a large parent, use one integration branch, give each child a temporary branch/worktree, integrate children serially, and require full parent acceptance before the one merge to `main`.
4. Map every committed acceptance criterion, implementation invariant, `SEC-*`, and `VER-*` obligation to executable task scope and final evidence.
5. When human or external dependencies exist, create one feature-local `EXECUTION-READINESS.md` under its contract, assign each item a stable `HIN-*` ID, and reference it from consuming tasks. Never record secret values or sensitive payloads.
6. Run local checks for coverage, unauthorized or duplicate work, bounded scope, missing or cyclic dependencies, verification, merge targets, control mapping, and readiness blockers.
7. Present the complete plan and one consolidated `needed now` / `needed later` human-input summary. Obtain explicit human approval of the task graph and readiness posture, close any obsolete handoff, and finish with a tracker-ready plan; publication remains a later explicit action through the target project's bounded intake path.

## Boundaries

- Do not redesign accepted product, architecture, or security. Return gaps upstream.
- Do not run routine cross-model or separate security review, publish tasks, create runtime worktrees, provision credentials, or implement code. Use the `cross-model-review` skill only on explicit human request; exceptional security work belongs before implementation approval.

## Completion

Report delivery shape, tasks and dependencies, committed/deferred scope, acceptance/control coverage, execution/validation profiles, merge targets, readiness result (`ready`, `ready_with_scheduled_inputs`, `ready_with_reduced_scope`, or `blocked`), all `needed now` and `needed later` human inputs, remaining decisions, and tracker readiness.
