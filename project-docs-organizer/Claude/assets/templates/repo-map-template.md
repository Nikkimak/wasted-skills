---
title: Repository Map
doc_type: repo_map
status: approved
authority_for:
  - repository_ownership
owner: project
last_reviewed: YYYY-MM-DD
related: []
supersedes: null
superseded_by: null
---

# Repository Map

## Detected Model

- model: `single_repo | split_src_repo | multi_repo_runtime | existing_other | no_git_found`
- explanation when `existing_other` or `no_git_found`: `<one line or n/a>`

## Ownership

- repository root and owned paths
- runtime work surfaces
- documentation/control-plane paths
- deploy-trigger paths and workflows

## Boundaries

- nested repositories or exclusions
- paths that must not be tracked by a parent
- relationship between runtime shape and git ownership

Project shape does not determine this repository model.
