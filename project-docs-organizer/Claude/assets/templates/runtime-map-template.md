---
title: Runtime Map
doc_type: runtime_map
status: approved
authority_for:
  - runtime_navigation
owner: runtime
last_reviewed: YYYY-MM-DD
related: []
supersedes: null
superseded_by: null
---

# Runtime Map

Project-level navigation between runtimes. Create it only when several runtimes
or deploy owners exist; a single runtime needs only its runtime README. It routes
between runtimes and never restates the capability-level ownership map that lives
inside each runtime README. Every line routes to an owner or to evidence; a line
without an anchor does not belong here.

## Runtime Surfaces

- runtime or application → code root → owner → local README → tests

## Environments And Deploy Ownership

- environment → deploy-trigger repo and path → release or evidence location

## Live Integrations

- integration → owning code or config path → owning runtime

## Operational Links

- deploy and rollback runbooks
- smoke or health evidence

This map routes to deployed-state evidence and local runtime documentation. It
replaces neither, and it does not describe environments, integrations, or runtime
behavior in prose.
