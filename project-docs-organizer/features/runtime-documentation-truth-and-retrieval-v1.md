---
title: Runtime Documentation Truth And Retrieval V1
doc_type: feature_prd
status: proposed
classification: large_feature
owner: project-docs-organizer
review_status: not_started
human_approval: pending
---

# Runtime Documentation Truth And Retrieval V1

## Business Outcome

Projects organized by `project-docs-organizer` should let a human or coding
agent find the correct source for a question without mistaking product intent,
historical decisions, or planning material for current runtime behavior.

The skill should establish a simple documentation model that remains useful as
a codebase grows, keeps implementation knowledge close to its owning runtime
surface, and can later support precise code and documentation retrieval without
turning the project wiki into a duplicate of the codebase.

## Users And Scenarios

Primary users are:

- project maintainers defining documentation and source-of-truth boundaries;
- coding agents entering an unfamiliar repository;
- engineers locating the runtime owner of a behavior before changing it;
- reviewers checking whether code, contracts, and documentation still agree.

Core scenarios are:

1. A user asks how a service or runtime flow currently works. The agent reaches
   the owning runtime documentation, code, and tests before consulting feature
   or decision history as behavioral truth.
2. A user asks why an architectural boundary exists. The agent reaches the
   accepted decision and then verifies how the boundary is represented in code.
3. A user asks what is deployed. The agent uses deployment/runtime evidence
   rather than assuming that the working tree, a feature document, or an ADR is
   the live contour.
4. A project grows beyond a single high-level runtime map. The documentation can
   zoom from project topology into ownership areas, selected runtime scenarios,
   module contracts, code, and tests without duplicating the same mutable facts.
5. A project later adds code-aware retrieval. Search preserves source class,
   authority, repository state, and ownership instead of blending all documents
   into one undifferentiated semantic corpus.

## Current Behavior

The skill currently provides a strong project-memory model for queues, current
project state, decisions, future work, runbooks, components, and runtime-facing
bridge documentation.

Its source-of-truth hierarchy is primarily document-oriented. It does not yet
define a complete authority model for questions about current implementation
behavior, an intent-specific startup path, a vertical runtime documentation
hierarchy, or a repository-state-aware retrieval contract.

As a result, a project can follow the documented folder structure while an agent
still over-trusts high-level current-state, feature, or decision documents and
stops before inspecting the owning runtime surface.

## Desired Behavior

The skill defines authority by question type rather than one global ordering of
all sources.

At minimum, it distinguishes:

- product intent and desired outcomes;
- accepted rationale and architectural boundaries;
- current implementation behavior;
- deployed/runtime contour;
- operational procedures;
- active work and future plans;
- verification evidence.

For current implementation behavior, code and executable tests are the final
authority. Runtime-owned documentation provides the shortest safe navigation
path into that code and describes relationships, ownership, contracts, and
failure semantics that are not obvious from isolated files.

Feature documents remain the authority for intended product outcomes and scope,
not proof of implemented behavior. Decision records explain why a rule or
boundary was accepted, not every detail of its current implementation.

The skill also defines a vertical runtime documentation model that can zoom
through these levels when they add value:

1. runtime entrypoint and ownership index;
2. ownership-area or service documentation close to the code;
3. selected architecturally significant runtime scenarios;
4. module or public API contracts;
5. implementation and tests.

Projects should create only the levels justified by their size and complexity.

## Scope

V1 covers the product semantics and reusable guidance of
`project-docs-organizer`:

- an authority matrix based on question type;
- intent-based read paths for implementation, product, rationale, operations,
  and deployment questions;
- a minimal vertical runtime documentation model;
- rules for separating project truth, implementation truth, deployed truth,
  future intent, and evidence;
- rules for keeping runtime documentation close to its owning code without
  duplicating a project wiki;
- guidance for selected runtime scenarios and ownership-area documentation;
- maintenance and review principles that detect documentation drift without
  requiring meaningless documentation churn for every code edit;
- a tool-neutral retrieval model covering deterministic search,
  structural/symbol navigation, selective semantic retrieval, graph expansion,
  metadata, and repository-state awareness, with its normative versus optional
  placement to be resolved before approval;
- aligned updates to the skill workflow, canonical playbook, mode-selection
  guidance, documentation matrix, templates, and validation checklist where the
  accepted model requires them.

The feature is defined at the logical skill level. Platform-specific Codex and
Claude implementations may use different host mechanics while preserving the
same accepted product semantics. A Kimi-native distribution remains separately
scoped and is not part of this paired V1 rollout.

## Non-Goals

V1 does not:

- reorganize or migrate any particular user project;
- encode names, paths, services, or examples from a private project;
- prescribe one programming language, framework, documentation generator,
  parser, vector database, embedding model, or retrieval vendor;
