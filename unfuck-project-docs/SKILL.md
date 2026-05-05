---
name: unfuck-project-docs
description: Organize and clean up project documentation, workspace structure, and repo boundaries for a real coding project using the bundled canonical playbook as read-only guidance. Use when Codex needs to do an initial bootstrap, one-time migration, or major structural cleanup of project docs; untangle messy canonical documentation; choose between a single project-root git repo, a split model where `src/` has its own git repo, or an advanced multi-runtime split under `src/`; verify or reshape existing git boundaries; choose minimal versus standard versus full documentation scope; or upgrade an existing project to a clearer source-of-truth model. Do not use this skill for routine day-to-day edits in a project that is already organized.
---

# Unfuck Project Docs

Use this skill to apply the bundled canonical playbook to a real project.

This is a bootstrap, migration, and structural-cleanup skill.
It is not the default operating mode for routine project work after the project is already organized.

Keep the canonical source of truth in:

- `references/llm-friendly-project-structure-playbook.md`
- `references/project-agents-template.md`

Do not treat this skill as a replacement for the canonical playbook. Use it as the execution layer that decides scope, selects templates, and verifies the result.

Protected sources:

- do not edit the canonical playbook files in `references/` as part of applying this skill to a project
- do not edit bundled templates unless the user explicitly asks to improve the skill itself
- when this skill is used on a target project, treat the bundled references as read-only authority

## Execution Contract

When this skill is used, the agent should assume the user wants the playbook applied to a real project, not merely described in the abstract, unless the user explicitly asks for analysis only.

Default stance:

- inspect the actual project before proposing structure changes
- keep discovery scoped to the target project unless the user explicitly approves an external reference project or document
- choose the smallest safe mode that removes ambiguity
- perform discovery and planning before any project mutation
- detect whether any relevant git topology already exists before proposing repo changes
- stop after discovery and wait for explicit user approval before entering execution
- if git already exists, ask explicitly whether to keep the current git topology before proposing a change
- if git does not exist yet, present the supported initialization options before proposing `git init`
- if the user explicitly asks for multiple separately versioned runtimes under `src/`, or the existing project already uses them, surface that as a custom multi-runtime repo model instead of forcing the simpler defaults
- if the project already has substantial documentation, ask whether to update/split existing docs only or also create missing canonical guides/docs
- ask explicitly whether to create the recommended preflight backup before the first mutation
- do not modify any project files until the user explicitly approves the proposed plan
- materialize missing canonical files only after that approval exists
- update existing canonical docs instead of creating parallel replacements
- verify the result against the bundled references before calling the work done

Do not stop at a generic recommendation if the project can be inspected and updated directly.
The required stop after discovery is not a generic recommendation stop; it is a mandatory approval boundary.

Invocation boundary:

- use this skill for initial setup of a new project
- use this skill for one-time migration of an older messy project into the canonical structure
- use this skill for major structural cleanup when source-of-truth, repo boundaries, or canonical docs are broken or unclear
- do not use this skill as the default tool for routine feature work, small documentation updates, or normal ongoing project maintenance once the project is already organized
- if the project already follows the intended structure closely, prefer ordinary project work without invoking this skill again

## Workflow

1. Read the canonical playbook and project bootstrap files first.
2. Inspect the project shape, repo layout, runtime surfaces, and existing docs.
3. Read `references/git-topology-checklist.md` before choosing the repo model.
4. Read `references/mode-selection.md` to choose `minimal`, `standard`, or `full` after the repo model is understood.
5. Read `references/canonical-docs-matrix.md` to determine the required file set for the chosen mode.
6. Read `references/implementation-checklist.md` before making edits.
7. Use the templates in `assets/templates/` only for the files that are actually needed.
8. Verify the final state against the implementation checklist and the canonical playbook.

## Approval Gate

This skill operates in two explicit phases:

1. discovery
2. execution

Discovery is allowed without approval:

- inspect the project
- inspect repo boundaries
- inspect git state in read-only ways
- inspect existing docs and bootstrap files
- choose a proposed mode
- identify the minimal required file and structure changes

Execution is not allowed without approval:

- creating, deleting, renaming, or editing project files
- changing git boundaries or repo layout
- running git mutations that change tracked state or repository topology
- creating canonical docs from templates
- rewriting or splitting existing project docs

Before entering execution, the agent must:

- provide a brief summary of the current project state
- report the detected git state
- state the proposed mode and repo model
- state whether the plan keeps the current git topology or changes it
- state the proposed documentation strategy, especially if the project already has existing docs
- list the files or areas it plans to create or update
- mention any risky or boundary-related operations
- state the backup plan it will create before the first mutation
- ask whether to create or update missing canonical guides/docs now, especially when existing documentation already exists
- ask whether to create the recommended preflight backup before the first mutation
- ask the user for explicit permission to proceed

After presenting that discovery report, stop and wait for the user's reply.
Do not create, edit, rename, move, or delete project files in the same turn as the initial approval request unless the user had already approved execution earlier in the conversation.

If the user has not clearly approved execution, remain in discovery mode.

## Git Guardrails

