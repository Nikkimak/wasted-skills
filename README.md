# Wasted Skills

Portable custom Codex skills maintained as a standalone repository.

Small, portable, and of highly questionable value.

These skills will not make anyone smarter, more talented, more employable, or more deserving of imaginary skill credits. They are mostly here to be used, copied, updated, and mildly regretted.

## Included Skills

- `unfuck-project-docs` — organizes project documentation, workspace structure, and repo boundaries using the bundled canonical playbook as guidance

### `unfuck-project-docs`

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

## Repository Purpose

This repository is the publishable container for custom skills.

Each skill should remain self-contained:

- `SKILL.md` defines when and how the skill is used
- `references/` holds bundled normative or supporting material the skill may need to read
- `assets/` holds reusable templates or output resources
- `agents/openai.yaml` provides UI metadata

## Update Model

This repo is intended to be the canonical sync point for distributed copies of these skills.

Portable copies may be shared as zip archives, but the git repo should remain the primary source for future updates.
