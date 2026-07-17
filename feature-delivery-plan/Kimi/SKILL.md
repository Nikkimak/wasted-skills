---
name: feature-delivery-plan
description: Turn an approved PRD and, when required, an approved implementation design into an executable feature delivery plan. Use after product and technical design approval when Kimi must decide one-task versus parent/child delivery, create bounded end-to-end tasks, enforce vertical slices, define committed and deferred work, dependencies, execution and validation profiles, feature/task branch merge targets, whole-feature acceptance, and tracker-ready task drafts. Review the task graph cross-model, then hand it to security review. Do not change PRD scope, invent architecture, publish tracker issues before approval, or implement code.
---

# Feature Delivery Plan

Convert accepted meaning into the smallest executable task graph. Keep business and technical decisions upstream; make delivery order, ownership, routing, and verification explicit here.

Read the target repository's instructions, accepted PRD, accepted implementation design or `implementation_doc_not_required` result, and current task/intake contracts. Read `${KIMI_SKILL_DIR}/references/delivery-plan-contract.md` completely.

## Session Continuity

When continuing an existing feature, use the `feature-context-handoff` skill (via the Skill tool, `/skill:feature-context-handoff`) to read any feature-local `WORK-HANDOFF.md` after mandatory repository instructions, then load only its named accepted inputs and active plan drafts. Canonical artifacts override the handoff.

Before starting cross-model review, rely only on the host-provided context indicator (`/usage` in Kimi Code). If the initial review, plan corrections, human decisions, and full recheck cannot safely fit, checkpoint with the `feature-context-handoff` skill and recommend a fresh session. Do not estimate context numerically or install automatic monitoring.

## Workflow

1. Verify exact accepted PRD and implementation inputs. If delivery planning exposes a product gap, return to the `feature-design` skill (via the Skill tool, `/skill:feature-design`); if it exposes a missing shared technical decision, return to the `implementation-design` skill (via the Skill tool, `/skill:implementation-design`).
2. Choose the delivery shape:
   - one small feature/task when one bounded end-to-end cycle is safe;
   - one parent feature plus child tasks when several substantial increments need shared acceptance and one feature integration branch;
   - one standalone fix task when restoring accepted behavior.
3. Decompose only into observable vertical increments. Every task must traverse the minimum required layers and provide a runnable verification path.
4. Group tightly coupled small increments when one bounded session/worktree can implement and verify them. Do not create one task per technical step or per minor finding.
5. Define parent relations, blocker graph, committed/deferred scope, execution profile, validation profile, merge target, and acceptance evidence.
6. Ensure all approved PRD acceptance criteria map to tasks and final parent acceptance; reject gaps, duplicates, cycles, and work not authorized by the accepted design.
7. Draft the complete delivery plan and every tracker-ready task contract without publishing them. Remove placeholders, make the complete graph self-contained, and record each known unresolved human decision.
8. Mark the full plan set `draft` or `proposed`, confirm that the human wants it reviewed, and verify enough session context remains for the complete review loop. An explicit review request already made in the current conversation counts.
9. Invoke the `cross-model-review` skill (via the Skill tool, `/skill:cross-model-review`) with the `task-plan` profile. Correct supported findings, resume the same Claude reviewer session for a full-plan recheck, and surface all remaining material/minor differences to the human.
10. Obtain human approval of the delivery graph as the planning baseline, but keep unpublished task contracts `proposed` until security review completes. Then invoke the `feature-security-review` skill (via the Skill tool, `/skill:feature-security-review`) before any tracker publication; that gate may add controls and requires final human approval of the amended task set.
11. Remove an obsolete `WORK-HANDOFF.md` through the `feature-context-handoff` skill when canonical documents and the work plan make the security phase clear. End with an approved, security-ready workflow handoff. Actual filing uses the target project's bounded intake path in a later explicit action.

## Large Feature Rules

- Use one parent feature and one integration branch without a persistent parent worktree.
- Give each child a temporary branch/worktree and integrate children serially into the feature branch.
- Use lighter child validation and full parent-level Testing/human review before the one merge to `main`.
- Keep all approved planned tasks visible in the tracker after publication, including deferred tasks.
- Batch small acceptance findings into same-issue remediation. Split fixes only for real repo, size, dependency, provider, or security boundaries.
- When reducing the current version, create the next-version parent and re-parent deferred tasks before accepting the current feature.

## Boundaries

- Do not change accepted business scope or architecture.
- Do not write a new PRD or implementation design inside the delivery plan.
- Do not publish tasks before cross-model, human, and security approval.
- Do not implement code or create runtime worktrees.

## Completion

Report the delivery shape, parent and child drafts, vertical outcomes, dependencies, committed/deferred scope, execution/validation profiles, merge targets, final acceptance coverage, cross-model review outcome, remaining human decisions, and readiness for the `feature-security-review` skill.
