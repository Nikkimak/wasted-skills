# Project Shape And Scope

## Project Shape

Shape selects guidance/templates, never maturity, documentation volume, git, or
permission.

| Shape | Evidence and consequence |
| --- | --- |
| `documentation_primary` | Documents are the work surface; helper scripts do not change that. Route by authority/status/topic; create no `src/` or runtime docs without evidence. |
| `single_runtime` | One entrypoint is enough for safe work. Prefer one concise runtime README/equivalent; add ownership docs only for real ambiguity, never folder count. |
| `modular_runtime` | Durable zones have public boundaries, protected internals, independent tests, or explicit cross-zone contracts. Domain count alone is weak; prefer `single_runtime` until evidence justifies this. |
| `multiple_runtime_surfaces` | Several runtimes must be navigated, built, tested, or operated. Document each entrypoint, owner, tests, and deploy relationship; do not infer multiple repositories or identical layouts. |

## Independent Selection Axes

Resolve every axis independently.

### Repository Model

- `single_repo`: one git history owns project documentation and runtime paths;
- `split_src_repo`: the project root and nested `src/` own separate histories;
- `multi_repo_runtime`: more than one runtime history exists;
- `existing_other`: a clear existing topology does not fit the supported labels;
- `no_git_found`: no relevant git ownership was detected.

Runtime shape and repo model answer different questions; never derive one from
the other.

### Documentation Scope

- `baseline`: smallest evidence-supported authority/navigation contract;
- `evidence_selected_areas`: baseline plus only evidenced decisions,
  operations, runtime ownership, future work, knowledge, or other areas.

Derive scope; do not ask the user to choose a tier.

### Mutation

- `audit_only`;
- `update_existing`;
- `create_missing`;
- `reorganize`.

Mutation grants no code, git, or retrieval authority by implication.

### Code Architecture Scope

- `none`;
- `assess_only`;
- `document_contract`;
- `propose_restructure`;
- `approved_restructure`.

Code-bearing may still use `none`; large/mixed files remain findings until
restructuring is explicitly approved.

### Runtime Documentation

- `not_applicable`;
- `existing_sufficient`;
- `update_entrypoint`;
- `add_ownership_docs`.

Use `add_ownership_docs` only for durable modular evidence, real ambiguity, or
an explicit request.

### Retrieval Scope

- `none`;
- `deterministic_guidance`;
- `assess_advanced`.

`assess_advanced` is analysis-only; creation needs separate listed approval.

## Selection Procedure

1. Inspect real work, instructions, docs, runtimes, tests, git, and deploy owners.
2. Choose the least structure that makes ownership and safe work clear.
3. Add only areas required by evidence, ambiguity, operations, or coordination.
4. Preserve clear repo models, including `existing_other`.
5. Separate assessment, documentation, proposals, and approved restructuring;
   present only applicable approval fields.

If an empty or nearly empty target lacks product context, ask the human rather
than borrowing architecture or naming from adjacent projects.

## Compatibility

- Map legacy `minimal`, `standard`, and `full` to present areas; they do not
  select files or shape and should not be renamed mechanically.
- Recognize `multi_runtime_split` as a legacy multi-repository label; preserve
  project language unless an update is approved.
