## 2026-05-21 - Project Handover

- Goal: Maintain thermal runaway analysis, reports, figures, video, and reusable Codex workflows for this project.
- Repo: Git is initialized and pushed to `https://github.com/matwerkzdev4/Thermal-runaway-analysis.git` on branch `main`.
- Main files: `Thermal_Runaway_Analysis_Report.md`, `Thermal_Runaway_200C_Findings_Report.md`, `Test Results.xlsm`, `create_clean_test_configuration_schematic.py`, `create_temperature_profile_video.py`, and `report_figures/`.
- Current outputs: clean schematic at `report_figures/Thermal_Runaway_Test_Configuration_Clean.png` / `.svg`; temperature video at `report_figures/thermal_runaway_temperature_profile.mp4`.
- Key timing decisions: C1 TR-like event is 48 min 54 s from T3 surface spike. C5 TR is 74 min 07 s from the post-73 min T19 spike; T19 reaches 358.0 C at 74 min 10 s. The old 63 min 30 s C5 T19 change is only an early disturbance, not C5 TR.
- Propagation intervals now used in reports: C2-to-C1 10 min 35 s, C2-to-C3 12 min 43 s, C3-to-C4 12 min 25 s, and C4-to-C5 10 min 40 s.
- Material finding: Cocoon FR Silicone is the TR test baseline jacket material.
- Data caveat: Do not use workbook columns `B:E` in `Test Results.xlsm` for timing analysis. Use raw timestamp column `A: Time` and thermocouple columns.
- Event caveat: C1 has no dedicated vent thermocouple, so its marker is lower-confidence than T7/T11/T15/T19 vent markers.
- Project workflows: `.codex/skills/test-setup-schematic/` creates clean setup schematics from sketches; `.codex/skills/test-temperature-profile-video/` creates animated temperature videos from setup sketches plus time-series data.
- Development note: README.md is written for non-technical users and contains the simplest commands to regenerate the schematic and video.
