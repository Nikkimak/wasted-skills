# Retrieval And Indexing

This is an optional advanced reference. V1 requires good information
architecture and deterministic search, not retrieval infrastructure.

## Deterministic Default

Use this order:

1. classify question intent and repository state;
2. filter by likely authority and ownership surface;
3. search exact paths, terms, symbols, and structural entrypoints;
4. rank a short candidate list;
5. open only relevant slices, local docs, code, contracts, and tests;
6. expand semantically only when deterministic recall is insufficient.

Raw search may return many matches. Evaluate whether the correct owner/source is
in the top five ranked surfaces.

## Source Classes

For current implementation questions, prefer runtime-owned code, public
contracts, and executable tests. Use local runtime docs for navigation.

Exclude or downrank by default:

- future-work and backlog material;
- artifacts, experiments, and generated prose;
- superseded decisions;
- dependencies and vendor source;
- generated bundles and coverage;
- unrelated repository states.

Change ranking when the question explicitly asks for planning, history,
evidence, vendor behavior, or another source class.

## Repository State

Keep working tree, accepted ref, and deployed release distinguishable. A future
local index should carry a logical repository identifier, ref or state, relative
path, content hash, source class, ownership surface, symbol when applicable, and
index time.

Avoid persisted personal absolute paths. Optional deployed indexes may carry
environment and verification metadata. Candidate and deployed corpora should be
named separately rather than treated as one universal primary index.

## Structural Chunking

If advanced retrieval is justified, prefer structural chunks:

- exported function, class, method, route, component, or public declaration;
- coherent patch target and hunk group;
- Markdown heading;
- test suite or materially distinct scenario.

Do not use blind token windows when a parser or stable document structure is
available. Code and direct evidence remain authoritative after retrieval.

## Mutation Boundary

`assess_advanced` permits analysis only. Do not create manifests, caches,
databases, embeddings, vector collections, or generated artifacts unless each
target is listed in the approved mutation scope.

Generated local search state should normally live in an ignored cache outside
canonical project truth. Version only small schemas, manifests, or evaluation
fixtures when they are deliberate project artifacts.

## Adoption Gate

Recommend advanced indexing only when real evaluation shows repeated owner or
source recall failures, cross-repository navigation cost, or unacceptable
latency that deterministic path and symbol search cannot solve. Repository size
alone is not sufficient evidence.
