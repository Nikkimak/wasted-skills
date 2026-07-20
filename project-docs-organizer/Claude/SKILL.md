---
name: project-docs-organizer
description: Audit or reorganize project documentation, authority routing, runtime guidance, workspace structure, and git topology with minimal mandatory context. Use for bootstrap, one-time documentation or context-economy audits, migrations, or major cleanup in documentation-primary or code-bearing projects; optionally assess code organization when explicit. Preserve strong structures and git, require approval plus a scoped backup before mutation, and exclude routine maintenance.
---

# Project Docs Organizer

Create the smallest sufficient documentation and read path. Treat bundled
resources as read-only. For analysis-only requests, inspect and report only.

## Reference Routing

Read only what the observed shape and action require:

- Discovery: the target project's own instructions,
  `references/authority-and-intent-routing.md`, and
  `references/project-shape-and-scope.md`.
- Documentation roles, locations, metadata, runtime-local docs, or routing:
  `references/documentation-architecture.md`.
- Code-bearing bootstrap, architecture audit or contract, or scoped code
  reorganization: `references/codebase-architecture.md`.
- Ambiguous, verified, or changing git/deploy ownership:
  `references/git-topology-checklist.md`.
- Retrieval quality or infrastructure: `references/retrieval-and-indexing.md`.
- Before mutation: `references/implementation-checklist.md` and
  `references/templates-policy.md`; use only approved templates.

Do not read every reference merely because it exists.

## Workflow

1. Confirm this is bootstrap, one-time audit, migration, or major cleanup; route
   routine maintenance elsewhere.
2. Classify intent and authority, then inspect only the target unless external
   references are approved. Resolve root, instructions, work surface, docs,
   runtime/tests, applicable git/deploy ownership, and conflicting truth.
3. Select the least structural evidence-supported shape and independent scopes.
   Preserve strong equivalents.
4. For analysis-only work, report and stop. Otherwise present the approval
   contract and wait for explicit approval.
5. After approval, create the scoped backup, apply only approved changes, and
   re-approve any expansion.
6. Verify routing, context economy, ownership, applicable git/deploy boundaries,
   negative requirements, and integrity. Report changes, omissions, and risks.

## Discovery Behavior

Discovery uses read-only inspection: Glob and Grep for paths, terms, symbols,
and ownership surfaces; Read for candidate slices; Bash only for non-mutating
commands such as `git status`, `git rev-parse`, `git log`, and `git check-ignore`.
Rank ownership candidates before opening content. When discovery would span many
independent areas, delegate bounded read-only sweeps to Explore or general-purpose
subagents and keep synthesis, the approval contract, and every mutation in this
session.

## Decision Rules

- Shape never grants documentation volume, mutation, git, or retrieval scope.
- Default to `documentation_primary` for document work and `single_runtime` for
  code unless durable contracts, protected internals, or independent tests
  justify more structure.
- Never create evidence-free runtime docs, empty layers, or ceremonial folders.
- Keep contributor guidance near code; keep product, rationale, deployment,
  operations, planning, and evidence distinct.
- Code/tests own implementation behavior; verified runtime evidence owns
  deployed state. Documents route to them and own durable meaning.
- Code does not authorize restructuring; logical services are not deploy units.
- Preserve git topology. Use deterministic retrieval unless separately approved.

## Approval Contract

Discovery is read-only. Any creation, edit, deletion, rename, split, move, code
reorganization, git change, retrieval infrastructure, or other mutation needs
approval.

Before mutation, report only applicable fields:

```text
project_shape: documentation_primary | single_runtime | modular_runtime | multiple_runtime_surfaces
detected_repo_model: single_repo | split_src_repo | multi_repo_runtime | existing_other | no_git_found
git_topology_decision: keep_existing | propose_change | approved_change | n/a
target_repo_model: single_repo | split_src_repo | multi_repo_runtime | existing_other | n/a
documentation_scope: baseline | evidence_selected_areas
mutation: audit_only | update_existing | create_missing | reorganize
code_architecture_scope: none | assess_only | document_contract | propose_restructure | approved_restructure
runtime_docs: not_applicable | existing_sufficient | update_entrypoint | add_ownership_docs
retrieval_scope: none | deterministic_guidance | assess_advanced
backup: required | explicitly_declined | not_applicable
backup_scope: exact targets | n/a
planned_changes: exact paths or areas
risks_or_unknowns: concise list | none
intent_paths_to_validate: subset of local_known_owner | unknown_owner | product | rationale | deployed_state | operations | documentation_lookup
```

Derive this contract; do not turn it into a questionnaire. Explain
`existing_other`. No field grants another. Stop and wait for approval. A granted
tool permission, an allowlisted command, and a permissive permission mode are
not approval; only the human's explicit answer to this contract is.

## Backup And Execution

- Before mutation, snapshot exact targets under
  `<project-root>/.playbook-backups/<timestamp>/`; include the contract and
  available branch, `HEAD`, and dirty state.
- Keep it local, immutable, untracked, and ignored; warn if not ignored. An
  ignore-rule edit needs approval. Record an explicit backup decline.
- Back up and approve newly expanded scope before changing it.
- Adapt templates to evidence; remove unused placeholders and preserve useful
  content and unrelated work.
- Never commit, push, or deploy. Those remain separate human instructions even
  after mutation is approved.

## Required Outcome

- Intent bounds startup context; each fact class has one authority and links.
- Documentation-primary projects avoid runtime ceremony; code-bearing projects
  get only sufficient local ownership and test navigation.
- Architecture, git, retrieval, and mutation scopes never expand implicitly.
- Report shape/scopes, approval/backup, changed or verified files, omissions,
  validation paths, and risks.
