# Ownership README

Use this only for a durable service, module, package, or feature ownership zone.
Do not create it for a trivial directory.

## Responsibility

- behavior and state owned here
- behavior explicitly owned elsewhere

## Public Contract

- supported entrypoints, commands, events, or interfaces
- invariants visible to neighboring zones

## Dependencies And Integrations

- allowed dependencies
- external providers or adapters
- private internals that neighboring zones must not import

## Failure And Recovery

- meaningful failure semantics
- retry, idempotency, rollback, or recovery rules when applicable

## Tests

- unit tests
- contract tests
- integration tests
- minimum verified commands

## Related Authority

- accepted decisions
- runtime/deploy evidence
- runbooks

Implementation details remain in code and tests.
