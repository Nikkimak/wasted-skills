# Implementation design contract

## Purpose

Capture technical meaning that several delivery tasks must share. Do not duplicate the PRD and do not pre-write every task.

## Semantic structure

Adapt headings to the target repository:

```markdown
# Implementation design: feature/version

## Accepted PRD reference
## Current system and owner components
## Proposed technical shape
## Contracts and data
## Integration boundaries
## Failure, retry, and recovery behavior
## Compatibility, migration, and rollback
## Security and trust boundaries
## Observability and operations
## Verification strategy
## Vertical-delivery constraints
## Open technical decisions
```

## Rules

- Bind the design to one accepted PRD version/hash.
- Name exactly one owner for orchestration state and each durable contract.
- Describe contracts and invariants, not speculative file-by-file edits.
- State failure, partial-success, retry, idempotency, and recovery behavior where relevant.
- Separate required current-version work from future technical horizon.
- Make the first meaningful end-to-end integration test possible early.
- Include migration/rollback only when the change needs them.
- Put security controls into the design, while leaving final security readiness to the `feature-security-review` skill (via the Skill tool, `/skill:feature-security-review`) after task planning.
- List open technical choices explicitly for human resolution.

## No-document result

Use `implementation_doc_not_required` when all shared technical meaning fits safely in one bounded task contract. Give a short evidence-based reason and any constraints that the `feature-delivery-plan` skill (via the Skill tool, `/skill:feature-delivery-plan`) must preserve.
