# Wasted Skills

Portable custom skills maintained as a standalone repository.

Small, portable, and of highly questionable value.

These skills will not make anyone smarter, more talented, more employable, or more deserving of imaginary skill credits. They are mostly here to be used, copied, updated, and mildly regretted.

## What This Repo Is

This repository is the source of truth for custom Codex, Claude Code, and Kimi Code skills that should remain platform-native instead of sharing one conditional cross-platform entrypoint.

Every logical skill owns separate native distributions:

```text
<skill-name>/
├── Codex/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── optional references, scripts, and assets
├── Claude/
│   └── Claude-native skill files
└── Kimi/
    └── Kimi Code-native skill files
```

`Codex/`, `Claude/`, and `Kimi/` may preserve the same product workflow, but each entrypoint should use the target host's native syntax, invocation model, metadata, tools, and provider adapters. Do not turn any version into a lowest-common-denominator skill full of host conditionals.

## Included Skills

| Skill | Purpose | Codex | Claude Code | Kimi Code |
| --- | --- | :---: | :---: | :---: |
| `feature-design` | Guides product discovery and produces a human-approved PRD. | Yes | Yes | Yes |
| `implementation-design` | Produces the smallest shared technical design justified by an approved PRD, or records that no separate design is needed. | Yes | Yes | Yes |
| `feature-delivery-plan` | Converts approved product and technical decisions into vertical tasks, dependencies, validation, and tracker-ready drafts. | Yes | Yes | Yes |
| `cross-model-review` | Runs a live review-and-recheck loop with the other model family while keeping findings ephemeral. | Yes | Yes | Yes |
| `feature-security-review` | Performs the human-gated security readiness check before task publication. | Yes | Yes | Yes |
| `feature-context-handoff` | Preserves the minimal state of unfinished feature work across fresh sessions. | Yes | Yes | Yes |
| `project-docs-organizer` | Bootstraps or substantially reorganizes project documentation, source-of-truth boundaries, and repository structure. | Yes | Not yet | Yes |

The five feature-preparation skills are available as separate native packages for all three platforms, and all three revisions now share the same complete-draft readiness and context-handoff behavior. Kimi remains an asymmetric integration: its authoring session may use Claude as reviewer, but Codex and Claude do not use Kimi as a reviewer, and Kimi does not need to mirror their host mechanics or reviewer-failure policy exactly. `feature-context-handoff` ships for all three platforms, while `project-docs-organizer` ships for Codex and Kimi; the remaining `Claude/` directories are placeholders rather than installable skills.

## Feature Preparation Suite

Use the suite as one staged sequence:

1. `feature-design` runs the guided product conversation and stops at an approved PRD.
2. `cross-model-review` challenges the complete review-ready PRD with one resumable, read-only cross-family reviewer session before human approval.
3. `implementation-design` decides whether a separate technical design is justified and, when needed, produces and cross-reviews it.
4. `feature-delivery-plan` creates the vertical task graph, dependencies, routing, validation profiles, branch targets, and parent acceptance from approved inputs, then cross-reviews the plan.
5. `feature-security-review` performs the final human-gated security check before the approved task set is filed in Linear or another tracker.

Use `feature-context-handoff` only when one of these phases stops incomplete or intentionally moves to a fresh session. It writes a short-lived `WORK-HANDOFF.md` inside the feature folder, points to canonical documents and the exact next action, and removes the file once canonical state makes continuation obvious. It does not duplicate PRDs, retain model transcripts, monitor context automatically, or install hooks/plugins.

The suite keeps only accepted documents as durable project truth. Raw model findings and review transcripts remain ephemeral. The live completion summary still lists every finding individually with its original severity, concise meaning, and final disposition; a count-only summary is not sufficient.

### How The Codex Versions Work

