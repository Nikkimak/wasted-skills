---
name: apply-project-playbook
description: Apply the canonical project repo and documentation playbook to a new or existing coding project. Use when Codex needs to bootstrap a project workspace, split or verify parent repo versus runtime repo boundaries, choose minimal versus standard versus full documentation scope, create canonical bootstrap/docs files from templates, or upgrade an existing project to the playbook model without violating the source-of-truth rules.
---

# Apply Project Playbook

Use this skill to apply the bundled canonical playbook to a real project.

Keep the canonical source of truth in:

- `references/llm-friendly-project-structure-playbook.md`
- `references/project-agents-template.md`

Do not treat this skill as a replacement for the canonical playbook. Use it as the execution layer that decides scope, selects templates, and verifies the result.

## Workflow

1. Read the canonical playbook and project bootstrap files first.
2. Inspect the project shape, repo layout, runtime surfaces, and existing docs.
3. Read `references/mode-selection.md` to choose `minimal`, `standard`, or `full`.
4. Read `references/git-topology-checklist.md` if repo boundaries are missing, ambiguous, or need to be created.
5. Read `references/canonical-docs-matrix.md` to determine the required file set for the chosen mode.
6. Read `references/implementation-checklist.md` before making edits.
7. Use the templates in `assets/templates/` only for the files that are actually needed.
8. Verify the final state against the implementation checklist and the canonical playbook.

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
  Read when creating or verifying parent repo versus runtime repo separation.
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
