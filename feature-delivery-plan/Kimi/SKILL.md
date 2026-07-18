---
name: feature-delivery-plan
description: Turn an approved PRD and approved security-aware implementation design, or an explicit no-document result, into the smallest executable vertical task graph. Use after product and technical approval when Kimi must map product criteria, technical invariants, security controls, verification, dependencies, routing, merge targets, and human/external prerequisites into tasks, create a conditional feature-local execution-readiness manifest, run deterministic local checks, and obtain human approval. Do not run a routine cross-model or separate security review, change upstream decisions, publish issues, or implement code.
---

# Feature Delivery Plan

Convert accepted meaning into the smallest executable task graph. Do not redesign product, architecture, or security during decomposition.

Read the target repository's instructions, accepted PRD, accepted implementation design or `implementation_doc_not_required`, and current task/intake contracts. Read `${KIMI_SKILL_DIR}/references/delivery-plan-contract.md` completely. If any human or external execution dependency exists, also read `${KIMI_SKILL_DIR}/references/execution-readiness-contract.md` completely.

## Session Continuity

When continuing a named feature, use the `feature-context-handoff` skill (via the Skill tool, `/skill:feature-context-handoff`) after mandatory repository instructions. Canonical artifacts override the handoff.

## Workflow

1. Verify exact accepted PRD and implementation inputs. Return product gaps to the `feature-design` skill (via the Skill tool, `/skill:feature-design`) and shared technical or security gaps to the `implementation-design` skill (via the Skill tool, `/skill:implementation-design`).
2. Choose one bounded feature/task, one parent with substantial child slices, or one standalone fix.
3. Decompose only into observable vertical increments with runnable verification paths. Group tightly coupled small work; do not create one task per technical step or minor finding.
4. Define parent relations, acyclic dependencies, committed/deferred scope, execution and validation profiles, merge targets, and parent acceptance.
5. Map every committed PRD acceptance criterion, implementation invariant, `SEC-*` control, and `VER-*` obligation to executable task scope and final acceptance.
6. Identify every human-supplied asset, dataset, access, credential, environment, budget authorization, external approval, or human validation dependency. When any exists, create one feature-local `EXECUTION-READINESS.md`; give each item a stable `HIN-*` ID and reference it from consuming tasks. Never store secret values or sensitive payloads.
7. Run deterministic local checks for coverage, unauthorized scope, duplicate work, missing or cyclic dependencies, unbounded tasks, control-to-task mapping, verification, merge targets, and readiness blockers.
8. Present the complete plan and one consolidated "what we need from you" summary grouped into `needed now` and `needed later`. Obtain explicit human approval of the task graph and readiness posture.
9. Remove an obsolete handoff through the `feature-context-handoff` skill when canonical state is clear. End with an approved tracker-ready plan; actual publication remains a later explicit action through the target project's bounded intake path.

## Large Feature Rules

- Use one parent feature and integration branch without a persistent parent worktree.
- Give each child a temporary branch/worktree and integrate children serially.
- Use proportional child validation and full parent acceptance before the one merge to `main`.
- Keep approved deferred tasks visible after publication.
- Split only for real repository, size, dependency, provider, or security boundaries.

## Boundaries

- Do not change accepted business, architecture, or security decisions.
- Do not run the `cross-model-review` skill (via the Skill tool, `/skill:cross-model-review`) by default; use it only on an explicit human request.
- Do not invoke the `feature-security-review` skill (via the Skill tool, `/skill:feature-security-review`); exceptional security work belongs before implementation approval.
- Do not publish tasks, create runtime worktrees, provision credentials, or implement code.

## Completion

Report delivery shape, tasks and dependencies, committed/deferred scope, acceptance/control coverage, execution/validation profiles, merge targets, readiness result (`ready`, `ready_with_scheduled_inputs`, `ready_with_reduced_scope`, or `blocked`), all `needed now` and `needed later` human inputs, remaining decisions, and tracker readiness.
