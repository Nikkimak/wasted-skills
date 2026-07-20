# Authority And Intent Routing

Select the smallest safe read path by intent; no source is globally
authoritative.

## Authority Matrix

| Intent | Start with | Final authority | Do not assume |
| --- | --- | --- | --- |
| Local known-owner implementation | Nearest runtime or ownership README | Inspected code and executable tests | Central current-state prose is exact implementation truth |
| Unknown-owner investigation | Path, lexical, symbol, and ownership search | Owning code, contracts, and tests | The most semantically similar document owns the behavior |
| Product meaning | Accepted product or feature contract | Accepted product scope and outcomes | Current code proves intended behavior |
| Rationale or invariant | Applicable accepted decision | Current non-superseded decision | An ADR describes every current implementation detail |
| Deployed state | Runtime/deploy map and release evidence | Verified deployment or runtime evidence | Working tree or accepted design is deployed |
| Operations | Applicable runbook | Verified procedure plus current runtime evidence | A runbook proves current deployment state by itself |
| Active work | Queue and applicable future-work contract | Current queue/status owner | Planned work is implemented |
| Documentation lookup | Short index or deterministic search | Document owning the requested fact class | Every canonical document must be read first |

Bootstrap files route and constrain; they are not implementation or deployment
truth.

## Repository-State Rule

Distinguish `working_tree` (local files), `accepted_ref` (selected branch, tag,
or commit), and `deployed` (verified release/artifact). Name the relevant state.

## Bounded Read Paths

### Known Owner

Read nearest instructions → local runtime/ownership entrypoint → relevant code,
contract, and tests. Load product, decision, runbook, or queue material only when
the task crosses that boundary; an already specified local task does not require
`WORKPLAN.md`.

### Unknown Owner

Search paths/terms, then symbols/entrypoints; rank ownership surfaces before
opening content. Inspect local docs, code, and tests for the best candidates and
expand centrally only if ownership remains unclear. Put the correct owner/source
in the top five; raw match count is irrelevant.

### Boundary Questions

Open the requested authority class first. Cross-check another only when needed:
product → code/tests for implementation status; decision → code for current
representation; runbook → deploy evidence for live result.

## Conflict Handling

- Code may expose stale docs but cannot silently change accepted intent or
  rationale; deployed evidence may validly differ from the working tree.
- Superseded decisions are historical; future work is not current behavior.
- Report competing owners of one authority class; do not invent a winner.

## Context-Economy Evaluation

Measure context before the first correct source, not repository size. Separate
organizer files/tokens from resulting project startup files/tokens; record
top-five owner/source placement, earlier wrong-authority opens, and final
correctness. Evaluate `local_known_owner`, `unknown_owner`, `product`,
`rationale`, `deployed_state`, `operations`, and `documentation_lookup`.
Accept reduction only without owner/source accuracy regression.
