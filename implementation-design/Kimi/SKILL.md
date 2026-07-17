---
name: implementation-design
description: Convert an approved PRD into the smallest sufficient shared technical design, or explicitly conclude that no separate implementation document is needed. Use after PRD approval when Kimi must analyze architecture, component ownership, contracts, data or migrations, integrations, failure and recovery behavior, compatibility, observability, security boundaries, verification strategy, and constraints that multiple tasks must share. Run cross-model implementation review and obtain human approval before delivery planning. Do not decompose tasks, choose task dependencies, file tracker issues, or implement code.
---

# Implementation Design

Start only from an approved PRD. Design shared technical meaning without turning the document into a task list.

Read the target repository's instructions, accepted PRD, current architecture, runtime map, and relevant decisions. Read `${KIMI_SKILL_DIR}/references/implementation-contract.md` completely.

## Session Continuity

When continuing an existing feature, use the `feature-context-handoff` skill (via the Skill tool, `/skill:feature-context-handoff`) to read any feature-local `WORK-HANDOFF.md` after mandatory repository instructions, then load its named accepted inputs and active implementation draft. Canonical artifacts override the handoff.

Before starting cross-model review, rely only on the host-provided context indicator (`/usage` in Kimi Code). If the full review-and-recheck loop cannot safely fit, checkpoint the coherent draft with the `feature-context-handoff` skill and recommend a fresh session. Do not estimate context numerically or install automatic monitoring.

## Decide Whether A Document Is Needed

Create a separate implementation document when the feature has material shared technical decisions involving one or more of:

- multiple substantial slices or repositories;
- shared domain/data models or migrations;
- API, event, storage, or integration contracts;
- component ownership or architecture boundaries;
- concurrency, consistency, retry, or recovery behavior;
- compatibility, rollout, rollback, or irreversible operations;
- meaningful security/trust boundaries;
- whole-feature verification constraints.

Skip the document when one bounded task can safely carry its implementation notes without duplicating shared decisions. Record the explicit `implementation_doc_not_required` conclusion and why, then hand off to the `feature-delivery-plan` skill (via the Skill tool, `/skill:feature-delivery-plan`).

## Workflow

1. Verify the PRD is accepted and identify its exact version/path or hash.
2. Map the affected current system and identify the owner component for each state transition or durable contract.
3. Ask the human only about material technical/product tradeoffs that cannot be resolved from canonical evidence. Return product changes to the `feature-design` skill (via the Skill tool, `/skill:feature-design`) rather than silently altering the PRD.
4. Draft the smallest complete technical contract sufficient for later task planning. Avoid low-level step-by-step implementation instructions that belong to tasks.
5. Check that the design enables thin vertical delivery and does not require completing horizontal layers before integration can be tested.
6. Remove placeholders, make every required section substantive, and record each known unresolved human choice in `Open technical decisions`. Mark the full artifact `draft` or `proposed`, confirm that the human wants it reviewed, and verify enough session context remains for the complete review loop. An explicit review request already made in the current conversation counts.
7. Invoke the `cross-model-review` skill (via the Skill tool, `/skill:cross-model-review`) with the `implementation` profile. Verify Claude findings against the repository, prepare supported corrections, and resume the same Claude reviewer session for a full-document recheck.
8. Surface every remaining material and minor disagreement to the human. Apply one final consolidated canonical patch only after human resolution.
9. Mark the implementation design accepted only after explicit human approval. Remove an obsolete `WORK-HANDOFF.md` through the `feature-context-handoff` skill (via the Skill tool, `/skill:feature-context-handoff`) when canonical documents and the work plan make the next phase clear. End with a workflow handoff to the `feature-delivery-plan` skill (via the Skill tool, `/skill:feature-delivery-plan`).

## Boundaries

- Do not rewrite business scope; return PRD changes to the `feature-design` skill.
- Do not create parent/child tasks or dependency graphs.
- Do not choose task-specific executors or validation profiles.
- Do not publish tracker issues.
- Do not implement code.

## Completion

Report either the accepted implementation document path or `implementation_doc_not_required`, the accepted PRD version it constrains, key shared technical decisions, remaining implementation constraints for planning, cross-model review outcome, and readiness for the `feature-delivery-plan` skill.
