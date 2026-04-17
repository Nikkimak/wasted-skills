# Mode Selection

Use this rubric before materializing the playbook.

## `minimal`

Choose `minimal` when most of these are true:

- the project is early-stage
- there is one runtime repo
- there are one or two runtime surfaces at most
- deploy/ops complexity is low
- contributor count is low
- future-work tracking does not need a dedicated area yet

Typical required outputs:

- `AGENTS.md`
- `WORKPLAN.md`
- `context/current/project-state.md`
- `context/current/runtime-map.md`
- `context/current/repo-map.md`
- `context/decisions/README.md`
- `src/README.md`

## `standard`

Choose `standard` when some of these are true:

- the project is already deployed or close to deployment
- there are multiple services, packages, or runtime boundaries
- there is meaningful rollout or ops complexity
- ownership boundaries need to be explicit
- agents or multiple contributors will touch the project repeatedly

Typical additions on top of `minimal`:

- `context/runbooks/deploy.md`
- `context/components/*`
- a chosen future-work area if active design work needs it

## `full`

Choose `full` when some of these are true:

- the system is multi-service or multi-repo
- rollout complexity is high
- multiple teams or agents coordinate through persistent task packets
- feature or initiative work needs a persistent future-work area
- richer metadata is worth maintaining

Typical additions on top of `standard`:

- explicit task layer
- richer runbooks
- fuller component guides
- chosen future-work area with durable status docs

## Decision Rule

Prefer the smallest mode that preserves:

- clear startup path
- unambiguous source of truth
- safe runtime editing boundaries
- adequate runtime self-sufficiency

Do not choose a larger mode only because the full playbook allows it.
