# LLM-Friendly Project Playbook

## Purpose

This document describes a reusable project structure optimized for:

- LLM-assisted coding
- low ambiguity around source of truth
- safe collaboration between humans and coding agents
- clean separation between deployable code and project memory
- project documentation that stays useful as the system grows

This is a general blueprint, not a project-specific note.
It should work for backend systems, web apps, mobile projects, automation-heavy systems, and mixed-language products.

## Stateless Session Rule

LLMs do not carry reliable project memory across sessions.
Every new session must be able to recover correct context from the workspace itself.

That means this blueprint is not only about storing information.
It is about making the right startup path obvious and cheap.

Non-negotiable rule:

- a new LLM session should be able to determine what to do, what is live, what is accepted, and where to edit with a short deterministic read path

If that cannot happen in a few minutes without human retelling, the workspace is not structured well enough.

## First Principle

The most important structural decision is:

- keep project memory and deployable code in separate git repositories

Recommended model:

1. parent workspace repo
2. `src/` runtime/code repo

Git topology rule:

- the parent workspace and `src/` are independent git repositories
- `src/` may live physically inside the parent workspace for convenience, but it must keep its own `.git`
- if `src/` is nested, the parent repo should ignore that path instead of accidentally versioning runtime code
- the parent repo must never become the deploy source for the runtime repo
- if the runtime layer later contains multiple independently deployable subprojects, those may also become separate git repos

Physical layout note:

- nested repos are acceptable and often convenient
- sibling repos may behave more predictably with some tooling
- choose the physical layout consciously; the real rule is split git ownership, not one mandatory folder arrangement

Why this matters:

- plans, rationale, and evidence do not pollute deployable code
- production pushes are easier to reason about
- agents are less likely to edit the wrong layer
- context loading becomes cheaper
- documentation can remain high-signal without turning the runtime repo into a notebook

## Playbook Application Rule

If a user says to apply this playbook to a project, the expected default meaning is:

- create or verify the parent project workspace repo
- create or verify the separate runtime repo in `src/` or the equivalent runtime path
- ensure the two git histories are independent
- ensure the parent repo ignores the nested runtime repo path when needed
- create or verify the canonical documentation and bootstrap files described by this playbook

In other words:

- "apply the playbook" means materialize the structure, not merely describe it
- the git topology is part of the playbook outcome, not an optional follow-up idea

Practical rule for coding agents:

- if the required parent repo or runtime repo does not exist yet, creating them is part of completing the playbook setup
- if both repos already exist, verify their boundaries instead of recreating them
- if nested git boundaries are broken or ambiguous, fix that before treating the playbook as applied

Minimum expected result after playbook application:

- a project workspace repo exists for project memory and control-plane docs
- a separate runtime repo exists for deployable code
- the parent repo does not accidentally version runtime files from the nested repo
- canonical docs and bootstrap files exist in the correct layer

## Parent Workspace Model

Think of the parent workspace repo as a control plane for the project.

It contains four different documentation layers:

- `knowledge/` = reusable library of blueprints, references, source material, vendor notes, and research
- `context/` = compiled project wiki for the current project
- bootstrap files such as `AGENTS.md` and `CLAUDE.md` = schema for how agents should read, update, and connect the workspace
- an optional task layer such as `task-management/` = execution support material, task packets, and handoff bundles

These layers must not be mixed casually.

Rule of thumb:

- if a document is reusable outside this project, it belongs in `knowledge/`
- if a document explains the current or planned state of this specific project, it belongs in `context/`
- if a document explains how an agent should behave in this workspace, it belongs in a bootstrap file
- if a document is task-local execution support rather than canonical project truth, it belongs in the task layer

## Architecture Quality Rules

Project structure is not enough on its own.
A repo is LLM-friendly only if ownership boundaries are explicit and enforced.

### 1. One owner of business correctness

For every critical domain, exactly one runtime service must own:

- state transitions
- validation and invariants
- idempotency
- source-of-truth writes

Do not split correctness across API, workflow tools, agents, workers, or UI.

### 2. Adapters are not second backends

Channel layers, MCP servers, workers, and automation tools may:

- normalize transport-specific input
- enforce channel-specific auth
- call explicit contracts
- orchestrate approved flows

They must not:

- invent hidden business rules
- reinterpret canonical domain states
- become a parallel mutation surface around the owner service

### 3. Source of truth must be singular

A project may have many projections, caches, CRMs, and operator tools.
It should still have one canonical transactional source of truth for each core domain.

Typical model:

- primary database = transactional truth
- CRM / Airtable / search index = projection or operator context
- workflows / queues = delivery and orchestration, not truth

### 4. Human docs and runtime code need the same boundary model

The doc structure and the code structure should reinforce the same ownership model.
If docs say one service owns correctness but the file layout encourages changes in three places, the structure is still poor.

### 5. Future design must not masquerade as live reality

Projects often contain:

- ideas
- target architecture
- accepted decisions
- implementation plans
- partially deployed work
- current live runtime

These must not be collapsed into one document class.
Agents must be able to distinguish "planned", "accepted", "in progress", and "live now" without guessing.

### 6. Secrets and runtime-mutated config stay outside git

Keep a hard distinction between:

