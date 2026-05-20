# Thermal Runaway Analysis

This project contains the analysis files, reports, figures, and video for the Cocoon thermal runaway test.

## What To Open First

- Main report: `Thermal_Runaway_Analysis_Report.md`
- 200 C findings report: `Thermal_Runaway_200C_Findings_Report.md`
- Final schematic: `report_figures/Thermal_Runaway_Test_Configuration_Clean.png`
- Final temperature video: `report_figures/thermal_runaway_temperature_profile.mp4`
- Raw test data: `Test Results.xlsm`

## Important Notes

- Use the raw timestamp column `A: Time` in `Test Results.xlsm` for timing analysis.
- Do not use workbook columns `B:E` for timing analysis.
- Current C1 thermal runaway marker: `48 min 54 s`, from the T3 surface spike.
- Current C5 thermal runaway marker: `74 min 07 s`, from the T19 spike after 73 minutes.
- The earlier C5 T19 change at `63 min 30 s` is treated as a disturbance, not C5 thermal runaway.

## Project Files

- `create_clean_test_configuration_schematic.py` creates the clean setup schematic.
- `create_temperature_profile_video.py` creates the animated temperature profile video.
- `report_figures/` stores final charts, images, and video outputs.
- `.codex/skills/` stores reusable Codex workflows for this project.
- `SESSION_LOG.md` records short handoff notes for future sessions.

## How To Continue Development

1. Install Python if it is not already installed.
2. Install Node.js if it is not already installed.
3. Install the video tool dependency:

```powershell
npm install
```

4. Regenerate the schematic:

```powershell
python create_clean_test_configuration_schematic.py
```

5. Regenerate the temperature profile video:

```powershell
python create_temperature_profile_video.py
```

The video script may take a few minutes because it creates many image frames before building the MP4.

## GitHub Workflow

After making changes:

```powershell
git status
git add .
git commit -m "Describe the change"
git push
```

Keep commit messages short and clear, for example:

```powershell
git commit -m "Update C5 thermal runaway timing"
```
