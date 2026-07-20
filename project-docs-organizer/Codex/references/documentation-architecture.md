# Documentation Architecture

## Contents

1. Common authority roles
2. Documentation-primary projects
3. Code-bearing projects
4. Metadata and lifecycle
5. Maintenance and drift
6. Size and decomposition

## Common Authority Roles

Use semantic roles instead of one mandatory folder tree. Existing strong
equivalents are valid.

- **Bootstrap/router**: nearest `AGENTS.md` or equivalent; intent routing,
  constraints, and useful entrypoints only.
- **Active queue**: `WORKPLAN.md` or one selected equivalent; priorities and
  blockers, not architecture or implementation truth.
- **Product contract**: intended users, outcomes, scope, and acceptance.
- **Current project snapshot**: concise project-level state and transitions; not
  exact code behavior or proof of deployment.
- **Accepted decisions**: rationale, invariants, and explicitly superseded
  boundaries.
- **Deployment/runtime evidence**: verified environment, release, artifact, or
  runtime state.
- **Runbooks**: procedures for operations, recovery, and diagnostics.
- **Future work**: proposed or in-progress changes that are not current truth.
- **Knowledge/reference**: reusable source material that informs work but is not
  automatically project authority.
- **Evidence/artifacts**: reviews, experiments, reports, generated output, and
  other evidence with explicit provenance.
- **Task layer**: delivery packets and handoffs; not the only owner of durable
  project facts.
- **Runtime-local documentation**: contributor navigation, ownership, public
  contracts, tests, and local operational facts close to code.

Each mutable fact class should have one owner. Other documents link to it rather
than maintaining a second paraphrased copy.

## Documentation-Primary Projects

Do not materialize runtime concepts without evidence. A compact shape may be:

```text
project-root/
├── AGENTS.md
├── README.md or index
├── current/ or accepted equivalent
├── decisions/ when durable rationale exists
├── future/ when planned work needs separation
└── references/ or knowledge/ when reusable sources exist
```

The names are illustrative. Prefer the existing vocabulary when its authority
roles are clear.

The bootstrap should route by question type, topic, status, and authority. It
should not instruct every session to read every index or current document.

## Code-Bearing Projects

Runtime documentation must make narrow local work safe without duplicating the
central wiki.

A runtime entrypoint or strong equivalent should identify:

- runtime apps or major ownership zones;
- where to change important behavior;
- local run, build, and test commands;
- public boundaries and integration warnings;
- deeper ownership docs only where they exist;
- deploy entrypoints at a high level without copying live topology.

Create a local service or ownership README only when a durable boundary needs
one. It should cover responsibility, public contract, important dependencies,
failure semantics, test surface, and links to applicable decisions or runbooks.
It should not narrate internal implementation line by line.

Central project docs own product, rationale, project snapshot, deployed contour,
operations, and planning. Runtime-local docs own contributor navigation and
local contracts. Code and tests remain final authority for current
implementation behavior.

## Metadata And Lifecycle

Metadata should help select authority and lifecycle, not add decorative churn.
Recommended fields for new canonical documents are:

- `title`;
- `doc_type`;
- `status`;
- `authority_for` as one or more explicit question classes;
- `owner`;
- `last_reviewed` when recency matters;
- `related` only for useful direct links;
- `supersedes` and `superseded_by` when lifecycle requires them.

Existing `source_of_truth` metadata may remain for compatibility, but a boolean
does not replace `authority_for` or the intent matrix. An index can be
authoritative for navigation without being authoritative for the facts it
links to.

Use lifecycle values consistently, for example `draft`, `proposed`, `approved`,
`in_progress`, `implemented`, `superseded`, and `archived`. Future-oriented
documents never prove current implementation or deployment.

## Maintenance And Drift

Update documentation when durable meaning changes, not after every internal
edit.

Review documentation impact when a change alters:

- product outcome or accepted scope;
- ownership, public contract, or cross-zone boundary;
- deployed topology, environment, or operational procedure;
- configuration shape needed by contributors;
- active priority or feature status;
- accepted rationale or invariant.

An internal refactor that preserves these meanings normally requires code and
test updates only. A move that changes ownership navigation may require the
runtime entrypoint or local README even when behavior is unchanged.

Prefer link, metadata, and ownership checks over generated prose. Generated
inventories may describe verifiable structure but must not become an
unreviewed second source of truth.

## Size And Decomposition

One document should have one primary semantic role.

- Short indexes and routers should remain concise enough to scan immediately.
- At roughly 300–600 lines, review whether one topic and owner still justify the
  document.
- At roughly 600–1000 lines, prefer an index plus directly linked child docs
  when more than one role is present.
- Above 1000 lines, require a clear reason to keep one file.

Split current facts from future design, rationale from procedures, ownership
guidance from domain reference, and feature scope from delivery history. Do not
split a coherent document solely to meet a line count.
