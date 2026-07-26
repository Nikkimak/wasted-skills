# Runtime README

Contributor entrypoint for this runtime. Link to project-level product,
rationale, deployed-state, and operations authority instead of copying it.

## Entry Points And Ownership

- runtime entrypoints
- capability or domain → owning path → entrypoint or symbol → tests → optional
  local note
- one line per top-level capability; record `tests: missing` instead of an
  invented path

## Run, Build, And Test

- minimum verified commands

## Public Boundaries

- contracts between ownership zones
- integration and shared-code warnings

## Deploy Entry Point

- high-level trigger and owning runtime map/runbook

## Code Shape

- place code by domain owner and behavioral role
- review responsibility around 300–500 lines
- require decomposition review above 500 lines while allowing cohesive
  generated, declarative, migration, fixture, and framework exceptions
- do not create microservices without a concrete deploy or ownership reason

## Deeper Ownership Docs

- links only where durable boundaries justify them
