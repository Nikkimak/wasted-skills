# Templates Policy

Templates are optional accelerators, not required project structure or
authority.

## Selection

- Use `project-router-template.md` only when creating or materially rewriting a
  project router; keep the project's existing router filename.
- Use `context-readme-template.md` for a real central documentation index.
- Use project-state, runtime-map, repo-map, decisions-index, deploy-runbook, and
  future-work templates only when the corresponding authority role exists.
- Use `src-readme-template.md` only for a code-bearing runtime.
- Use `service-readme-template.md` only for a durable ownership boundary that
  benefits from local contract and test guidance.

Do not create a file merely because a template exists.

## Adaptation

- Preserve stronger existing content and vocabulary.
- Replace every used placeholder and remove unused sections.
- Express authority by question type; do not copy a global source-of-truth
  hierarchy.
- Keep physical runtime layouts illustrative.
- Do not materialize empty folders referenced by an example.
- Keep indexes navigational and local runtime docs contributor-focused.
- Keep the full file-size table in bundled guidance; add only adapted project
  rules that will actually be maintained.

## Negative Checks

Before completion, confirm which templates were intentionally not used and why.
Verify that the result did not create:

- artificial runtime structure in a documentation-primary project;
- a second current-state wiki inside runtime code;
- ownership READMEs for trivial directories;
- duplicated mutable facts;
- unused placeholders or ceremonial files.
