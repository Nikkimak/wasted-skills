# CLAUDE.md

<!-- Use the project's existing router filename. `CLAUDE.md` is the Claude Code
     default; `AGENTS.md` or another established equivalent is equally valid. -->

## Scope

Short operating router for this project. Link to detailed authority; do not copy
it here.

## Project Shape

- primary surface: `<documents or runtime>`
- shape: `documentation_primary | single_runtime | modular_runtime | multiple_runtime_surfaces`
- repo model: `<detected model>`
- runtime/deploy owners: `<paths or n/a>`

## Route By Intent

- known-owner code change → nearest runtime/ownership README, code, tests
- unknown owner → path/lexical/symbol search, then top ownership candidates
- product meaning → `<product contract or n/a>`
- rationale/invariants → `<decisions or n/a>`
- deployed state → `<runtime/deploy evidence or n/a>`
- operations → `<runbooks or n/a>`
- active work → `<queue or n/a>`
- document lookup → `<short index or search guidance>`

Open only the route required by the task.

## Authority

- code and executable tests own current implementation behavior
- verified runtime/deploy evidence owns deployed state
- accepted product contracts own intended outcomes
- accepted non-superseded decisions own rationale and invariants
- runbooks own procedures; future-work docs are not current truth
- indexes route to facts and do not replace them

Name `working_tree`, `accepted_ref`, or `deployed` when state matters.

## Runtime Rules

<!-- Remove when runtime is not applicable. -->

- runtime entrypoint and ownership docs: `<paths>`
- place code by domain owner and behavioral role
- review responsibility around 300–500 lines; require decomposition review
  above 500 lines while allowing cohesive exceptions
- do not create microservices without a concrete runtime or ownership reason
- integrations and shared helpers do not own hidden business rules

## Update And Safety Rules

- update only the authority whose durable meaning changed
- internal edits that preserve product, ownership, deployment, and procedure do
  not require ceremonial documentation churn
- analysis does not authorize mutation; code-bearing does not authorize
  restructuring
- git, commit, push, deploy, secrets, destructive actions, and retrieval
  infrastructure require their own applicable authorization
- preserve unrelated work and follow the nearest repository instructions
