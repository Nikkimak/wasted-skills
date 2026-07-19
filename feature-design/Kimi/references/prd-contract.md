# PRD contract

## Conversation outcome

The PRD should let a reader understand why the feature exists, what observable result the current version must deliver, and what remains deliberately outside it without needing the authoring chat.

## Semantic structure

Adapt headings to the target repository, but preserve this meaning:

```markdown
# Feature name and version

## Business outcome
## Users and scenarios
## Current behavior
## Desired behavior
## Scope
## Non-goals
## Constraints and accepted assumptions
## Known human-supplied inputs and external dependencies
## Acceptance criteria
## Current version / MVP
## Architecture horizon
## Deferred candidate work
## Open human decisions
```

## Content rules

- `Business outcome` explains value, not implementation.
- `Users and scenarios` names actors and concrete journeys.
- `Current behavior` states verified present reality.
- `Desired behavior` states observable changes.
- `Scope` is the committed authority boundary for the current version.
- `Non-goals` prevents adjacent expansion.
- `Constraints and accepted assumptions` separates known limits from guesses.
- `Known human-supplied inputs and external dependencies` records only dependencies already known to product discovery; omit the section when none exist and defer technical format, storage, and timing to later phases.
- `Acceptance criteria` is externally verifiable and includes meaningful failure behavior.
- `Current version / MVP` is a delivery commitment.
- `Architecture horizon` constrains future technical design but is not current implementation scope.
- `Deferred candidate work` remains visible without becoming current commitment.
- `Open human decisions` is explicit; do not let an LLM silently decide them.

## Classification

| Kind | Product meaning |
| --- | --- |
| `large_feature` | One business result is likely to require several substantial delivery increments |
| `small_feature` | One bounded end-to-end capability can likely be delivered as one task |
| `fix` | Restore already-accepted behavior rather than introduce a new capability |

Classification is provisional until technical design and delivery planning confirm the shape. Do not decompose tasks during PRD authoring.

## Lightweight triage

- Return `prd_not_applicable` when a correction changes no observable product behavior or accepted requirement. This is not feature/fix classification and creates no PRD artifact or approval gate.
- Return `prd_change_not_required` for a `fix` only when a canonical accepted artifact or decision establishes the exact intended behavior being restored. Cite that evidence; current code or reported behavior alone does not establish product intent.
- If the evidence does not show whether the request restores accepted behavior or changes product meaning, ask the human one focused question instead of defaulting to a full PRD.
- A confirmed change to observable behavior, scope, acceptance, or failure behavior requires PRD work. When revising an accepted PRD, preserve its baseline and change only the affected product meaning.
- Neither no-PRD outcome is eligible for PRD cross-model review or PRD approval. Report downstream impact and route to the lightest valid next workflow.

## Review readiness

The PRD is eligible for cross-model review only as one complete, self-contained `draft` or `proposed` artifact. Every required section must be substantive, placeholders and TODOs must be removed, current scope must be separated from horizon, and every known unresolved product decision must be explicitly listed. Discovery notes, question lists, outlines, and partial drafts are not review inputs. Cross-model review is optional and requires explicit human approval after the complete PRD is presented; acceptance always requires explicit human approval whether review is performed or declined.
