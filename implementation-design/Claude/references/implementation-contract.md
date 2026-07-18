# Implementation design contract

## Purpose

Capture technical and security meaning shared by multiple delivery tasks. Do not duplicate the PRD or pre-write the task graph.

## Semantic structure

Adapt headings to the target repository while preserving:

```markdown
# Implementation design: feature/version

## Accepted PRD reference
## Current system and owner components
## Proposed technical shape
## Contracts and data
## Integration boundaries
## Failure, retry, and recovery
## Compatibility, migration, rollout, and rollback
## Security and trust boundaries
## Observability and operations
## Verification strategy
## External inputs and execution prerequisites
## Vertical-delivery constraints
## Open technical or risk decisions
```

## Core rules

- Bind the design to one accepted PRD version or hash.
- Assign one owner to orchestration state and every durable contract.
- Describe invariants and boundaries, not speculative file-by-file edits.
- State partial success, retry, idempotency, concurrency, recovery, and rollback where relevant.
- Enable an early meaningful end-to-end verification path.
- Separate current-version requirements from future horizon.

## Security contract

Classify depth:

- `quick`: no new material trust, sensitive-data, privilege, or external-input boundary;
- `standard`: ordinary auth, stored data, external input, or integration risk;
- `deep`: payment, identity, privileged secrets, sensitive user data, multi-tenant isolation, destructive/irreversible behavior, or comparable high impact.

For relevant risks, define actors, assets, trust boundaries, authorization ownership, data and secret lifecycle, external-input abuse cases, dependency failure, fail-open/fail-closed behavior, recovery, and residual risk. Give required controls and verification stable IDs such as `SEC-01` and `VER-01` so delivery planning can map them without redesigning them.

Invoke the `feature-security-review` skill (via the Skill tool as `/feature-security-review`) only for `deep` risk or explicit human request. Keep its durable result in this implementation document, then use one `cross-model-review` `implementation` pass for the combined technical and security contract.

## External prerequisites

Record every known human-supplied asset, dataset, access, credential, environment, budget authorization, external approval, or human validation dependency. State why it is needed, the stage that consumes it, safe handling, and what may proceed without it. Never record secret values or sensitive payloads. Detailed status tracking belongs to delivery planning's conditional `EXECUTION-READINESS.md`.

## No-document result

Use `implementation_doc_not_required` only when one bounded task can safely own all shared notes and no material shared security decision exists. Give the reason and constraints that the `feature-delivery-plan` skill must preserve.

## Review readiness

Cross-model review requires one complete, self-contained `draft` or `proposed` implementation artifact with substantive sections, no placeholders, an exact PRD reference, explicit open decisions, security depth, and known external prerequisites.
