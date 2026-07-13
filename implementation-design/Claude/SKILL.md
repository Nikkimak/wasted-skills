---
name: implementation-design
description: Convert an approved PRD into the smallest sufficient shared technical design, or explicitly conclude that no separate implementation document is needed. Use after PRD approval when Claude must analyze architecture, component ownership, contracts, data or migrations, integrations, failure and recovery behavior, compatibility, observability, security boundaries, verification strategy, and constraints that multiple tasks must share. Run cross-model implementation review and obtain human approval before delivery planning. Do not decompose tasks, choose task dependencies, file tracker issues, or implement code.
---

# Implementation Design

Start only from an approved PRD. Design shared technical meaning without turning the document into a task list.

Read the target repository's instructions, accepted PRD, current architecture, runtime map, and relevant decisions. Read `references/implementation-contract.md` completely.

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

Skip the document when one bounded task can safely carry its implementation notes without duplicating shared decisions. Record the explicit `implementation_doc_not_required` conclusion and why, then hand off to the `feature-delivery-plan` skill (invoked via the Skill tool as `/feature-delivery-plan`).

## Workflow

1. Verify the PRD is accepted and identify its exact version/path or hash.
2. Map the affected current system and identify the owner component for each state transition or durable contract.
3. Ask the human only about material technical/product tradeoffs that cannot be resolved from canonical evidence. Return product changes to the `feature-design` skill (invoked via the Skill tool as `/feature-design`) rather than silently altering the PRD.
4. Draft the smallest technical contract sufficient for later task planning. Avoid low-level step-by-step implementation instructions that belong to tasks.
5. Check that the design enables thin vertical delivery and does not require completing horizontal layers before integration can be tested.
6. Invoke the `cross-model-review` skill (via the Skill tool as `/cross-model-review`) with the `implementation` profile. Verify GPT findings against the repository, prepare supported corrections, and resume the same GPT reviewer session for a full recheck.
7. Surface every remaining material and minor disagreement to the human. Apply one final consolidated canonical patch only after human resolution.
8. Mark the implementation design accepted only after explicit human approval. End with a handoff to the `feature-delivery-plan` skill.

## Boundaries

- Do not rewrite business scope; return PRD changes to the `feature-design` skill.
- Do not create parent/child tasks or dependency graphs.
- Do not choose task-specific executors or validation profiles.
- Do not publish tracker issues.
- Do not implement code.

## Completion

Report either the accepted implementation document path or `implementation_doc_not_required`, the accepted PRD version it constrains, key shared technical decisions, remaining implementation constraints for planning, cross-model review outcome, and readiness for the `feature-delivery-plan` skill.
