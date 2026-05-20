# Thermal Runaway 200C Findings Report

## Scope and method

This report uses 200 °C as the thermal runaway trigger / protection temperature.

Thermal runaway test timing was computed from `Test Results.xlsm` using the raw timestamp column `A: Time` and thermocouple columns only. Benchmark material scaling was computed from `Test Data.xlsx` in the 1200 W heater benchmark folder, using each material cold-face `T2` time to 200 °C.

The thermal runaway test insulation jacket used Cocoon FR Silicone, so Cocoon FR Silicone is the baseline for extrapolation.

Extrapolation formula:

`Extrapolated time = observed Cocoon time x (benchmark material T2-to-200C time / benchmark Cocoon T2-to-200C time)`

## 1. Thermal Runaway Test Findings

### 1.1 T6, T7, and T8 exposure above 200 °C

T6 and T8 are positioned between the insulation jacket and the heater. T7 is positioned on the C2 battery vent area.

Individual thermocouple exposure above 200 °C:

| Thermocouple | Above-200C period | Duration above 200 °C |
|---|---:|---:|
| T6 | 34 min 25 s to 226 min 33 s | 192 min 09 s |
| T7 | 38 min 18 s to 47 min 40 s; 47 min 46 s to 188 min 22 s | 150 min 00 s total |
| T8 | 37 min 05 s to 242 min 03 s | 204 min 59 s |

Period where T6, T7, and T8 were all above 200 °C at the same time:

| Condition | Start | End | Duration |
|---|---:|---:|---:|
| First continuous period | 38 min 18 s | 47 min 40 s | 9 min 23 s |
| Second continuous period | 47 min 46 s | 188 min 22 s | 140 min 37 s |
| Total simultaneous time | - | - | 150 min 00 s |

C2 thermal runaway started at about 38 min 18 s to 38 min 19 s, which is almost immediately after T6, T7, and T8 were all above 200 °C.

### 1.2 Adjacent cell surface time to 200 °C

Using the first monitored surface thermocouple on each cell to reach 200 °C. Left/right is referenced to the cell orientation in `Thermal runaway test configuration.png`, viewed from C1 on the left toward C5 on the right.

| Cell | First TC to reach 200 °C | Side / location | Time from start |
|---|---|---|---:|
| C2 | T7 | C2 battery vent area; best C2 battery-side marker because no TC was placed between the heater and C2 battery surface | 38 min 17 s |
| C1 | T4 | Right side, C2-facing battery surface | 40 min 05 s |
| C3 | T10 | Left side, C2-facing surface | 40 min 15 s |
| C4 | T14 | Left side, C3-facing surface | 55 min 49 s |
| C5 | T18 | Left side, C4-facing surface | 67 min 54 s |

Using all monitored thermocouples around each cell above 200 °C:

| Cell | TCs checked | Time from start |
|---|---|---:|
| C1 | T3 / T4 / T5 | 48 min 43 s |
| C3 | T10 / T11 / T12 / T13 | 52 min 56 s |
| C4 | T14 / T15 / T16 / T17 | 65 min 55 s |
| C5 | T18 / T19 / T20 / T21 | 74 min 50 s |

### 1.3 Exposure to 200 °C before thermal runaway

For adjacent cells, the clearest estimate is from the hot-side surface thermocouple reaching 200 °C to the cell runaway marker. C1 uses the T3 surface spike because no dedicated C1 vent thermocouple was available. C5 uses the post-73 min T19 spike at 74 min 07 s; the earlier T19 disturbance at 63 min 30 s is not treated as C5 thermal runaway because the C5 surface thermocouples were still near 80-100 °C.

| Cell | Hot-side TC | 200 °C time | Runaway time | Exposure before runaway |
|---|---|---:|---:|---:|
| C1 | T4 | 40 min 05 s | 48 min 54 s | 8 min 49 s |
| C3 | T10 | 40 min 15 s | 51 min 02 s | 10 min 47 s |
| C4 | T14 | 55 min 49 s | 63 min 27 s | 7 min 38 s |
| C5 | T18 | 67 min 54 s | 74 min 07 s | 6 min 13 s |

Finding: in this test, an adjacent battery exposed at the hot-side surface above 200 °C went into thermal runaway after about 6 min 13 s to 10 min 47 s, depending on the cell and marker used.

C2 was directly heated, so it is not a clean adjacent-cell exposure case. T8 reached 200 °C at 37 min 05 s, and C2 runaway occurred at about 38 min 19 s, giving about 1 min 14 s from nearby surface exposure to runaway.

### 1.4 Interval for adjacent batteries to reach 200 °C on the surface

Using the first surface thermocouple on each cell to reach 200 °C. This means the interval is measured from the first thermocouple on the start cell to reach 200 °C to the first thermocouple on the next referenced cell to reach 200 °C.

| Interval | Start TC | Start side / location | End TC | End side / location | Time gap |
|---|---|---|---|---|---:|
| C2 to C1 | T7 | C2 battery vent area | T4 | C1 right side, C2-facing battery surface | 1 min 48 s |
| C2 to C3 | T7 | C2 battery vent area | T10 | C3 left side, C2-facing surface | 1 min 58 s |
| C3 to C4 | T10 | C3 left side, C2-facing surface | T14 | C4 left side, C3-facing surface | 15 min 34 s |
| C4 to C5 | T14 | C4 left side, C3-facing surface | T18 | C5 left side, C4-facing surface | 12 min 06 s |

