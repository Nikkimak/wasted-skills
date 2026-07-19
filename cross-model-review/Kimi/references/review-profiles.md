# Review profiles

## PRD

Challenge business outcome, users, current/desired behavior, scope, non-goals, MVP boundary, contradictions, unsupported assumptions, open product decisions, observable acceptance/failure behavior, and known human-supplied dependencies. For a proposed update to an accepted PRD, use its baseline and intended delta when provided, check for hidden scope and downstream impact, and still read the full proposed PRD. Do not invent implementation detail merely to add completeness.

## Implementation

Challenge the complete technical and security contract:

- fidelity to the accepted PRD and declared delta from any accepted baseline;
- affected ownership, contracts, data/migration, integration, concurrency, compatibility, rollout, rollback, recovery, observability, and verification;
- materially changed authentication/authorization, assets, boundaries, privileges/isolation, secrets/data lifecycle, external inputs, abuse/dependency failure, and fail-open/closed behavior;
- new or changed `SEC-*`/`VER-*` obligations sufficient for delivery, without duplicating inherited controls or demanding prose for unaffected sections;
- human-supplied assets, datasets, access, credentials, environments, approvals, budgets, and validation, including safe handling and known blocking stage;
- unnecessary complexity and unresolved product, architecture, security, or residual-risk decisions.

For a proposed update to an accepted implementation design, use its baseline and intended delta when provided, check affected downstream contracts, and still read the full proposed design.

For deep-risk deltas, use the implementation already enriched by the `feature-security-review` skill (via the Skill tool, `/skill:feature-security-review`); do not create a second security review stage.

## Task plan

Use only on explicit human request. Challenge requirement/control coverage, vertical slices, bounded scope, dependencies, deferred work, routing, validation, merge targets, parent acceptance, and execution-readiness mapping. Do not make this a default gate.

## Finding format

```text
[ID] [blocking|material|minor] Summary
Evidence: exact path/section and contradiction or missing contract
Impact: why it matters
Recommendation: smallest correction preserving the intended outcome
Human decision: yes/no; exact question when yes
```

On recheck, re-read the whole corrected draft, resolve prior findings, and list every remaining or new issue. Say `CLEAN` only when none remains.
