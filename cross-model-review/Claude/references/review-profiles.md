# Review profiles

## PRD

Challenge business outcome, users, current/desired behavior, scope, non-goals, MVP boundary, contradictions, unsupported assumptions, open product decisions, observable acceptance/failure behavior, and known human-supplied dependencies. For a proposed update to an accepted PRD, use its baseline and intended delta when provided, check for hidden scope and downstream impact, and still read the full proposed PRD. Do not invent implementation detail merely to add completeness.

## Implementation

Challenge the complete technical and security contract:

- fidelity to the accepted PRD/version;
- component ownership, contracts, data, migration, integration, concurrency, compatibility, rollout, rollback, and recovery;
- authentication/authorization ownership, assets, actors, trust boundaries, privileges, isolation, secrets, sensitive-data lifecycle, and log/redaction behavior;
- external inputs, abuse cases, replay/idempotency, resource bounds, dependency failure, and fail-open/fail-closed decisions;
- observability, operations, testability, and executable security verification;
- stable `SEC-*` and `VER-*` obligations sufficient for downstream task mapping;
- human-supplied assets, datasets, access, credentials, environments, approvals, budgets, and validation, including safe handling and known blocking stage;
- unnecessary complexity and unresolved product, architecture, security, or residual-risk decisions.

For a proposed update to an accepted implementation design, use its baseline and intended delta when provided, check affected downstream contracts, and still read the full proposed design.

For deep-risk features, use the proposed implementation already enriched by the `feature-security-review` skill; do not create a second security review stage.

## Task plan

Use only on explicit human request. Challenge requirement/control coverage, vertical slices, bounded scope, dependencies, deferred work, routing, validation, merge targets, parent acceptance, and execution-readiness mapping. Do not make this a default gate.

## Finding format

The GPT reviewer returns concise live findings, not an artifact:

```text
[ID] [blocking|material|minor] Summary
Evidence: exact path/section and contradiction or missing contract
Impact: why it matters
Recommendation: smallest correction preserving the intended outcome
Human decision: yes/no; exact question when yes
```

On recheck, the reviewer re-reads the whole corrected draft, resolves prior findings, and lists every remaining or new issue. It says `CLEAN` only when none remains.
