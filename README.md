# Wasted Skills

Portable custom Codex skills maintained as a standalone repository.

## Included Skills

- `apply-project-playbook` — applies the bundled project structure and documentation playbook to a new or existing coding project

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
