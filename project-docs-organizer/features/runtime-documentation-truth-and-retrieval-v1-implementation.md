---
title: Implementation Design — Context-Efficient Project Documentation And Runtime Architecture V1
doc_type: implementation_design
status: approved
owner: project-docs-organizer
security_depth: quick
human_approval: approved
---

# Implementation Design: Context-Efficient Project Documentation And Runtime Architecture V1

## Accepted PRD Reference

This design implements the accepted product contract in
`project-docs-organizer/features/runtime-documentation-truth-and-retrieval-v1.md`.

The material delta is limited to the Codex-native package under
`project-docs-organizer/Codex/`. Kimi remains unchanged, and the Claude
placeholder remains empty.

## Current System And Owner Components

The Codex package currently consists of:

- a concise `SKILL.md` that requires a complete read of one large canonical
  playbook before structural recommendations;
- overlapping references for playbook authority, modes, git topology,
  canonical documents, templates, and verification;
- templates that assume a code-bearing project and a global
  `source_of_truth` hierarchy more strongly than the accepted PRD allows;
- no dedicated conditional codebase-architecture contract;
- no explicit evaluation contract for mandatory context cost.

The canonical editable package remains `project-docs-organizer/Codex/`. The
installed mirror is a deployment target only and must not be edited directly.

## Proposed Technical Shape

### Entrypoint

Keep `SKILL.md` short. It owns only:

- trigger and non-trigger boundaries;
- discovery and read-only behavior;
- intent, project-shape, and scope selection;
- conditional reference routing;
- approval, backup, mutation, verification, and reporting gates.

It must not restate detailed documentation or codebase architecture guidance.
It must not require every reference for every audit.

### Canonical References

Replace the monolithic canonical playbook and overlapping mode guidance with a
small directly routed set:

- `authority-and-intent-routing.md`: question classes, authority selection,
  bounded read paths, repository-state distinctions, and context-economy
  evaluation semantics;
- `project-shape-and-scope.md`: project shape, documentation scope, repo-model
  independence, mutation scope, and selection evidence;
- `documentation-architecture.md`: baseline documentation roles,
  documentation-primary behavior, conditional runtime/local ownership docs,
  metadata semantics, and drift principles;
- `codebase-architecture.md`: optional code-bearing guidance for domain
  ownership, modular services, public contracts, test surfaces, decomposition,
  and soft file-size review triggers;
- `git-topology-checklist.md`: detected and target git ownership, deploy
  ownership, and explicit topology approval;
- `retrieval-and-indexing.md`: optional deterministic-first retrieval guidance
  and deferred advanced indexing constraints;
- `implementation-checklist.md`: context economy, negative checks, mutation
  scope, package consistency, and final verification;
- `templates-policy.md`: evidence-based template selection and adaptation.

`playbook-source.md` becomes a short map of these canonical responsibilities or
is removed if `SKILL.md` can route them without a second index. The old
`llm-friendly-project-structure-playbook.md`, `mode-selection.md`,
`canonical-docs-matrix.md`, and `project-agents-template.md` reference are
removed only after all still-valid semantics have one new canonical owner and
all inbound references are updated.

No replacement reference should exceed the context justified by its routed
purpose. Longer references must provide a table of contents.

### Templates

Retain and adapt only templates that support evidence-selected outputs:

- project `AGENTS.md` becomes a short intent router and constraint file;
- context index expresses authority by question type rather than a global
  boolean hierarchy;
- runtime README becomes conditional on a code-bearing shape;
- add a service/ownership README template for durable modular boundaries;
- current-state, repo-map, runbook, decision-index, and future-work templates
  remain conditional and must not imply mandatory creation;
- templates must not create empty architecture layers or fixed framework trees.

Templates may contain placeholders because they are assets, but the execution
checklist must require replacing or removing every unused placeholder in a
materialized project document.

## Contracts

### Selection Axes

Discovery resolves independent values:

```text
project_shape:
  documentation_primary | single_runtime | modular_runtime |
  multiple_runtime_surfaces

detected_repo_model:
  single_repo | split_src_repo | multi_repo_runtime | existing_other |
  no_git_found

git_topology_decision:
  keep_existing | propose_change | approved_change | n/a

target_repo_model:
  single_repo | split_src_repo | multi_repo_runtime | existing_other | n/a

documentation_scope:
  baseline | evidence_selected_areas

mutation:
  audit_only | update_existing | create_missing | reorganize

code_architecture_scope:
  none | assess_only | document_contract | propose_restructure |
  approved_restructure

runtime_docs:
  not_applicable | existing_sufficient | update_entrypoint |
  add_ownership_docs

retrieval_scope:
  none | deterministic_guidance | assess_advanced

backup:
  required | explicitly_declined | not_applicable
```

The agent derives these values from evidence. They are not a user questionnaire.
Non-applicable fields stay compact. `existing_other` requires a one-line
explanation and is preserved unless a change is explicitly approved.

