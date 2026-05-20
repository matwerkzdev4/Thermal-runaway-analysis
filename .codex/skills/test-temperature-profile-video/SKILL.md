---
name: test-temperature-profile-video
description: Create animated, report-ready temperature-profile videos from a test setup sketch/schematic and time-series measurement data such as Excel/CSV thermocouple logs. Use when Codex is asked to recreate or generalize thermal_runaway_temperature_profile.mp4, animate sensors on a physical test layout, show temperature color changes over time, mark test events, or produce an MP4/GIF-style engineering test visualization.
---

# Test Temperature Profile Video

## First Requirements

Require both:

- A sketch, photo, screenshot, or existing schematic showing the physical test setup and sensor locations.
- Time-series measurement data with a timestamp/elapsed-time column and sensor columns.

If either is missing, ask for it before creating the video. Do not infer sensor placement from data headers alone unless the user explicitly accepts a placeholder layout.

## Workflow

1. Inspect the setup visual and map each sensor ID to its physical location.
2. Inspect the data source using raw timestamps or trustworthy elapsed-time fields. Avoid helper columns if project instructions say they are unreliable.
3. Define event markers from data and user-approved interpretation, not just from earlier labels. Record the marker sensor, event time, and temperature signature.
4. Build a deterministic rendering script that:
   - loads the raw measurement data,
   - interpolates sensor values at frame times,
   - draws the setup layout,
   - colors sensor markers by value,
   - labels current elapsed time,
   - shows a compact event list and timeline,
   - writes image frames, then encodes MP4.
5. Render representative preview frames around important events and the final frame.
6. Verify the video/frames visually and numerically before delivery.

## Visual Standard

Use the thermal runaway profile video as the baseline style:

- 16:9 canvas, usually 1920 x 1080.
- Main apparatus large and readable in the upper/middle area.
- Sensor markers fixed at their physical locations.
- Sensor color reflects live measured value using a clear cold-to-hot scale.
- Sensor label and numeric value stay readable and do not overlap critical geometry.
- Event list appears only after events occur.
- Timeline shows event ticks across the full test duration.
- The video prioritizes measured data and setup clarity over decorative animation.

## Reverse-Engineered Prompt Pattern

Use this as the working prompt to yourself:

```text
Create a report-ready animated temperature profile video from the provided test setup sketch/schematic and time-series measurement data.
Preserve the physical sensor locations from the setup visual. Animate each sensor by interpolating the measured value at each frame time, mapping temperature to a cold-to-hot color scale, and displaying the current value beside the marker.
Add a concise elapsed-time display, color scale, event list, and event timeline. Event markers must come from verified data signatures and user-approved interpretation.
Generate deterministic frames and encode an MP4. Verify preview frames around each key event and ensure labels, markers, colors, and event times align with the data.
```

For implementation details, read `references/video-method.md`.

## Output Contract

Deliver:

- Final MP4.
- One preview PNG when useful for quick review.
- The rendering script used to regenerate the video.
- A short note listing event definitions, data source, frame rate/duration compression, and any assumptions.