- versioned non-secret config and templates
- secrets
- runtime-mutated operational config

Do not let a blueprint blur these layers.

## Canonical Workspace Layout

This layout describes a project workspace root.
If you also have a larger multi-project container above it, that higher-level root may be much thinner and act mainly as a routing layer into individual projects.
The layout below shows `context/features/` as the default example for future-work docs.
Projects may instead choose another canonical future-work area such as `context/implementation-plans/`.

```text
project-root/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── WORKPLAN.md
├── task-management/         # optional task packets / execution state, not canonical wiki truth
├── context/
│   ├── README.md
│   ├── current/
│   │   ├── project-state.md
│   │   ├── runtime-map.md
│   │   └── repo-map.md
│   ├── decisions/
│   │   ├── README.md
│   │   └── YYYY-MM-DD-topic.md
│   ├── features/
│   │   ├── README.md
│   │   └── FEATURE-001-example/
│   │       ├── status.md
│   │       ├── vision.md
│   │       ├── domain-design.md
│   │       ├── implementation-plan.md
│   │       └── migration-plan.md
│   ├── runbooks/
│   │   ├── README.md
│   │   ├── deploy.md
│   │   ├── rollback.md
│   │   └── smoke-tests.md
│   ├── components/
│   │   ├── README.md
│   │   ├── api.md
│   │   ├── gateway.md
│   │   ├── worker.md
│   │   └── frontend.md
│   ├── domains/
│   │   ├── README.md
│   │   ├── billing.md
│   │   ├── crm.md
│   │   └── auth.md
│   └── glossary.md
├── knowledge/
│   ├── README.md
│   ├── blueprints/
│   ├── references/
│   ├── vendors/
│   └── research/
├── artifacts/
│   ├── deploy-evidence/
│   ├── reviews/
│   ├── incidents/
│   └── experiments/
├── templates/
│   ├── decision-template.md
│   ├── feature-status-template.md
│   ├── runbook-template.md
│   ├── component-guide-template.md
│   └── workplan-template.md
└── src/
    ├── README.md
    ├── docs/                # optional runtime-facing contributor docs
    │   ├── local-dev.md
    │   ├── testing.md
    │   ├── deploy-surface.md
    │   ├── runtime-config.md
    │   └── boundaries.md
    ├── .github/
    │   └── workflows/
    ├── services/
    ├── packages/
    ├── workers/
    ├── infra/
    ├── scripts/
    └── ...
```

The exact names can vary.
The important part is role separation, not folder spelling.

## Repository Roles

### Parent Workspace Repo

Use this repo for:

- current queue and execution priorities
- project-level architecture decisions
- current project wiki
- feature design and rollout planning
- runbooks
- component boundaries
- domain notes
- deployment evidence
- bootstrap instructions for coding agents

Do not use this repo for:

- deploy-triggering code
- runtime secrets
- generated bundles
- service build artifacts
- migrations that belong to the runtime repo
- long-lived code branches pretending to be documentation

### `src/` Runtime Repo

Use this repo for:

- production code
- non-secret runtime configuration under version control
- migrations
- CI workflows
- infra or deploy code that is versioned with the runtime
- service-level READMEs
- runtime-facing contributor docs
- service tests

Do not use this repo as the canonical home for:

- execution history
- architecture rationale
- long-form planning
- mutable operational notes
- secrets
- runtime-only env files edited directly on servers or deploy targets

### Runtime-Owned Docs Rule

The runtime repo must not be silent.

At minimum, a contributor opening only `src/` should be able to:

1. understand what services or apps exist
2. run the relevant build, test, or local-dev path
3. identify where a narrow behavior change belongs
4. avoid violating obvious runtime boundaries

That does not mean the runtime repo should duplicate the full parent workspace wiki.
It means contributor-critical runtime knowledge must remain locally available in `src/`.

Required minimum runtime-owned docs:

- `src/README.md`
- service-level `README.md` files where ownership would otherwise be unclear
- local run/build/test guidance
- deploy surface summary for this repo
- runtime config shape or examples for versioned non-secret config

Recommended pattern for larger repos:

- keep concise runtime-facing docs in `src/docs/`
- keep them operational and contributor-oriented, not as a second architecture wiki

### Bridge Docs Rule

Some runtime docs necessarily summarize truths that are maintained canonically in the parent workspace.

These bridge docs are allowed inside `src/` when they are:

- short
- runtime-facing
- explicitly derivative of canonical parent docs
- limited to the local assumptions a contributor needs in this repo

Good examples:

- boundary summaries
- deploy entrypoint summaries
- runtime assumptions and config shape summaries

Bad examples:

- full copies of decision docs
- duplicated rollout logs
- a second mutable source of architecture truth

### Runtime Self-Sufficiency Threshold

If an engineer opens only `src/`, they should be able to make a narrow local change safely without mandatory reading in the parent repo, unless the task crosses architectural, rollout, or cross-service boundaries.

If that threshold is not met, the runtime repo is under-documented.

### Runtime Structure Contract

Runtime structure needs explicit enforcement too.
The exact folder names may vary, but the ownership model must not be ambiguous.

Each runtime repo should make these responsibility classes easy to locate:

