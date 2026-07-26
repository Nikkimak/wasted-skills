# Codebase Architecture

## Applicability And Outcome

Read this reference only for code-bearing bootstrap, architecture audit, a
project-local contributor contract, or explicitly approved reorganization.

The desired outcome is a codebase where a contributor can identify the owner of
behavior, change it through an explicit contract, and run a bounded test surface.
No physical tree is universally required. Prefer a modular monolith or cohesive
existing runtime until independent deployment, scaling, security isolation, or
organizational ownership justifies a separate runtime service.

## Ownership-Oriented Services

A service is a durable logical ownership zone: a module, package, directory,
application component, or separately deployed process. A distinct boundary is
justified when several of these are true:

- it owns a coherent business capability or state transition;
- it exposes a public contract to neighboring zones;
- its internals should not be imported directly;
- it has a meaningful independent unit, contract, or integration test surface;
- failure and recovery semantics differ from neighboring behavior;
- a stable team or runtime owner can be named.

Do not create a service for every entity, endpoint, framework primitive, or small
helper, and do not create empty `domain`, `application`, `contract`, or
`infrastructure` layers in anticipation of future complexity.

Possible layouts include domain modules inside one application, packages inside a
monorepo, feature-oriented frontend areas, or several deployable runtimes. Use
the project's framework-native shape when it preserves ownership clarity.

## Boundaries And Dependencies

- Assign one owner of business correctness for each domain behavior.
- Keep transport handlers, persistence, and provider adapters inside their roles
  — input and response mapping, storage mapping and queries, external
  translation — and out of domain policy.
- Use explicit public contracts across ownership zones, and prevent neighboring
  zones from importing private internals by convention, tooling, or review where
  proportionate.
- Keep shared areas limited to genuinely shared primitives. Move business logic
  back to a named owner instead of growing generic `utils` or `helpers` dumps.
- Place new work by domain ownership and behavioral role from the start.

Cross-zone orchestration belongs to a clearly named application owner and must
not duplicate the state machine of the services it coordinates.

## Testing Shape

Tests should make ownership and failure boundaries visible.

- Unit tests cover pure policies, calculations, and state transitions.
- Contract tests cover the public behavior exposed to neighboring zones.
- Integration tests cover persistence, providers, queues, frameworks, and other
  real adapters at the appropriate boundary.
- End-to-end tests cover a small number of critical paths across owners.
- Test support and fixtures need an explicit scope and must not become a second
  implementation of business behavior.

Prefer tests colocated with the owner or in a mirrored ownership structure. A
service boundary is weak if its behavior can be verified only through the full
application.

## File Decomposition Heuristics

Line counts trigger responsibility review; they do not replace cohesion
judgment. Below roughly 300 lines is the normal target while the file stays
coherent; 300–500 warrants a responsibility and testability review; above 500
requires an explicit decomposition review; above 800 expects an approved split or
a documented cohesive exception.

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
these ranges without hiding mixed ownership. Avoid arbitrary extraction into
generic helper files; split by domain owner, use case, public contract,
side-effect boundary, or testable behavior.

## Project-Local Contract

The bundled guidance helps bootstrap or assess a project; it is not the daily
authority afterward. Keep only a short placement rule in the project router
(`AGENTS.md` or its equivalent):

- place code by domain owner and behavioral role;
- do not create microservices without a concrete runtime or ownership reason.

Put adapted thresholds, exceptions, service boundaries, and test commands in a
runtime README or an optional runtime-local contributor contract, and only when
the project needs them. Each rule has exactly one owning document: a
project-level owner for rules shared across the project, an owner inside the
runtime for runtime-specific ones. Do not copy the full default table into every
project, and never maintain the same rule in two scopes or in both the router and
a runtime document.

That document is a contract for contributors, not a design overview. It must not
contain an account of how the system works, a component inventory, runtime or
request flows, a restatement of the dependency graph, or implementation detail.
An architectural reason belongs in a decision, location belongs in the ownership
map, and behavior belongs in code and tests. A document that starts growing those
sections is a high-level design under another name; stop it there.

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