Using all monitored thermocouples around each cell above 200 °C. Here the interval endpoint is the time when every listed thermocouple around that cell had reached at least 200 °C.

| Interval | Start TC set | End TC set | End-side completion TC | Time gap |
|---|---|---|---|---:|
| C2 to C1 | T6 / T7 / T8 | T3 / T4 / T5 | T5, right side of C1 | 10 min 26 s |
| C1 to C3 | T3 / T4 / T5 | T10 / T11 / T12 / T13 | T13, right side of C3 | 4 min 13 s |
| C3 to C4 | T10 / T11 / T12 / T13 | T14 / T15 / T16 / T17 | T17, right side of C4 | 12 min 59 s |
| C4 to C5 | T14 / T15 / T16 / T17 | T18 / T19 / T20 / T21 | T21, right side of C5 | 8 min 55 s |

## 2. Heater Benchmark and Thermal Runaway Extrapolation

### 2.1 Benchmark time to 200 °C and scaling factor

The benchmark comparison uses cold-face `T2` reaching 200 °C. Cocoon FR Silicone is the baseline because it was used in the thermal runaway test jacket.

| Material | Benchmark T2 time to 200 °C | Scaling factor vs Cocoon |
|---|---:|---:|
| Cocoon FR Silicone | 1 min 18 s | 1.000 |
| Aerogel Ceramic Fiber | 0 min 48 s | 0.615 |
| Aerogel Glass Fiber | 0 min 40 s | 0.504 |
| Mica | 0 min 17 s | 0.223 |
| 1360 Ceramic Fiber | 0 min 13 s | 0.172 |

Interpretation: all other tested single-sheet materials reached 200 °C faster than Cocoon FR Silicone in the heater benchmark. Therefore, under this simple scaling method, their extrapolated battery surface trigger times are shorter than the Cocoon thermal runaway test result.

### 2.2 Extrapolated time for battery surfaces to reach 200 °C

These are the first-surface 200 °C times aligned to the thermal runaway test. Cocoon FR Silicone is the actual thermal runaway test baseline material; the other materials are extrapolated from the heater benchmark scaling factor.

| Material | C2 vent-area 200C | C1 surface 200C | C3 surface 200C | C4 surface 200C | C5 surface 200C |
|---|---:|---:|---:|---:|---:|
| Cocoon FR Silicone, actual TR test baseline | 38 min 17 s | 40 min 05 s | 40 min 15 s | 55 min 49 s | 67 min 54 s |
| Aerogel Ceramic Fiber | 23 min 33 s | 24 min 40 s | 24 min 46 s | 34 min 20 s | 41 min 46 s |
| Aerogel Glass Fiber | 19 min 18 s | 20 min 12 s | 20 min 17 s | 28 min 08 s | 34 min 14 s |
| Mica | 8 min 33 s | 8 min 57 s | 8 min 59 s | 12 min 27 s | 15 min 09 s |
| 1360 Ceramic Fiber | 6 min 35 s | 6 min 54 s | 6 min 56 s | 9 min 36 s | 11 min 41 s |

### 2.3 Extrapolated intervals for adjacent batteries to reach 200 °C

These intervals use the first surface thermocouple on each cell to reach 200 °C. Cocoon FR Silicone is the actual thermal runaway test baseline; the other material intervals are extrapolated.

| Material | C2 to C1 | C2 to C3 | C3 to C4 | C4 to C5 |
|---|---:|---:|---:|---:|
| Cocoon FR Silicone, actual TR test baseline | 1 min 48 s | 1 min 58 s | 15 min 34 s | 12 min 06 s |
| Aerogel Ceramic Fiber | 1 min 06 s | 1 min 13 s | 9 min 35 s | 7 min 26 s |
| Aerogel Glass Fiber | 0 min 54 s | 0 min 59 s | 7 min 51 s | 6 min 05 s |
| Mica | 0 min 24 s | 0 min 26 s | 3 min 28 s | 2 min 42 s |
| 1360 Ceramic Fiber | 0 min 19 s | 0 min 20 s | 2 min 41 s | 2 min 05 s |

## 3. Key Findings

1. T6, T7, and T8 were all simultaneously above 200 °C for 150 min 00 s total.
2. C2 entered thermal runaway almost immediately after T6, T7, and T8 were all above 200 °C.
3. C1 thermal runaway is marked at 48 min 54 s from the T3 surface spike. C5 thermal runaway is marked at 74 min 07 s from the post-73 min T19 spike; the earlier T19 disturbance at 63 min 30 s is not treated as C5 thermal runaway.
4. Adjacent-cell hot-side exposure above 200 °C before runaway was about 6 min 13 s to 10 min 47 s.
5. With Cocoon FR Silicone, C2 vent-area T7 reached 200 °C at 38 min 17 s, almost coincident with C2 thermal runaway. Adjacent battery surfaces first reached 200 °C at 40 min 05 s for C1, 40 min 15 s for C3, 55 min 49 s for C4, and 67 min 54 s for C5.
6. The heater benchmark indicates Cocoon FR Silicone gave the longest delay to 200 °C among the tested single-sheet materials.
7. Extrapolated from the benchmark, Aerogel Ceramic Fiber would reach 200 °C at about 61.5% of the Cocoon timing, Aerogel Glass Fiber at about 50.4%, Mica at about 22.3%, and 1360 Ceramic Fiber at about 17.2%.
8. None of the tested single-sheet benchmark materials appears adequate by itself if the target is to keep adjacent cell surfaces below 200 °C for a long propagation-resistance window.