Git inspection is part of discovery and is allowed in read-only form:

- inspect whether any git repo already exists at the project root or intended runtime path
- inspect whether the project root has a git repo and whether `src/` has its own git repo
- inspect whether there is one git repo for the whole project or a split model where `src/` owns its own history
- inspect whether there are multiple separately versioned runtime repos under `src/`
- inspect current git status, branch, and tracked boundaries for each detected repo

Git choice rules:

- if git already exists, ask explicitly whether to keep the current git topology before proposing topology-changing work
- if git does not exist yet, present `single_repo` and `split_src_repo` as the default initialization choices
- if the user explicitly requests multiple separately versioned runtimes under `src/`, or the existing project already has them, use `multi_runtime_split` instead of forcing the simpler defaults

Git mutations require explicit approval:

- `git init`
- editing `.gitignore` for nested repo boundaries
- moving files across repo boundaries
- creating or restructuring project-root versus `src/` repo separation
- any other action that changes tracked state, history, or topology

The agent must explicitly surface the detected git state, the proposed repo model, and whether the current topology will be preserved or changed before applying changes that depend on that model.

## Required Initial Assessment

Before choosing a mode or creating docs, establish these facts from the real project:

- what directory is the actual project root
- whether the target project is effectively empty or near-empty
- whether any git repo already exists, and which path or paths it covers
- whether the project root has a git repo, whether `src/` has a git repo, or whether one repo owns both
- whether `src/` contains multiple independently deployable runtime repos
- which files or directories trigger deploys
- whether canonical bootstrap files already exist
- whether `context/`, `knowledge/`, `WORKPLAN.md`, and `src/README.md` already exist
- whether there is already substantial project documentation that should be updated or split instead of replaced
- whether current docs mix live truth, accepted decisions, and future plans in the same files

If one of these facts is unclear, inspect further before deciding scope.
Do not satisfy missing target-project context by borrowing structure or naming from sibling directories, adjacent repos, or similarly named projects unless the user explicitly approved that reference.

## Decision Heuristics

Use these heuristics to reduce agent drift:

- first decide whether this skill should be used at all, not just which mode to choose
- if the project is already structurally sound and the requested work is ordinary maintenance, do not enter execution under this skill
- default to `minimal` unless there is concrete evidence that `standard` or `full` is needed
- choose `standard` when runtime boundaries, deploy rules, or ownership boundaries would remain unclear under `minimal`
- choose `full` only when the project genuinely has multi-service or multi-repo coordination needs, persistent task packets, or durable future-work tracking needs
- do not create a dedicated future-work area unless active design or rollout work clearly needs one
- if the project already has substantial documentation, prefer updating or splitting the strongest existing docs over creating parallel guide files
- prefer updating and splitting mixed legacy docs over rewriting the entire documentation layer at once
- prioritize navigability and source-of-truth clarity before pursuing completeness
- preserve an existing git topology by default unless the user explicitly approves changing it
- if no git exists yet, do not silently assume split repos; present the supported options and recommend one only when there is a concrete reason
- if the project genuinely needs multiple separately versioned runtime repos under `src/`, surface that as an explicit advanced model instead of overloading `split_src_repo`
- if the target project is empty or near-empty, do not infer architecture or naming from nearby projects; either stay within the canonical template or ask the user for the missing product context

Use-skill decision rule:

- if the main problem is "this project is messy or not yet set up", this skill is appropriate
- if the main problem is "make a normal change inside an already organized project", this skill is not the right default
- if unsure, stay in discovery and explicitly tell the user whether the project appears to need one-time structural adoption or only normal maintenance

## Editing Rules

Apply the playbook with explicit operational discipline:

- read the nearest existing bootstrap files before writing new ones
- never modify project files on the agent's own authority
- never modify the bundled canonical playbook references during project application
- preserve useful project-specific content when adapting templates
- do not replace a stronger existing document with a weaker template-shaped version
- do not create duplicate "current state" files in multiple locations
- do not create empty ceremonial directories just because the full playbook mentions them
- if git topology needs to change, inspect first and request approval before destructive or boundary-altering actions
- if the request is analysis-only, produce a concrete gap report and recommended next edits instead of making changes
- after approval, keep execution scoped to the approved plan or explicitly re-ask if the plan changes materially

## Expected Output

When reporting after discovery, before approval, the agent should report:

- the current project shape in brief
- the detected git state
- whether this project appears to need one-time structural adoption at all
- which mode it recommends and why
- which repo model it recommends and whether git topology changes are needed
- which documentation strategy it recommends and why
- which files or areas it proposes to change
- what backup scope it plans to capture before editing
- which assumptions or blockers still exist
- a direct question about whether to create or update missing canonical guides/docs now
- a direct question about whether to create the recommended preflight backup
- a direct request for permission to proceed

When closing out work after execution, the agent should report:

- which mode was chosen and why
- which repo model was found or created
- which documentation strategy was chosen and why
- whether the approved backup was created or explicitly declined by the user
- which canonical files were created, updated, or verified
- what was intentionally left out of scope
- what risks, ambiguities, or follow-up items remain

