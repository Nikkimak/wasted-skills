---
name: implementation-design
description: Convert an approved PRD into the smallest sufficient security-aware technical design, or explicitly conclude that no separate implementation document is needed. Use after PRD approval to define shared architecture, contracts, failure and recovery, verification, external prerequisites, and security controls; invoke deep feature security analysis only for exceptional risk; then run one combined cross-model implementation/security review and obtain human approval. Do not decompose tasks, publish tracker issues, or implement code.
---

# Implementation Design

Start only from an approved PRD. Capture shared technical and security meaning without turning the document into a task list.

Read the target repository's instructions, accepted PRD, current architecture, runtime map, and relevant decisions. Read `references/implementation-contract.md` completely.

## Session Continuity

When continuing a named feature, use the `feature-context-handoff` skill (invoked via the Skill tool as `/feature-context-handoff`) to read any feature-local `WORK-HANDOFF.md` after mandatory repository instructions. Canonical artifacts override the handoff.

Before cross-model review, rely only on the host-provided context indicator (the Claude Code `/context` view or status line) when available. If the complete review loop cannot safely fit, checkpoint the coherent draft with the `feature-context-handoff` skill and recommend a fresh session. Do not estimate context numerically or install automatic monitoring.

## Decide Whether A Document Is Needed

Create a separate design for shared contracts, multiple substantial slices or repositories, data/migrations, integrations, concurrency/recovery, compatibility/rollout, meaningful trust boundaries, or whole-feature verification constraints.

Use `implementation_doc_not_required` only when one bounded task can safely own all implementation notes and the feature introduces no material shared security decision. Record why and pass any constraints to the `feature-delivery-plan` skill (invoked via the Skill tool as `/feature-delivery-plan`).

## Workflow

1. Bind the design to the exact accepted PRD version or hash.
2. Map affected components and assign one owner to each durable contract and state transition.
3. Classify security depth as `quick`, `standard`, or `deep`. Use `deep` for payments, identity, privileged secrets, sensitive user data, multi-tenant isolation, destructive or irreversible operations, or comparable high impact.
4. Draft the smallest complete implementation contract. Include security controls and verification obligations, plus every known human-supplied asset, dataset, access, credential, environment, budget authorization, external approval, or human validation dependency. Do not store secret values or sensitive data in the document.
5. Ask the human only about material choices unsupported by canonical evidence. Return product changes to the `feature-design` skill (invoked via the Skill tool as `/feature-design`).
6. For `deep` risk or an explicit human request, invoke the `feature-security-review` skill (via the Skill tool, `/feature-security-review`) against the proposed implementation draft. Incorporate its confirmed requirements before cross-model review; it is not a later delivery gate.
7. Make the full draft self-contained, substantive, and `draft` or `proposed`. List every open human decision explicitly.
8. Invoke the `cross-model-review` skill (via the Skill tool, `/cross-model-review`) with the `implementation` profile. That profile challenges architecture and security together. Verify GPT findings against the repository, prepare supported corrections, and complete the bounded full-document recheck in the same reviewer session.
9. Obtain explicit human approval of the implementation and security posture. Remove an obsolete `WORK-HANDOFF.md` through the `feature-context-handoff` skill when canonical state is clear, then hand off to the `feature-delivery-plan` skill.

## Boundaries

- Do not change accepted business scope; return PRD changes to the `feature-design` skill.
- Do not create task graphs, choose task executors, or publish tracker issues.
- Do not create a separate security report when controls belong in the implementation design.
- Do not implement code.

## Completion

Report the accepted design path or `implementation_doc_not_required`, accepted PRD version, security depth and posture, key shared decisions and control IDs, known execution prerequisites for planning, remaining human decisions, cross-model review outcome, and readiness for the `feature-delivery-plan` skill.
