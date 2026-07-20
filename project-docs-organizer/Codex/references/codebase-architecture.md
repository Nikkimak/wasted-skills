# Codebase Architecture

## Contents

1. Applicability and outcome
2. Ownership-oriented services
3. Boundaries and dependencies
4. Testing shape
5. File decomposition heuristics
6. Project-local contract
7. Audit behavior

## Applicability And Outcome

Read this reference only for code-bearing bootstrap, architecture audit,
project-local architecture documentation, or explicitly approved
reorganization.

The desired outcome is a codebase where a contributor can identify the owner of
behavior, change it through an explicit contract, and run a bounded test surface.
No physical tree is universally required.

Prefer a modular monolith or cohesive existing runtime until independent
deployment, scaling, security isolation, or organizational ownership justifies
a separate runtime service.

## Ownership-Oriented Services

A service is a durable logical ownership zone. It may be a module, package,
directory, application component, or separately deployed process.

A distinct service boundary is justified when several of these are true:

- it owns a coherent business capability or state transition;
- it exposes a public contract to neighboring zones;
- its internals should not be imported directly;
- it has a meaningful independent unit, contract, or integration test surface;
- failure and recovery semantics differ from neighboring behavior;
- a stable team or runtime owner can be named.

Do not create a service for every entity, endpoint, framework primitive, or
small helper. Do not create empty `domain`, `application`, `contract`, or
`infrastructure` layers in anticipation of future complexity.

Possible layouts include domain modules inside one application, packages inside
a monorepo, feature-oriented frontend areas, or several deployable runtimes.
Use the project's framework-native shape when it preserves ownership clarity.

## Boundaries And Dependencies

- Assign one owner of business correctness for each domain behavior.
- Keep transport handlers focused on input, owner invocation, and response
  mapping.
- Keep persistence focused on storage mapping and queries, not domain policy.
- Keep provider and integration adapters from becoming hidden domain owners.
- Use explicit public contracts across ownership zones.
- Prevent neighboring zones from importing private internals by convention,
  tooling, or review where proportionate.
- Keep shared areas limited to genuinely shared primitives. Move business logic
  back to a named owner instead of growing generic `utils` or `helpers` dumps.
- Place new work by domain ownership and behavioral role from the start.

Cross-zone orchestration belongs to a clearly named application owner. It must
not duplicate the state machine of the services it coordinates.

## Testing Shape

Tests should make ownership and failure boundaries visible.

- Unit tests cover pure policies, calculations, and state transitions.
- Contract tests cover the public behavior exposed to neighboring zones.
- Integration tests cover persistence, providers, queues, frameworks, and other
  real adapters at the appropriate boundary.
- End-to-end tests cover a small number of critical paths across owners.
- Test support and fixtures should have an explicit scope and must not become a
  second implementation of business behavior.

Prefer tests colocated with the owner or in a mirrored ownership structure. A
service boundary is weak if its behavior can be verified only through the full
application.

## File Decomposition Heuristics

Line counts trigger responsibility review; they do not replace cohesion
judgment.

### General Scale

- Below roughly 300 lines: normal target when the file remains coherent.
- 300–500 lines: review responsibility and testability; keep when one owner and
  role remain clear.
- Above 500 lines: require an explicit decomposition review.
- Above 800 lines: expect an approved split or a documented cohesive exception.

### Type-Specific Targets

| File type | Typical target | Review pressure |
| --- | ---: | --- |
| Route, controller, or transport handler | 150–250 | Extract business behavior before adding branches |
| Domain policy, value object, or pure behavior | 150–300 | Split when several invariants or state machines mix |
| Application service or use case | 250–400 | Split orchestration by use case or owner |
| Integration or provider adapter | 300–500 | Separate transport, mapping, retry, and domain policy |
| UI component | 150–250 | Separate rendering, data orchestration, and state policy |
| Feature container or screen | 250–400 | Extract stable subcomponents and behavioral hooks |
| Test suite | 400–600 | Split by behavior, contract, or scenario rather than setup alone |

Functions around 40–60 lines with several branches deserve extraction review,
especially when pure rules and side effects mix.

Generated code, declarative schemas, migrations, static mappings, fixtures,
framework-required aggregators, and other cohesive mechanical files may exceed
these ranges. The exception must not hide mixed ownership.

Avoid arbitrary extraction into generic helper files. Split by domain owner,
use case, public contract, side-effect boundary, or testable behavior.

## Project-Local Contract

The bundled guidance helps bootstrap or assess a project; it is not the daily
authority afterward.

Keep only a short rule in project `AGENTS.md`:

- place code by domain owner and behavioral role;
- review responsibility around 300–500 lines;
- require decomposition review above 500 lines;
- do not create microservices without a concrete runtime or ownership reason.

Put adapted thresholds, exceptions, service boundaries, and test commands in a
runtime README or an optional runtime-local architecture document only when the
project needs them. Do not copy the full default table into every project.

## Audit Behavior

During audit:

1. identify actual ownership and test surfaces;
2. report ambiguous boundaries, private cross-imports, ownerless shared logic,
   and mixed-responsibility large files;
3. distinguish documentation gaps from code restructuring;
4. propose the smallest boundary or documentation improvement;
5. stop for explicit approval before moving or rewriting code.

Existing god-files are debt findings, not permission to refactor during
documentation bootstrap.
