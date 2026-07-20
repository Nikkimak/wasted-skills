---
title: Context-Efficient Project Documentation And Runtime Architecture V1
doc_type: feature_prd
status: approved
classification: large_feature
owner: project-docs-organizer
review_status: external_audits_incorporated
human_approval: approved
---

# Context-Efficient Project Documentation And Runtime Architecture V1

## Business Outcome

Projects organized by `project-docs-organizer` should let a human or coding
agent begin correct work with the smallest sufficient mandatory context.
Documentation should improve authority selection, ownership discovery, and safe
navigation without forcing every task to load the complete project memory.

The same skill must remain useful for documentation-primary projects, a single
runtime, a modular runtime with durable ownership zones, and projects with
multiple runtime surfaces. These projects should share authority and navigation
semantics without being forced into one physical folder tree or one source-code
architecture.

The primary principle is:

> Minimize mandatory context before correct work starts, without reducing
> source and owner accuracy.

## Users And Scenarios

Primary users are:

- maintainers organizing a new or existing project;
- coding agents entering an unfamiliar code-bearing repository;
- agents working in research, legal, knowledge, content, or other
  documentation-primary projects;
- engineers locating the runtime owner and test surface of a behavior;
- reviewers checking whether product intent, accepted rationale, deployed
  state, implementation, and evidence still agree.

Core scenarios are:

1. A known-owner local code change starts from short project instructions and
   the nearest runtime or ownership documentation, then reaches code and tests
   without reading the project queue or complete central wiki.
2. An unknown-owner investigation uses deterministic path, lexical, symbol, and
   ownership search to rank likely surfaces before opening detailed content.
3. A product question reaches the applicable product or feature contract rather
   than treating current code as intended product meaning.
4. A rationale question reaches the accepted decision and then verifies how the
   boundary is represented in current code or documents.
5. A deployed-state question uses runtime and deployment evidence rather than
   assuming that the working tree, an ADR, or a feature document is live.
6. An operational question reaches the applicable runbook without loading
   unrelated product and architecture material.
7. A documentation-primary project gets precise authority and search routing
   without an artificial `src/` tree or runtime documents.
8. A code-bearing project keeps contributor-critical ownership, contracts, and
   test guidance close to the runtime while central documentation remains
   concise.
9. A project with several durable ownership zones can organize them as
   understandable, testable services without turning every module into a
   separately deployed microservice.

## Current Behavior

The skill currently provides a strong project-memory model for queues, current
state, decisions, future work, runbooks, components, runtime-facing bridge
documentation, and git topology.

Its workflow still has four material problems:

- a universal canonical read sequence encourages agents to load documents that
  are irrelevant to the current intent;
- a large canonical playbook must be read completely before a structural
  recommendation, weakening progressive disclosure inside the skill itself;
- the source-of-truth model is primarily document-oriented and does not fully
  distinguish product intent, accepted rationale, working-tree implementation,
  deployed state, operations, plans, and evidence;
- code-bearing and documentation-primary projects are described through one
  broad structure, which can encourage unnecessary runtime documents or an
  overly literal physical tree.

The result can be high token use before useful work begins, over-trust in broad
current-state documents, duplicated implementation prose, and structural
ceremony that is not justified by the project.

## Desired Behavior

### Context Economy And Intent Routing

The skill replaces one universal read order with bounded read paths selected by
task intent. At minimum it distinguishes:

- local known-owner implementation work;
- unknown-owner investigation;
- product intent and desired outcomes;
- accepted rationale and architectural boundaries;
- current implementation behavior;
- deployed/runtime contour;
- operational procedures;
- active work and future plans;
- verification evidence;
- documentation-primary lookup.

For current implementation behavior, inspected code and executable tests are
the final authority. For deployed state, deployment and runtime evidence are
authoritative. Feature documents define intended outcomes and scope, while
accepted decisions define rationale and invariants. No one document class is a
global source of truth for every question.

Project `AGENTS.md` remains a short router and constraint surface. It does not
become a project encyclopedia. A concrete coding task does not automatically
require `WORKPLAN.md`, all current-state documents, or the complete decisions
index.

### Project Shape Selection

The skill selects one observed project shape only to route applicable
references and templates:

- `documentation_primary`: documents are the primary work surface; incidental
  scripts do not make the project runtime-first;
- `single_runtime`: one runtime entrypoint is sufficient for safe local work,
  and cross-zone contracts do not require a separate documentation model;
- `modular_runtime`: durable ownership zones have public boundaries,
  independent test surfaces, or protected internals that justify local
  ownership documentation;
- `multiple_runtime_surfaces`: more than one runtime work surface must be
  navigated or operated explicitly.

Project shape is not a maturity ladder and does not select git topology,
documentation volume, or permission to mutate code. The number of domains is
only a weak signal. The skill defaults to `documentation_primary` or
`single_runtime` unless project evidence justifies escalation.

`multiple_runtime_surfaces` is distinct from a multi-repository model: shape
answers how runtime work is divided, while repo model answers which git history
and deploy boundary own each path.

### Documentation Scope

