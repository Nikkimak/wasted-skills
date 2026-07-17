# AGENTS.md

## Scope

This repository is the canonical editable source for platform-specific Codex, Claude Code, and Kimi Code skills. These instructions apply to the whole repository.

## Repository Model

Each logical skill owns one root directory and separate native distributions:

```text
<skill-name>/
├── Codex/
│   └── SKILL.md
├── Claude/
│   └── SKILL.md
└── Kimi/
    └── SKILL.md
```

The logical root `<skill-name>/` groups the platform implementations. It is not itself an installable skill and must not contain a root `SKILL.md`.

Canonical editable sources:

- Codex: `<skill-name>/Codex/`
- Claude Code: `<skill-name>/Claude/`
- Kimi Code: `<skill-name>/Kimi/`

Installed runtime mirrors are not sources of truth:

- Codex: `~/.codex/skills/<skill-name>/`
- Claude Code: `~/.claude/skills/<skill-name>/`
- Kimi Code: `~/.kimi-code/skills/<skill-name>/` (moves with `$KIMI_CODE_HOME`)

Never edit an installed mirror directly. Edit this repository first, validate, then synchronize.

## Codex Skill Work

When creating or updating a Codex version:

1. Read the system `skill-creator` instructions completely.
2. Edit only `<skill-name>/Codex/` unless the user explicitly requests paired Claude changes.
3. Keep `SKILL.md` and supporting references/scripts/assets self-contained inside `Codex/`.
4. Generate or update `Codex/agents/openai.yaml` through the skill-creator helper when UI metadata changes.
5. Validate the canonical package:

   ```bash
   python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "<skill-name>/Codex"
   ```

6. Synchronize only after validation:

   ```bash
   rsync -a --delete "<skill-name>/Codex/" "$HOME/.codex/skills/<skill-name>/"
   ```

7. Validate the installed mirror and compare it with the canonical source.

Do not put Claude-specific invocation syntax or adapters into a Codex `SKILL.md` merely to make it cross-platform.

## Claude Skill Work

Claude-native implementations belong only in `<skill-name>/Claude/`. Codex may inspect them for consistency but must not author or rewrite them unless the user explicitly requests Codex to do so.

When Claude creates a native version, it may inspect the paired `Codex/` implementation for agreed product semantics, but it must use Claude Code-native frontmatter, invocation syntax, tools, and reviewer adapters rather than mechanically copying the Codex entrypoint.

## Kimi Skill Work

Kimi Code-native implementations belong only in `<skill-name>/Kimi/`. When creating or updating a Kimi version:

1. Edit only `<skill-name>/Kimi/` unless the user explicitly requests paired changes on another platform.
2. Keep `SKILL.md` and supporting references/scripts/assets self-contained inside `Kimi/`.
3. Use Kimi Code-native frontmatter (`name`, `description`), Skill tool / `/skill:<name>` invocation references, and `${KIMI_SKILL_DIR}` for package-relative file access. Do not put Codex `$skill` syntax or Claude `/skill-name` invocation syntax into a Kimi `SKILL.md` merely to make it cross-platform.
4. Validate the canonical package before synchronizing: frontmatter must parse with required `name` and `description`, referenced files must exist, and bundled scripts must compile.
5. Synchronize only after validation:

   ```bash
   rsync -a --delete "<skill-name>/Kimi/" "${KIMI_CODE_HOME:-$HOME/.kimi-code}/skills/<skill-name>/"
   ```

6. Validate the installed mirror and compare it with the canonical source.

## Shared Product Semantics

Paired versions may share the same workflow outcome while differing in host mechanics. Keep these semantics aligned when both versions exist:

- artifact/output contracts;
- human approval gates;
- stage boundaries;
- security stop conditions;
- what is durable versus ephemeral.

Do not force identical implementation text. Host-specific execution quality takes precedence over textual sameness.

## Documentation Updates

Update root `README.md` when:

- adding, removing, or renaming a logical skill;
- changing the repository layout or installation model;
- changing the feature-preparation sequence or public output contract.

Update a skill's platform-local references when its detailed contract changes. Do not add per-skill README files; `SKILL.md` plus referenced resources are the package documentation.

Update external project documentation only when delivery status, architecture, names, or scope changes. Routine wording or implementation refinements inside one skill do not require updates outside this repository.

## Portability

- Keep distributable skill packages independent of personal accounts, organization-specific repositories, and workstation-specific paths.
- Never embed credentials, access tokens, account identifiers, fixed session identifiers, or generated authentication state.
- Prefer package-relative paths and caller-supplied paths. Use standard environment variables such as `$HOME`, `$PWD`, `CODEX_HOME`, `CODEX_BIN`, and `CLAUDE_BIN` when a host path is required.
- Treat authenticated provider CLIs and model access as runtime prerequisites, not bundled configuration. Document those prerequisites and fail clearly when they are unavailable.
- Before public distribution, scan the complete repository for personal home paths, private project names, credentials, symlinks outside the repository, and other machine-local state.

## Safety

- Preserve unrelated worktree changes.
- Do not stage, commit, push, or publish skills unless the user explicitly requests it.
- Keep empty platform placeholders with `.gitkeep` until a native implementation exists.
- Run `git diff --check` and platform validation before reporting completion.