Avoid vague summaries such as "set up docs" or "applied structure". The close-out should make it obvious whether the playbook was actually materialized.

## Mandatory Approval Fields

The approval request before execution must include all of these fields in compact form:

- `mode`: the proposed `minimal`, `standard`, or `full` mode
- `git_state`: the detected git boundaries, or `no_git_found`
- `repo_model`: `single_repo`, `split_src_repo`, or `multi_runtime_split`
- `runtime_git_paths`: `n/a` for `single_repo`, `src/` for `split_src_repo`, or the explicit list of separately versioned runtime paths for `multi_runtime_split`
- `git_topology_decision`: `keep_existing_git`, `create_single_repo`, `create_split_src_repo`, `create_multi_runtime_split`, or a brief description of the approved topology change
- `documentation_strategy`: `audit_only`, `update_existing_docs`, or `create_missing_canonical_docs`, plus a brief note when splits or guide creation are proposed
- `git_topology_impact`: `none` or a brief description of the topology change requested
- `backup_decision`: `create_backup` unless the user explicitly declines; this must be asked, not assumed silently
- `backup_scope`: what will be snapshotted before the first mutation
- `planned_changes`: the files or areas to create, update, split, or reorganize
- `risks_or_unknowns`: any unresolved ambiguity, especially around repo boundaries or large document splits

Do not enter execution until the user has approved these fields.

## Preflight Backup Policy

If the user approves execution, create a preflight backup before the first project mutation.

Backup rules:

- create a timestamped snapshot directory under `<project-root>/.playbook-backups/`
- treat `.playbook-backups/` as outside canonical project truth
- do not modify older backup snapshots once created
- do not use the backup directory as working space for canonical docs
- treat the backup directory as local safety data, not as part of the intended project diff
- do not stage, commit, or present backup files as canonical project changes
- include a manifest that records the proposed mode, repo model, git topology decision, backup scope, and planned changes

Scope rules:

- by default, back up only the files and directories the agent plans to change
- if the plan includes splitting or restructuring large mixed docs, back up the full affected doc set, not just the extracted fragments
- if the plan includes broad documentation reorganization, back up the relevant canonical doc areas such as `context/`, `WORKPLAN.md`, bootstrap files, and other approved targets
- if git exists, include read-only git context in the manifest such as branch, `HEAD` when available, and whether the working tree was dirty
- if git exists and `.playbook-backups/` is not ignored, warn that it will remain local untracked safety data unless the user separately approves an ignore-rule change

Plan-change rule:

- if the approved execution scope changes materially later, re-ask for approval and create a new timestamped snapshot for the newly affected scope before mutating it

The backup directory is write-once for the initial snapshot and then should be left untouched during the rest of execution unless the user explicitly asks otherwise.

## Non-Negotiable Rules

- Keep the canonical truth hierarchy intact.
- Keep `WORKPLAN.md` as the single canonical queue summary.
- Keep task packets outside `context/`.
- Keep exactly one chosen future-work area per project.
- Keep `src` self-sufficient for narrow local changes.
- Do not create heavy ceremony for a small project when `minimal` mode is sufficient.
- Do not silently duplicate parent truth into runtime docs.
- Do not create or modify git topology destructively without the needed approval.

## When To Read Which Reference

- `references/playbook-source.md`
  Read when you need the authoritative source paths or the current interpretation of the skill's relationship to the canonical playbook.
- `references/mode-selection.md`
  Read when it is unclear how much of the documentation system should be materialized.
- `references/git-topology-checklist.md`
  Read when creating or verifying project-root git versus split `src/` git separation.
- `references/implementation-checklist.md`
  Read when executing the playbook on a project.
- `references/canonical-docs-matrix.md`
  Read when deciding which canonical docs are required, optional, or out of scope.
- `references/templates-policy.md`
  Read before stamping templates into a project.

## Templates

Use the templates in `assets/templates/` as accelerators, not as unconditional output.

Prioritize these templates first:

- `project-agents-template.md`
- `context-readme-template.md`
- `project-state-template.md`
- `runtime-map-template.md`
- `repo-map-template.md`
- `decisions-readme-template.md`
- `deploy-runbook-template.md`
- `src-readme-template.md`

Use `future-work-status-template.md` only when the project actually needs a future-work area.

## Definition Of Done

Do not consider the playbook application complete until all relevant items below are true:

- existing git presence was checked before topology changes were proposed
- if git already existed, the user explicitly answered whether to keep it
- if git did not exist, the user was offered the supported initialization choices before `git init`
- if `multi_runtime_split` was used, the runtime repo paths were made explicit before execution
- execution was explicitly approved by the user before project files were changed
- the repo model was explicitly confirmed before git topology-changing actions were taken
- a preflight backup was created before the first approved mutation, unless the user explicitly declined it
- the project has a clear startup path for future agents
- the active source-of-truth hierarchy is explicit and non-contradictory
- the chosen mode matches the actual project complexity
- required canonical docs for that mode exist or were explicitly verified as already adequate
- `src/` git boundaries are verified, or the remaining blocker is stated explicitly
- the final report names what was changed, what was verified, and what still needs decisions from the user
