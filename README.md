# Wasted Skills

Portable custom Codex skills maintained as a standalone repository.

Small, portable, and of highly questionable value.

These skills will not make anyone smarter, more talented, more employable, or more deserving of imaginary skill credits. They are mostly here to be used, copied, updated, and mildly regretted.

## What This Repo Is

This repository is the source of truth for custom Codex skills that we want to keep portable, reusable, and easy to install into a local Codex setup.

Each skill is self-contained and ships with:

- `SKILL.md` for behavior and usage rules
- `references/` for bundled guidance or canonical support material
- `assets/` for reusable templates and helper resources
- `agents/openai.yaml` for UI metadata

The goal is simple: keep the skills here clean, versioned, and easy to sync into `~/.codex/skills`.

## Included Skills

- `project-docs-organizer` — organizes project documentation, workspace structure, and repo boundaries using the bundled canonical playbook as guidance

### `project-docs-organizer`

Use this skill when a project needs one serious cleanup pass, not routine maintenance.

What it does:

- reviews the current project structure, docs, and repo boundaries
- decides whether the project actually needs migration or structural cleanup
- proposes a minimal plan before changing anything
- asks for explicit approval before edits or git-boundary changes
- creates a safety backup before the first approved mutation
- reorganizes canonical docs and workspace structure around a clearer source-of-truth model

What to expect:

- it is best for initial setup, one-time migration, or major documentation cleanup
- it is intentionally conservative and should stay in discovery until approval is given
- it is not meant to be the default skill for normal day-to-day feature work

In practice, this skill is useful when a project has:

- mixed current-state docs, decisions, and future plans in the same files
- unclear git boundaries, especially when runtime isolation is requested or already exists
- missing canonical entrypoints such as `WORKPLAN.md`, `context/README.md`, or `src/README.md`
- large, messy documentation that needs one careful restructuring pass

## How To Use

Typical workflow:

1. Update or develop the skill in this repository.
2. Validate the skill locally.
3. Sync it into `~/.codex/skills/`.
4. Restart Codex if needed so the updated installed copy is picked up.

This repository should remain the editable source of truth.
The installed copy in `~/.codex/skills` should be treated as a runtime mirror.

## Repository Purpose

This repository is the publishable container for custom skills.

It is meant to solve two practical problems:

- keep local skills versioned and reviewable
- make it easy to ship or reuse the same skill set across machines and projects

## Update Model

This repo is intended to be the canonical sync point for distributed copies of these skills.

Portable copies may be shared as zip archives, but the git repo should remain the primary source for future updates.

## Development Notes

- Edit skills here first.
- Keep references and templates aligned when the contract changes.
- Validate before syncing.
- Sync the installed copy only after the repo version looks correct.
