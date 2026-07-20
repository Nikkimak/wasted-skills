# Git Topology Checklist

Read this reference only when git or deploy ownership is ambiguous, being
verified, or may change. Project shape never selects repository topology.

## Detect

- Resolve every relevant `.git` boundary without mutation.
- Determine which git history owns project documentation and each runtime path.
- Determine whether nested runtime paths are tracked by a parent repository.
- Identify which repo, path, workflow, or artifact triggers each deploy.
- Record branch, `HEAD`, and dirty state when useful for backup or topology work.
- Label a clear unsupported topology as `existing_other` and explain it in one
  line rather than forcing a migration.

## Supported Models

### `single_repo`

- one history owns documentation and runtime paths;
- deploy-triggering paths and workflows are explicit;
- documentation-only changes do not trigger production unless intentionally
  configured.

### `split_src_repo`

- the project root and nested `src/` own separate histories;
- the parent does not accidentally track the nested runtime;
- the runtime repo owns its commits, CI, and deploy-triggering changes.

### `multi_repo_runtime`

- more than one runtime history exists;
- every runtime repo path and deploy owner is explicit;
- the control-plane repo does not accidentally version nested runtime repos.

Legacy `multi_runtime_split` may be recognized as an older label for this git
shape. Do not rename project documentation without approval.

### `existing_other`

- preserve a clear existing topology by default;
- document its actual ownership and deploy behavior;
- propose change only when concrete ambiguity, safety, or operational evidence
  justifies it.

### `no_git_found`

- no relevant git boundary exists;
- keep this as the detected model unless git is created;
- if repository creation is approved, default the target model to `single_repo`.

## Decision Rules

- Preserve existing git topology unless the human approves a change.
- When detection returns `no_git_found`, do not relabel current state. If the
  human approves creating git, default the target to `single_repo`.
- Use `split_src_repo` only for an explicit isolation request or concrete
  deploy/ownership need.
- Use `multi_repo_runtime` only when multiple runtime histories are requested or
  already exist and remain justified.
- Never infer a split repo because project shape is `modular_runtime` or
  `multiple_runtime_surfaces`.
- Never infer a single runtime surface because one repo owns everything.

## Approval And Verification

Before mutation, distinguish:

```text
detected_repo_model: current state
git_topology_decision: keep_existing | propose_change | approved_change | n/a
target_repo_model: intended state | n/a
git_topology_impact: exact paths, histories, ignore rules, CI, and deploy effects
```

Creating repositories, changing nested boundaries, editing ignore rules, moving
files across histories, or changing deploy ownership requires explicit approval
and the approved backup.

After an approved change, verify:

- exactly one intended git owner for every relevant path;
- no accidental parent tracking of nested repos;
- documented repo and deploy ownership match actual configuration;
- unrelated work remains intact;
- no commit, push, or deploy occurred unless separately authorized.
