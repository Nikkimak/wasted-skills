# Implementation Checklist

Use this only after discovery and explicit mutation approval.

## Preflight

- Reconfirm target root, intent, project shape, detected repo model,
  documentation scope, mutation, code-architecture scope, runtime-doc scope,
  retrieval scope, planned changes, risks, and validation intents.
- Verify code restructuring, git changes, and retrieval infrastructure are each
  separately approved when applicable.
- Create the approved scoped backup and manifest, or record the human's explicit
  decline.
- Stop and re-approve if scope changes materially.

## Apply

- Update strong existing documents instead of creating parallel truth.
- Create only evidence-selected files and directories.
- Do not create runtime files for `documentation_primary` projects without
  evidence.
- Do not create local ownership docs without durable modular boundaries or real
  ambiguity.
- Treat physical trees as examples; create no empty architecture layers.
- Keep the project router (`AGENTS.md` or its established equivalent) short and
  routing-focused.
- Keep implementation knowledge close to code without duplicating product,
  rationale, deployed state, or operations.
- Report oversized or mixed-responsibility code without restructuring it beyond
  the approved code-architecture scope.
- Remove unused template placeholders and preserve unrelated work.

## Authority And Context Economy

- Each question class has a clear authority and bounded read path.
- No universal startup sequence is required for all tasks.
- Known-owner local work reaches local docs, code, and tests without mandatory
  queue or full-wiki reading.
- Unknown-owner routing uses search before broad document loading.
- Product, rationale, deployed state, operations, planning, and evidence remain
  distinct.
- Indexes route to facts and do not claim authority over linked content.
- Split references are loaded conditionally rather than all at once.
- Trace one named local change end to end: router → ownership map → local README
  → code and tests, adding the project runtime map hop when several runtimes
  exist, and without opening the documentation index, the queue, or the full
  decision set.

## Runtime And Codebase

- Runtime entrypoints exist only where applicable and identify ownership and
  test commands.
- A code-bearing result exposes the canonical ownership chain from its router —
  one map for a single runtime, one per runtime plus a project-level runtime map
  when several exist — covers each top-level capability at one line, and stays a
  zone map rather than a file listing.
- Ownership-map entries name real paths and tests; a zone without a single
  entrypoint carries no invented symbol, and an absent test surface is recorded
  as `tests: missing`.
- Every mapped path, symbol, and test anchor resolves in the working tree.
- Logical service boundaries do not imply separate deployment.
- Public contracts and tests support any documented modular boundary.
- Shared areas do not become ownerless business-logic dumps.
- File-size guidance remains a soft review trigger with explicit exceptions.

## Git And Retrieval

- Git and deploy ownership match the approved independent repo decision.
- No project shape implicitly changed repository topology.
- `assess_advanced` created no retrieval artifacts.
- Any approved generated retrieval state stays outside canonical truth unless
  its small durable artifacts were explicitly approved.

## Verify And Close

- Required internal links resolve and no obsolete reference remains.
- No central document narrates current implementation, component structure,
  runtime flow, or live integration state.
- No local README restates code, schemas, or tests instead of linking them.
- No personal paths, project-specific names, credentials, or external symlinks
  entered a portable package.
- Relevant validation intents pass without lower owner/source accuracy.
- `git diff --check` passes and the project's own type/lint checks still pass
  when the approved scope touched code.
- Report selected scopes, backup result, created/updated/verified files,
  intentional omissions, negative checks, remaining debt, and unresolved risks.
