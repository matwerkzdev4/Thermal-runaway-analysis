# Temperature Profile Video Method

## Inputs To Extract

From the setup sketch/schematic:

- Main components and coordinate layout.
- Sensor IDs and physical contact points.
- Semantic groups such as vent sensors, surface sensors, air sensors, hot-face sensors, or cold-face sensors.
- Apparatus regions that should be colored or kept static.

From the data:

- Timestamp or elapsed-time column.
- Sensor columns and units.
- Sampling interval.
- Test start and end.
- Missing values, invalid headers, or derived columns to avoid.

From the user or analysis:

- Event names.
- Event marker sensors.
- Event times.
- Event interpretation caveats.

## Rendering Recipe

1. Define constants: canvas size, FPS, video duration, real elapsed end time, temperature min/max, output paths.
2. Load data with a structured parser. Use raw timestamps when available.
3. Convert timestamps to elapsed seconds from the first valid record.
4. Store sensor series as numeric arrays.
5. For each frame:
   - Map frame number to real elapsed time.
   - Interpolate sensor values.
   - Draw static setup geometry.
   - Draw sensor circles with color and size based on value.
   - Draw sensor ID and current value.
   - Highlight event-marker sensors near their event times.
   - Draw elapsed-time text, color scale, event list, and timeline.
6. Encode frames with ffmpeg or an equivalent encoder.

## Temperature Color Guidance

Use a smooth stepped scale with readable engineering meaning:

- cold/ambient: blue
- warm: cyan/green
- caution/threshold: yellow
- hot: orange/red
- extreme: pale or white-hot

Anchor the scale to domain thresholds. For battery thermal runaway work, 200 C is a useful protected-side threshold and should be visible on the legend.

## Event Marker Guidance

- Prefer sharp one-second rises on vent or event-specific sensors when those sensors exist.
- Confirm surface temperature context around the event; a lone spike can be hot-gas exposure rather than full component runaway.
- When a component lacks a dedicated vent sensor, mark the strongest relevant surface spike and clearly state lower confidence.
- Keep obsolete or rejected event markers out of the timeline unless the user asks to show them as disturbances.

## Verification Checklist

Check at least:

- A frame before the first event.
- A frame at each event.
- A frame at the corrected/revised event if the analysis changed.
- A late frame near peak exposure.

For each preview frame:

- Elapsed time matches the intended real test time.
- Sensor temperatures match interpolated data.
- Event list includes only events that have occurred.
- Timeline ticks and labels are readable.
- Highlighted sensor is the correct marker.
- Labels and numeric values do not overlap in a confusing way.

## Thermal Runaway Profile Pattern

The existing `thermal_runaway_temperature_profile.mp4` used these transferable decisions:

- Static test schematic geometry shared with the clean setup diagram.
- Thermocouple circles placed on physical contact points.
- Live numeric temperature boxes under each thermocouple.
- Temperature-driven marker color and size.
- Top-right elapsed-time clock.
- Left-side event list populated as events occur.
- Bottom color scale and propagation timeline.
- MP4 generated from deterministic PNG frames.

Do not hard-code battery-specific labels for unrelated tests; reuse the structure: physical layout plus live sensor values plus verified events.