1. Invoke `feature-design` while discussing a feature. It reads canonical context, summarizes what the human already explained, asks adaptive high-value questions, classifies the work provisionally, and drafts only the PRD.
2. Invoke `cross-model-review` only when a complete, self-contained PRD, implementation design, or task plan is in review-ready `draft`/`proposed` state. The current GPT/Codex session remains the author; a real minimal CLI probe verifies Claude/model access, one read-only Claude session reviews the full draft, GPT checks and prepares corrections, and the same Claude session rechecks the complete corrected draft. The Codex distribution explicitly uses `claude-opus-4-8` with `xhigh` effort for probe, start, and resume instead of inheriting the interactive Claude CLI default. Provider calls are polled at roughly 60-second intervals and are never retried automatically. All remaining material and minor differences return to the human before one final patch is applied. The final live summary lists every finding, including corrected and rejected findings, rather than reporting only aggregate counts.
3. Invoke `implementation-design` only after PRD approval. It either produces the smallest shared technical contract and cross-reviews it, or explicitly records that one task can safely carry its own implementation notes.
4. Invoke `feature-delivery-plan` after product and technical approval. It creates the minimal vertical delivery graph without changing upstream scope or architecture.
5. Invoke `feature-security-review` after decomposition and before tracker publication. It treats accepted PRD/design artifacts as immutable context, adds confirmed controls to proposed task contracts, reopens upstream documents only through their owning phase, and blocks publication when critical risk or a required human risk decision remains.

### How The Claude Versions Work

The Claude distributions preserve the same staged workflow, with the cross-family review direction mirrored: Claude is the author and editor, and GPT is the read-only reviewer. They now match the Codex complete-draft readiness and context-handoff revision.

1. Invoke `feature-design` while discussing a feature. It reads canonical context, summarizes what the human already explained, asks adaptive high-value questions, classifies the work provisionally, and drafts only the PRD.
2. Invoke `cross-model-review` only when a complete, self-contained PRD, implementation design, or task plan is in review-ready `draft`/`proposed` state. The current Claude session remains the author and sole editor; a real minimal CLI probe verifies `codex` login and model access, one read-only GPT reviewer session — driven through the local `codex exec` CLI under a read-only sandbox — reviews the full draft, Claude verifies findings and prepares corrections, and the same resumable GPT session rechecks the complete corrected draft. The Claude distribution pins `gpt-5.6-sol` at `high` reasoning effort for probe, start, and resume via `scripts/gpt_review.py`. Provider calls are polled at roughly 60-second intervals and are never retried automatically. All remaining material and minor differences return to the human before one final patch is applied. The final live summary lists every finding, including corrected and rejected findings, rather than reporting only aggregate counts.
3. Invoke `implementation-design` only after PRD approval. It either produces the smallest shared technical contract and cross-reviews it, or explicitly records that one task can safely carry its own implementation notes.
4. Invoke `feature-delivery-plan` after product and technical approval. It creates the minimal vertical delivery graph without changing upstream scope or architecture.
5. Invoke `feature-security-review` after decomposition and before tracker publication. It treats accepted PRD/design artifacts as immutable context, adds confirmed controls to proposed task contracts, reopens upstream documents only through their owning phase, and blocks publication when critical risk or a required human risk decision remains.

### How The Kimi Versions Work

The Kimi distributions use their own asymmetric staged workflow: the current Kimi session is the author and editor, and Claude is its read-only reviewer. Kimi is not a reviewer provider for the Codex or Claude flows and is not required to mirror their reviewer mechanics exactly.

1. Invoke `feature-design` while discussing a feature. It reads canonical context, summarizes what the human already explained, asks adaptive high-value questions, classifies the work provisionally, and drafts only the PRD.
2. Invoke `cross-model-review` only when a complete, self-contained PRD, implementation design, or task plan is in review-ready `draft`/`proposed` state. The current Kimi session remains the author and sole editor; a real minimal CLI probe verifies Claude/model access, one read-only Claude session reviews the full draft, Kimi verifies findings and prepares corrections, and the same resumable Claude session rechecks the complete corrected draft. The Kimi distribution pins `claude-opus-4-8` at `xhigh` effort for probe, start, and resume via `scripts/claude_review.py`. Provider calls are polled at roughly 60-second intervals and are never retried automatically. All remaining material and minor differences return to the human before one final patch is applied. The final live summary lists every finding, including corrected and rejected findings, rather than reporting only aggregate counts.
3. Invoke `implementation-design` only after PRD approval. It either produces the smallest shared technical contract and cross-reviews it, or explicitly records that one task can safely carry its own implementation notes.
4. Invoke `feature-delivery-plan` after product and technical approval. It creates the minimal vertical delivery graph without changing upstream scope or architecture.
5. Invoke `feature-security-review` after decomposition and before tracker publication. It treats accepted PRD/design artifacts as immutable context, adds confirmed controls to proposed task contracts, reopens upstream documents only through their owning phase, and blocks publication when critical risk or a required human risk decision remains.

