# Ownership README

Use this only for a durable service, module, package, or feature ownership zone,
and only for knowledge the code does not already express. Do not create it for a
trivial directory.

Every section below is conditional: keep what applies and delete the rest. Any
fact recoverable from code, schemas, configuration, or tests becomes a link to
that path, symbol, or test — never a paragraph restating it.

## Code Anchors

- owning path, primary entrypoint or symbol, tests

## Responsibility Boundary

- what is owned here and what is explicitly owned elsewhere, when the code
  structure does not already make that obvious

## Non-Obvious Invariants

- rules a reader would violate after reading the code alone

## External Constraints

- provider, protocol, regulatory, or legacy limits the code cannot state itself

## Failure And Recovery

- semantics that cannot be inferred safely from the implementation
- link the applicable runbook instead of copying its procedure

## Related Authority

- accepted decisions, runtime or deploy evidence, runbooks

Do not restate here: file listings, method signatures, the dependency graph, APIs
or schemas already expressed in code, request flows, the current algorithm, or
change history.
