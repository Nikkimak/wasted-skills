# Runtime Loop

This skill is informed by the Claude Design architecture pattern recovered from the design dump.

The useful lesson is not the private prompt internals. The useful lesson is the workflow:

1. the project files are the source of truth
2. the model edits files through explicit tools
3. the result is rendered in preview
4. preview output, logs, and screenshots feed the next repair step

## What to copy from that pattern

- Treat file edits as primary, not chat prose.
- Keep the edit loop explicit and traceable.
- Use preview as a first-class part of the workflow.
- Separate generation from verification.
- Prefer a thin UI and a stronger project/runtime layer when building systems of this kind.

## Practical rule for this skill

When tools exist, work in this order:

1. inspect current files
2. edit the smallest responsible set of files
3. render the output
4. inspect screenshot or preview
5. inspect console/runtime failures
6. repair

If preview tooling does not exist, still behave as though the rendered result matters: reason about DOM structure, responsive behavior, asset loading, and likely runtime errors instead of stopping at static code.

## Verification bar

Do not call a UI task complete merely because the code compiles.

A UI change is only in good shape when:

- the visual hierarchy is coherent
- the layout renders as intended
- the interactions have sensible states
- there are no obvious runtime or asset failures
- the result matches the requested surface and tone
