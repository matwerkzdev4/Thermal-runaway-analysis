## 2026-05-19 12:00 - Session Summary

- Goal: Analyze thermal runaway timing at 200 °C, compile findings, create a clean test schematic, and update the thermal profile video.
- Files: Created `Thermal_Runaway_200C_Findings_Report.md`; created/updated `create_clean_test_configuration_schematic.py`; updated `create_temperature_profile_video.py`; generated outputs in `report_figures/`.
- Findings: Cocoon FR Silicone is the TR test baseline jacket material. For 200 °C timing, C2 battery-side marker uses T7, C1 surface uses T4, and T5 is inter-jacket, not battery surface.
- Decisions: Clean schematic uses equal C1-C5 blocks, black insulation jackets, red heaters flush to C2, same-size yellow thermocouples, T1/T21 as outer-jacket contact points, and surface thermocouples centered in gaps to show two-surface contact.
- State: Current approved schematic outputs are `report_figures/Thermal_Runaway_Test_Configuration_Clean.png` and `.svg`. Current video is `report_figures/thermal_runaway_temperature_profile.mp4` with preview `thermal_runaway_temperature_profile_preview.png`.
- Next: Review the updated video visually; if accepted, use the clean schematic geometry as the basis for future video/report graphics.
- Caveats: Do not use workbook columns B:E in `Test Results.xlsm` for timing analysis; use raw timestamp column A and thermocouple columns. `ffmpeg-static` was installed locally under `node_modules` to render MP4.

## 2026-05-19 14:35 - Session Summary

- Goal: Correct C5 thermal runaway timing in the video and reports, add C1 TR marker, and preserve handoff context.
- Files: Updated `create_temperature_profile_video.py`, regenerated `report_figures/thermal_runaway_temperature_profile.mp4`, updated `Thermal_Runaway_Analysis_Report.md`, `Thermal_Runaway_200C_Findings_Report.md`, and `report_figures/fig4_propagation_lag_bar.svg`.
- Findings: C1 TR-like event is marked at 48 min 54 s from T3 surface spike. C5 TR is marked at 74 min 07 s from the post-73 min T19 spike; T19 reached 358.0 °C at 74 min 10 s. The old 63 min 30 s C5 marker is only an early T19 disturbance while C5 surfaces were still near 80-100 °C.
- Decisions: Reports now treat adjacent propagation intervals as C2-to-C1 10 min 35 s, C2-to-C3 12 min 43 s, C3-to-C4 12 min 25 s, and C4-to-C5 10 min 40 s.
- State: Video and report text now align with the revised C1 and C5 TR event markers.
- Next: If figures beyond `fig4_propagation_lag_bar.svg` are regenerated later, keep the revised C1/C5 event definitions consistent.
- Caveats: C1 has no dedicated vent thermocouple; its event marker is lower-confidence than T7/T11/T15/T19 vent markers.
