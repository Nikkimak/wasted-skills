# Retrieval And Indexing

An optional advanced reference. V1 requires good information architecture and
deterministic search, not retrieval infrastructure.

## Deterministic Default

Classify question intent and repository state, filter by likely authority and
ownership surface, search exact paths, terms, symbols, and structural
entrypoints, rank a short candidate list, then open only relevant slices, local
docs, code, contracts, and tests. Expand semantically only when deterministic
recall proves insufficient.

Raw search may return many matches. Evaluate whether the correct owner or source
is in the top five ranked surfaces; raw match count is irrelevant.

## Source Classes

For current implementation questions, prefer runtime-owned code, public
contracts, and executable tests, and use local runtime docs for navigation.

Exclude or downrank by default:

- future-work and backlog material;
- artifacts, experiments, and generated prose;
- archived documents and superseded decisions;
- dependencies and vendor source;
- generated bundles and coverage;
- unrelated repository states.

Change ranking when the question explicitly asks for planning, history, evidence,
vendor behavior, or another source class.

## Repository State

Keep working tree, accepted ref, and deployed release distinguishable. A future
local index should carry a logical repository identifier, ref or state, relative
path, content hash, source class, ownership surface, symbol when applicable, and
index time. Avoid persisted personal absolute paths. Optional deployed indexes
may carry environment and verification metadata; candidate and deployed corpora
are named separately rather than treated as one universal primary index.

## Structural Chunking

If advanced retrieval is justified, prefer structural chunks: an exported
function, class, method, route, component, or public declaration; a coherent
patch target and hunk group; a Markdown heading; a test suite or materially
distinct scenario. Do not use blind token windows when a parser or stable
document structure is available. Code and direct evidence remain authoritative
after retrieval.

## Mutation Boundary

`assess_advanced` permits analysis only. Do not create manifests, caches,
databases, embeddings, vector collections, or generated artifacts unless each
target is listed in the approved mutation scope. Generated local search state
normally lives in an ignored cache outside canonical project truth; version only
small schemas, manifests, or evaluation fixtures that are deliberate project
artifacts.

## Adoption Gate

Recommend advanced indexing only when real evaluation shows repeated owner or
source recall failures, cross-repository navigation cost, or unacceptable latency
that deterministic path and symbol search cannot solve. Repository size alone is
not sufficient evidence.
