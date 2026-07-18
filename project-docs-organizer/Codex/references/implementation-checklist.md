# Implementation Checklist

Use this after discovery and explicit approval. The approved fields in `SKILL.md` define execution scope.

## Preflight

- Reconfirm target root, mode, repo model, runtime git paths, documentation strategy, planned changes, and risks.
- Verify that topology and file mutations were explicitly approved.
- Create the approved scoped backup and manifest before the first mutation, or record the human's explicit decline.
- If scope has changed materially, stop, obtain new approval, and back up the newly affected targets.

## Apply

- Apply repo-boundary changes only as approved and verify ownership using `git-topology-checklist.md`.
- Create or update only the documents required by `canonical-docs-matrix.md` and project evidence.
- Update or split strong existing docs instead of creating parallel truth.
- Adapt templates under `templates-policy.md`; remove placeholders and preserve project-specific content.
- Keep unrelated work intact and keep `.playbook-backups/` outside canonical project changes.

## Verify

- The chosen git model is documented in project `AGENTS.md` and `context/current/repo-map.md`.
- Every relevant path has one git owner and every deploy-triggering surface has an explicit owner.
- The source-of-truth hierarchy is singular: `WORKPLAN.md` owns the queue, `context/current/` owns live state, `context/decisions/` owns accepted decisions, and task packets stay outside `context/`.
- Required docs for the selected mode exist or stronger equivalents are explicitly verified.
- `context/README.md` is an entrypoint, not a second wiki; at most one future-work area exists.
- `src/README.md` exists and `src/` is self-sufficient for narrow work without duplicating parent truth.
- No stale document masquerades as live truth and no unnecessary ceremonial structure was added.

## Close

- Report the chosen mode, repo model, documentation strategy, and backup result.
- List created, updated, and verified files, intentional omissions, remaining risks, and unresolved human decisions.
