# Schematic Method

## Extraction Checklist

From the user's sketch, capture:

- Apparatus title and test type.
- Ordered main components and whether they repeat.
- Component categories and their visual identity: specimen/sample, heat source, insulation/barrier, fixture, chamber, sensor, cable, flow path.
- Contact relationships: touching, separated by gap, wrapped around, embedded in, clamped to, or outside/ambient.
- Sensor IDs, measurement type, and exact contact points.
- Directional meaning: left-to-right order, vertical stack, hot/cold side, inlet/outlet, upstream/downstream.
- Notes that explain the setup rather than the drawing process.

## Geometry Rules

- Build from named coordinate helpers, not one-off coordinates.
- Define canvas, margins, apparatus area, legend area, and repeated component dimensions first.
- Calculate related positions from component boxes: centers, edges, gaps, midpoint between neighbors, sensor contact points.
- Use a small number of semantic gaps:
  - contact gap: 0-4 px or touching edges
  - sensor gap: diameter-based gap for visible contact
  - air/separation gap: visibly larger
  - special gap: only when a fixture or heat source requires it
- Keep repeated components equal unless the sketch clearly shows different sizes.
- Route callout lines after placing labels. Move labels before moving physical contact points.

## Drawing Recipe

1. Draw background.
2. Draw apparatus band/container.
3. Draw passive barriers, insulation, or fixtures behind active components.
4. Draw main samples/components.
5. Draw heat sources, loads, clamps, or flow arrows.
6. Draw sensors at physical points.
7. Draw leaders and labels.
8. Draw legend and short setup notes.
9. Export PNG and SVG.

## Verification

Before final delivery, inspect the rendered image and check:

- Every source-sketch component appears or is intentionally omitted.
- Repeated elements are aligned and equal-sized.
- Sensors touch the correct surfaces/locations.
- Labels do not overlap components or each other.
- Leader lines do not imply the wrong contact point.
- Legend colors match the drawing.
- The schematic still reads at report scale.

## Thermal Runaway Schematic Pattern

The existing clean thermal runaway schematic used these transferable decisions:

- Five equal battery blocks on a common horizontal axis.
- Black vertical insulation jackets around each battery.
- Red heater strips flush to the trigger cell.
- Yellow thermocouple circles placed at exact vent, surface, inter-jacket, heater/jacket, and outer/air positions.
- Label boxes with orange leaders so thermocouple IDs remain readable.
- A lower legend band grouping component colors and thermocouple categories.

Do not hard-code these details for unrelated setups; reuse the structure: normalize repeated components, separate semantic color categories, place sensors physically, and verify against the sketch.