### Approval Contract

Before mutation, report the applicable selection axes plus:

- exact planned changes;
- affected paths and backup scope;
- risks and unknowns;
- structured intent paths selected for validation;
- whether code or git restructuring is only assessed, proposed, or approved.

Supported validation intents are:

- `local_known_owner`;
- `unknown_owner`;
- `product`;
- `rationale`;
- `deployed_state`;
- `operations`;
- `documentation_lookup`.

No axis implies mutation authority for another axis.

### Runtime And Codebase Contract

For code-bearing projects, local runtime documentation is the contributor entry
path. The skill may propose an ownership-oriented modular structure but must
treat physical trees as examples.

`codebase-architecture.md` defines portable defaults:

- logical service boundaries do not imply separately deployed microservices;
- public contracts and independent tests justify modular ownership docs;
- domain ownership and behavioral role drive placement and decomposition;
- ordinary code aims below roughly 300 lines where cohesion permits;
- 300–500 lines triggers responsibility review;
- above 500 lines requires explicit decomposition review;
- above 800 lines expects an explicit cohesive exception or approved split;
- narrower type-specific ranges are advisory only;
- generated, declarative, migration, fixture, framework-aggregator, and other
  justified cohesive files may be exceptions;
- existing oversized files are reported, not rewritten during documentation
  bootstrap without approval.

Project `AGENTS.md` receives only the short mandatory rule. A project-local
runtime architecture document is created or updated only when the project needs
an adapted durable contract.

### Retrieval Contract

Deterministic retrieval is guidance, not required infrastructure. Search should
rank the correct owner/source in the top five candidate surfaces and open only
relevant slices.

`assess_advanced` authorizes analysis only. Creating manifests, caches, indexes,
embeddings, or vector infrastructure requires an explicit planned change and
mutation approval. Planning, generated, vendor, artifact, and superseded sources
must not rank as current runtime truth by default.

## Compatibility, Migration, Rollout, And Rollback

- Existing projects are never automatically migrated.
- Legacy `minimal`, `standard`, and `full` labels may be recognized for reporting
  but do not drive new behavior.
- Strong existing documents and clear nonstandard structures remain valid
  equivalents.
- Removed Codex references have their still-valid semantics migrated before
  deletion; no dangling internal links remain.
- Internal authoring may proceed in phases, but canonical-to-installed sync
  occurs only after the whole Codex package is coherent and valid.
- If validation fails, do not sync. The canonical git diff remains the recovery
  surface.
- If post-sync comparison fails, stop and report the mismatch rather than
  editing the installed mirror.

## Security And Trust Boundaries

Security depth is `quick` because the delta changes documentation and agent
workflow only. It introduces no production identity, payment, secret,
sensitive-data, tenant, or destructive-runtime boundary.

Existing protections remain:

- inspect before mutation;
- require explicit mutation and topology approval;
- scope and create the approved backup before mutation;
- preserve unrelated work;
- never record secrets or machine-local authentication state;
- keep canonical packages portable and free of personal paths.

## Verification Strategy

### Package Verification

- validate frontmatter and package naming with `quick_validate.py`;
- verify every referenced file exists and every obsolete inbound reference is
  removed;
- verify no personal project names, home paths, credentials, or external
  symlinks enter the package;
- run `git diff --check`;
- inspect that `SKILL.md`, references, templates, and checklists express the same
  axes, authority model, and approval boundary;
- validate the installed mirror and compare it with canonical source only after
  approved synchronization.

### Context-Economy Evaluation

Use fixtures representing:

- a documentation-primary project;
- a single runtime;
- a modular runtime;
- multiple runtime surfaces with repo ownership distinguished from shape.

Measure separately:

1. organizer execution cost: mandatory references and tokens loaded by project
   shape and action;
2. resulting project startup cost: mandatory project files and tokens loaded by
   validation intent.

Freeze current-skill baselines before evaluating the revision. For
`local_known_owner` and `unknown_owner`, target at least 60 percent reduction in
mandatory startup context, require correct owner/source accuracy to meet or
exceed baseline, and record wrong-authority sources opened before the correct
one.

Forward tests must receive the raw revised skill and fixture request without the
expected answer or prior diagnosis.

## External Inputs And Execution Prerequisites

No external accounts, secrets, services, or runtime dependencies are required.
Codex `skill-creator` validation tools and the local canonical/installed skill
paths remain prerequisites for final validation and synchronization.

## Vertical-Delivery Constraints

- Keep the canonical package coherent throughout the final delivered state.
- Do not sync a partial phase.
- Do not modify Kimi or Claude distributions in this rollout.
- Do not reorganize any user project as part of implementing the skill package.
- Do not add retrieval infrastructure or repository-specific examples.
- Preserve unrelated worktree changes.

## Open Technical Or Risk Decisions

No material technical or risk decisions remain open. Detailed file-by-file
delivery sequencing belongs to the delivery plan after this design is approved.
