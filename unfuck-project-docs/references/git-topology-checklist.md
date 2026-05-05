# Git Topology Checklist

Use this checklist when creating or verifying repo boundaries.

## Questions To Answer

- Does any relevant `.git` already exist?
- If git exists, which path or paths does it cover?
- Is this a greenfield project or an existing one?
- Does the project root already have a git repo?
- Does `src/` already have its own git repo?
- Does `src/` already contain multiple separately versioned runtime repos?
- Is `src/` currently tracked by the project-root repo?
- Which repo and path own deploy-triggering changes?
- Does the requested work require creating or modifying git boundaries?

## Required Outcomes

- the detected git state is documented before any topology-changing work
- if git already exists, the user explicitly decides whether to keep it before topology mutations
- if no git exists yet, the user explicitly chooses `single_repo` or `split_src_repo` before `git init`, unless they explicitly request `multi_runtime_split`
- if `split_src_repo` is chosen, the project root repo and `src/` repo are separate git histories
- if `split_src_repo` is chosen, the project-root repo does not become the deploy source for runtime code
- if `split_src_repo` is chosen, `src/` is ignored by the project-root repo
- if `split_src_repo` is chosen, the `src/` repo owns its own commits, CI, and deploy-triggering changes
- if `single_repo` is chosen, one repo owns both layers and the deploy-triggering `src/` path is documented clearly
- if `single_repo` is chosen and deploy automation uses path filters or similar gating, those rules point at `src/` rather than docs-only paths unless broader deploy triggers are explicitly intended
- if `multi_runtime_split` is chosen, each separately versioned runtime path under `src/` is listed explicitly and its deploy ownership is documented
- if `multi_runtime_split` is chosen, the project-root repo ignores those nested runtime repos appropriately

## If The Project Is Greenfield

- if no git exists, present `single_repo` and `split_src_repo` explicitly as the default choices
- if the target project is empty or nearly empty, do not infer naming or architecture from sibling directories, adjacent repos, or similarly named projects
- if the target project is empty and product shape is still unclear, ask the user for the missing context instead of scavenging nearby projects
- if `split_src_repo` is chosen, create the separate repo inside `src/` and ignore `src/` from the project-root repo
- if the user explicitly asks for multiple separately versioned runtimes, create `multi_runtime_split` under `src/` and document each runtime repo path explicitly
- ensure the chosen model is documented in project `AGENTS.md`

## If The Project Already Exists

- inspect current `.git` boundaries
- ask whether the current git topology should be kept before proposing a change
- inspect whether runtime files are tracked by the wrong repo
- verify that deploy-triggering files live in `src/` and are owned by the correct git repo
- if multiple runtime repos exist under `src/`, enumerate them explicitly instead of collapsing them into `split_src_repo`
- fix ambiguity before declaring the playbook applied

## Approval Rule

If applying the playbook requires creating repos, changing nested boundaries, editing ignore rules, or doing any other git mutation:

- request explicit user approval before proceeding
- stop and wait for the user's reply
- do not rely on sandbox or tool-level permission prompts as a substitute for the skill's approval gate