Every project receives only a baseline authority and navigation contract.
Operations, decisions, future-work areas, runtime ownership documentation, and
other document classes are added only when project evidence requires them.

Legacy `minimal`, `standard`, and `full` terminology may be recognized for
compatibility or reporting, but it must not drive project shape, runtime
structure, or automatic document creation.

Documentation-primary projects must not receive artificial runtime directories
or templates. Code-bearing projects must keep contributor-critical runtime
knowledge close to the owning code without duplicating the central project
wiki.

### Runtime And Ownership Documentation

For an applicable code-bearing project, runtime documentation provides:

1. a concise runtime entrypoint and ownership map;
2. local ownership documentation only where a durable service or module boundary
   benefits from it;
3. public contract, dependency, failure, and test guidance that is not cheap to
   recover from file names and symbols alone;
4. links to applicable decisions, operations, and deployed-state evidence.

Physical layouts are examples, not mandatory templates. The skill must not
create empty service layers or invent folders such as `domain`, `application`,
`contract`, or `infrastructure` unless the real project already benefits from
those responsibility boundaries.

### Codebase Architecture Guidance

For code-bearing bootstrap, architecture audit, or approved major cleanup, the
skill provides optional portable guidance for organizing a modular codebase.
That guidance prefers durable domain ownership and testable service boundaries
without treating each ownership zone as a separately deployed microservice.

It establishes these semantics:

- a service is a logical ownership boundary, not automatically a process,
  repository, container, or deploy unit;
- one owner holds business correctness for each domain behavior;
- neighboring services use explicit public contracts rather than importing
  internal implementation details;
- transport and integration layers do not become hidden business owners;
- shared areas contain genuinely shared primitives rather than ownerless
  business logic;
- new code is placed by domain ownership and behavioral role;
- tests follow ownership boundaries and make local behavior independently
  verifiable;
- decomposition separates responsibilities rather than moving unrelated logic
  into generic helper files.

File-size guidance is a review heuristic, not a style-linter or automatic
failure. The skill may define portable default ranges and exception classes in
an optional architecture reference. Project `AGENTS.md` keeps only a short
rule, while an adapted project-local runtime contract records thresholds and
exceptions only when they are useful. Existing large files are reported as
debt; bootstrap does not force a rewrite without approval.

The organizer is not the daily architecture authority after bootstrap or
cleanup. The durable accepted contract belongs to the project through its
runtime entrypoint, local ownership documents, and accepted decisions.

### Retrieval

Normative V1 retrieval is deterministic-first:

- route by intent and authority class;
- use path, lexical, and symbol search;
- rank likely ownership surfaces before opening full content;
- open only the relevant slices, local documentation, code, and tests;
- exclude or downrank planning, generated output, artifacts, dependencies,
  vendor code, and superseded material for current-runtime questions.

V1 does not require a manifest, cache, embedding pipeline, vector database, or
index artifact. Advanced retrieval assessment is optional and does not itself
authorize creation of retrieval infrastructure. Any generated index or cache
must be separately included in approved planned changes.

## Scope

V1 updates the Codex-native `project-docs-organizer` contract to include:

- context economy as the primary optimization objective;
- authority by question type instead of one global truth hierarchy;
- intent-specific bounded read paths;
- independent project-shape, documentation-scope, repo-model, mutation, runtime
  documentation, code-architecture, retrieval, and backup decisions;
- an evidence-selected baseline rather than fixed documentation depth driving
  file creation;
- conditional runtime and local ownership documentation for code-bearing
  projects;
- conditional portable codebase-architecture and file-decomposition guidance;
- deterministic-first retrieval guidance with vector infrastructure deferred;
- progressive disclosure inside the skill through bounded reference routing;
- an approval contract that distinguishes inspection, project documentation,
  proposed restructuring, and approved mutation;
- validation of both skill execution context and resulting project startup
  context;
- aligned Codex workflow, references, templates, and checklists that express one
  coherent model before synchronization.

## Non-Goals

V1 does not:

- force one physical project, runtime, service, or test folder tree;
- require source code or a `src/` directory in documentation-primary projects;
- turn logical services into independently deployed microservices by default;
- prescribe one language, framework, parser, documentation generator, or test
  stack;
- require a code manifest, embeddings, vector database, MCP server, or search
  portal;
- make generated summaries or indexes a second source of truth;
- replace direct inspection of code, tests, runtime state, or deployment
  evidence;
- require every project to materialize every documentation level;
- make the organizer a daily architecture authority after the project owns its
  accepted runtime contract;
- automatically migrate or reorganize an existing project;
- force remediation of existing large files during documentation bootstrap;
- authorize code moves, git changes, or retrieval infrastructure merely because
  a project contains source code;
- publish a partially migrated Codex package whose workflow, references,
  templates, and checklists express different models;
- update Kimi or create a Claude-native distribution in the first rollout;
- author an implementation design or delivery task graph.

## Constraints And Accepted Assumptions

- The model must remain portable across project domains, languages, frameworks,
  repository layouts, and agent hosts.
- Human-readable information architecture comes before retrieval
  infrastructure.
- The smallest sufficient mandatory context is preferred over completeness of
  initial reading.
