# EP25 (CI/CD) -- beat windows + payoff-word timings, OUTPUT timeline

Derived from the stamped `_beat_windows_output_timeline` in edl.A.json / edl.B.json
(24fps ceil grid, fix_windows.py) and the cached word-level transcript
(`transcripts/ep25.json`). Word boxes are Scribe's; range EDGES were measured
acoustically (see `_dead_air_note` in the EDLs). Scribe pads final-word boxes on this
shoot, so treat a phrase's trailing `end` as an upper bound -- the voice can stop up to
~200ms earlier (worst offenders flagged inline; the pathological case is the B-intro's
'CI/CD.' boxed 2.6s wide, cut acoustically in the EDL).
Everything after INTRO is 0.5417s earlier in B than in A (B's intro segment is 4.500s
vs A's 5.042s on the 24fps grid). Word rows below are variant A; for variant B subtract
0.5417 from every A time, or use the output-B phrase column.

## INTRO
- window A: 0.0000 - 5.0417  (source 33.73-38.76, 'prepping you for your system design interview')
- window B: 0.0000 - 4.5000  (source 18.88-23.38, 'Exploring Really Cool Tech', second cool-tech take)
- no overlay payoff phrases requested for this beat

## HOOK  (source 55.80-62.00)
- window A: 5.0417 - 11.2500
- window B: 4.5000 - 10.7083

| phrase | source | output A | output B | per-word (output A / output B = A - 0.5417) |
|---|---|---|---|---|
| thousands of times a day | 57.38-58.70 | 6.622-7.942 | 6.080-7.400 | thousands 6.62-7.08, of 7.14-7.24, times 7.30-7.57, a 7.62-7.66, day 7.74-7.94 |
| rarely break | 59.04-59.70 | 8.282-8.942 | 7.740-8.400 | rarely 8.28-8.58, break. 8.68-8.94 |
| CI/CD (acoustic end 61.87 -- box is honest here) | 61.28-61.88 | 10.522-11.122 | 9.980-10.580 | CI/CD. 10.52-11.12 |

## PROBLEM  (source 69.00-77.98)
- window A: 11.2500 - 20.2500
- window B: 10.7083 - 19.7083

| phrase | source | output A | output B | per-word (output A / output B = A - 0.5417) |
|---|---|---|---|---|
| months of changes | 72.06-72.92 | 14.310-15.170 | 13.768-14.628 | months 14.31-14.51, of 14.55-14.67, changes 14.71-15.17 |
| release day | 74.18-74.84 | 16.430-17.090 | 15.888-16.548 | release 16.43-16.79, day 16.83-17.09 |
| everyone prays | 75.14-76.02 | 17.390-18.270 | 16.848-17.728 | everyone 17.39-17.81, prays. 17.87-18.27 |
| big batches, big risk (acoustic end of 'risk.' is 77.77, ~160ms before the box) | 76.50-77.93 | 18.750-20.180 | 18.208-19.638 | Big 18.75-18.89, batches, 18.99-19.42, big 19.71-19.87, risk. 19.91-20.18 |

## CI  (source 79.26-84.14)
- window A: 20.2500 - 25.1667
- window B: 19.7083 - 24.6250

| phrase | source | output A | output B | per-word (output A / output B = A - 0.5417) |
|---|---|---|---|---|
| automatically built and tested | 81.64-83.10 | 22.630-24.090 | 22.088-23.548 | automatically 22.63-23.23, built 23.24-23.53, and 23.54-23.68, tested 23.73-24.09 |
| moment it's merged (acoustic end of 'merged.' is 84.01, ~150ms before the box) | 83.28-84.16 | 24.270-25.150 | 23.728-24.608 | moment 24.27-24.59, it's 24.65-24.80, merged. 24.83-25.15 |

## CD  (source 86.98-95.98)
- window A: 25.1667 - 34.1667
- window B: 24.6250 - 33.6250

| phrase | source | output A | output B | per-word (output A / output B = A - 0.5417) |
|---|---|---|---|---|
| automated pipeline | 89.76-90.64 | 27.947-28.827 | 27.405-28.285 | automated 27.95-28.41, pipeline. 28.45-28.83 |
| build, test, security scan, deploy | 91.08-93.24 | 29.267-31.427 | 28.725-30.885 | Build, 29.27-29.48, test, 29.77-30.05, security 30.15-30.59, scan, 30.69-31.01, deploy, 31.09-31.43 |
| no human hands (acoustic end of 'hands.' is 95.85, ~130ms before the box) | 95.14-95.98 | 33.327-34.167 | 32.785-33.625 | no 33.33-33.45, human 33.55-33.77, hands. 33.85-34.17 |

## ROLLBACK  (source 96.40-101.12)
- window A: 34.1667 - 38.9167
- window B: 33.6250 - 38.3750

| phrase | source | output A | output B | per-word (output A / output B = A - 0.5417) |
|---|---|---|---|---|
| easy to test and roll back | 97.82-99.16 | 35.587-36.927 | 35.045-36.385 | easy 35.59-35.85, to 35.89-36.01, test 36.05-36.29, and 36.33-36.41, roll 36.47-36.61, back, 36.71-36.93 |
| stops being scary (acoustic end of 'scary.' is 100.99) | 100.02-101.08 | 37.787-38.847 | 37.245-38.305 | stops 37.79-38.07, being 38.15-38.39, scary. 38.43-38.85 |

## AI_ANGLE  (source 102.90-108.75)
- window A: 38.9167 - 44.7917
- window B: 38.3750 - 44.2500

| phrase | source | output A | output B | per-word (output A / output B = A - 0.5417) |
|---|---|---|---|---|
| auto-reviewing code | 105.12-106.12 | 41.137-42.137 | 40.595-41.595 | auto-reviewing 41.14-41.76, code 41.82-42.14 |
| generating tests | 106.34-107.18 | 42.357-43.197 | 41.815-42.655 | generating 42.36-42.84, tests 42.88-43.20 |

## PAYOFF  (source 111.38-118.10)
- window A: 44.7917 - 51.5417
- window B: 44.2500 - 51.0000

| phrase | source | output A | output B | per-word (output A / output B = A - 0.5417) |
|---|---|---|---|---|
| automate the scary parts | 111.78-112.92 | 45.192-46.332 | 44.650-45.790 | automate 45.19-45.57, the 45.58-45.69, scary 45.71-45.95, parts 46.07-46.33 |

