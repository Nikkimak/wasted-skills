# Claude Skills Repository Instructions

This repository stores paired platform-native skill implementations under each logical skill root.

```text
<skill-name>/
├── Codex/   # Codex-native source
└── Claude/  # Claude Code-native source
```

When asked to create or improve a Claude Code skill, edit only `<skill-name>/Claude/` unless the user explicitly requests changes to the Codex version.

Use the paired `<skill-name>/Codex/` package only as a product-semantics reference. Preserve agreed outcomes, approvals, stage boundaries, security stops, and durable output contracts, but rewrite the entrypoint for Claude Code's native skill format, invocation syntax, tools, permissions, session behavior, and provider adapters. Do not mechanically copy Codex-specific `$skill` syntax, `agents/openai.yaml`, or a reviewer helper that assumes GPT/Codex is the current author.

Every installable Claude package must place its required `SKILL.md` inside `<skill-name>/Claude/` and keep all Claude-only references, scripts, examples, and assets inside that same directory.

The canonical source is this repository. `~/.claude/skills/<skill-name>/` is only an installed runtime mirror. Edit here first, validate the Claude-native package, then synchronize with:

```bash
rsync -a --delete "<skill-name>/Claude/" "$HOME/.claude/skills/<skill-name>/"
```

Do not edit installed mirrors directly. Do not add a root `<skill-name>/SKILL.md`. Do not modify `Codex/` while authoring Claude versions unless explicitly authorized.

Update the repository `README.md` when adding/removing/renaming logical skills or changing the platform layout, suite sequence, or public output contracts. Do not create per-skill README files.

## Portability

- Keep every distributable package independent of personal accounts, organization-specific repositories, and workstation-specific paths.
- Never embed credentials, access tokens, account identifiers, fixed session identifiers, or generated authentication state.
- Prefer package-relative and caller-supplied paths. Use standard variables such as `$HOME`, `$PWD`, `CODEX_BIN`, and `CLAUDE_BIN` when a host path is required.
- Document authenticated provider CLIs and model availability as runtime prerequisites; do not bundle or infer authentication configuration.
- Before public distribution, scan the complete repository for personal paths, private project names, credentials, and symlinks outside the repository.
