# Security readiness checklist

## Scope and assets

- What user/business outcome is being protected?
- Which sensitive data, credentials, money, identity, permissions, or critical operations are introduced or changed?
- What is explicitly outside the current version?

## Actors and trust boundaries

- Human roles, service identities, agents, admins, anonymous users, attackers.
- Browser/client, API, worker, database, third party, build/deploy, and local machine boundaries.
- Authentication source and authorization decision owner.
- Tenant, project, repository, or account isolation.

## Entry points and abuse cases

- UI/API/webhook/file/prompt/CLI inputs and validation.
- Injection, traversal, SSRF, unsafe deserialization, request replay, confused deputy, mass assignment, and unbounded resource use where relevant.
- Abuse by an authenticated but unauthorized actor.
- Rate, size, concurrency, and retry bounds.

## Data lifecycle

- Collection minimization and purpose.
- Storage, encryption, access, logging/redaction, retention, deletion, export, backup, and migration.
- Cache, analytics, model/provider, and third-party propagation.

## Secrets and privileged execution

- Secret source, least-privilege scope, inheritance, rotation, revocation, and redaction.
- Worker/tool/shell/network/filesystem permissions.
- Whether untrusted or agent-written code can reach runtime credentials or production data.

## Integrations and dependencies

- Third-party auth and permission model.
- Webhook authenticity, replay protection, routing, and idempotency.
- Dependency provenance and high-impact version/config changes.
- Failure when the dependency is missing, slow, duplicated, or malicious.

## State, failure, and recovery

- One owner for security-sensitive state transitions.
- Atomicity/idempotency and race behavior.
- Fail-open versus fail-closed decisions.
- Rollback/revert and recovery evidence.
- Human override and auditability.

## Delivery graph

- Security controls belong to concrete vertical tasks.
- Verification is executable, not a prose promise.
- Deferred work does not defer a control required to make the current version safe.
- Child validation plus parent acceptance cover integration boundaries.
- Deployment and migration requirements are explicit when in scope.
- Accepted PRD and implementation artifacts remain immutable reviewer context unless the owning phase explicitly reopens them as proposed revisions.
- Task contracts remain `proposed` until the final amended set and security posture receive human approval.

## Gate severity

- `critical/blocking`: plausible compromise, privilege bypass, destructive loss, secret exposure, or unsafe irreversible behavior without adequate mitigation. Do not publish tasks.
- `material`: meaningful exploit/failure path requiring mitigation or explicit human risk decision.
- `minor`: worthwhile hardening with limited impact; surface to the human and decide whether to include now.
- `unsupported`: not evidenced by the proposed design/current system; reject with evidence rather than adding ceremony.