- build a code index, vector service, MCP server, or documentation portal;
- require full-repository vectorization;
- make generated summaries a second source of runtime truth;
- replace direct code inspection, tests, or deployment verification;
- require every project to adopt every documentation level;
- author an implementation design or delivery task graph;
- require a coordinated Kimi implementation or mechanical parity with the
  Codex and Claude host workflows.

## Constraints And Accepted Assumptions

- The model must remain portable across languages, frameworks, repository
  layouts, and agent hosts.
- The smallest sufficient documentation structure remains the default.
- Human-readable information architecture comes before retrieval optimization.
- Runtime documentation should explain ownership and behavior that cannot be
  recovered cheaply from file names, public contracts, and tests.
- Generated inventories may describe verifiable structure, but generated prose
  must not silently become canonical truth.
- Retrieval must preserve source class and repository state. Working tree,
  accepted branch, and deployed release may represent different valid truths for
  different questions.
- Planning and historical corpora must not rank as current implementation truth
  merely because they are semantically similar to a query.
- The existing discovery and explicit approval boundary of
  `project-docs-organizer` remains in force for changes to a target project.

## Acceptance Criteria

The feature is acceptable when:

1. A new skill user can determine which source is authoritative for product,
   rationale, implementation, deployment, operations, planning, and evidence
   questions.
2. The skill no longer implies that one manually maintained current-state
   document can override inspected code for current implementation behavior.
3. The skill provides distinct, bounded read paths for common question types
   instead of requiring the same full canonical read sequence for every task.
4. The runtime documentation model identifies a concise entrypoint, local
   ownership documentation, selected scenarios, module contracts, code, and
   tests while making each level optional when it adds no value.
5. Feature documents and ADRs retain clear roles without being treated as live
   implementation descriptions.
6. Current project/runtime topology documents stay concise and link into local
   runtime truth instead of accumulating detailed feature implementation logs.
7. Maintenance guidance distinguishes meaningful documentation-impact changes
   from ordinary internal code edits and defines a reviewable drift signal.
8. Retrieval guidance separates lexical/symbol search from semantic
   retrieval, supports selective rather than complete vectorization, and carries
   authority, ownership, path, symbol, content hash, and repository-state
   metadata.
9. Retrieval guidance excludes or downranks planning, artifacts, superseded
   decisions, generated output, dependencies, and vendor code for current-runtime
   questions unless the query explicitly requests those sources.
10. All examples and templates are generic and portable, with no dependency on a
    particular private repository or workstation path.
11. The skill's workflow and all affected references/templates/checklists express
    one consistent model with no contradictory source-of-truth rules.
12. Validation can demonstrate the model against more than one language or
    runtime shape without adding stack-specific requirements to the base skill.

## Current Version / MVP

V1 is the smallest coherent revision of the skill's documentation architecture.
It defines the authority model, intent routing, vertical runtime documentation,
maintenance contract, and tool-neutral retrieval principles, then aligns the
existing skill resources with those semantics.

V1 does not implement a retrieval engine. It must leave a project with a
structure that works through ordinary file navigation and deterministic search
before optional indexing is introduced.

## Architecture Horizon

The accepted V1 model must not block later additions such as:

- language-specific documentation and symbol adapters;
- generated ownership and dependency catalogs;
- documentation coverage and link validation;
- repository-state-aware local indexes;
- hybrid lexical and semantic retrieval;
- graph-based expansion from ownership areas to symbols and tests;
- retrieval evaluation suites with expected source and symbol results;
- native Codex and Claude implementations with equivalent product semantics.

These capabilities should extend the base model rather than require another
project documentation hierarchy.

## Deferred Candidate Work

- A concrete code-index manifest and interchange schema.
- Stack adapters for common language ecosystems.
- CI integrations for documentation coverage, drift, and generated catalog
  verification.
- A reference local retrieval implementation.
- Migration guidance for projects already using the earlier global truth
  hierarchy.
- Quantitative retrieval evaluation guidance and benchmark fixtures.
- A Claude-native `project-docs-organizer` distribution.

## Open Human Decisions

1. Should V1 define one preferred physical location for ownership-area documents,
   or specify only required semantics and let each runtime choose colocated versus
   centralized paths?
2. Should tool-neutral retrieval guidance be normative V1 behavior or an optional
   advanced appendix layered on top of the documentation model?
3. What minimum drift enforcement belongs in every mode, and what should remain a
   recommendation for larger projects?
4. Should the existing `minimal`, `standard`, and `full` modes gain a separate
   runtime-documentation dimension, or should runtime depth remain part of each
   existing mode definition?
5. Should the first implementation update only the Codex distribution, or should
   shared semantics be approved before native Codex and Claude implementations
   are scheduled separately?
6. What backward-compatibility and migration promises should the skill make for
   projects previously organized under the current playbook?
