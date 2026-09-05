# ep21-kanonymity — beats

Output windows stamped by `fix_windows.py --write` (24fps extract grid). Word timings below are
in OUTPUT-timeline seconds: `out = window_start + (src - range_start)`, using the ASR word boxes;
remember Scribe pads box ENDS (see per-beat notes and the EDL `reason` fields for the acoustic truth).

## BLOOPER

- A window: **0.0000 - 2.8333**  |  B window: **0.0000 - 2.8333**  (src 53.53-56.36)
- Cold-open gag, precedes the intro per STYLE.md's EP7 blooper rule. Internal 0.41s beat (out A 1.72-2.13) between 'Ana-anonymity.' and the clean third 'Anonymity.' is kept.

## INTRO

- A window: **2.8333 - 8.1667** (src 67.55-72.85)
- B window: **2.8333 - 7.6667** (src 21.14-25.96)
- A = interview take (only complete one). B = cool-tech take at src 21.24, chosen over the 13.30 take: the 13.30 take has pre-speech noise from ~13.01 and its final 'k-anonymity.' is boxed 1.34s past the acoustic stop (17.92 vs 19.26).

## HOOK

- A window: **8.1667 - 14.9167**  |  B window: **7.6667 - 14.4167**  (src 83.0-89.75)
- ASR boxes "isn't." to src 90.40; acoustic stop is 89.60. Range ends 150ms after the acoustic stop.

**"leaked in a breach"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| leaked | 10.067 | 10.387 | 9.567 | 9.887 |
| in | 10.427 | 10.487 | 9.927 | 9.987 |
| a | 10.527 | 10.537 | 10.027 | 10.037 |
| breach | 10.627 | 10.947 | 10.127 | 10.447 |

**"without you ever sending"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| without | 10.987 | 11.347 | 10.487 | 10.847 |
| you | 11.407 | 11.527 | 10.907 | 11.027 |
| ever | 11.587 | 11.787 | 11.087 | 11.287 |
| sending | 11.827 | 12.117 | 11.327 | 11.617 |

**"impossible, but it isn't"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| impossible, | 13.487 | 14.127 | 12.987 | 13.627 |
| but | 14.147 | 14.227 | 13.647 | 13.727 |
| it | 14.287 | 14.377 | 13.787 | 13.877 |
| isn't. | 14.427 | 15.567 | 13.927 | 15.067 |

NOTE: "isn't." end above is the padded ASR box (runs past the cut). Acoustic end = src 89.60 -> out A **14.767** / B **14.267**; the beat window ends A 14.917 / B 14.417.

## PROBLEM

- A window: **14.9167 - 24.0833**  |  B window: **14.4167 - 23.5833**  (src 98.1-107.25)
- Ends right after 'catch-22.' (acoustic stop src 107.09; ASR box ran to 108.14). The trailing false start 'Here's the trick. Your device hashes the ha...' is excluded.

**"hundreds of millions"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| hundreds | 16.337 | 16.657 | 15.837 | 16.157 |
| of | 16.677 | 16.757 | 16.177 | 16.257 |
| millions | 16.817 | 17.157 | 16.317 | 16.657 |

**"even hashed"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| even | 19.957 | 20.197 | 19.457 | 19.697 |
| hashed, | 20.257 | 20.667 | 19.757 | 20.167 |

**"catch-22"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| catch-22. | 23.157 | 24.957 | 22.657 | 24.457 |

NOTE: "catch-22." end above is the padded ASR box (runs past the cut). Acoustic end = src 107.09 -> out A **23.907** / B **23.407**; the beat window ends A 24.083 / B 23.583.

## BUILD

- A window: **24.0833 - 30.7083**  |  B window: **23.5833 - 30.2083**  (src 117.48-124.08)
- Clean retake of the sentence PROBLEM fumbled.

**"hashes the password locally"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| hashes | 25.523 | 25.783 | 25.023 | 25.283 |
| the | 25.903 | 25.963 | 25.403 | 25.463 |
| password | 26.003 | 26.363 | 25.503 | 25.863 |
| locally, | 26.463 | 26.973 | 25.963 | 26.473 |

