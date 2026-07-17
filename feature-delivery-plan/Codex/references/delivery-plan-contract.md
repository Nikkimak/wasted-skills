# Feature delivery plan contract

## Delivery shapes

| Shape | Use when | Merge behavior |
| --- | --- | --- |
| `small_feature` | One bounded end-to-end capability fits one task | Task review, then direct merge to `main` |
| `large_feature` | Several substantial increments share one business acceptance | Children integrate into one feature branch; parent owns final merge |
| `fix` | Restore accepted behavior | Active issue remediation or one small standalone task |

## Vertical slice contract

```markdown
## Slice: Observable behavior

Business Outcome:
End-to-End Path:
Included:
Deferred:
Integration Risk Closed:
Verification:
Dependencies:
Execution Profile:
Validation Profile:
Merge Target:
```

A valid slice reaches an observable result through all required layers. A task named only after a component (`database`, `API`, `frontend`) needs a concrete justification or redesign.

## Executable task contract

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
## Execution Profile
## Validation Profile
## Merge Target
## Commitment
```

Use `committed` for current-version acceptance and `deferred` for visible planned work that does not yet block current acceptance.

## Graph checks

- Every committed PRD acceptance criterion maps to executable scope and final acceptance.
- No task adds behavior absent from accepted PRD/implementation design.
- Dependencies are complete, directional, acyclic, and not used as hidden prose.
- Task count is minimal without making sessions/worktrees unsafe or unbounded.
- Execution routing follows work surface; UI-heavy bounded full-stack work may go entirely to Claude.
- Validation depth is proportional: `quick`, `slice_light`, `slice_standard`, or `feature_acceptance` as project policy defines.
- Parent/child ownership and merge targets are explicit.
- Deferred tasks stay visible after publication and receive an explicit later disposition.

## Parent acceptance

Children integrate into the feature branch and wait in review. The parent tests the exact combined feature SHA, receives whole-feature human review, batches small findings into parent remediation, and owns the only merge to `main`.

## Review readiness

Cross-model review begins only when the delivery plan and all task contracts form one complete, self-contained `draft` or `proposed` graph. Every committed acceptance criterion must be mapped, required fields must be substantive, placeholders and TODOs must be removed, and every known unresolved human decision must be explicit. Partial task lists and in-progress decomposition are not review inputs.

## Status lifecycle

Human approval after delivery-plan review establishes the planning baseline but does not finalize or publish task contracts. Keep them `proposed` through `$feature-security-review`; after the final security posture and amended task set receive human approval, move them to the target repository's approved/accepted status. Accepted PRD and implementation artifacts remain immutable upstream context. If security work requires a product or shared-architecture change, return to the owning authoring skill, create a proposed revision, and re-obtain the corresponding approval before the security gate can return `ready`.
