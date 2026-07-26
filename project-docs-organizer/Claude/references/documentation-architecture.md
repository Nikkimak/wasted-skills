# Documentation Architecture

## Common Authority Roles

Use semantic roles instead of one mandatory folder tree. Existing strong
equivalents are valid.

- **Bootstrap/router**: nearest `CLAUDE.md`, `AGENTS.md`, or equivalent; intent
  routing, constraints, and useful entrypoints only.
- **Active queue**: `WORKPLAN.md` or one selected equivalent; current priorities
  and blockers. Carry only open work and remove entries as they land; a queue
  that accumulates completed items becomes a second changelog.
- **Product contract**: intended users, outcomes, scope, and acceptance.
- **Active coordination state**: migrations in flight, partial rollouts,
  temporary arrangements, and blocked areas. A role, not a default document.
- **Accepted decisions**: rationale, invariants, and explicitly superseded
  boundaries.
- **Deployment/runtime evidence**: verified environment, release, artifact, or
  runtime state.
- **Runbooks**: procedures for operations, recovery, and diagnostics.
- **Future work**: proposed or in-progress changes that are not current truth.
- **Knowledge/reference**: reusable source material that informs work but is not
  automatically project authority.
- **Evidence/artifacts**: reviews, experiments, reports, and generated output
  with explicit provenance.
- **Task layer**: delivery packets and handoffs; not the only owner of durable
  project facts.
- **Runtime-local documentation**: contributor navigation, ownership, public
  contracts, tests, and local operational facts close to code.

Each mutable fact class should have one owner. Other documents link to it rather
than maintaining a second paraphrased copy.

### Active Coordination Has No Default Document

An in-flight migration or partial rollout belongs to whoever is met on the
working path, not to a central file a task-focused session never opens:

- a transition owned by one feature → that feature package;
- a blocker → the active queue;
- a zone affected by another owner's transition → one pointer line in that zone's
  local README, linking the owner instead of copying its state.

Create a separate coordination document only when a transition spans several
owners and no feature package holds it. Delete it when the transition closes.

## Feature Packages

Give every new feature one stable, project-wide identity and package directory:

```text
<feature-area>/FEATURE-NNN-short-name/
├── prd.md
├── implementation-design.md
├── delivery-plan.md
├── EXECUTION-READINESS.md
└── WORK-HANDOFF.md
```

Use the next number above the highest existing project feature ID, starting with
`FEATURE-001`; never reuse or renumber it. Keep the directory basename stable
except for an approved slug rename, and begin canonical titles with
`FEATURE-NNN`. Record `feature_id: FEATURE-NNN` when the project uses
frontmatter. The repository may choose the parent feature area, but not a
different package basename. Create only artifacts required by the active
workflow; do not precreate empty files. Preserve legacy feature paths unless
migration is explicitly approved.

## Documentation-Primary Projects

Do not materialize runtime concepts without evidence. A compact shape may be:

```text
project-root/
├── CLAUDE.md or the project's established router
├── README.md or index
├── current/ or accepted equivalent
├── decisions/ when durable rationale exists
├── future/ when planned work needs separation
└── references/ or knowledge/ when reusable sources exist
```

The names are illustrative; prefer existing vocabulary when its authority roles
are clear. The bootstrap routes by question type, topic, status, and authority,
and never instructs every session to read every index.

## Code-Bearing Projects

Documentation lives next to the code it complements. Central documents hold
product, rationale, operations, and planning, and route to everything else.

### Shape

Scale depth to the project. A single-runtime repository often needs only the
router, the runtime README, and one decisions folder; add a line below only when
present evidence requires it.

```text
project-root/
├── CLAUDE.md            router: intent routes and constraints only
├── README.md            product purpose; routes to the runtime README
├── WORKPLAN.md          open work only, when a queue is needed
├── src/
│   ├── README.md        canonical ownership map for this runtime
│   ├── payments/
│   │   └── README.md    only knowledge the code cannot express
│   └── users/
├── tests/
└── docs/                only the central roles that actually exist
    ├── features/FEATURE-NNN-short-name/
    ├── decisions/
    ├── evidence/
    └── runbooks/
```

