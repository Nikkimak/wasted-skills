---
name: feature-revision
description: Revise an approved feature's PRD, implementation design, delivery plan, and optional execution-readiness document as one atomic change set. Use when decisions change after downstream documents exist and the human wants one consolidated review instead of repeating stage reviews. Preserve the accepted baseline, propagate the change, run traceability checks, then use the revision cross-model profile and obtain human approval. Do not use for initial discovery, implementation, or tracker publication.
---

# Feature Revision

Read the target repository's instructions and accepted PRD, implementation design or `implementation_doc_not_required`, delivery plan, conditional `EXECUTION-READINESS.md`, and relevant canonical context. Confirm the change intent; use `$feature-design` first if product discovery is still needed. Treat non-semantic edits as direct maintenance unless the human requests review.

## Workflow

1. Capture exact baseline versions or hashes and affected documents and IDs: acceptance criteria, invariants, `SEC-*`, `VER-*`, tasks, dependencies, and `HIN-*`. Create complete `draft` or `proposed` copies in an owner-only scratch area; leave canonical documents unchanged.
2. Keep an ephemeral change intent covering outcome, scope, non-goals, and open decisions, plus a baseline-to-proposal diff. Propagate the change from PRD through implementation/security, delivery, and readiness; preserve valid IDs and remove stale references.
3. Check cross-document traceability, contradictions, unauthorized scope, orphaned IDs, dependencies, verification, merge targets, and readiness.
4. If the change introduces exceptional payment, identity, privileged-secret, sensitive-user-data, isolation, destructive, irreversible, or comparable risk, invoke `$feature-security-review` on the proposed implementation before review. This is enrichment, not another gate.
5. Invoke `$cross-model-review` with the `revision` profile. Pass proposed documents as artifacts and baselines, intent, diff, repository instructions, and unchanged related documents as context. Evaluate every finding, correct confirmed issues, and recheck the full bundle in the same reviewer session; do not run separate stage reviews.
6. Obtain human resolution for material scope, architecture, security, residual-risk, or irreversible decisions. After explicit approval, apply one canonical patch, update bindings/statuses, and remove scratch state. If the review loop cannot finish in this session, use `$feature-context-handoff` before review.

## Boundaries

- Do not invent product decisions or persist change intent, diffs, review transcripts, finding ledgers, or reviewer session IDs.
- Do not implement code, publish tracker issues, provision external inputs, or change unrelated documents.

## Completion

Report the accepted baseline, changed canonical paths, propagated product/technical/security/task effects, review outcome, any human-resolved exceptions, readiness result, remaining decisions, and whether the consolidated patch was applied.