- transport or interface entrypoints
- application or service orchestration
- domain logic and state transitions
- persistence or data access
- provider or external integration adapters
- tests

Not every project needs each class as a top-level folder.
The rule is that these concerns must not collapse into one ambiguous mutable blob.

Runtime enforcement rules:

- exactly one runtime owner of business correctness per domain
- transport layers do not own domain state transitions
- persistence layers do not own business decisions
- integration layers do not become hidden domain owners
- runtime-facing docs stay short and local; canonical architecture truth stays in the parent workspace docs

## Git Model

Repository boundary:

- the parent workspace repo and the `src/` repo are separate git histories
- this is true even if `src/` is physically nested under the parent workspace directory
- do not treat `src/` as a normal folder owned by the parent repo

### Parent Repo

Recommended mode:

- project-memory repo
- may be local/private or hosted, depending on project sensitivity
- versioned independently from runtime code
- if `src/` is nested, ignore it from the parent repo instead of tracking runtime files here

### `src/` Repo

Recommended mode:

- canonical repo for deployable runtime code
- owns its own commit history, branches, CI, and deploy-triggering changes
- only runtime repos should trigger production deploys

Rule:

- production code is committed and pushed only from runtime repos
- project memory may be versioned, but should not become the deploy source by accident
- do not mirror runtime commits into the parent repo just because the directories are colocated

## Documentation Information Architecture

The documentation model should be explicit.

### 1. Working Plan

File:

- `WORKPLAN.md`

Purpose:

- what is next
- what is blocked
- what phase is active

Rule:

- queue-first, not architecture truth and not runtime truth
- `WORKPLAN.md` stays the single canonical queue summary even if additional task tooling exists

### 1a. Optional Task Layer

Files:

- `task-management/*`
- `taskplane-tasks/*`
- or an equivalent dedicated task directory outside `context/`

Purpose:

- task packets
- delivery-local execution state
- checklists
- agent handoff material

Rule:

- task material is execution support, not canonical project wiki truth
- do not hide accepted architecture or live runtime facts only inside task packets
- if this layer exists, keep it outside `context/` to avoid mixing queue/execution state with project truth

### 1b. Context Index

File:

- `context/README.md`

Purpose:

- short index for the project wiki
- source-of-truth summary for the `context/` layer
- pointer to current-state docs, decision docs, runbooks, and the chosen future-work area

Rule:

- this file is the canonical entrypoint into `context/`
- it should stay short and navigational
- it should not become a second copy of the current-state docs or decision docs

### 2. Current Project Wiki

Files:

- `context/current/project-state.md`
- `context/current/runtime-map.md`
- `context/current/repo-map.md`

Purpose:

- `project-state.md` = short snapshot of the project as a whole
- `runtime-map.md` = live runtime topology, services, environments, deploy contour, current integrations
- `repo-map.md` = codebase and git topology, ownership of repos, where to change what

Rule:

- this layer describes what is currently real
- it must stay concise and maintainable
- do not turn one file into a giant mutable encyclopedia

### 3. Accepted Decisions

Files:

- `context/decisions/*.md`
- indexed by `context/decisions/README.md`

Purpose:

- architecture decisions
- invariants
- important implementation decisions that have been accepted

Rule:

- normative
- accepted decisions are more authoritative than feature design docs
- decision indexes should stay short; the real content belongs in the decision files

### 4. Feature Lifecycle Docs

Files:

- `context/features/FEATURE-*/status.md`
- `context/features/FEATURE-*/vision.md`
- `context/features/FEATURE-*/domain-design.md`
- `context/features/FEATURE-*/implementation-plan.md`
- `context/features/FEATURE-*/migration-plan.md`

Purpose:

- organize future work by feature or initiative
- preserve the path from idea to architecture to implementation
- separate target design from live runtime facts

Rule:

- use feature dossiers for large, multi-step, architecturally meaningful changes
- smaller accepted changes may be represented by `WORKPLAN.md` + `context/decisions/` + code changes without a dedicated feature tree
- not every bugfix, refactor, or narrow enhancement needs `context/features/FEATURE-*`
- feature docs are not automatically source of truth for live behavior
- if a design becomes accepted, capture the normative parts in a decision doc
- if a rollout becomes live, update `context/current/`

Canonical-home rule:

- each project should choose one canonical home for future and in-progress design work
- acceptable choices include `context/features/` or an explicitly chosen equivalent such as `context/implementation-plans/`
- do not split the same class of future-work docs casually across both

### 4a. Accepted Decisions Versus Implementation Plans

Keep normative rules separate from execution planning.

`context/decisions/` is for:

- accepted boundaries
- invariants
- normative ownership rules

Implementation plans belong in:

- `context/features/*/implementation-plan.md`
- or a dedicated `context/implementation-plans/` area if the project chooses that model

Rule:

- a decision file must not quietly become a delivery log
- an implementation plan must not pretend to be accepted architecture
- if the project uses a separate implementation-plans directory, it is still subordinate to accepted decisions and current-state docs

### 5. Runbooks

Files:

- `context/runbooks/*.md`

Purpose:

- deploy
- rollback
- smoke tests
- diagnostics
- operations

Rule:

- procedural, not architectural

### 6. Component Guides

Files:

- `context/components/*.md`

Purpose:

