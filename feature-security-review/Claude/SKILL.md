---
name: feature-security-review
description: Perform the human-gated security readiness review of an accepted PRD, optional implementation design, and vertically decomposed task graph before tasks are published to Linear or another tracker. Use when feature planning is complete and Claude must check trust boundaries, sensitive data, authorization, secrets, external inputs, abuse cases, dependency/integration risks, safe rollout and rollback, and whether security acceptance criteria are assigned to concrete tasks. Stop on unresolved critical risk and require explicit human decisions for material residual risk; do not trade away the required business outcome silently.
---

# Feature Security Review

Review the proposed change, not the repository in the abstract. This is the final human-in-the-loop gate after design/decomposition and before tracker publication.

Read the target repository's instructions and canonical security/architecture decisions. Read `references/security-readiness-checklist.md` completely before reviewing.

## Session Continuity

When continuing an existing feature, use the `feature-context-handoff` skill (invoked via the Skill tool as `/feature-context-handoff`) to read any feature-local `WORK-HANDOFF.md` after mandatory repository instructions, then load its named accepted inputs and active security-review state. Canonical artifacts override the handoff.

Before a standard or deep cross-family challenge, rely only on the host-provided context indicator (the Claude Code `/context` view or status line) when available. If the complete challenge, corrections, human risk decisions, and full recheck cannot safely fit, checkpoint with the `feature-context-handoff` skill and recommend a fresh session. Do not estimate context numerically or install automatic monitoring.

## Preconditions

Require:

- an accepted PRD or feature artifact;
- an implementation design when the feature needs shared technical contracts;
- proposed task contracts with vertical scope, dependencies, and validation plans;
- the relevant current architecture and accepted decisions.

If decomposition is incomplete, return to feature design rather than inventing missing tasks inside the security gate.

## Workflow

1. Classify depth:
   - `quick`: small UI change or fix with no new trust/data boundary;
   - `standard`: ordinary feature touching auth, stored data, external input, or integrations;
   - `deep`: cross-system, privileged, payment, identity, secret-bearing, destructive, or high-impact change.
2. Trace assets, actors, trust boundaries, entry points, data lifecycle, privileges, external dependencies, and failure/rollback paths.
3. Evaluate each task, not only the parent PRD. Confirm that security controls and verification belong to executable vertical slices.
4. Distinguish:
   - confirmed blocking risk;
   - material risk requiring mitigation;
   - residual risk requiring human acceptance;
   - hardening suggestion that does not block delivery;
   - unsupported concern.
5. Propose the smallest corrections that preserve the business outcome. Never silently remove required behavior to make the review pass.
6. Prepare confirmed controls and security acceptance criteria in the proposed task contracts. Keep accepted PRD and implementation artifacts as immutable context. If a mitigation requires changing accepted product scope or a shared technical contract, return to the `feature-design` or `implementation-design` skill, reopen the affected document as a proposed revision, and re-obtain its approval. Do not create a separate report for a low-risk feature. Before any cross-family challenge, ensure the complete mutable review target is self-contained, has no placeholders, and explicitly records every known open human risk decision.
7. Stop and ask the human when:
   - a critical risk cannot be mitigated within scope;
   - a mitigation changes product behavior or architecture materially;
   - residual risk is material;
   - the safe path requires an irreversible or operational commitment.
8. Recheck the corrected plan. Obtain explicit human approval of the final amended task set and security posture; require separate reapproval of any reopened PRD or implementation revision. Then mark the task contracts approved/accepted according to the target repository's status convention. After completion, remove an obsolete `WORK-HANDOFF.md` through the `feature-context-handoff` skill when canonical documents and the work plan make publication readiness clear. Publish nothing to the tracker before those approvals.

## Cross-Family Challenge

For `standard` or `deep` reviews, first confirm that the human wants the complete review-ready target challenged; an explicit request already made in the current conversation counts. Invoke the `cross-model-review` skill (via the Skill tool, `/cross-model-review`) against the full proposed task set and any upstream document explicitly reopened as a proposed revision. Supply unchanged accepted PRD and implementation artifacts as immutable reviewer context, together with the security questions in the checklist. Never send partial control edits or an unfinished security analysis. Reuse the live Claude/GPT loop, but apply this skill's stricter stop rules: models cannot accept material risk for the human.

Do not create raw findings artifacts. Record only durable security requirements in canonical design/task docs and lasting accepted risks in the repository's decision mechanism when appropriate.

## Gate Result

Return one of:

- `ready`: controls and verification are represented in the plan;
- `ready_with_human_accepted_risk`: the human explicitly accepted named residual risk and the decision is durably recorded;
- `changes_required`: correctable design/task gaps remain;
- `blocked`: critical risk or missing human decision prevents publication.

List the exact documents/tasks changed and any human decision still required. Do not file or update Linear tasks as part of this skill.
