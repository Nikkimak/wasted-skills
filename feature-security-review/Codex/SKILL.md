---
name: feature-security-review
description: Deepen a proposed implementation design before its combined cross-model implementation/security review when a feature involves payments, identity, privileged secrets, sensitive user data, multi-tenant isolation, destructive or irreversible operations, comparable high impact, or an explicit human request. Add durable controls and risk decisions to the implementation draft. Do not act as a routine post-delivery gate, review task graphs, publish issues, or run a separate cross-family review.
---

# Feature Security Review

Use this as an exceptional implementation-design escalation, not a mandatory final stage. Review the proposed change rather than the repository in the abstract.

Read the target repository's instructions, accepted PRD, proposed implementation design, and canonical security/architecture decisions. Read `references/security-readiness-checklist.md` completely.

## Preconditions

Require an accepted PRD and a complete proposed implementation draft. If product meaning is missing, return to `$feature-design`; if the technical draft is incomplete, return to `$implementation-design`.

## Workflow

1. Confirm the exceptional trigger and affected assets, actors, privileges, trust boundaries, data, secrets, integrations, and irreversible operations.
2. Trace entry points, authorization decisions, data lifecycle, abuse cases, dependency failure, recovery, rollback, and audit evidence.
3. Distinguish blocking risk, required mitigation, residual risk requiring human acceptance, non-blocking hardening, and unsupported concern.
4. Propose the smallest controls that preserve the accepted business outcome. Give durable controls and verification stable IDs such as `SEC-*` and `VER-*`.
5. Stop for human resolution when mitigation changes product behavior or architecture materially, accepts material residual risk, or requires an irreversible operational commitment.
6. Put confirmed requirements and accepted risks into the proposed implementation design. Do not create a separate report or modify delivery tasks.
7. Return the enriched draft to `$implementation-design` for its single combined `$cross-model-review` `implementation` pass and human approval.

## Gate Result

Return one of:

- `deep_security_design_ready`;
- `changes_required`;
- `blocked_on_human_risk_decision`;
- `blocked_on_product_or_architecture_revision`.

List the implementation sections changed, control IDs added, residual risks, and exact human decisions still required.

## Boundaries

- Do not invoke `$cross-model-review`; `$implementation-design` owns the one combined review.
- Do not review or amend delivery plans.
- Do not accept material risk for the human.
- Do not publish tracker issues or implement code.