- ownership
- code placement
- non-negotiable boundaries
- what each service may and may not own

Rule:

- short, practical, and easy for agents to parse

### 7. Domain Notes

Files:

- `context/domains/*.md`

Purpose:

- provider notes
- domain vocabulary
- external API notes
- stable domain context useful for implementation

Rule:

- helpful context, but not authoritative over accepted decisions or live runtime facts
- if a business rule becomes mandatory, move it into an accepted decision

### 8. Reusable Knowledge Library

Files:

- `knowledge/blueprints/*`
- `knowledge/references/*`
- `knowledge/vendors/*`
- `knowledge/research/*`

Purpose:

- reusable material not tied to one project's current state
- source material that informs implementation but is not the project wiki

Rule:

- `knowledge/` should not quietly become another `context/`
- if a note becomes project-canonical, move or summarize it into `context/`

## Document Metadata Model

Canonical project docs should carry explicit metadata.
This can be YAML frontmatter or another structured header, but the semantics should be consistent.

Operational rule:

- for `context/README.md`, `context/current/*`, `context/decisions/*`, the project's chosen future-work area, `context/runbooks/*`, and `context/components/*`, metadata should be treated as required, not optional
- `knowledge/*` may use lighter metadata if needed, because it is reference material rather than live project truth
- bootstrap files such as `AGENTS.md`, queue summaries such as `WORKPLAN.md`, and runtime bridge docs such as `src/README.md` may use lighter metadata unless the project explicitly standardizes them
- if metadata is declared required, the project should ideally validate it with automation or review checklists
- do not impose heavyweight frontmatter that the team will not maintain

Required minimum fields for canonical project docs:

- `title`
- `doc_type`
- `status`
- `source_of_truth`
- `owner`
- `last_updated`
- `related`
- `supersedes`
- `superseded_by`

Example:

```yaml
---
title: Itemized Orders Vision
doc_type: vision
status: proposed
source_of_truth: false
owner: orders-domain
last_updated: 2026-04-13
related:
  - context/current/project-state.md
  - context/decisions/2026-04-13-orders-boundary.md
supersedes: null
superseded_by: null
---
```

Recommended `doc_type` values:

- `workplan`
- `context_index`
- `project_state`
- `runtime_map`
- `repo_map`
- `decision`
- `decision_index`
- `feature_status`
- `vision`
- `domain_design`
- `implementation_plan`
- `migration_plan`
- `runbook`
- `component_guide`
- `domain_note`
- `knowledge_reference`

Recommended `status` values:

- `draft`
- `proposed`
- `approved`
- `in_progress`
- `implemented`
- `superseded`
- `archived`

Interpretation rule:

- `source_of_truth: true` should be rare
- future-oriented docs such as `vision`, `domain_design`, `implementation_plan`, and `migration_plan` should usually be `source_of_truth: false`
- accepted decisions and current-state docs may be source-of-truth documents if they are actively maintained

Pragmatic rule:

- if there is no metadata lint or other enforcement, prefer a lighter metadata subset over decorative noise
- metadata is useful only if it helps humans and agents distinguish authority, status, and recency correctly

## Source-Of-Truth Rules

These rules are more important than the exact folder structure.

- queue lives in exactly one place: `WORKPLAN.md`
- optional task directories may exist, but they do not replace `WORKPLAN.md` as the canonical queue summary
- current project truth lives in exactly one place: `context/current/`
- accepted architecture lives in exactly one place: `context/decisions/`
- future and in-progress design work live in exactly one canonical home per project: `context/features/` or one explicitly chosen equivalent
- procedures live in exactly one place: `context/runbooks/`
- service ownership guides live in exactly one place: `context/components/`
- reusable reference material lives in exactly one place: `knowledge/`
- other documents should link to canonical sources instead of re-explaining mutable facts

Truth hierarchy:

1. bootstrap files define how to navigate the workspace
2. `context/current/` defines what is currently real
3. `context/decisions/` defines accepted rules and boundaries
4. the project's chosen future-work area defines future or in-progress change work
5. `knowledge/` informs work, but is not project truth by default

Conflict rule:

- if a future-oriented design doc conflicts with `context/current/`, current reality wins
- if a future-work doc conflicts with an accepted decision, the accepted decision wins unless superseded explicitly

## Bootstrap Files For Agents

Bootstrap files may exist at both workspace root and project root.

