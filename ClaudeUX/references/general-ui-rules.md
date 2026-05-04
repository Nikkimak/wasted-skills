# General UI Rules

Use these rules when the project does not already impose a stronger visual language.

## Core stance

- Prefer intentional composition over safe defaults.
- Use a clear visual direction; do not mix unrelated styles.
- Match the interface density to the product.
- Preserve an existing design system when it is coherent.

## Typography

- Give typography a job: display, section heading, body, meta, labels, numbers.
- Avoid default system-looking output when the product needs a stronger identity.
- Keep the scale compact and purposeful; do not spray many near-identical font sizes.
- Numbers and KPIs should feel deliberate, not like regular body text.

## Layout

- Start with hierarchy, not decoration.
- Decide what the primary action is, then design around that.
- Use strong sectioning and spacing rhythm.
- Avoid pages made of interchangeable cards unless the product actually needs that structure.

## Color

- Choose a constrained palette with one dominant accent.
- Prefer variables/tokens over raw color values.
- Use semantic colors for state, not as random decoration.
- Backgrounds should support the composition; do not default to a flat single color if the page needs atmosphere.

## Motion

- Add only a few meaningful motion moments: entry, hover, reveal, emphasis.
- Motion should clarify structure or state.
- Do not add constant floating, bouncing, or ornamental animation loops.

## Frontend quality

- Desktop and mobile both need to load cleanly.
- Respect the framework patterns already in the repo.
- In React, avoid unnecessary abstractions and memoization churn.
- Prefer focused component boundaries and explicit ownership of layout and state.

## Failure modes to avoid

- generic hero + feature cards + CTA clone pages
- random gradients with no relation to the product
- typography that looks like defaults
- inconsistent radius, shadow, and border logic
- shipping without checking the rendered result
