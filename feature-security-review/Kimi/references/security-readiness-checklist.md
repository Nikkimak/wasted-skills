# Deep feature security checklist

## Outcome and scope

- Protected business outcome and assets.
- Explicit current-version boundary and excluded behavior.
- Human roles, service identities, admins, anonymous actors, and plausible attackers.

## Trust and privilege

- Browser/client, API, worker, database, third party, build/deploy, and local-machine boundaries.
- Authentication source, authorization owner, least privilege, and tenant/account isolation.
- Human override, privileged execution, and audit evidence.

## Inputs and abuse

- UI, API, webhook, file, prompt, CLI, and provider inputs.
- Injection, traversal, SSRF, unsafe deserialization, replay, confused deputy, mass assignment, and unbounded resource use where relevant.
- Authenticated-but-unauthorized abuse, concurrency, size, rate, and retry bounds.

## Data and secrets

- Collection minimization, purpose, storage, encryption, access, logging/redaction, retention, deletion, export, backup, and migration.
- Cache, analytics, model/provider, and third-party propagation.
- Secret source, scope, rotation, revocation, inheritance, and redaction.
- Safe delivery and verification of human-supplied credentials or sensitive datasets without recording values in project documents.

## Integrations and dependencies

- Third-party identity and permission model.
- Webhook authenticity, routing, replay protection, and idempotency.
- Dependency provenance and compromised, missing, slow, duplicated, or malicious behavior.

## State and recovery

- One owner for security-sensitive state transitions.
- Atomicity, races, partial failure, and fail-open/fail-closed behavior.
- Rollback, recovery, evidence preservation, and irreversible operations.

## Durable result

- Put required controls and verification in the implementation design with stable `SEC-*` and `VER-*` IDs.
- Record material residual risk only through an explicit human decision.
- Leave downstream task mapping to the `feature-delivery-plan` skill.
