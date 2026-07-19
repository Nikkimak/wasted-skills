---
name: implementation-design
description: Create or revise the smallest sufficient security-aware technical design from an approved PRD, or explicitly conclude that no separate implementation document is needed. Use after PRD approval to define shared architecture, contracts, failure and recovery, verification, external prerequisites, and security controls. Create a document only when shared technical meaning requires one; after a complete document, recommend for or against cross-model review, ask the human, and invoke it only with explicit approval. Do not decompose tasks, publish tracker issues, or implement code.
---

# Implementation Design

Read the target repository's instructions, accepted PRD, current architecture, runtime map, and relevant decisions. Read `references/implementation-contract.md` completely.

For unfinished named work, use `$feature-context-handoff`; canonical artifacts override it.

## Decide Whether A Document Is Needed

Create a separate design when shared contracts, multiple substantial slices or repositories, data/migrations, integrations, recovery, rollout, trust boundaries, or whole-feature verification require shared meaning. Otherwise record `implementation_doc_not_required` with its reason and planning constraints, using the exact rule in the contract.

## Workflow

1. Bind the result to the exact accepted PRD version or hash. When revising an accepted design, preserve its baseline and identify existing delivery artifacts that require reassessment.
2. If no separate document is justified, present `implementation_doc_not_required`, its reason, and planning constraints for explicit human approval. Do not offer cross-model review without an implementation artifact. After approval, close any obsolete handoff, hand off to `$feature-delivery-plan`, and stop.
3. For a document, map affected components and one owner for each durable contract and state transition. Classify security depth as `quick`, `standard`, or `deep` and draft the smallest complete contract, including stable controls, verification, and known external execution prerequisites. Never record secret values or sensitive payloads.
4. Ask only about material technical or risk decisions unsupported by evidence. Return product changes to `$feature-design`.
5. For `deep` risk or an explicit human request, invoke `$feature-security-review` and incorporate confirmed requirements.
6. Make the document self-contained and `draft` or `proposed`, with every open decision explicit. Assess whether cross-model review is worth the added cost, then ask the human and give a concise recommendation with reasons. Recommend it for material architecture or security uncertainty, broad integration impact, or complex revisions; never invoke it before explicit human approval. An earlier clear request for this document counts.
7. If approved, use `$cross-model-review` with the `implementation` profile, evaluate findings, prepare supported corrections, and complete the full-document recheck. If declined, proceed without it. Before an approved review, use `$feature-context-handoff` if the full loop cannot fit safely.
8. Obtain explicit human approval of the technical and security posture, close any obsolete handoff, and hand off to `$feature-delivery-plan`.

## Boundaries

- Do not change accepted business scope, create task graphs, choose executors, publish issues, or implement code.
- Keep durable security controls in the implementation design, not a separate report.

## Completion

Report the accepted design path or `implementation_doc_not_required`, accepted PRD version, security depth and posture, key shared decisions and control IDs, affected delivery artifacts, known execution prerequisites for planning, remaining human decisions, cross-model review decision and outcome (`not_applicable` for a no-document result), and readiness for `$feature-delivery-plan`.
