# Execution readiness contract

Create one feature-local `EXECUTION-READINESS.md` only when execution depends on a human or external party. It is the status source for prerequisites; tasks reference its IDs instead of duplicating status.

## Dependency types

- `test_asset`, `dataset`, `access`, `credential`, `environment`;
- `budget_authorization`, `external_approval`, `human_decision`, `human_validation`.

## Item contract

```markdown
## HIN-01 — Short name

Type:
Status: needed | requested | provided | verified | waived | expired
Blocking mode: upfront_blocker | stage_blocker | optional_quality | production_gate
Required by: task and gate
Needed timing: now | later
Provided by:

What is needed:
Why it is needed:
Safe delivery or storage location:
Format, quality, and least-privilege constraints:
Verification:
What may proceed without it:
What must stop without it:
Expiry, rotation, or cleanup when relevant:
```

Never record credentials, secret values, sensitive payloads, fixed authenticated sessions, or unnecessary personal data. Record only the approved secret/data location and verification state.

## Readiness behavior

- Surface all known dependencies before autonomous execution, but collect expiring credentials and production access just in time.
- Group the human summary into `needed now` and `needed later` with the exact task/gate each item blocks.
- Require each consuming task to check its referenced `HIN-*` status before crossing the gate and request a scheduled later input when its lead time begins, not only after work is blocked.
- Verify provided inputs; do not treat presence as suitability.
- Update the manifest when an item is requested, provided, verified, waived, or expired.
- Do not fabricate missing real data or silently replace it with synthetic fixtures.
- Stop only the blocked branch when independent tasks may safely continue.
- Return `ready`, `ready_with_scheduled_inputs`, `ready_with_reduced_scope`, or `blocked`.