### PRD Output Format

`feature-design` outputs a canonical Markdown draft in the target project's existing feature-document structure. It is not JSON, a model transcript, or a separate review report.

```markdown
# Feature name and version

## Business outcome
## Users and scenarios
## Current behavior
## Desired behavior
## Scope
## Non-goals
## Constraints and accepted assumptions
## Acceptance criteria
## Current version / MVP
## Architecture horizon
## Deferred candidate work
## Open human decisions
```

For a large feature, later stages may additionally produce a justified shared `implementation.md` and a vertical parent/child task plan. For a small feature, implementation notes stay in its single task contract. Cross-model findings remain live and ephemeral; only human-approved final documentation is durable.

## Project Docs Organizer

Use `project-docs-organizer` for an initial bootstrap, one-time migration, or major structural cleanup, not routine project maintenance.

It reviews existing docs and git boundaries, chooses the smallest safe organization mode, requests explicit approval before mutation, creates the approved preflight backup, and applies the bundled canonical playbook without replacing stronger project-specific documentation.

## Development And Installation

### Portability And Runtime Requirements

The repository contains no bundled credentials, account identifiers, fixed reviewer sessions, or workstation-specific home paths. Skill packages use relative paths, caller-provided project paths, and standard user-level installation locations.

Most skills require only their native host. Cross-family review additionally requires a locally installed and authenticated reviewer CLI:

- Codex `cross-model-review` invokes the `claude` CLI and defaults to `claude-opus-4-8` with `xhigh` effort. The user running it must have access to that model, or explicitly select another supported reviewer model and effort.
- Kimi `cross-model-review` invokes the `claude` CLI with the same `claude-opus-4-8` / `xhigh` defaults as the Codex distribution. The user running it must have access to that model, or explicitly select another supported reviewer model and effort.
- Claude `cross-model-review` invokes the `codex` CLI and defaults to `gpt-5.6-sol` with `high` reasoning effort. The user running it must have access to that model (or explicitly select another supported reviewer model and effort) and authenticate that CLI separately.

Authentication remains local to each CLI and must never be committed to this repository. `CLAUDE_BIN` and `CODEX_BIN` may point to non-default executable locations without modifying a skill.

1. Edit the matching platform source under `<skill-name>/Codex/`, `<skill-name>/Claude/`, or `<skill-name>/Kimi/`.
2. Validate the native package before installation.
3. Sync Codex from `<skill-name>/Codex/` into `~/.codex/skills/<skill-name>/`.
4. Sync Claude from `<skill-name>/Claude/` into `~/.claude/skills/<skill-name>/` after Claude creates and validates that native version.
5. Sync Kimi from `<skill-name>/Kimi/` into `${KIMI_CODE_HOME:-$HOME/.kimi-code}/skills/<skill-name>/`.
6. Treat installed copies as runtime mirrors, never as the editable source of truth.

Codex validation and synchronization for one skill:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "<skill-name>/Codex"
rsync -a --delete "<skill-name>/Codex/" "$HOME/.codex/skills/<skill-name>/"
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$HOME/.codex/skills/<skill-name>"
diff -qr "<skill-name>/Codex" "$HOME/.codex/skills/<skill-name>"
```

Claude synchronization after Claude has created and validated the native package:

```bash
rsync -a --delete "<skill-name>/Claude/" "$HOME/.claude/skills/<skill-name>/"
```

Kimi synchronization after the native package is validated:

```bash
rsync -a --delete "<skill-name>/Kimi/" "${KIMI_CODE_HOME:-$HOME/.kimi-code}/skills/<skill-name>/"
```

Portable copies may be shared as archives, but this git repository remains the primary source for future updates.

## Development Notes

- Keep platform entrypoints and adapters native.
- Keep paired product semantics aligned deliberately when both platforms implement the same workflow.
- Keep references, scripts, and templates inside the platform distribution that uses them.
- Validate before syncing.
- Sync installed copies only after the repository versions are correct.
