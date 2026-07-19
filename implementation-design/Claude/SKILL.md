---
name: implementation-design
description: Create or revise the smallest sufficient security-aware technical design from an approved PRD, or explicitly conclude that no separate implementation document is needed. Use after PRD approval to define shared architecture, contracts, failure and recovery, verification, external prerequisites, and security controls. Create a document only when shared technical meaning requires one; after a complete document, recommend for or against cross-model review, ask the human, and invoke it only with explicit approval. Do not decompose tasks, publish tracker issues, or implement code.
---

# Implementation Design

Start only from an approved PRD. Capture shared technical and security meaning without turning the document into a task list.

Read the target repository's instructions, accepted PRD, current architecture, runtime map, and relevant decisions. Read `references/implementation-contract.md` completely.

## Session Continuity

For unfinished named work, use the `feature-context-handoff` skill (via the Skill tool, `/feature-context-handoff`) to read any feature-local `WORK-HANDOFF.md` after mandatory repository instructions; canonical artifacts override it. That skill owns context-capacity judgment and checkpointing before the review loop.

## Decide Whether A Document Is Needed

Create a separate design when shared contracts, multiple substantial slices or repositories, data/migrations, integrations, concurrency/recovery, compatibility/rollout, meaningful trust boundaries, or whole-feature verification require shared meaning. Otherwise record `implementation_doc_not_required` only when one bounded task can safely own all implementation notes and the feature introduces no material shared security decision; record why and pass any planning constraints to the `feature-delivery-plan` skill (via the Skill tool, `/feature-delivery-plan`).

## Workflow

1. Bind the result to the exact accepted PRD version or hash. When revising an accepted design, preserve its baseline and identify existing delivery artifacts that require reassessment.
2. If no separate document is justified, present `implementation_doc_not_required`, its reason, and planning constraints for explicit human approval. Do not offer cross-model review without an implementation artifact. After approval, close any obsolete handoff, hand off to the `feature-delivery-plan` skill, and stop.
3. For a document, map affected components and assign one owner to each durable contract and state transition. Classify security depth as `quick`, `standard`, or `deep` (`deep` = payments, identity, privileged secrets, sensitive user data, multi-tenant isolation, destructive or irreversible operations, or comparable high impact). Draft the smallest complete contract, including stable controls, verification, and every known human-supplied asset, dataset, access, credential, environment, budget authorization, external approval, or human validation dependency. Never record secret values or sensitive payloads.
4. Ask the human only about material technical or risk decisions unsupported by canonical evidence. Return product changes to the `feature-design` skill (via the Skill tool, `/feature-design`).
5. For `deep` risk or an explicit human request, invoke the `feature-security-review` skill (via the Skill tool, `/feature-security-review`) and incorporate confirmed requirements; it is not a later delivery gate.
6. Make the document self-contained, substantive, and `draft` or `proposed`, with every open human decision explicit. Assess whether cross-model review is worth the added cost, then ask the human and give a concise recommendation with reasons. Recommend it for material architecture or security uncertainty, broad integration impact, or complex revisions; never invoke it before explicit human approval. An earlier clear request for this document counts.
7. If approved, invoke the `cross-model-review` skill (via the Skill tool, `/cross-model-review`) with the `implementation` profile, verify findings, prepare supported corrections, and complete the full-document recheck. If declined, proceed without it. Before an approved review, use the `feature-context-handoff` skill if the full loop cannot fit safely.
8. Obtain explicit human approval of the technical and security posture, close any obsolete handoff, and hand off to the `feature-delivery-plan` skill.

## Boundaries

- Do not change accepted business scope, create task graphs, choose executors, publish issues, or implement code.
- Keep durable security controls in the implementation design, not a separate report.

## Completion

Report the accepted design path or `implementation_doc_not_required`, accepted PRD version, security depth and posture, key shared decisions and control IDs, affected delivery artifacts, known execution prerequisites for planning, remaining human decisions, cross-model review decision and outcome (`not_applicable` for a no-document result), and readiness for the `feature-delivery-plan` skill.
