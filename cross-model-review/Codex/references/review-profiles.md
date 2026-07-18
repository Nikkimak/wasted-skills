# Review profiles

## PRD

Challenge business outcome, users, current/desired behavior, scope, non-goals, MVP boundary, contradictions, unsupported assumptions, open product decisions, observable acceptance/failure behavior, and known human-supplied dependencies. Do not invent implementation detail merely to add completeness.

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

For deep-risk features, use the proposed implementation already enriched by `$feature-security-review`; do not create a second security review stage.

## Task plan

Use only on explicit human request. Challenge requirement/control coverage, vertical slices, bounded scope, dependencies, deferred work, routing, validation, merge targets, parent acceptance, and execution-readiness mapping. Do not make this a default gate.

## Revision

Review a proposed change across an already approved feature-document set. Use the accepted baselines, change intent, and diff to understand the intended delta, but re-read every proposed artifact in full.

Challenge:

- whether the proposed change matches its stated intent without hidden scope expansion;
- PRD coherence and propagation into implementation, security controls, verification, tasks, dependencies, and readiness;
- stale, contradictory, duplicated, or orphaned acceptance criteria, invariants, `SEC-*`, `VER-*`, tasks, and `HIN-*` items;
- unchanged decisions or documents that the revision invalidates;
- migration, compatibility, rollout, rollback, recovery, trust-boundary, residual-risk, and external-prerequisite effects;
- whether the proposed bundle remains complete, executable, and internally consistent.

Treat the bundle as one feature contract. Do not request separate stage reviews merely because multiple document types changed.

## Finding format

```text
[ID] [blocking|material|minor] Summary
Evidence: exact path/section and contradiction or missing contract
Impact: why it matters
Recommendation: smallest correction preserving the intended outcome
Human decision: yes/no; exact question when yes
```

On recheck, re-read the whole corrected draft, resolve prior findings, and list every remaining or new issue. Say `CLEAN` only when none remains.
