---
title: Repo Map
doc_type: repo_map
status: approved
source_of_truth: true
owner: project
last_updated: YYYY-MM-DD
related: []
supersedes: null
superseded_by: null
---

# Repo Map

## Repo Model

- chosen model: `single_repo`, `split_src_repo`, or `multi_runtime_split`
- runtime git paths: `n/a`, `src/`, or `<explicit list under src/>`
- how `src/` is versioned: tracked by the project-root repo, owns its own `.git`, or contains nested runtime repos

## Physical Layout

- where the workspace control-plane layer lives
- where `src/` lives
- which repo or path owns deploy-triggering changes

## Ownership

- where major code surfaces live

## Git Boundaries

- if `single_repo` is chosen, confirm that one repo owns both layers and that the deploy-triggering `src/` path is documented
- if `split_src_repo` is chosen, confirm that the project-root repo and `src/` repo are separate histories
- if `split_src_repo` is chosen, confirm that the project-root repo does not track `src/` incorrectly
- if `multi_runtime_split` is chosen, list each separately versioned runtime repo path under `src/` and confirm which deploy surface it owns
