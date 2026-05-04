# Operator Method

This reference captures the working method behind this skill.

It takes the useful lessons from the Claude Design dump, but adapts them to a direct coding workflow.

## Core stance

Treat UI work as operational work, not as a speculative design essay.

That means:

- recover context first
- inspect the files that actually own the interface
- edit the smallest responsible set of files
- render the result
- inspect what the user would actually see
- repair if needed

## What is portable from Claude Design

The useful lessons from Claude Design are architectural and procedural:

- files are the source of truth
- preview is first-class
- screenshots and logs help repair bad output
- project context matters more than isolated prompts
- explicit tools beat vague ambient access

What is not copied here:

- Anthropic-specific transport
- private prompt internals
- product-specific RPC mechanics

## Behavior rules

### Ask less, but ask better

Questions are good only when they change the outcome.

Ask when ambiguity materially changes:

- the interface structure
- the visual language
- the interaction model
- the intended audience or tone

Do not ask questions that the codebase already answers.

### Preserve before replacing

When a project already has a coherent UI language:

- preserve its patterns
- tighten them where weak
- extend them consistently

Do not import a new aesthetic just because you can.

### Direct implementation beats abstract advice

If the environment allows code changes, prefer code changes.

Only stay in analysis mode when:

- the user explicitly asks for analysis
- the context is too incomplete to edit safely
- the user wants options before implementation

### One strong pass by default

For normal scoped UI work:

- make one strong implementation pass
- verify it
- refine if needed

Do not force multi-variant exploration onto routine work.

### Variations are a tool, not a default

Offer multiple directions only when:

- the user asks for options
- the task is exploratory by nature
- the product has no clear existing language

When you do use variations, make them explicit and comparable.

### Verification matters

A UI task is not done because the code looks plausible.

It is done when:

- the hierarchy is coherent
- the layout renders
- visible states make sense
- there are no obvious runtime or asset failures
- the result matches the requested tone and surface