`docs/` is one possible name for the central roles; established project
vocabulary wins. Never create a folder for a role the project does not have.

### Ownership Map

A code-bearing project must expose an ownership map reachable from its router —
one for a single runtime, one per runtime when several exist. Every map uses this
chain verbatim:

```text
capability or domain → owning path → entrypoint or symbol → tests → optional local note
```

Place it at the runtime root — `src/README.md` or the equivalent runtime
entrypoint — so it sits on the path from router to code. When the repository
itself is the runtime, its root README is that entrypoint.

Several runtimes mean several ownership maps, one per runtime README, plus one
project-level runtime map that routes between them:

```text
runtime → code root → owner → local README → tests → deploy evidence
```

The two levels never restate each other: the runtime map names runtimes, each
runtime README names its own capabilities.

Each runtime has exactly one ownership map; other documents link to it instead of
restating the chain. Map every top-level capability at one line each. It must
never grow into a file listing. A capability owned by several zones lists those
owners in flow order and stays navigation rather than a description of behavior.

Name an entrypoint or symbol when the zone has one; when no single entrypoint
exists, let the owning path stand alone instead of inventing a symbol. Name the
participating tests, or record `tests: missing`.

### Local Documentation

The runtime README owns the ownership map, verified run, build, and test
commands, public boundaries, integration warnings, and deploy entrypoints at a
high level without copying live topology. The root README states product purpose
and routes to it; it repeats none of that. When the repository itself is the
runtime, the two are one file.

Create a deeper ownership README only when a durable boundary needs one, and only
for knowledge the code does not already express: reasons, non-obvious invariants,
cross-file relationships, external constraints, and failure or recovery
semantics. Anything recoverable from code, schemas, configuration, or tests
becomes a link, not a paragraph.

When a monolith or vendored tree offers no clean directory boundary, use a
code-anchored note under the nearest logical owner. Anchor it to stable paths and
symbols, name the participating tests, add the vendor commit or version when the
code is external, and never anchor to line numbers.

Code and tests remain final authority for current implementation behavior;
verified runtime or deploy evidence remains final authority for deployed state.

## Metadata And Lifecycle

Metadata should help select authority and lifecycle, not add decorative churn.
For new canonical documents use `title`, `doc_type`, `status`, `owner`, and
`authority_for` as one or more explicit question classes; add `last_reviewed`
when recency matters, `related` for useful direct links, and `supersedes` or
`superseded_by` when lifecycle requires them.

Existing `source_of_truth` metadata may remain for compatibility, but a boolean
does not replace `authority_for` or the intent matrix. An index can be
authoritative for navigation without being authoritative for the facts it links
to.

Use lifecycle values consistently, for example `draft`, `proposed`, `approved`,
`in_progress`, `implemented`, `superseded`, and `archived`. Future-oriented
documents never prove current implementation or deployment.

## Maintenance And Drift

Update documentation when durable meaning changes, not after every internal edit.

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

Updating is not the only valid outcome. Choose one:

- **update** when durable meaning changed;
- **relocate** when the knowledge now belongs to another owner;
- **reduce to a link** when code and tests already express the fact clearly;
- **delete or archive** when the document owns no unique knowledge.

When an audit finds a central document narrating current behavior, identify the
owning code and move only the complementing knowledge next to it. Then either
reduce the document to a map when it still carries an independent navigational
role, or delete it and put the link into the existing router or map. Do not leave
a stub file whose only content is one link.

Archive only historical evidence. An archived document carries `status: archived`,
leaves every current route and index, names the owner that replaced it, and stays
out of current-behavior retrieval.

Any of these migrations is a mutation and needs the same approval and backup as
any other. Prefer link, metadata, and ownership checks over generated prose;
generated inventories may describe verifiable structure but must not become an
unreviewed second source of truth.

## Size And Decomposition

One document should have one primary semantic role. Indexes and routers stay
scannable at a glance. At roughly 300–600 lines review whether one topic and
owner still justify the document; at 600–1000 prefer an index plus linked child
docs when more than one role is present; above 1000 require a clear reason to
keep one file.

Split current facts from future design, rationale from procedures, ownership
guidance from domain reference, and feature scope from delivery history. Do not
split a coherent document solely to meet a line count.
