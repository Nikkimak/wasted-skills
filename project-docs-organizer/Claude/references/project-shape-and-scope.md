# Project Shape And Scope

## Project Shape

Shape selects guidance and templates, never maturity, documentation volume, git,
or permission.

| Shape | Evidence and consequence |
| --- | --- |
| `documentation_primary` | Documents are the work surface; helper scripts do not change that. Route by authority/status/topic; create no `src/` or runtime docs without evidence. |
| `single_runtime` | One entrypoint is enough for safe work. Prefer one concise runtime README/equivalent; add ownership docs only for real ambiguity, never folder count. |
| `modular_runtime` | Durable zones have public boundaries, protected internals, independent tests, or explicit cross-zone contracts. Domain count alone is weak; prefer `single_runtime` until evidence justifies this. |
| `multiple_runtime_surfaces` | Several runtimes must be navigated, built, tested, or operated. Document each entrypoint, owner, tests, and deploy relationship; do not infer multiple repositories or identical layouts. |

## Independent Selection Axes

Resolve every axis independently; none grants another.

**Repository model.** `single_repo` — one git history owns documentation and
runtime paths; `split_src_repo` — the root and a nested `src/` own separate
histories; `multi_repo_runtime` — more than one runtime history exists;
`existing_other` — a clear existing topology fits none of the labels;
`no_git_found`. Runtime shape and repo model answer different questions; never
derive one from the other.

**Documentation scope.** `baseline` is the smallest evidence-supported
authority/navigation contract; `evidence_selected_areas` adds only evidenced
decisions, operations, runtime ownership, future work, knowledge, or other areas.
Derive scope; do not ask the user to choose a tier.

**Mutation.** `audit_only`, `update_existing`, `create_missing`, `reorganize`.
Mutation grants no code, git, or retrieval authority by implication.

**Code architecture scope.** `none`, `assess_only`, `document_contract`,
`propose_restructure`, `approved_restructure`. Code-bearing may still use `none`;
large or mixed files remain findings until restructuring is explicitly approved.

**Runtime documentation.** `not_applicable`, `existing_sufficient`,
`update_entrypoint`, `add_ownership_docs`. Use `add_ownership_docs` only for
durable modular evidence, real ambiguity, or an explicit request.

**Retrieval scope.** `none`, `deterministic_guidance`, `assess_advanced`.
`assess_advanced` is analysis-only; creation needs separate listed approval.

## Selection Procedure

1. Inspect real work, instructions, docs, runtimes, tests, git, and deploy owners.
2. Identify what each named thing is before choosing its path: workspace,
   project, application, runtime, feature, or document. Do not let an empty tree
   decide that relationship.
3. Reuse established target vocabulary and identifiers. Treat adjacent projects
   as examples unless the human or target instructions establish a shared
   convention. For a new feature, use the standard feature package in
   `documentation-architecture.md`; never transfer its prefix or number to an
   application, decision, or other entity.
4. Choose the least structure that makes ownership and safe work clear. Prefer
   one file for one coherent artifact; create an entity folder only for multiple
   current artifacts or a durable boundary, not anticipated future files. A
   standard feature package is a durable identity boundary from its first PRD.
5. Add only areas required by evidence, ambiguity, operations, or coordination.
   Do not duplicate a project overview across a root entrypoint and a docs index.
6. Preserve clear repo models, including `existing_other`.
7. Separate assessment, documentation, proposals, and approved restructuring;
   present only applicable approval fields.

If an empty or nearly empty target lacks product context, ask the human rather
than borrowing architecture or naming from adjacent projects.

## Compatibility

- Map legacy `minimal`, `standard`, and `full` to present areas; they do not
  select files or shape and should not be renamed mechanically.
- Recognize `multi_runtime_split` as a legacy multi-repository label; preserve
  project language unless an update is approved.
