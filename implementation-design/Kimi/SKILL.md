---
name: implementation-design
description: Convert an approved PRD into the smallest sufficient security-aware technical design, or explicitly conclude that no separate implementation document is needed. Use after PRD approval to define shared architecture, contracts, failure and recovery, verification, external prerequisites, and security controls; invoke deep feature security analysis only for exceptional risk; then run one combined cross-model implementation/security review and obtain human approval. Do not decompose tasks, publish tracker issues, or implement code.
---

# Implementation Design

Read the target repository's instructions, accepted PRD, current architecture, runtime map, and relevant decisions. Read `${KIMI_SKILL_DIR}/references/implementation-contract.md` completely.

For unfinished named work, use the `feature-context-handoff` skill (via the Skill tool, `/skill:feature-context-handoff`); canonical artifacts override it.

## Decide Whether A Document Is Needed

Create a separate design when shared contracts, multiple substantial slices or repositories, data/migrations, integrations, recovery, rollout, trust boundaries, or whole-feature verification require shared meaning. Otherwise record `implementation_doc_not_required` with reason and planning constraints for the `feature-delivery-plan` skill (`/skill:feature-delivery-plan`), per the exact rule in the contract.

## Workflow

1. Bind the design to the exact accepted PRD version or hash. Map affected components and one owner for each durable contract and state transition.
2. Classify security depth as `quick`, `standard`, or `deep`; use `deep` for payments, identity, privileged secrets, sensitive user data, multi-tenant isolation, destructive or irreversible operations, or comparable high impact. Draft the smallest complete contract with security controls, verification obligations, and known external execution prerequisites. Never record secret values or sensitive payloads.
3. Ask only about material choices unsupported by canonical evidence. Return product changes to the `feature-design` skill (`/skill:feature-design`).
4. For `deep` risk or explicit human request, invoke the `feature-security-review` skill (`/skill:feature-security-review`) on the proposed draft and incorporate confirmed requirements before the combined review.
5. Make the artifact self-contained and `draft` or `proposed`, with every open decision explicit. Before review, rely only on `/usage` for capacity; if the complete review loop cannot fit safely, checkpoint with the `feature-context-handoff` skill (`/skill:feature-context-handoff`) and recommend a fresh session.
6. Invoke the `cross-model-review` skill (`/skill:cross-model-review`) with the `implementation` profile. Evaluate findings, prepare supported corrections, and complete the full-document recheck.
7. Obtain explicit human approval of the technical and security posture, close any obsolete handoff, and hand off to the `feature-delivery-plan` skill (`/skill:feature-delivery-plan`).

## Boundaries

- Do not change accepted business scope, create task graphs, choose executors, publish issues, or implement code.
- Keep durable security controls in the implementation design, not a separate report.

## Completion

Report the accepted design path or `implementation_doc_not_required`, accepted PRD version, security depth and posture, key shared decisions and control IDs, known execution prerequisites for planning, remaining human decisions, cross-model outcome, and readiness for the `feature-delivery-plan` skill.