- Reduced token use must not reduce correct source or owner selection.
- Strong existing documentation and unconventional but clear project structures
  are preserved by default.
- Project shape is inferred from evidence and is not a user questionnaire or a
  persisted maturity score.
- Approval fields are produced by the agent after discovery; non-applicable
  fields remain compact rather than creating ceremony.
- Working tree, accepted ref, and deployed release may be different valid states
  for different questions.
- Planning and historical corpora must not rank as current implementation truth
  merely because they are semantically similar.
- Default file-size ranges are soft review triggers. Generated code,
  declarative schemas, migrations, fixtures, framework aggregators, and other
  justified cohesive files may be exceptions.
- Internal implementation may proceed in phases, but the installed mirror is
  synchronized only after the complete Codex package is internally consistent,
  validated, and ready as one coherent V1.
- Existing discovery, explicit mutation approval, scoped backup, and preservation
  of unrelated work remain mandatory.

## Acceptance Criteria

The feature is acceptable when:

1. A new user can determine which source class is authoritative for product,
   rationale, working implementation, deployed state, operations, planning, and
   evidence questions.
2. A known-owner local task reaches applicable local documentation, code, and
   tests without mandatory reading of the project queue and complete central
   documentation set.
3. For unknown-owner evaluation prompts, the correct owner or source appears in
   the top five ranked candidate surfaces without reducing accuracy relative to
   the current skill.
4. Mandatory startup files and tokens are measured by intent class. The target
   reduction for known-owner and unknown-owner paths is at least 60 percent
   against frozen current-skill baselines, subject to no regression in owner or
   source accuracy.
5. Evaluation records whether wrong-authority sources were opened before the
   correct source and demonstrates a reduction from baseline.
6. Skill execution context is measured separately from resulting project
   startup context, proving that split references are selectively loaded rather
   than all read automatically.
7. A documentation-primary fixture receives authority and navigation guidance
   without artificial runtime files.
8. A single-runtime fixture receives a concise runtime entrypoint without
   unnecessary ownership-document proliferation.
9. A modular-runtime fixture exposes durable ownership, public boundaries, and
   independent test surfaces without requiring microservice deployment.
10. A multiple-runtime-surfaces fixture distinguishes runtime shape from repo and
    deploy ownership.
11. Physical layout examples are not copied mechanically, and no empty
    architectural layers or ceremonial directories are created.
12. Runtime and ownership documentation remains close to owning code, central
    topology documents stay concise, and mutable implementation facts are not
    duplicated across both layers.
13. Code-architecture guidance is loaded only for applicable code-bearing audit,
    bootstrap, or cleanup requests and does not block documentation work on
    existing oversized files.
14. Retrieval defaults to deterministic guidance; advanced assessment creates
    no index, cache, manifest, or vector infrastructure without separate
    approval.
15. The approval contract distinguishes detected state, intended result, and
    mutation authority, including code-architecture and git-topology scope.
16. Existing projects are audited before change, strong equivalents are
    preserved, and no migration or restructuring occurs without explicit
    approval.
17. `SKILL.md`, all affected references, templates, and checklists express one
    consistent model before the canonical package is synchronized.
18. The Codex package validates, its installed mirror matches the canonical
    source after synchronization, and repository checks pass.

## Current Version / MVP

V1 is one coherent Codex-native revision. It delivers context economy,
intent-based authority routing, project-shape selection, conditional local
runtime documentation, conditional codebase-architecture guidance, a revised
approval contract, progressive skill reference routing, and deterministic-first
retrieval guidance.

V1 may be authored through internal phases, but it is not shipped as a
half-migrated package. The installed Codex mirror changes only after the full V1
contract and all affected bundled resources are consistent and validated.

## Architecture Horizon

The accepted V1 model must allow later additions such as:

- language- or framework-specific symbol and test adapters;
- generated ownership and dependency catalogs;
- documentation link, metadata, and drift validation;
- repository-state-aware local indexes;
- hybrid lexical and semantic retrieval;
- graph expansion from ownership areas to symbols, contracts, and tests;
- quantitative retrieval evaluation fixtures;
- a separate architecture-focused skill if real usage later demonstrates that
  bootstrap and major cleanup no longer provide a sufficient trigger boundary;
- native Kimi and Claude implementations that preserve accepted product
  semantics through host-native mechanics.

These capabilities must extend the project-owned authority and runtime model
rather than establish another documentation hierarchy.

## Deferred Candidate Work

- Concrete code-index manifests, schemas, caches, and interchange formats.
- Embedding or vector retrieval implementation.
- Stack-specific architecture and symbol adapters.
- CI enforcement for documentation coverage, drift, or file-size review.
- Automatic migration of projects organized under the earlier global read
  hierarchy.
- A separate daily codebase-architecture skill.
- Kimi-native semantic alignment after the Codex rollout.
- A future Claude-native distribution.

## Open Human Decisions

No unresolved product-scope decisions remain from discovery.

Before this PRD can be accepted, the human must decide whether to request an
optional cross-model PRD review and must explicitly approve the final proposed
PRD. Implementation details, file decomposition, and delivery sequencing belong
to the later implementation-design and delivery-planning stages.