Common bootstrap file names:

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`

In a single-project repo, the root bootstrap may also be the main project bootstrap.
In a multi-project workspace, the root bootstrap should usually be routing-only.

Avoid putting full runtime snapshots into bootstrap files.
They should point to canonical docs, not duplicate them.

### Root Versus Project-Level `AGENTS.md`

In a multi-project workspace, do not force one detailed `AGENTS.md` onto every project.

Recommended hierarchy:

- workspace root `AGENTS.md` = routing layer only
- project-level `AGENTS.md` = canonical operating manual for that specific project

Root `AGENTS.md` should usually contain only:

- that the repo is a multi-project workspace
- that the agent must identify the target project first
- that the nearest local `AGENTS.md` is authoritative for project work
- a few safe global defaults that do not assume one shared documentation model

Project-level `AGENTS.md` should contain the actual workflow for that project:

- canonical read order
- documentation model for that project
- source-of-truth rules
- runtime repo boundaries
- deploy and verification guidance at a high level
- project-specific non-negotiable constraints

Required minimum content for a project-level bootstrap:

- what this project is
- which repo is deployable runtime and which repo is project memory, if split
- canonical read order for a fresh session
- source-of-truth rules for this project
- where runtime code lives
- what runtime-owned docs must remain in `src/`
- where current-state docs live
- where accepted decisions live
- how deploy works at a high level
- what must be updated after runtime changes
- hard boundaries the agent must not violate

Rule:

- if a project has its own `AGENTS.md`, it should override the root bootstrap for project-specific behavior
- the root file should not assume every project uses the same `context/`, `knowledge/`, or `WORKPLAN.md` structure

## Recommended Read Order

Use exactly one of these startup paths.

### Single-Project Repo

1. nearest `AGENTS.md` or active bootstrap file
2. `WORKPLAN.md`
3. `context/README.md`
4. `context/current/project-state.md`
5. `context/current/runtime-map.md`
6. `context/current/repo-map.md`
7. `context/decisions/README.md`
8. then only task-specific docs

### Multi-Project Workspace

1. workspace root `AGENTS.md`
2. identify the target project
3. nearest project-level `AGENTS.md`
4. project `WORKPLAN.md`
5. project `context/README.md`
6. project `context/current/project-state.md`
7. project `context/current/runtime-map.md`
8. project `context/current/repo-map.md`
9. project `context/decisions/README.md`
10. then only task-specific docs

This keeps startup context short and stable while preventing agents from opening the wrong project queue first.

## New Session Recovery Contract

Bootstrap files and canonical docs must make a new session operational without relying on chat history.

The minimum questions a fresh session should answer quickly are:

- what task or queue is active right now
- what is currently live
- what rules and boundaries are already accepted
- which repo and service own the requested change
- which documents are canonical versus merely informative

Operational rule:

- if an agent needs a human to re-explain the project because the docs are ambiguous, the documentation model has failed

Maintenance rule:

- after meaningful runtime or rollout changes, update `context/current/`
- after accepting a boundary or architecture rule, update `context/decisions/`
- after changing near-term priorities, update `WORKPLAN.md`
- do not rely on stale feature docs or chat transcripts as implicit project memory

## Operational Enforcement

This blueprint only works if documentation updates are part of execution, not an optional cleanup step.

Minimum enforcement model:

- a task is not fully complete if runtime reality changed but `context/current/` was not updated
- a task is not fully complete if an accepted rule changed but `context/decisions/` was not updated
- a task is not fully complete if the active queue changed materially but `WORKPLAN.md` still describes the old queue

Practical ownership model:

- the implementer updates runtime code and the matching canonical docs in the same work cycle
- the reviewer checks code changes and canonical-doc alignment together
- if there is no separate reviewer, the implementing agent must perform an explicit self-check against canonical docs before calling the work complete

Definition-of-done minimum:

- runtime changes made in the correct repo
- canonical docs updated where required
- stale future docs did not remain masquerading as live truth
- deploy or rollout evidence linked or recorded in the appropriate place when relevant

## Runtime Repo Structure

A good runtime repo should expose service boundaries immediately.

Two acceptable patterns:

- top-level service directories with explicit names
- a `services/` container if ownership is still obvious

What matters is that a newcomer can answer "which service owns this behavior?" within seconds.

Example with explicit top-level services:

```text
src/
├── README.md
├── .github/workflows/
├── services/
│   ├── core-api/
│   │   ├── README.md
│   │   ├── app/
│   │   ├── tests/
│   │   └── ...
│   ├── channel-gateway/
│   │   ├── README.md
│   │   ├── app/
│   │   ├── frontend/
│   │   ├── tests/
│   │   └── ...
│   ├── mcp-server/
│   │   ├── README.md
│   │   ├── src/
│   │   ├── tests/
│   │   └── ...
│   └── worker/
├── packages/
├── infra/
├── scripts/
└── ...
```

Example with a smaller single-app runtime repo:

```text
src/
├── README.md
├── .github/workflows/
├── app/
├── frontend/
├── tests/
├── infra/
└── scripts/
```

### `src/README.md` Must Exist

This file should answer:

- what services or apps exist
- which service owns what
- where to change billing/orders/auth/frontend/mobile/integrations
- how deploy works at a high level
- how to run tests/builds locally

If `src/README.md` is empty, the repo is materially worse for LLM work.

## Generated Runtime Scaffolding

This blueprint is compatible with generator or improvement tools such as agent starter kits, scaffolding CLIs, and repo enhancement flows.

Examples of acceptable runtime-only operations:

- create a new runtime repo skeleton
- enhance an existing runtime repo with CI/CD, infra, observability, or playground tooling
- extract runtime logic into a cleaner package layout
- upgrade generated runtime scaffolding

Boundary rule:

- these tools operate on `src/` or another runtime repo only
- they do not replace the parent workspace repo
- they do not become the canonical source of project architecture truth

Recommended model:

- use the parent workspace repo as the control plane for plans, decisions, current-state docs, and evidence
- use generated scaffolding only as an implementation accelerator for deployable runtime code

Interpretation rule:

- `create` or `enhance` style tooling improves engineering maturity of the runtime layer
- it does not replace `WORKPLAN.md`, `context/current/`, `context/decisions/`, or the project's chosen future-work area

Failure mode to avoid:

- treating a generated runtime README or agent bootstrap file as the only architecture source for the whole project

## Internal Code Shape

Top-level repo structure is only half the problem.
The inside of each service must also be shaped for LLM navigation.

The goal is:

- small, predictable modules
- obvious ownership
- low need to load huge files just to make one change

One more rule matters just as much:

- a code path should cross boundaries through explicit contracts, not through hidden imports or duplicated business logic

## Boundary Enforcement Checklist

Use this to judge whether the structure is genuinely high quality.

- Can you identify the owner service for any business rule in under 30 seconds?
- Can you identify the transport, service, domain, persistence, and integration boundaries inside the relevant runtime owner without guesswork?
- Does exactly one service own the domain state machine and source-of-truth write?
- Are adapters, workers, MCP tools, and workflows unable to bypass that owner?
- Are secrets and runtime-mutated env files kept outside git?
- Can an agent find the canonical queue, current runtime truth, and accepted decisions without ambiguity?
- Does each major service have a README or equivalent entrypoint guidance?
- Do migrations live with the runtime repo, not the project-memory repo?
- Are projections and operator tools clearly treated as non-canonical unless explicitly stated otherwise?

### Recommended Service Layout

For a backend service:

```text
service/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── dependencies.py
│   ├── routers/
│   ├── services/
│   ├── repos/
│   ├── models/
│   ├── schemas/
│   ├── domain/
│   ├── integrations/
│   └── utils/
└── tests/
```

For a frontend app:

```text
frontend/
├── src/
│   ├── app/
│   ├── screens/
│   ├── components/
│   ├── features/
│   ├── api/
│   ├── hooks/
│   ├── theme/
│   ├── lib/
│   └── routes/
└── tests/
```

These are patterns, not mandatory folder names.
The real standard is ownership clarity and decomposition quality.

### Allowed Runtime Layout Patterns

Use a layout close to one of these shapes unless there is a strong reason not to:

- multi-service runtime repo with `services/`, optional `packages/`, `workers/`, `infra/`, and `scripts/`
- single backend app with an internal `app/` decomposition such as routers, services, repos, domain, schemas, and integrations
- frontend app with a `src/` decomposition such as app, screens, components, features, api, hooks, theme, lib, and routes
- shared runtime packages repo with clear consuming apps or services and explicit package ownership

Rule:

- prefer an existing recognized runtime shape over inventing novel top-level folders
- invent a new folder only when it represents a real ownership boundary, not a naming preference
- if a new folder does not correspond to a durable responsibility class, do not create it

### File Decomposition Rules

Prefer splitting by responsibility, not by arbitrary technical category.

Good splits:

- router vs service vs repository
- domain transitions vs transport schema
- feature API client vs feature UI
- pure validation logic vs side-effectful orchestration

Bad splits:

- one file per framework primitive with no ownership logic
- giant `utils.py` or `helpers.ts`
- one huge router file for the whole domain
- one giant React screen that also owns data fetching, validation, mutation, modal logic, and styling decisions

### File Size Heuristics

Use these as default decomposition review thresholds for LLM-friendly runtime maintenance.

- under `150` lines: usually easy to reason about
- `150-300` lines: still acceptable if cohesive
- `300-500` lines: decomposition review required
- over `500` lines: split or document a clear reason to keep the file intact
- over `800` lines: treat as a god-file and split unless there is an exceptional reason

The problem is not raw line count alone.
The real risk is when a file mixes:

- transport layer
- business rules
- data access
- provider integration
- UI state and rendering

That is where LLM-assisted changes become fragile.

Review trigger rule:

- if a runtime file crosses a review threshold, either decompose it or make the exception explicit in review or local service guidance
- do not silently normalize oversized mixed-responsibility files as acceptable structure

### Function Size Heuristics

Use these as extraction triggers, not as casual style suggestions.

- handlers should usually be thin
- orchestration functions should be readable in one screen
- pure business transitions should be extracted into named functions
- if a single function has more than roughly `40-60` lines and multiple branches, review it for extraction

### Router Rules

Routers/controllers should mainly:

- validate transport input
- call service/domain functions
- map domain errors to HTTP/UI responses

They should not own:

- persistence logic
- state transitions
- provider-specific business rules

### Service Rules

Services should own:

- orchestration
- business use-cases
- transaction boundaries
- domain invariants at the application level

They should not own:

- raw SQL details
- transport serialization
- global utility dumping grounds

### Repository Rules

Repositories should own:

- queries
- persistence mapping
- storage-specific filtering

They should not own:

- business transitions
- UI assumptions
- cross-service orchestration

### Frontend Screen Rules

A screen should not become a god-component.

Prefer:

- one screen file
- small presentational subcomponents
- extracted hooks for fetching and mutations
- isolated feature-level state machines where necessary

If a screen starts combining:

- route parsing
- fetch orchestration
- long conditional rendering
- modal orchestration
- form validation
- mutation retries

split it.

### Runtime Anti-Patterns

Treat these as structural smells that should trigger cleanup planning:

- giant `utils` modules that absorb unrelated responsibilities
- giant cross-domain routers or controllers
- service modules that mix transport, orchestration, persistence, and provider logic together
- frontend screens that become the hidden owner of data flow, validation, mutations, and rendering policy
- integration adapters that quietly become the source of business truth
- new top-level folders added without a clear ownership reason

## Documentation Shape

Documentation needs decomposition too.
The rule is not "every doc must be tiny".
The rule is "one document should have one primary semantic role".

Good documentation splits:

- current runtime facts vs accepted decisions
- feature vision vs implementation plan
- migration plan vs rollout runbook
- service ownership guide vs domain note

Bad documentation splits:

- one giant architecture file mixing live facts, target design, migration steps, and open questions
- a workplan that quietly contains accepted architecture
- a decision file that also acts as a runbook and as a delivery log

### Documentation Size Heuristics

These are softer than code heuristics, but still useful.

- under `200-300` lines: usually easy to maintain
- `300-600` lines: acceptable if it is one coherent topic
- `600-1000` lines: review for split or index-plus-child-doc structure
- over `1000` lines: usually split unless there is a strong reason not to

Split a document when it starts combining:

- current truth and future design
- multiple services with different owners
- architecture and procedural operations
- feature scope, migration details, and execution log

### Retrieval And Chunking Rule

If you plan to chunk or vectorize docs later, structure still matters.

Best practice:

- one file = one clear entity or one coherent subject
- use short indexes that point to child docs
- avoid giant mixed-topic files that create ambiguous chunks

Human readability comes first, but good human information architecture also improves retrieval quality.

## Testing Structure

Tests should mirror code ownership.

Prefer:

- `tests/routers`
- `tests/services`
- `tests/repos`
- `tests/domain`

or the equivalent structure in the language/framework.

Do not force every test into one flat directory if the codebase is growing.

## Deployment Model

This blueprint is deployment-model agnostic.
Do not encode one delivery style as a universal law.

Common acceptable patterns:

- file sync to a small VPS or dedicated server
- image-based deploy through a registry
- platform-managed deploys
- GitOps or infra-managed rollout

What matters is not the exact delivery tool.
What matters is that the project documents:

- which repo triggers deploy
- what artifact is being deployed
- what environments exist
- where version truth lives
- how rollout verification works
- where rollback procedure is documented

Put live deploy truth in `context/current/runtime-map.md`.
Put procedures in `context/runbooks/`.

## Service Boundary Rules

For multi-service systems, define ownership in plain language.

Example:

- `api` owns business correctness
- `gateway` owns channel adaptation and request translation
- `mcp-server` owns operator or agent facade only
- `workers` own transport, scheduling, or proxy behavior only
- orchestration tools do not own business rules
- the primary database is source of truth, not CRM or projection tools

If this is not documented clearly, LLM agents will leak logic into the wrong service.

## Anti-Patterns To Avoid

- mixing plans, runtime notes, and accepted decisions in one file
- storing mutable runtime state in multiple conflicting documents
- leaving `src/README.md` empty
- giant god-files without service-level decomposition
- giant cross-domain routers
- giant screen components
- giant `utils` modules
- one giant architecture doc that mixes live state, target design, and rollout steps
- using the runtime repo as a general notebook
- pushing project-memory docs together with production code by accident
- relying on implicit status instead of explicit document metadata
- treating a proposal as live truth because it was written recently

## Minimal File Templates

Each template below that belongs to a canonical doc class with required metadata should begin with the metadata header described in `Document Metadata Model`.
Bootstrap files and runtime bridge docs may use lighter metadata when appropriate.
The bullet lists below describe the semantic content that should follow.

### `AGENTS.md` in a Project Root

Should contain:

- what this specific project is
- whether it is a single-project repo or part of a larger workspace
- where deployable runtime code lives
- canonical read order for a fresh session
- source-of-truth rules for this project
- where `current`, `decisions`, the chosen future-work area, and runbooks live for this project
- what runtime-facing docs must remain inside `src/`
- what to update after runtime changes
- deploy model at a high level
- hard architectural and ownership boundaries

Should not contain:

- full copies of runtime maps or decision docs
- broad workspace routing logic that belongs in a higher-level bootstrap
- long historical notes pretending to be operating instructions

### `WORKPLAN.md`

Should contain:

- active priorities
- open blockers
- near-term execution queue
- short recent completions

Should not contain:

- full runtime snapshot
- long architectural rationale

### Optional `task-management/` Layer

Should contain:

- task packets
- execution-local checklists
- handoff notes
- ephemeral delivery support material

Should not contain:

- the only copy of accepted architecture
- the only copy of live runtime truth
- the canonical queue summary if `WORKPLAN.md` exists

### `context/README.md`

Should contain:

- short explanation of what belongs in `context/`
- source-of-truth rules for current docs, decisions, runbooks, and future-work docs
- concise read order into `context/current/` and `context/decisions/`
- links to the chosen future-work area and runbooks when they exist

Should not contain:

- full copies of current-state docs
- accepted decision content that belongs in `context/decisions/*`
- long delivery history or mutable execution notes

### `context/current/project-state.md`

Should contain:

- what is currently live at a project level
- what major initiatives are in progress
- what is blocked or transitional
- short notes on major recent changes

### `context/current/runtime-map.md`

Should contain:

- live services and environments
- current deploy topology
- live integrations
- current verified config and secrets layout at a high level
- links to runbooks and component guides

### `context/current/repo-map.md`

Should contain:

- all runtime repos and project-memory repos
- physical workspace layout if relevant
- which repo owns deploy-triggering changes
- where major components live

### Future-Work Status Doc

Example path:

- `context/features/FEATURE-*/status.md`

Should contain:

- current feature stage
- which feature docs are active
- what has been accepted
- what has been implemented already
- what remains future-only

Use this template only when the change is large enough to justify a feature dossier.
Do not create feature trees mechanically for every small change.
Equivalent locations are fine if the project uses another chosen future-work area.

### `context/components/<service>.md`

Should contain:

- owner
- responsibility
- what this service may change
- what it must not own
- links to code paths and decisions

### `context/runbooks/deploy.md`

Should contain:

- deploy trigger path
- artifact or sync target
- verification steps
- rollback entrypoint
- common failure interpretation

Use this when the project has a real deploy surface or operational procedure worth preserving.

### `src/README.md`

Should contain:

- runtime entrypoint summary
- service/app ownership map
- local run/build/test minimum
- deploy trigger surface for this repo
- links to any deeper runtime-facing docs in `src/docs/` if they exist

Should not contain:

- the only live runtime topology for the project
- a second mutable replacement for `context/current/runtime-map.md`
- long-form architectural rationale that belongs in parent workspace docs

## Default Project Creation Checklist

When creating a new project, do this immediately:

1. create the project workspace repo with `README.md`, `WORKPLAN.md`, `context/`, `knowledge/`, `artifacts/`, and project bootstrap files
2. if this project lives inside a larger multi-project workspace, add a project-level `AGENTS.md` even if a root routing bootstrap already exists
3. create `src/` as a separate git repo
4. if `src/` is nested inside the project workspace, ignore it from the parent repo
5. add `src/README.md`
6. ensure `src/` meets the runtime self-sufficiency threshold for narrow local changes
7. create `context/README.md` and define source-of-truth rules in it
8. create `context/current/project-state.md`
9. create `context/current/runtime-map.md`
10. create `context/current/repo-map.md`
11. create `context/decisions/README.md`
12. create the chosen future-work area only if the project needs it early, for example `context/features/README.md`
13. create `context/runbooks/deploy.md` if the project already has a real deploy surface or operational procedure worth documenting
14. document service ownership in `context/components/`
15. define deploy truth and environment model
16. define service-internal layout rules before files start growing
17. if task packets will exist, create a dedicated task layer outside `context/`
18. set a team rule to split code and docs before they become god-files

## Incremental Adoption For Existing Projects

Most real projects will not start from a clean blueprint.
Do not block adoption just because the repo is messy today.

Recommended adoption order for an existing project:

1. add or fix the project-level `AGENTS.md`
2. create `src/README.md` if runtime ownership is unclear
3. make the runtime repo self-sufficient for narrow local changes
4. create `context/current/project-state.md`
5. create `context/current/runtime-map.md`
6. create `context/current/repo-map.md`
7. create `context/decisions/README.md`
8. move only the highest-value accepted rules into `context/decisions/`
9. create `WORKPLAN.md` as the single active queue
10. add a separate task layer only if task packets are actually needed
11. split legacy mixed docs gradually instead of rewriting everything at once

Pragmatic rule:

- fix navigability first
- then fix source-of-truth ambiguity
- then improve structure and decomposition

Do not wait for a perfect documentation migration before using the system.

## Minimum Viable Mode

For a small or early-stage project, use the smallest version that still preserves clarity.

Minimum viable set:

- project-level `AGENTS.md`
- `WORKPLAN.md`
- `context/README.md`
- `context/current/project-state.md`
- `context/current/runtime-map.md`
- `context/current/repo-map.md`
- `context/decisions/README.md`
- `src/README.md`

As the project grows, you can add the chosen future-work area, `runbooks/`, `components/`, `domains/`, `artifacts/`, a task layer, and richer metadata.

Rule:

- do not introduce full ceremony before the project needs it
- do introduce the canonical read path and source-of-truth model as early as possible
- keep `src/` self-sufficient before expanding the parent doc system

## Short Version

If you want the shortest rule set:

- parent repo = control plane and project memory
- `src/` = deployable runtime code
- `knowledge/` = reusable library
- `context/` = project wiki
- `WORKPLAN.md` = next
- `context/README.md` = index and source-of-truth entrypoint for the project wiki
- `context/current/` = live now
- `context/decisions/` = accepted
- the chosen future-work area (for example `context/features/`) = future and in-progress change work
- `context/runbooks/` = how to operate
- `src/README.md` = runtime contributor entrypoint and local bridge doc, not the canonical runtime map
- `src/` must remain self-sufficient for narrow local changes
- task packets, if used, belong in a dedicated task layer outside `context/`
- each service and each document set should be decomposed by ownership instead of growing into giant mixed files

That structure is close to ideal for LLM-assisted project work because it minimizes ambiguity in both documentation and code.
