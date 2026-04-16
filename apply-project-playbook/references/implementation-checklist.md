# Implementation Checklist

Use this checklist when applying the playbook to a project.

## 1. Inspect

- read the nearest relevant `AGENTS.md`
- inspect project layout
- inspect runtime surfaces
- inspect existing canonical docs
- inspect repo boundaries

## 2. Choose Scope

- select `minimal`, `standard`, or `full`
- identify the chosen future-work area if one is needed
- decide whether a task layer is needed

## 3. Verify Or Create Repo Boundaries

- parent repo exists or is created
- runtime repo exists or is created
- deploy-triggering changes belong to the runtime repo
- parent repo does not track runtime repo files incorrectly

## 4. Materialize Canonical Docs

- create or update project-level `AGENTS.md`
- create or update `WORKPLAN.md`
- create or update `context/current/project-state.md`
- create or update `context/current/runtime-map.md`
- create or update `context/current/repo-map.md`
- create or update `context/decisions/README.md`
- create runbooks, component guides, and future-work docs only if needed by the chosen mode
- create `src/README.md`

## 5. Verify Hard Rules

- `WORKPLAN.md` remains the canonical queue summary
- task layer is outside `context/`
- there is one chosen future-work area at most
- `src` is not silent
- runtime docs do not become a second architecture wiki

## 6. Close Out

- verify docs match current mode
- verify no stale docs masquerade as live truth
- summarize what was created, what was verified, and what remains intentionally out of scope
