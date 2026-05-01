# Implementation Checklist

Use this checklist when applying the playbook to a project.

## 1. Inspect

- read the nearest relevant `AGENTS.md`
- inspect project layout
- inspect runtime surfaces
- inspect existing canonical docs
- inspect repo boundaries

## 2. Decide Whether This Skill Should Be Used

- decide whether the project actually needs one-time structural adoption, migration, or major cleanup
- if the project is already organized and the request is ordinary maintenance, stop here and use normal project work instead
- if unsure, stay in discovery and state explicitly why this skill does or does not apply

## 3. Assess Repo Boundaries And Existing Documentation

- inspect whether the parent repo exists
- inspect whether the runtime repo exists
- deploy-triggering changes belong to the runtime repo
- parent repo does not track runtime repo files incorrectly
- inspect whether there is already substantial project documentation
- identify which existing docs should be updated or split instead of replaced

## 4. Choose Scope

- select `minimal`, `standard`, or `full`
- identify the chosen future-work area if one is needed
- decide whether a task layer is needed
- decide whether the documentation strategy is `audit_only`, `update_existing_docs`, or `create_missing_canonical_docs`

## 5. Approval Gate

- summarize current project state, proposed mode, repo model, planned changes, and risks
- include the mandatory approval fields defined by `SKILL.md`
- ask whether to create or update missing canonical guides/docs now, especially when existing documentation already exists
- ask whether to create the recommended preflight backup before the first mutation
- ask the user for explicit permission to proceed
- stop and wait for the user's reply
- do not create, edit, rename, move, or delete project files before that reply

## 6. Create The Approved Preflight Backup

- create the approved preflight backup before the first mutation
- record the approved mode, repo model, documentation strategy, backup scope, and planned changes in the backup manifest

## 7. Apply Approved Repo Boundary Changes And Materialize Canonical Docs

- create or update repo boundaries only after approval

- create or update project-level `AGENTS.md`
- create or update `WORKPLAN.md`
- create or update `context/README.md`
- create or update `context/current/project-state.md`
- create or update `context/current/runtime-map.md`
- create or update `context/current/repo-map.md`
- create or update `context/decisions/README.md`
- create runbooks, component guides, and future-work docs only if needed by the chosen mode
- create `src/README.md`

## 8. Verify Hard Rules

- `WORKPLAN.md` remains the canonical queue summary
- task layer is outside `context/`
- `context/README.md` remains a short entrypoint and not a second wiki
- there is one chosen future-work area at most
- `src` is not silent
- runtime docs do not become a second architecture wiki

## 9. Close Out

- verify docs match current mode
- verify the approved backup was created or explicitly declined by the user
- verify no stale docs masquerade as live truth
- summarize what was created, what was verified, and what remains intentionally out of scope
