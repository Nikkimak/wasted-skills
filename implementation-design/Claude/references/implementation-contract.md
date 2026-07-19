# Implementation design contract

## Purpose

Capture technical and security meaning shared by multiple delivery tasks. Do not duplicate the PRD or pre-write the task graph.

## Semantic structure

Use only the headings needed to make changed shared meaning self-contained; combine or omit irrelevant sections and reference unchanged canonical baselines instead of restating them:

```markdown
# Implementation design: feature/version

## Accepted PRD reference
## Current system and owner components
## Proposed technical shape
## Contracts and data
## Integration boundaries
## Failure, retry, and recovery
## Compatibility, migration, rollout, and rollback
## Security and trust boundaries
## Observability and operations
## Verification strategy
## External inputs and execution prerequisites
## Vertical-delivery constraints
## Open technical or risk decisions
```

## Core rules

- Bind the design to one accepted PRD version or hash.
- Define the material delta first; preserve and cite unchanged accepted contracts.
- Assign one owner to each changed durable contract or state transition.
- Describe affected invariants and boundaries, not file-by-file edits.
- State partial success, retry, concurrency, recovery, and rollback only where relevant.
- Enable an early meaningful end-to-end verification path.
- Separate current-version requirements from future horizon.

## Security contract

Classify depth:

- `quick`: no material new or changed security boundary;
- `standard`: the delta materially changes ordinary auth, stored data, external input, or integration risk without a high-impact boundary;
- `deep`: the delta introduces or materially changes payment, identity, privileged-secret, sensitive-data, tenant-isolation, destructive/irreversible, or comparable high-impact boundaries.

Existing high-impact functionality alone does not raise the depth. For affected risks, define only the actors, assets, boundaries, lifecycle, abuse/failure behavior, recovery, and residual risk needed to explain the delta. Reference inherited controls once; create `SEC-*` and `VER-*` IDs only for new or changed obligations.

Invoke the `feature-security-review` skill (via the Skill tool as `/feature-security-review`) only for `deep` risk or explicit human request and keep its durable result in this implementation document. After the document is complete, ask the human whether to run one `cross-model-review` `implementation` pass; never infer approval from security depth or from having run the security enrichment.

## External prerequisites

Record only known prerequisites affected or introduced by the change, with purpose, consuming stage, safe handling, and what may proceed without them. Never record secret values or sensitive payloads; status belongs to delivery planning's conditional `EXECUTION-READINESS.md`.

## No-change and no-document results

- `implementation_change_not_required`: an accepted design or no-document result remains valid and the delta changes no shared technical/security contract. Cite the baseline; do not edit, review, or reapprove it.
- `implementation_doc_not_required`: one bounded task can own all notes and no new or changed shared contract/security decision exists. Give the reason and the planning constraints that the `feature-delivery-plan` skill must preserve.

## Review readiness

Approved review requires one self-contained `draft` or `proposed` artifact with no placeholders, exact PRD/baseline references, explicit open decisions, delta-based security depth, and affected prerequisites. Completeness is about material decisions, not filled headings. No-change and no-document results are not review artifacts and are approved directly by the human.
