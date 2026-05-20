---
name: test-setup-schematic
description: Create clean, report-ready technical schematics of physical test setups from a user-provided sketch, photo, screenshot, or rough layout. Use when Codex is asked to convert a hand sketch or informal test setup drawing into a polished PNG/SVG diagram, recreate the Thermal_Runaway_Test_Configuration_Clean.png style, or make a repeatable engineering setup schematic with labeled components, sensors, heaters, fixtures, samples, wiring, flow paths, or measurement points.
---

# Test Setup Schematic

## First Requirement

Start from a user-provided sketch/photo/screenshot of the test setup. If no visual sketch or source layout is available, ask the user to provide one before creating the schematic. Do not invent geometry from prose alone unless the user explicitly asks for a conceptual placeholder.

## Workflow

1. Inspect the sketch and identify all physical elements: samples, cells, heaters, jackets, fixtures, sensors, cables, flow paths, supports, boundaries, and labels.
2. Ask for missing critical labels or ambiguous component roles only when they affect correctness. Otherwise, make conservative assumptions and state them briefly.
3. Convert the sketch into a normalized 2D engineering layout:
   - Preserve topology and contact relationships over exact hand-drawn proportions.
   - Align repeated items on a common axis.
   - Use equal dimensions for repeated equivalent parts.
   - Use consistent gaps to show contact, separation, insulation, or air space.
   - Place sensors at their true physical contact points, not merely near their labels.
4. Create a deterministic drawing script when the output must be reproducible. Prefer generating both PNG and SVG.
5. Add a compact legend and short notes only for information needed to interpret the setup. Keep the first visual area focused on the actual apparatus.
6. Render and visually verify the final schematic against the user sketch. Check label legibility, line routing, contact points, repeated-part alignment, and no overlaps.

## Visual Standard

Use the Thermal Runaway clean schematic as the baseline style:

- Canvas: 16:9 report-friendly layout, typically 1920 x 1080.
- Background: light neutral page with a subtle apparatus band and a separate legend band.
- Main components: simple filled shapes with thin outlines; avoid decorative gradients.
- Labels: short component IDs inside or next to elements; label boxes may be used when many callouts are present.
- Callouts: thin leader lines from labels to exact connection/contact points.
- Repeated parts: same size, same color, same line weight.
- Colors: reserve distinct colors for semantic categories, such as sample/component, heat source, insulation/barrier, and sensors.
- Legend: explain color/category mapping and special sensor groups. Do not add long procedural text.

## Reverse-Engineered Prompt Pattern

When creating the schematic, use this as the working prompt to yourself:

```text
Create a clean, report-ready technical schematic from the provided test setup sketch.
Preserve the physical topology, contact relationships, component order, and sensor locations.
Normalize the sketch into a precise 2D layout with aligned repeated components, equal sizes for equivalent parts, consistent gaps, and clear callout leaders.
Show the actual apparatus as the first visual priority, then add a compact legend and notes band.
Use a light engineering-report style: neutral background, solid component colors, thin outlines, readable labels, and no decorative effects.
Generate deterministic PNG and SVG outputs using code, then visually verify that all labels, contact points, and component relationships match the sketch.
```

For detailed implementation rules and a reusable extraction checklist, read `references/schematic-method.md`.

## Output Contract

Deliver:

- A PNG for reports and presentations.
- An SVG when the schematic should remain editable or scalable.
- The drawing script if future revisions are likely.
- A brief note listing any assumptions made from the sketch.
