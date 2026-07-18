---
name: project-docs-organizer
description: Organize project documentation, source-of-truth boundaries, workspace structure, and related git topology using the bundled canonical playbook. Use for initial bootstrap, one-time migration, or major structural cleanup; choose the smallest documentation mode, preserve existing git by default, use split runtime repos only when justified, require approval and a preflight backup before mutation, then verify the result. Do not use for routine maintenance in an already organized project.
---

# Project Docs Organizer

Apply the bundled playbook to a real project. Treat all bundled references and templates as read-only unless the human is updating this skill itself. Inspect and report only when the request is analysis-only.

## Reference Routing

- Always read target repository instructions, `references/playbook-source.md`, `references/git-topology-checklist.md`, `references/mode-selection.md`, and `references/canonical-docs-matrix.md` during discovery.
- Read `references/llm-friendly-project-structure-playbook.md` completely before a concrete structural recommendation or execution.
- Before execution, also read `references/implementation-checklist.md` and `references/templates-policy.md`. Read `references/project-agents-template.md` when creating or validating project `AGENTS.md`.
- Use only the templates required by the approved mode and project evidence.

## Workflow

1. Decide whether this skill applies. Use it only for bootstrap, migration, or major structural cleanup; use ordinary project work for routine maintenance.
2. Inspect only the target project unless the human approves an external reference. Resolve the actual root, existing instructions, git boundaries, runtime/deploy surfaces, canonical docs, and whether live truth, decisions, and future plans are mixed. If an empty project lacks product context, ask instead of borrowing names or architecture from nearby repositories.
3. Choose the smallest sufficient `minimal`, `standard`, or `full` mode, the repo model, and `audit_only`, `update_existing_docs`, or `create_missing_canonical_docs`. Prefer updating or splitting strong existing docs over parallel replacements.
4. Present the discovery report and approval contract below. Stop for explicit approval before any mutation.
5. After approval, create the approved preflight backup before the first mutation. Apply only the approved structure, git-boundary, and documentation changes; re-ask if scope changes materially.
6. Verify the result against the full playbook and implementation checklist, then report the realized topology, documentation strategy, files changed or verified, intentional omissions, and remaining risks.

## Decision Rules

- Preserve existing git topology by default. If git exists, ask whether to keep it before proposing a change.
- If no git exists, recommend `single_repo`. Use `split_src_repo` only for explicit runtime isolation or a concrete deploy/ownership reason. Use `multi_runtime_split` only when requested or already present, and enumerate every runtime repo path.
- Default to `minimal`; use larger modes only when runtime, ownership, operations, or coordination evidence requires them.
- Do not create duplicate current-state docs, empty ceremonial directories, or a weaker template-shaped replacement for stronger project documentation.
- Keep exactly one owner for each canonical fact and git path. Document deploy-triggering ownership explicitly.

## Approval Contract

Discovery and read-only git inspection need no approval. Creation, editing, deletion, renaming, document splitting, git initialization, ignore-rule changes, file moves across repo boundaries, and other topology mutations do.

Before execution, provide these fields in compact form:

```text
mode: minimal | standard | full
git_state: detected boundaries | no_git_found
repo_model: single_repo | split_src_repo | multi_runtime_split
runtime_git_paths: n/a | src/ | explicit paths
git_topology_decision: keep_existing_git | create_single_repo | create_split_src_repo | create_multi_runtime_split | approved change
documentation_strategy: audit_only | update_existing_docs | create_missing_canonical_docs
git_topology_impact: none | concise impact
backup_decision: ask create_backup or explicit decline
backup_scope: exact targets
planned_changes: exact files or areas
risks_or_unknowns: unresolved boundaries or splits
```

Ask whether to create/update missing canonical docs, whether to create the recommended backup, and whether execution is approved. Stop and wait; tool permission prompts do not replace this gate.

## Backup And Execution

- Create the approved timestamped snapshot under `<project-root>/.playbook-backups/` before mutation. Scope it to planned targets, or the full affected doc set for broad splits/reorganization.
- Include a manifest with the approved mode, repo model, topology decision, documentation strategy, scope, planned changes, and read-only branch/`HEAD`/dirty-state context when available.
- Keep snapshots immutable, local, untracked, and outside canonical truth. Warn when the directory is not ignored; changing ignore rules requires separate approval. Record an explicit decline instead of silently skipping backup.
- If approved scope expands materially, obtain approval and create a new snapshot for the newly affected targets.
- Adapt templates to project evidence, preserve useful content and unrelated work, and never modify bundled references while applying the skill.

## Required Outcome

- The source-of-truth hierarchy and startup read path are explicit and non-contradictory.
- `WORKPLAN.md` is the canonical queue; task packets stay outside `context/`; at most one future-work area exists.
- Required documents for the selected mode exist or are verified as stronger equivalents.
- `src/` remains self-sufficient for narrow changes without becoming a second architecture wiki.
- Git ownership and deploy boundaries match the approved repo model.
- The final report states the chosen mode/model/strategy and rationale, backup result, created/updated/verified files, excluded scope, and unresolved decisions.
