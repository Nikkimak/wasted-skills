# Templates Policy

Templates are optional accelerators, not required project structure or
authority.

## Selection

- Use `project-agents-template.md` only when creating or materially rewriting a
  project router; keep the project's existing router filename.
- Use `context-readme-template.md` only when a documentation folder is large
  enough that finding a document by name is slow; it indexes that folder and
  never repeats the router's intent routes.
- Use repo-map, decisions-index, deploy-runbook, and future-work templates only
  when the corresponding authority role exists.
- Use `runtime-map-template.md` only when several runtimes or deploy owners
  exist; a single runtime keeps its map in its runtime README.
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
- Keep the full file-size table in bundled guidance; place each adapted rule in
  exactly one owning document — project-level when shared, inside the runtime
  when runtime-specific — and never the same rule in two scopes.

## Negative Checks

Before completion, confirm which templates were intentionally not used and why.
Verify that the result did not create:

- artificial runtime structure in a documentation-primary project;
- a second current-state wiki inside runtime code;
- ownership READMEs for trivial directories;
- duplicated mutable facts;
- the same adapted rule maintained in two documents or two scopes;
- an ownership map that grew into a file listing;
- a central coordination document for state a feature package or the queue
  already owns;
- unused placeholders or ceremonial files.
