---
name: feature-security-review
description: Deepen a proposed implementation design only when its delta introduces or materially changes payments, identity, privileged secrets, sensitive data, tenant isolation, destructive/irreversible behavior, or comparable high-impact boundaries, or when the human explicitly requests it. Review only affected risk, add only new or changed durable controls to the implementation draft, and create no separate report. Do not act as a routine gate, review task graphs, publish issues, or run cross-family review.
---

# Feature Security Review

Use this as an exceptional implementation-design escalation. Review the material delta, not the feature domain or repository in the abstract.

Read the target repository's instructions, accepted PRD, proposed implementation design, and canonical security/architecture decisions. Read `references/security-readiness-checklist.md` completely.

## Preconditions

Require an accepted PRD and a complete proposed implementation draft. If product meaning is missing, return to the `feature-design` skill (invoked via the Skill tool as `/feature-design`); if the technical draft is incomplete, return to the `implementation-design` skill (invoked via the Skill tool as `/implementation-design`).

## Workflow

1. Compare the proposed delta with accepted security baselines. If it introduces or materially changes no high-impact boundary, return `deep_security_review_not_required` without editing the design.
2. For a deep delta, inspect only affected assets, actors, privileges, boundaries, data/secrets, inputs, integrations, failure/recovery, and audit evidence using the checklist. Cite unchanged baseline controls once; do not restate them.
3. Distinguish blocking risk, required mitigation, human-accepted residual risk, optional hardening, and unsupported concern.
4. Add the smallest new or changed controls that preserve the accepted business outcome. Reuse existing IDs for unchanged obligations; create `SEC-*`/`VER-*` only for new ones.
5. Stop for human resolution only when mitigation changes product behavior or architecture materially, accepts material residual risk, or requires an irreversible operational commitment.
6. Put confirmed changes in the implementation design, create no separate report or delivery-task edits, and return to the `implementation-design` skill for its review decision and final approval.

## Gate Result

Return one of:

- `deep_security_design_ready`;
- `deep_security_review_not_required`;
- `changes_required`;
- `blocked_on_human_risk_decision`;
- `blocked_on_product_or_architecture_revision`.

For `deep_security_review_not_required`, cite the baseline and delta reason. Otherwise list the changed implementation sections and control IDs, residual risks, and exact human decisions still required.

## Boundaries

- Do not invoke or presume approval for the `cross-model-review` skill; the `implementation-design` skill owns the explicit review decision.
- Do not review or amend delivery plans.
- Do not accept material risk for the human.
- Do not publish tracker issues or implement code.
