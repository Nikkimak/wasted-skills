# Canonical Docs Matrix

Use this matrix to decide which files are required.

## Always Required

- project-level `AGENTS.md`
- `WORKPLAN.md`
- `context/README.md`
- `context/current/project-state.md`
- `context/current/runtime-map.md`
- `context/current/repo-map.md`
- `context/decisions/README.md`
- `src/README.md`

## Required In `standard` And Above

- `context/runbooks/deploy.md` when the project has a real deploy surface or operational procedure worth preserving
- `context/components/` guides where ownership would otherwise be unclear

## Required Only If The Project Needs Them

- chosen future-work area
- task layer
- richer metadata discipline
- domain notes
- broader runbooks

## Decision Rule

Do not create documents merely because the full playbook mentions them.
Create only the smallest set that preserves clarity for the actual project.
