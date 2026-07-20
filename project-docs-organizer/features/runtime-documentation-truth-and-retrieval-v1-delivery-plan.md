---
title: Delivery Plan — Context-Efficient Project Documentation And Runtime Architecture V1
doc_type: delivery_plan
status: implemented
classification: large_feature
owner: project-docs-organizer
human_approval: approved
readiness: forward_validation_pending
validation_status: static_passed_forward_pending
---

# Delivery Plan: Context-Efficient Project Documentation And Runtime Architecture V1

## Parent Feature

Deliver one coherent Codex-native `project-docs-organizer` package bound to:

- `runtime-documentation-truth-and-retrieval-v1.md`;
- `runtime-documentation-truth-and-retrieval-v1-implementation.md`.

The parent accepts only a complete canonical package whose entrypoint,
references, templates, and checks express the same context-economy model.

## Slice 1: Canonical Reference Architecture

### Business Outcome

The skill can load only the guidance applicable to the observed project shape,
intent, and requested action.

### Scope

- create bounded canonical references for authority and intent routing, project
  shape and scope, documentation architecture, codebase architecture, and
  optional retrieval guidance;
- migrate still-valid semantics from the monolithic playbook and overlapping
  references;
- update direct reference routing;
- remove obsolete Codex references only after inbound links and unique
  semantics are resolved.

### Acceptance Criteria

- no concrete recommendation requires the complete former monolithic playbook;
- documentation-primary and code-bearing guidance are separable;
- codebase architecture is conditional;
- git topology remains an independent decision axis;
- no repository-specific names or paths enter the package.

### Validation Plan

- reference and link inventory;
- contradiction search;
- portability scan;
- manual semantic coverage against the accepted implementation design.

### Dependencies

None.

### Execution And Validation Profile

Local serial authoring; static contract validation.

### Merge Target

Canonical working tree only. No commit, push, or publication is in scope.

### Commitment

Committed.

## Slice 2: Entrypoint, Approval Contract, And Templates

### Business Outcome

Agents receive a short workflow, derive independent selection axes, and
materialize only evidence-supported project documents.

### Scope

- rewrite `SKILL.md` around intent, shape, conditional routing, approval,
  backup, execution, and reporting;
- revise the approval contract with detected versus target state and explicit
  code-architecture scope;
- make `AGENTS.md` a short router template;
- update context, current-state, repo, runbook, decisions, and runtime templates
  to avoid a global truth hierarchy;
- add a conditional service/ownership README template;
- update template policy and implementation checklist.

### Acceptance Criteria

- project shape never implies repo model, documentation volume, or mutation;
- no code-bearing shape authorizes restructuring;
- documentation-primary projects do not receive runtime files;
- physical code trees remain illustrative;
- materialized templates require no unused placeholders;
- file-size guidance is short in project `AGENTS.md` and detailed only in the
  conditional architecture reference or adapted project-local contract.

### Validation Plan

- approval-field consistency search;
- template placeholder and source-authority inspection;
- compare every routed reference with the entrypoint conditions.

### Dependencies

Slice 1.

### Execution And Validation Profile

Local serial authoring; static and scenario validation.

### Merge Target

Canonical working tree only.

### Commitment

Committed.

## Slice 3: Context-Economy And Package Acceptance

### Business Outcome

The revised skill demonstrates lower mandatory context without lower owner or
source accuracy.

### Scope

- freeze current mandatory-read baselines;
- exercise documentation-primary, single-runtime, modular-runtime, and
  multiple-runtime-surfaces scenarios;
- inspect organizer reference loading and resulting project startup paths;
- run package, link, portability, and whitespace validation;
- correct any contradiction across the final package.

### Acceptance Criteria

- known-owner and unknown-owner scenarios target at least 60 percent lower
  mandatory startup context;
- correct owner/source remains at or above baseline and appears in the top five
  candidate surfaces for unknown-owner scenarios;
- irrelevant authority classes are opened less often;
- split references are not all mandatory;
- canonical validation and `git diff --check` pass.

### Validation Plan

- representative scenario matrix;
- token/line proxy comparison for mandatory reads;
- `quick_validate.py`;
- internal reference existence checks;
- personal-path and symlink scan;
- final diff review.

### Dependencies

Slice 2.

### Execution And Validation Profile

Local serial validation with temporary fixtures only; full parent acceptance.

### Merge Target

Canonical working tree only.

### Commitment

Committed.

## Slice 4: Installed Mirror Synchronization

### Business Outcome

Codex runs the exact validated canonical package.

### Scope

- synchronize `project-docs-organizer/Codex/` to the installed Codex mirror only
  after Slice 3 passes;
- validate the mirror;
- compare mirror and canonical source.

### Acceptance Criteria

- no partial package is synchronized;
- installed validation passes;
- recursive comparison reports no difference;
- Kimi and Claude distributions remain unchanged.

### Validation Plan

- canonical validation immediately before sync;
- installed validation after sync;
- recursive canonical/mirror comparison.

### Dependencies

Slice 3.

### Execution And Validation Profile

Local serial synchronization and exact comparison.

### Merge Target

Installed runtime mirror; no git publication.

### Commitment

Committed.

## Coverage And Readiness

The canonical implementation is coherent and statically validated. Full PRD
acceptance remains pending Slice 3 independent forward tests, including all four
project shapes, source/owner accuracy, and context-economy measurements.

Deferred work remains limited to advanced indexes, vector retrieval, automatic
migrations, stack-specific adapters, Kimi alignment, and a future Claude-native
distribution.

## Implementation Results

Slices 1 and 2 and the static portion of Slice 3 are complete. The installed
mirror was synchronized for local preview and matches canonical, but final
Slice 3 and Slice 4 acceptance remain pending the required forward tests.

Mandatory skill-context line measurements against the frozen previous package:

| Scenario | Previous baseline | Revised path | Reduction |
| --- | ---: | ---: | ---: |
| Discovery only | 1956 | 262 | 86.6% |
| Documentation recommendation | 1956 | 406 | 79.2% |
| Code-architecture audit | 1956 | 407 | 79.2% |
| Git-topology recommendation | 1956 | 349 | 82.2% |
| Advanced retrieval assessment | 1956 | 337 | 82.8% |
| Documentation execution | 2026 | 515 | 74.6% |
| Code-architecture execution | 2026 | 516 | 74.5% |

The generated project-startup proxy reduced mandatory files for a known-owner
path from six old template-owned files before the required `WORKPLAN.md` to two
local entry files, a 66.7% file-count reduction. Its word-count proxy reached
59.6% before counting the old required `WORKPLAN.md`; any nontrivial queue pushes
the frozen old baseline beyond the 60% target.

Static scenario assertions verified documentation-primary exclusion of runtime
ceremony, independent code-restructure authority, deterministic retrieval by
default, conditional ownership templates, logical-service rather than
microservice guidance, and code/test authority for implementation behavior.

Canonical and installed `quick_validate.py` checks passed, YAML/frontmatter
parsed, internal reference inventory was exact, portability and external-symlink
scans were clean, `git diff --check` passed, and the installed Codex mirror
matched the canonical package after synchronization.

Independent raw-fixture forward tests for `documentation_primary`,
`single_runtime`, `modular_runtime`, and `multiple_runtime_surfaces` remain
pending. Until all four pass without an owner/source-accuracy regression,
validation status remains `static_passed_forward_pending`.
