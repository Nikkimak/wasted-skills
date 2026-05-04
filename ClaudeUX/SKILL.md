---
name: ClaudeUX
description: Use when the user wants UI, UX, design, prototype, or frontend presentation work and the work should be handled with a strong operator workflow: recover project context first, inspect the real files that control the interface, implement directly when scope is clear, use preview/screenshots/logs to verify, and improve visual quality without drifting away from the product. This skill is for practical design-and-build work, not abstract design advice.
---

# ClaudeUX

Use this skill for practical design-and-build work.

This is not a generic "give UI tips" skill. It is for taking a product brief, existing screen, or codebase and producing stronger UI output with a repeatable context-first, file-first, preview-and-repair loop.

## What this skill is for

- designing and implementing landing pages, dashboards, app screens, flows, and components
- turning a rough brief into a concrete UI direction and then into code
- improving layout, copy hierarchy, spacing, typography, color, and motion
- using preview, screenshots, and logs to iterate instead of stopping at a first draft
- treating files as the source of truth and preview as part of the workflow
- making visual changes that preserve or strengthen the product's existing language

## Invocation boundary

Use this skill when the user asks to:

- design or redesign a page, screen, component, or section
- build a UI from a description
- improve visual quality, UX, layout, copy hierarchy, or polish
- make a frontend output feel intentional instead of generic
- iterate on a preview until the result is visually coherent
- create a prototype, mockup, tweakable exploration, or HTML proof of concept
- repair a visually broken interface where correctness includes what the user sees, not just whether the code compiles

Do not use this skill for:

- pure backend work
- abstract design theory with no expected implementation
- isolated bugfixes that do not affect the rendered interface
- work where the nearest project instructions already provide stronger, more specific frontend process

## Required reads

Always start with the real project context, not assumptions.

1. Read the nearest local `AGENTS.md`.
2. Inspect the existing UI files before proposing a rewrite.
3. Read [references/operator-method.md](references/operator-method.md).
4. Read [references/general-ui-rules.md](references/general-ui-rules.md).
5. Read [references/runtime-loop.md](references/runtime-loop.md).
6. Stay project-agnostic unless the current project provides its own stronger design rules.

All operational guidance required by this skill is bundled inside this skill folder.

## Default operating mode

Assume the user wants implementation, not just commentary, unless they explicitly ask for analysis only.

Do not stop at a moodboard or bullet list if code can be changed directly.

Default stance:

- inspect first, then edit
- ask only the questions that materially change the outcome
- implement directly when the scope is already clear
- prefer code and design-system context over screenshots alone
- verify visually when the environment allows it
- stay concise and concrete; do not turn small UI tasks into long design workshops

## Workflow

### 1. Classify the surface

Reduce the task to one of these:

- marketing page
- application screen
- dashboard / dense data surface
- component / pattern library unit
- design system or theme layer

Then decide whether the work should preserve an existing visual language or intentionally introduce a new one.

Also classify the mode:

- patch
- implementation
- prototype
- exploration

### 2. Build a compact design brief

Before editing, make the brief explicit in your head:

- user goal
- primary screen action
- audience and tone
- density level: sparse / balanced / dense
- device scope: desktop / responsive / mobile-first
- visual direction: restrained, bold, editorial, operational, glass, etc.
- constraints from the project or design system

If the brief is missing details, infer only what is needed to move forward safely.

Ask questions only when ambiguity materially affects:

- the product surface
- the interaction model
- the intended tone
- whether to preserve or replace the current visual language

If the request is already specific enough, skip the questions and build.

### 3. Gather design context before inventing

Good design work does not start from scratch unless forced to.

Actively look for:

- existing codebase UI patterns
- design tokens or theme files
- shared components
- screenshots or prior product surfaces
- imported design systems or UI kits
- brand assets and copy style

If strong context exists, follow it. If context is missing, say that explicitly and then choose a deliberate direction.

Default to preserving the product's vocabulary unless the user clearly wants a new direction.

### 4. Inspect before editing

Read the existing files that actually control the screen.

Prefer this order:

- route/page entry file
- local layout/container
- major section/component files
- tokens/theme/styles

Do not redesign from memory when the codebase already contains the truth.

### 5. Implement with strong visual decisions

Turn the brief into concrete decisions:

- layout structure
- section order
- typography scale
- spacing rhythm
- color system
- interaction states
- motion moments
- copy hierarchy

Avoid generic filler patterns. If the interface starts looking like default cards on a flat background, change direction.

For small scoped tasks, make one strong pass instead of generating many options.

Use variations only when:

- the user asks for options
- the brief is exploratory
- multiple directions are genuinely useful

If creating a standalone artifact or HTML prototype, use descriptive filenames and keep revisions explicit.

### 6. Work in an edit -> preview -> repair loop

When preview tooling is available:

1. make a focused edit
2. render the result
3. inspect the preview or screenshot
4. inspect console/runtime errors if present
5. repair the result

Do not claim success without visual verification when the environment makes verification possible.

### 7. Preserve or enforce the right system

If the project has an existing design system, preserve it.

If the project is visually weak or underspecified, enforce a stronger system by introducing:

- reusable tokens or variables
- a consistent typography hierarchy
- clearer section patterns
- explicit state styling
- consistent border, radius, and shadow logic

Do not redesign an entire surface just because one section is weak, unless the user asked for a broader pass.

### 8. Make revisions explicit when needed

When the user asks for a new version or a change:

- preserve the previous direction when practical
- make the revision explicit
- prefer toggles, variants, or clearly named revisions over silently overwriting the only good state

### 9. Finish with evidence

Before closing:

- verify the layout renders
- verify major interactions do not visually break
- note any residual gaps such as missing assets, missing mobile pass, or unavailable runtime checks
- mention what you verified and what you could not verify

## Non-negotiable quality bar

- no generic "AI slop" layouts
- no random mix of visual languages
- no unexplained typography choices
- no arbitrary colors when tokens exist
- no decorative motion without purpose
- no claims of completion without checking the rendered result when possible
- no jumping straight into a visual direction when strong project context exists but has not been inspected
- no broad rewrites when the request only needs a focused UI fix
