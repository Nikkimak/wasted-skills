# Review profiles

## PRD

Challenge:

- business outcome and user value;
- current versus desired behavior;
- scope, non-goals, and MVP boundary;
- contradictory scenarios or acceptance criteria;
- missing product decisions;
- unsupported assumptions about current reality;
- architecture-horizon requirements accidentally treated as current scope;
- observable acceptance and failure behavior.

Do not invent implementation detail unless needed to expose a product gap.

## Implementation

Challenge:

- fidelity to the accepted PRD/version;
- component ownership and contracts;
- data model, migration, compatibility, and rollback;
- failure, retry, concurrency, and consistency behavior;
- observability and operational recovery;
- security boundaries and secret/data handling;
- testability and verification environments;
- feature-branch integration and safe incremental delivery;
- unnecessary complexity or missing shared decisions.

Separate product questions from technical corrections.

## Task plan

Challenge the complete graph:

- every committed acceptance criterion maps to executable scope;
- no task implements requirements absent from the accepted design;
- slices are vertical and independently verifiable;
- task scope is bounded without micro-task fragmentation;
- dependencies are complete, directional, and acyclic;
- deferred work is visible but does not block current acceptance;
- execution and validation profiles fit the work;
- merge targets and parent/child ownership are explicit;
- final parent acceptance covers combined behavior;
- security and integration verification are assigned to concrete tasks.

## Security

Use this profile only inside a human-gated feature security review. Challenge:

- assets, actors, trust boundaries, and privileges;
- authentication/authorization ownership and isolation;
- secrets, sensitive-data lifecycle, and log/redaction behavior;
- external inputs, abuse cases, replay/idempotency, and resource bounds;
- third-party failure and compromised-dependency behavior;
- fail-open/fail-closed, rollback, and recovery decisions;
- whether mitigations and verification belong to concrete vertical tasks;
- any residual risk that requires an explicit human decision.

Models may propose mitigations but cannot accept material risk for the human.

## Finding format

The GPT reviewer returns concise live findings, not an artifact:

```text
[ID] [blocking|material|minor] Summary
Evidence: exact section/path and contradiction or missing contract
Impact: why this matters
Recommendation: smallest correction preserving intended outcome
Human decision: yes/no; exact question when yes
```

On recheck, the reviewer re-reads the whole corrected draft. It states which prior findings are resolved, lists any remaining or new finding including minor ones, and says `CLEAN` only when none remain.
