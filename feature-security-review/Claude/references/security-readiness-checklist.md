# Deep feature security checklist

Use this as a relevance filter, not an output template. Analyze only the material delta and affected inherited controls; omit unaffected categories, cite accepted baselines once, and create no separate report.

## Scope and access

- Protected outcome, affected assets/actors, current boundary, and exclusions.
- Changed trust/privilege boundaries, authentication source, authorization owner, least privilege, isolation, overrides, and audit evidence.

## Inputs and abuse

- Affected UI/API/webhook/file/prompt/CLI/provider inputs.
- Relevant injection, traversal, SSRF, deserialization, replay, confused-deputy, mass-assignment, authorization, concurrency, size/rate, and resource-exhaustion cases.

## Data, secrets, and dependencies

- Changed collection, purpose, storage, encryption, access, logging/redaction, retention/deletion/export, backup/migration, cache/analytics, and third-party propagation.
- Changed secret source, scope, delivery, rotation/revocation, inheritance, and redaction; never record values.
- Changed third-party identity/permissions, webhook authenticity, dependency provenance/failure, replay, and idempotency.

## State and result

- Owner of changed security-sensitive state; atomicity, races, partial failure, fail-open/closed behavior, rollback/recovery, evidence, and irreversibility.
- Put only new or changed required controls and verification in the implementation design; reuse existing IDs and create new `SEC-*`/`VER-*` only when needed.
- Record material residual risk only through an explicit human decision.
- Leave task mapping to the `feature-delivery-plan` skill.
