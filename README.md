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
| `implementation-design` | Produces the smallest shared technical and security design justified by an approved PRD, or records that no separate design is needed. | Yes | Yes | Yes |
| `feature-delivery-plan` | Converts approved decisions into vertical tasks, execution readiness, dependencies, validation, and tracker-ready drafts. | Yes | Yes | Yes |
| `cross-model-review` | Runs a live review-and-recheck loop with the other model family while keeping findings ephemeral. | Yes | Yes | Yes |
| `feature-security-review` | Deepens exceptional high-risk implementation designs without authorizing cross-model review. | Yes | Yes | Yes |
| `feature-context-handoff` | Preserves the minimal state of unfinished feature work across fresh sessions. | Yes | Yes | Yes |
| `project-docs-organizer` | Bootstraps or substantially reorganizes project documentation, source-of-truth boundaries, and repository structure. | Yes | Not yet | Yes |

The feature-preparation skills are available as separate native packages. All three distributions use the same human-controlled review workflow: security is embedded in implementation design, exceptional deep security analysis enriches that same draft, and no cross-model review runs without explicit human approval. Their host mechanics remain native: Codex and Kimi use Claude as reviewer, Claude uses GPT/Codex, and Kimi is not a reviewer provider for the other flows. `feature-context-handoff` ships for all three platforms, while `project-docs-organizer` ships for Codex and Kimi.

## Feature Preparation Suite

The shared sequence is:

1. `feature-design` produces or revises a complete PRD, recommends for or against cross-model review, and asks the human before invoking it. The PRD always requires explicit human approval, including when review is declined.
2. `implementation-design` first decides whether shared technical/security meaning changes and whether a document is justified. Review and controls cover the material delta, reference unchanged baselines, and never require prose for unaffected sections. Only a delta that introduces or materially changes a high-impact boundary may invoke `feature-security-review`; its result stays in the implementation design, and cross-model review remains separately optional.
3. `feature-delivery-plan` derives the vertical task graph, maps product criteria plus `SEC-*`/`VER-*` obligations, and creates a feature-local `EXECUTION-READINESS.md` only when human or external inputs exist. It uses local deterministic checks and human approval. It neither runs nor routinely offers cross-model task-plan review; the human must request that review directly.
4. Tracker publication remains a later explicit action.

Changes to an accepted feature return to the authoring skill that owns the affected artifact. `feature-design` owns PRD changes, `implementation-design` owns technical/security design changes, and `feature-delivery-plan` owns task/readiness changes. Each preserves the accepted baseline and reports downstream impact. PRD and implementation skills ask separately before any cross-model review; complex, broad, or risky changes should receive a recommendation to review, but the human may approve or decline it. Delivery planning never offers review routinely and uses it only when the human requests it.

Use `feature-context-handoff` only when one of these phases stops incomplete or intentionally moves to a fresh session. It writes a short-lived `WORK-HANDOFF.md` inside the feature folder, points to canonical documents and the exact next action, and removes the file once canonical state makes continuation obvious. It does not duplicate PRDs, retain model transcripts, monitor context automatically, or install hooks/plugins.

The suite keeps only accepted documents as durable project truth. Raw model findings and review transcripts remain ephemeral. The live completion summary still lists every finding individually with its original severity, concise meaning, and final disposition; a count-only summary is not sufficient.

### How The Codex Versions Work

1. Invoke `feature-design` while discussing or revising a feature or deciding whether a requested correction changes product meaning. The Codex version returns `prd_not_applicable` for non-product corrections and `prd_change_not_required` for fixes that restore canonically accepted behavior; when the distinction is unclear, it asks one focused human question rather than defaulting to a full PRD. Only actual product changes enter PRD drafting, review choice, and PRD approval.
2. When approved for a complete PRD or implementation design, `cross-model-review` keeps the current GPT/Codex session as author while one read-only Claude session reviews the full draft and rechecks the corrected document. Task-plan review runs only when the human directly requests it. Provider calls are polled at roughly 60-second intervals and never retried automatically.
3. Invoke `implementation-design` only after PRD approval. The Codex version may return `implementation_change_not_required` when an accepted technical/security baseline remains valid, or `implementation_doc_not_required` when one task can own the notes. Otherwise it documents only changed shared meaning, classifies security from the material delta, and invokes `feature-security-review` only when that delta introduces or materially changes a high-impact boundary. Existing payment, identity, sensitive-data, privilege, isolation, or destructive functionality alone does not trigger deep review.
4. Invoke `feature-delivery-plan` after product and technical/security approval. It creates the minimal vertical delivery graph, conditionally creates `EXECUTION-READINESS.md`, runs local checks, and obtains human approval without offering routine Claude review.
5. Publish approved tracker drafts only through the project's bounded intake path on a later explicit action.

### How The Claude Versions Work

The Claude distribution preserves the shared streamlined workflow with the review direction mirrored: Claude is author/editor and GPT/Codex is the read-only reviewer.

