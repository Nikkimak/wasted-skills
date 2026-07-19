# Feature delivery plan contract

## Delivery shapes

| Shape | Use when | Merge behavior |
| --- | --- | --- |
| `small_feature` | One bounded end-to-end capability fits one task | Human approval, then direct merge to `main` |
| `large_feature` | Several substantial increments share one business acceptance | Children integrate into one feature branch; parent owns final merge |
| `fix` | Restore accepted behavior | Active remediation or one small standalone task |

## Vertical slice

```markdown
## Slice: Observable behavior

Business Outcome:
End-to-End Path:
Included:
Deferred:
Integration Risk Closed:
Verification:
Dependencies:
Required Human Inputs:
Execution Profile:
Validation Profile:
Merge Target:
```

Each slice must reach an observable result through the required layers. Component-only tasks need concrete justification.

## Executable task

```markdown
## Parent Feature
## Objective
## Business Outcome
## Scope
## Vertical Slice
## Acceptance Criteria
## Required Context
## Implementation Notes
## Validation Plan
## Dependencies
## Required Human Inputs
## Execution Profile
## Validation Profile
## Merge Target
## Commitment
```

Use `committed` for current-version acceptance and `deferred` for visible later work.

## Local checks

- Map every committed PRD acceptance criterion to task scope and parent acceptance.
- Map every implementation invariant, `SEC-*` control, and `VER-*` obligation applicable to this delivery delta to an owning task and executable evidence; do not taskify unchanged baseline controls.
- Reject behavior absent from accepted upstream documents.
- Require complete, directional, acyclic dependencies and minimal bounded task count.
- Require proportional validation, explicit merge targets, and combined parent acceptance.
- Require each `HIN-*` dependency to name its consuming task and gate.
- Do not defer an input or control required to make current-version execution safe.

## Approval and status

The plan and tasks remain `proposed` until local checks, execution readiness, and explicit human approval complete. Do not offer routine cross-model or separate post-plan security review; run task-plan cross-model review only when the human explicitly requests it. A newly discovered product gap returns to the `feature-design` skill; a shared technical or security gap returns to the `implementation-design` skill and reopens only the affected accepted contract.
