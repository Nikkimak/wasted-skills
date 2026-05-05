# AGENTS.md

## Scope

This file is the canonical operating manual for this project.
It overrides higher-level workspace routing files for project-specific behavior.

## Project Summary

- what this project is
- what problem or product surface it owns
- whether it is a standalone repo or part of a larger workspace

## Repository Model

- repo model: `single_repo`, `split_src_repo`, or `multi_runtime_split`
- workspace control-plane location: `<path or explanation>`
- deployable runtime location: `src/`
- runtime git paths: `n/a`, `src/`, or `<explicit list under src/>`
- if current git topology is being preserved intentionally, say so explicitly
- if `split_src_repo` is chosen, clarify that `src/` is a separate git repo and ignored by the project-root repo
- if `multi_runtime_split` is chosen, enumerate each separately versioned runtime repo path under `src/`
- state which repo and path trigger deploys

## Canonical Read Order

For a fresh session, read in this order:

1. `WORKPLAN.md`
2. `context/README.md`
3. `context/current/project-state.md`
4. `context/current/runtime-map.md`
5. `context/current/repo-map.md`
6. `context/decisions/README.md`
7. then only task-specific docs

If this project uses a different structure, replace this list with the actual canonical path.

## Source Of Truth Rules

- `WORKPLAN.md` = active queue
- optional task directories may exist, but they do not replace `WORKPLAN.md` as the canonical queue summary
- `context/current/` = current live truth
- `context/decisions/` = accepted rules and boundaries
- the chosen future-work area = future or in-progress change work
- `knowledge/` = reference material unless explicitly promoted into canonical docs

If two docs conflict:

- current live docs beat future-oriented design docs
- accepted decisions beat future-work proposals unless superseded explicitly

## Required Update Rules

After meaningful runtime or rollout changes:

- update `context/current/`

After accepting or changing a rule or boundary:

- update `context/decisions/`

After changing active priorities:

- update `WORKPLAN.md`

Do not call work complete if runtime reality changed and canonical docs were left stale.

If this project uses task packets or handoff bundles:

- keep them in a dedicated task layer outside `context/`
- do not store the only copy of live truth or accepted architecture in task packets

## Runtime Ownership

State clearly:

- where runtime code lives
- what runtime-facing docs must remain in `src/`
- which service owns business correctness for each major domain
- which layers are adapters only
- what must not become a shadow backend
- what a contributor can do safely using only `src/`

## Deploy Model

Document at a high level:

- which repo and path trigger deploy
- what artifact is deployed
- which environments exist
- where rollback and smoke-test procedures live

## Boundaries

Non-negotiable rules for this project:

- exactly one owner of business correctness per domain
- adapters, workers, MCP servers, and workflows do not own hidden business rules
- projections and operator tools are not source of truth unless explicitly documented otherwise
- secrets and runtime-mutated config do not belong in git

## Project Paths

Useful paths:

- runtime code: `src/`
- runtime-facing docs in src: `<path>`
- current-state docs: `<path>`
- decisions: `<path>`
- future-work docs: `<path>`
- runbooks: `<path>`
- task layer: `<path or n/a>`
- tests: `<path>`

## Notes For Agents

- prefer canonical docs over chat history
- do not assume reference notes are live truth
- identify the owner service before changing business logic
- keep code and canonical docs aligned in the same work cycle
- keep `src/` self-sufficient for narrow local changes
- do not create a full feature dossier for every small change