**"first five characters"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| first | 27.843 | 28.213 | 27.343 | 27.713 |
| five | 28.243 | 28.493 | 27.743 | 27.993 |
| characters | 28.523 | 28.883 | 28.023 | 28.383 |

**"just the prefix"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| just | 29.703 | 29.833 | 29.203 | 29.333 |
| the | 29.863 | 29.943 | 29.363 | 29.443 |
| prefix. | 29.963 | 30.483 | 29.463 | 29.983 |

## SCAN

- A window: **30.7083 - 37.4583**  |  B window: **30.2083 - 36.9583**  (src 145.06-151.78)
- First half of the long 145.18-162.46 take; butts against KANON at src 151.78 exactly (zero-gap split between 'locally.' and 'The').

**"hundreds of them"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| hundreds | 34.218 | 34.528 | 33.718 | 34.028 |
| of | 34.568 | 34.637 | 34.068 | 34.137 |
| them, | 34.668 | 35.098 | 34.168 | 34.598 |

**"checks for a match locally"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| checks | 35.748 | 35.988 | 35.248 | 35.488 |
| for | 36.028 | 36.118 | 35.528 | 35.618 |
| a | 36.128 | 36.188 | 35.628 | 35.688 |
| match | 36.228 | 36.488 | 35.728 | 35.988 |
| locally. | 36.548 | 37.408 | 36.048 | 36.908 |

## KANON

- A window: **37.4583 - 48.2500**  |  B window: **36.9583 - 47.7500**  (src 151.78-162.56)
- Second half of the same take, contiguous at src 151.78. 'k-anonymity' acoustic end is src 158.29 (ASR box 158.799); 0.53s beat before 'Browsers' kept.

**"never tell"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| never | 38.018 | 38.208 | 37.518 | 37.708 |
| tell | 38.238 | 38.468 | 37.738 | 37.968 |

**"hidden in a crowd"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| hidden | 40.558 | 40.778 | 40.058 | 40.278 |
| in | 40.818 | 40.878 | 40.318 | 40.378 |
| a | 40.888 | 40.918 | 40.388 | 40.418 |
| crowd, | 41.018 | 41.278 | 40.518 | 40.778 |

**"k-anonymity"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| k-anonymity. | 43.018 | 44.477 | 42.518 | 43.977 |

NOTE: "k-anonymity." end above is the padded ASR box. Acoustic end = src 158.29 -> out A **43.968** / B **43.468** (then a 0.53s beat before "Browsers").

**"browsers use this exact scheme"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| Browsers | 44.498 | 44.898 | 43.998 | 44.398 |
| use | 44.978 | 45.118 | 44.478 | 44.618 |
| this | 45.158 | 45.287 | 44.658 | 44.787 |
| exact | 45.318 | 45.678 | 44.818 | 45.178 |
| scheme | 45.718 | 46.038 | 45.218 | 45.538 |

## PAYOFF

- A window: **48.2500 - 54.5833**  |  B window: **47.7500 - 54.0833**  (src 205.48-211.78)
- Final take; all earlier closes are false starts / off-script wordings.

**"send a crowd it can hide in"**

| word | A start | A end | B start | B end |
|---|---|---|---|---|
| Send | 49.570 | 49.710 | 49.070 | 49.210 |
| a | 49.750 | 49.790 | 49.250 | 49.290 |
| crowd | 49.850 | 50.170 | 49.350 | 49.670 |
| it | 50.190 | 50.250 | 49.690 | 49.750 |
| can | 50.290 | 50.410 | 49.790 | 49.910 |
| hide | 50.470 | 50.650 | 49.970 | 50.150 |
| in. | 50.670 | 50.830 | 50.170 | 50.330 |

## Dead-air audit (kept ranges)

Acoustic scan (find_dead_air, 0.3s min, -18dB drop) inside kept ranges: BLOOPER 0.41s (55.25-55.66,
the gag beat), PROBLEM 0.36s (103.89-104.25, after 'hashed,'), KANON 0.53s (158.29-158.83, before
'Browsers'). **No internal dead air >= 0.8s in any kept range.**
