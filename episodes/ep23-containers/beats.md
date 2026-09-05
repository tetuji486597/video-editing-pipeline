# ep23-containers — beat windows + payoff-word timings (OUTPUT timeline)

Derived from the stamped `_beat_windows_output_timeline` in `edl.A.json` / `edl.B.json`
(fix_windows.py, 24fps ceil grid). Word times are ASR word boxes mapped onto the output
timeline: `output = source - range_start + beat_window_start`. All times in seconds,
rounded to 1ms. Variant B runs 0.1667s (4 frames) earlier than A from HOOK onward
(B's intro take is one segment 4 frames shorter).

Word-box caveat: these are Scribe boxes. Starts are trustworthy; ends are padded
(see find_dead_air.py header). For frame-exact overlay hits, land cues on word STARTS.

## INTRO
- A window: 0.000 – 5.083 (source 20.18–25.24, "prepping you for your system design interview")
- B window: 0.000 – 4.917 (source 13.52–18.42, "Exploring Really Cool Tech")
- No overlay-sync phrases requested.

## HOOK
- A window: 5.083 – 10.167   |   B window: 4.917 – 10.000   (source 38.52–43.58)

"works on my machine":  A 7.423 – 8.323   |   B 7.257 – 8.157

| word      | src start | src end | A start | A end | B start | B end |
|-----------|-----------|---------|---------|-------|---------|-------|
| works     | 40.860 | 41.050 | 7.423 | 7.613 | 7.257 | 7.447 |
| on        | 41.100 | 41.230 | 7.663 | 7.793 | 7.497 | 7.627 |
| my        | 41.240 | 41.370 | 7.803 | 7.933 | 7.637 | 7.767 |
| machine," | 41.440 | 41.760 | 8.003 | 8.323 | 7.837 | 8.157 |

"got killed by containers":  A 8.703 – 9.903   |   B 8.537 – 9.737

| word        | src start | src end | A start | A end | B start | B end |
|-------------|-----------|---------|---------|-------|---------|-------|
| got         | 42.140 | 42.320 | 8.703 | 8.883 | 8.537 | 8.717 |
| killed      | 42.380 | 42.600 | 8.943 | 9.163 | 8.777 | 8.997 |
| by          | 42.620 | 42.700 | 9.183 | 9.263 | 9.017 | 9.097 |
| containers. | 42.780 | 43.340 | 9.343 | 9.903 | 9.177 | 9.737 |

## PROBLEM
- A window: 10.167 – 18.667   |   B window: 10.000 – 18.500   (source 60.54–69.02)

"runtime, libraries, and config":  A 11.907 – 14.047   |   B 11.740 – 13.880

| word       | src start | src end | A start | A end  | B start | B end  |
|------------|-----------|---------|---------|--------|---------|--------|
| runtime,   | 62.280 | 62.690 | 11.907 | 12.317 | 11.740 | 12.150 |
| libraries, | 62.880 | 63.440 | 12.507 | 13.067 | 12.340 | 12.900 |
| and        | 63.460 | 63.580 | 13.087 | 13.207 | 12.920 | 13.040 |
| config.    | 63.600 | 64.420 | 13.227 | 14.047 | 13.060 | 13.880 |

"break in mysterious ways":  A 17.187 – 18.527   |   B 17.020 – 18.360

| word       | src start | src end | A start | A end  | B start | B end  |
|------------|-----------|---------|---------|--------|---------|--------|
| break      | 67.560 | 67.800 | 17.187 | 17.427 | 17.020 | 17.260 |
| in         | 67.880 | 67.940 | 17.507 | 17.567 | 17.340 | 17.400 |
| mysterious | 68.000 | 68.490 | 17.627 | 18.117 | 17.460 | 17.950 |
| ways.      | 68.580 | 68.900 | 18.207 | 18.527 | 18.040 | 18.360 |

## BUILD
- A window: 18.667 – 26.458   |   B window: 18.500 – 26.292   (source 70.24–78.00)

"packages your app":  A 19.607 – 20.507   |   B 19.440 – 20.340

| word     | src start | src end | A start | A end  | B start | B end  |
|----------|-----------|---------|---------|--------|---------|--------|
| packages | 71.180 | 71.600 | 19.607 | 20.027 | 19.440 | 19.860 |
| your     | 71.640 | 71.820 | 20.067 | 20.247 | 19.900 | 20.080 |
| app      | 71.880 | 72.080 | 20.307 | 20.507 | 20.140 | 20.340 |

"runtime, libraries, settings":  A 22.407 – 23.927   |   B 22.240 – 23.760

| word       | src start | src end | A start | A end  | B start | B end  |
|------------|-----------|---------|---------|--------|---------|--------|
| runtime,   | 73.980 | 74.400 | 22.407 | 22.827 | 22.240 | 22.660 |
| libraries, | 74.580 | 75.040 | 23.007 | 23.467 | 22.840 | 23.300 |
| settings,  | 75.200 | 75.500 | 23.627 | 23.927 | 23.460 | 23.760 |

"one standardized unit":  A 24.727 – 26.367   |   B 24.560 – 26.200
(note: 'unit.' ASR box tail is padded — audio actually decays by A 26.297 / B 26.130)

| word         | src start | src end | A start | A end  | B start | B end  |
|--------------|-----------|---------|---------|--------|---------|--------|
| one          | 76.300 | 76.480 | 24.727 | 24.907 | 24.560 | 24.740 |
| standardized | 76.660 | 77.320 | 25.087 | 25.747 | 24.920 | 25.580 |
| unit.        | 77.580 | 77.940 | 26.007 | 26.367 | 25.840 | 26.200 |

## RUNS
- A window: 26.458 – 33.208   |   B window: 26.292 – 33.042   (source 79.37–86.10)

"runs identically":  A 27.228 – 28.188   |   B 27.062 – 28.022

| word        | src start | src end | A start | A end  | B start | B end  |
|-------------|-----------|---------|---------|--------|---------|--------|
| runs        | 80.140 | 80.360 | 27.228 | 27.448 | 27.062 | 27.282 |
| identically | 80.420 | 81.100 | 27.508 | 28.188 | 27.342 | 28.022 |

"laptop":  A 28.528 – 28.948   |   B 28.362 – 28.782

| word    | src start | src end | A start | A end  | B start | B end  |
|---------|-----------|---------|---------|--------|---------|--------|
| laptop, | 81.440 | 81.860 | 28.528 | 28.948 | 28.362 | 28.782 |

"teammate's machine":  A 29.328 – 30.148   |   B 29.162 – 29.982

| word       | src start | src end | A start | A end  | B start | B end  |
|------------|-----------|---------|---------|--------|---------|--------|
| teammate's | 82.240 | 82.620 | 29.328 | 29.708 | 29.162 | 29.542 |
| machine,   | 82.660 | 83.060 | 29.748 | 30.148 | 29.582 | 29.982 |

"the cloud":  A 30.308 – 30.648   |   B 30.142 – 30.482

| word  | src start | src end | A start | A end  | B start | B end  |
|-------|-----------|---------|---------|--------|---------|--------|
| the   | 83.220 | 83.280 | 30.308 | 30.368 | 30.142 | 30.202 |
| cloud | 83.320 | 83.560 | 30.408 | 30.648 | 30.242 | 30.482 |

## VM
- A window: 33.208 – 42.208   |   B window: 33.042 – 42.042   (source 86.40–95.40)

"shares the host OS kernel":  A 35.148 – 36.588   |   B 34.982 – 36.422

| word    | src start | src end | A start | A end  | B start | B end  |
|---------|-----------|---------|---------|--------|---------|--------|
| shares  | 88.340 | 88.620 | 35.148 | 35.428 | 34.982 | 35.262 |
| the     | 88.680 | 88.760 | 35.488 | 35.568 | 35.322 | 35.402 |
| host    | 88.800 | 89.040 | 35.608 | 35.848 | 35.442 | 35.682 |
| OS      | 89.180 | 89.460 | 35.988 | 36.268 | 35.822 | 36.102 |
| kernel, | 89.520 | 89.780 | 36.328 | 36.588 | 36.162 | 36.422 |

"boots in seconds":  A 37.648 – 38.448   |   B 37.482 – 38.282

| word     | src start | src end | A start | A end  | B start | B end  |
|----------|-----------|---------|---------|--------|---------|--------|
| boots    | 90.840 | 91.060 | 37.648 | 37.868 | 37.482 | 37.702 |
| in       | 91.080 | 91.160 | 37.888 | 37.968 | 37.722 | 37.802 |
| seconds. | 91.240 | 91.640 | 38.048 | 38.448 | 37.882 | 38.282 |

"same box, any ship, any port":  A 40.068 – 42.088   |   B 39.902 – 41.922

| word  | src start | src end | A start | A end  | B start | B end  |
|-------|-----------|---------|---------|--------|---------|--------|
| same  | 93.260 | 93.520 | 40.068 | 40.328 | 39.902 | 40.162 |
| box,  | 93.560 | 93.860 | 40.368 | 40.668 | 40.202 | 40.502 |
| any   | 94.060 | 94.240 | 40.868 | 41.048 | 40.702 | 40.882 |
| ship, | 94.310 | 94.520 | 41.118 | 41.328 | 40.952 | 41.162 |
| any   | 94.740 | 94.960 | 41.548 | 41.768 | 41.382 | 41.602 |
| port. | 94.980 | 95.280 | 41.788 | 42.088 | 41.622 | 41.922 |

## PAYOFF
- A window: 42.208 – 48.208   |   B window: 42.042 – 48.042   (source 106.58–112.55, FINAL take)

"ship the whole kitchen, not just the recipe":  A 42.458 – 44.398   |   B 42.292 – 44.232

| word     | src start | src end  | A start | A end  | B start | B end  |
|----------|-----------|----------|---------|--------|---------|--------|
| ship     | 106.830 | 107.060 | 42.458 | 42.688 | 42.292 | 42.522 |
| the      | 107.070 | 107.160 | 42.698 | 42.788 | 42.532 | 42.622 |
| whole    | 107.200 | 107.380 | 42.828 | 43.008 | 42.662 | 42.842 |
| kitchen, | 107.420 | 107.840 | 43.048 | 43.468 | 42.882 | 43.302 |
| not      | 107.850 | 108.060 | 43.478 | 43.688 | 43.312 | 43.522 |
| just     | 108.100 | 108.270 | 43.728 | 43.898 | 43.562 | 43.732 |
| the      | 108.300 | 108.360 | 43.928 | 43.988 | 43.762 | 43.822 |
| recipe.  | 108.380 | 108.770 | 44.008 | 44.398 | 43.842 | 44.232 |
