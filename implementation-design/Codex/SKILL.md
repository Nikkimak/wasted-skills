---
name: implementation-design
description: Convert an approved PRD into the smallest sufficient security-aware technical design, or explicitly conclude that no separate implementation document is needed. Use after PRD approval to define shared architecture, contracts, failure and recovery, verification, external prerequisites, and security controls; invoke deep feature security analysis only for exceptional risk; then run one combined cross-model implementation/security review and obtain human approval. Do not decompose tasks, publish tracker issues, or implement code.
---

# Implementation Design

Read the target repository's instructions, accepted PRD, current architecture, runtime map, and relevant decisions. Read `references/implementation-contract.md` completely.

For unfinished named work, use `$feature-context-handoff`; canonical artifacts override it.

## Decide Whether A Document Is Needed

Create a separate design when shared contracts, multiple substantial slices or repositories, data/migrations, integrations, recovery, rollout, trust boundaries, or whole-feature verification require shared meaning. Otherwise record `implementation_doc_not_required` with its reason and planning constraints, using the exact rule in the contract.

## Workflow

1. Bind the result to the exact accepted PRD version or hash. Map affected components and one owner for each durable contract and state transition.
2. Classify security depth as `quick`, `standard`, or `deep` and draft the smallest complete contract, including stable controls, verification, and known external execution prerequisites. Never record secret values or sensitive payloads.
3. Ask only about material technical or risk decisions unsupported by evidence. Return product changes to `$feature-design`.
4. For `deep` risk or explicit human request, invoke `$feature-security-review` on the proposed draft and incorporate confirmed requirements before the combined review.
5. Make the artifact self-contained and `draft` or `proposed`, with every open decision explicit. If the complete review loop cannot fit safely, use `$feature-context-handoff` before review.
6. Invoke `$cross-model-review` with the `implementation` profile. Evaluate findings, prepare supported corrections, and complete the full-document recheck.
7. Obtain explicit human approval of the technical and security posture, close any obsolete handoff, and hand off to `$feature-delivery-plan`.

## Boundaries

- Do not change accepted business scope, create task graphs, choose executors, publish issues, or implement code.
- Keep durable security controls in the implementation design, not a separate report.

## Completion

Report the accepted design path or `implementation_doc_not_required`, accepted PRD version, security depth and posture, key shared decisions and control IDs, known execution prerequisites for planning, remaining human decisions, cross-model outcome, and readiness for `$feature-delivery-plan`.