1. Invoke `feature-design` while discussing or revising a feature or deciding whether a requested correction changes product meaning. It returns `prd_not_applicable` for non-product corrections and `prd_change_not_required` for fixes that restore canonically accepted behavior; when the distinction is unclear, it asks one focused human question rather than defaulting to a full PRD. Only actual product changes enter PRD drafting, review choice, and PRD approval.
2. When approved for a complete PRD or implementation design, `cross-model-review` keeps the current Claude session as sole editor while `${CLAUDE_SKILL_DIR}/scripts/gpt_review.py` drives one resumable GPT/Codex reviewer under a read-only sandbox for initial review and one corrected-document recheck. Task-plan review runs only when the human directly requests it.
3. Invoke `implementation-design` after PRD approval. It may return `implementation_change_not_required` when an accepted technical/security baseline remains valid, or `implementation_doc_not_required` when one task can own the notes. Otherwise it documents only changed shared meaning, classifies security from the material delta, and invokes `feature-security-review` only when that delta introduces or materially changes a high-impact boundary. Existing payment, identity, sensitive-data, privilege, isolation, or destructive functionality alone does not trigger deep review.
4. Invoke `feature-delivery-plan` after technical/security approval. It maps only the obligations applicable to the delivery delta, conditionally creates `EXECUTION-READINESS.md`, runs local checks, and obtains human approval without offering routine GPT review.
5. Publish approved tracker drafts only through the project's bounded intake path on a later explicit action.

### How The Kimi Versions Work

The Kimi distributions use their own asymmetric staged workflow: the current Kimi session is the author and editor, and Claude is its read-only reviewer. Kimi is not a reviewer provider for the Codex or Claude flows and is not required to mirror their reviewer mechanics exactly.

1. Invoke `feature-design` while discussing or revising a feature or deciding whether a requested correction changes product meaning. It returns `prd_not_applicable` for non-product corrections and `prd_change_not_required` for fixes that restore canonically accepted behavior; when the distinction is unclear, it asks one focused human question rather than defaulting to a full PRD. Only actual product changes enter PRD drafting, review choice, and PRD approval.
2. When approved for a complete PRD or implementation design, `cross-model-review` keeps the current Kimi session as author and sole editor while one resumable read-only Claude session reviews and rechecks the corrected draft. Task-plan review runs only when the human directly requests it. The Kimi distribution pins `claude-opus-4-8` at `xhigh` effort and never retries provider failures automatically.
3. Invoke `implementation-design` only after PRD approval. It may return `implementation_change_not_required` when an accepted technical/security baseline remains valid, or `implementation_doc_not_required` when one task can own the notes. Otherwise it documents only changed shared meaning, classifies security from the material delta, and invokes `feature-security-review` only when that delta introduces or materially changes a high-impact boundary. Existing payment, identity, sensitive-data, privilege, isolation, or destructive functionality alone does not trigger deep review.
4. Invoke `feature-delivery-plan` after product and technical/security approval. It creates the minimal vertical delivery graph, maps only the obligations applicable to the delivery delta, conditionally creates `EXECUTION-READINESS.md`, runs local checks, and obtains human approval without offering routine Claude review.
5. Publish approved tracker drafts only through the project's bounded intake path on a later explicit action.

### PRD Output Format

When PRD work is required, `feature-design` outputs a canonical Markdown draft in the target project's existing feature-document structure. It is not JSON, a model transcript, or a separate review report. Triage that establishes no product change or a fix restoring canonically accepted behavior may instead return `prd_not_applicable` or `prd_change_not_required` with evidence and downstream routing; neither creates a PRD artifact or approval gate.

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

For a large feature, later stages may additionally produce a justified shared `implementation.md`, a vertical parent/child task plan, and—only when external prerequisites exist—`EXECUTION-READINESS.md`. For a small feature, implementation notes stay in its single task contract. When cross-model review is approved, its findings remain live and ephemeral; only human-approved final documentation is durable.

## Project Docs Organizer

Use `project-docs-organizer` for an initial bootstrap, one-time migration, or major structural cleanup, not routine project maintenance.

It reviews existing docs and git boundaries, chooses the smallest safe organization mode, requests explicit approval before mutation, creates the approved preflight backup, and applies the bundled canonical playbook without replacing stronger project-specific documentation.

## Development And Installation

### Portability And Runtime Requirements

The repository contains no bundled credentials, account identifiers, fixed reviewer sessions, or workstation-specific home paths. Skill packages use relative paths, caller-provided project paths, and standard user-level installation locations.

Most skills require only their native host. Cross-family review additionally requires a locally installed and authenticated reviewer CLI:

- Codex `cross-model-review` invokes the `claude` CLI and defaults to `claude-opus-4-8` with `xhigh` effort. The user running it must have access to that model, or explicitly select another supported reviewer model and effort.
- Kimi `cross-model-review` invokes the `claude` CLI with the same `claude-opus-4-8` / `xhigh` defaults as the Codex distribution. The user running it must have access to that model, or explicitly select another supported reviewer model and effort.
- Claude `cross-model-review` invokes the `codex` CLI through its package-local helper and defaults to `gpt-5.6-sol` with `high` reasoning effort. The user running it must have access to that model (or explicitly select another supported reviewer model and effort) and authenticate that CLI separately. Mutable review targets outside the project must be copied into an owner-only scratch directory and passed with `--scratch-root`.

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
