# ep20-tokenization — beat windows and key-phrase word timings

Windows are the stamped `_beat_windows_output_timeline` from `fix_windows.py --write`
(24fps grid, `ceil(nominal*24)/24` per segment). Word output times below are
`word_source_start - range_start + segment_offset`, where segment offsets are the same
cumulative quantized durations fix_windows uses — so every B time is exactly
**5.000s earlier** than its A time (A's INTRO quantizes to exactly 5.000s).

Word source times are ASR starts from `transcripts/ep20.json`; phrase END times are the
ASR end of the last word (flagged where acoustics disagree — see edl reasons).

## Beat windows (output timeline, seconds)

| Beat          | A window          | B window          | dur (s) | source range     |
|---------------|-------------------|-------------------|---------|------------------|
| INTRO         | 0.0000 – 5.0000   | —                 | 5.0000  | 13.80 – 18.76    |
| HOOK          | 5.0000 – 11.7917  | 0.0000 – 6.7917   | 6.7917  | 21.82 – 28.58    |
| PROBLEM       | 11.7917 – 20.2500 | 6.7917 – 15.2500  | 8.4583  | 34.40 – 42.84    |
| BUILD         | 20.2500 – 29.4583 | 15.2500 – 24.4583 | 9.2083  | 61.52 – 70.70    |
| NEW_COMPONENT | 29.4583 – 38.2083 | 24.4583 – 33.2083 | 8.7500  | 79.28 – 88.00    |
| TOKENS        | 38.2083 – 44.1667 | 33.2083 – 39.1667 | 5.9583  | 102.84 – 108.79  |
| PAYOFF        | 44.1667 – 51.6667 | 39.1667 – 46.6667 | 7.5000  | 111.34 – 118.82  |

Totals: **A = 51.6667s**, **B = 46.6667s**.

## HOOK (range start 21.82; offset A +5.0000, B +0.0000)

### "get it wrong"
| word   | source start | out A  | out B  |
|--------|--------------|--------|--------|
| get    | 25.820       | 9.000  | 4.000  |
| it     | 25.940       | 9.120  | 4.120  |
| wrong  | 26.080       | 9.260  | 4.260  |
| (end)  | 26.380       | 9.560  | 4.560  |

### "seen the word strawberry"
| word         | source start | out A  | out B  |
|--------------|--------------|--------|--------|
| seen         | 27.540       | 10.720 | 5.720  |
| the          | 27.760       | 10.940 | 5.940  |
| word         | 27.860       | 11.040 | 6.040  |
| strawberry.  | 28.100       | 11.280 | 6.280  |
| (end)        | 28.520       | 11.700 | 6.700  |

## PROBLEM (range start 34.40; offset A +11.7917, B +6.7917)

### "letter by letter"
| word    | source start | out A  | out B  |
|---------|--------------|--------|--------|
| letter  | 36.720       | 14.112 | 9.112  |
| by      | 36.940       | 14.332 | 9.332  |
| letter  | 37.100       | 14.492 | 9.492  |
| (end)   | 37.320       | 14.712 | 9.712  |

### "vocabulary of millions"
| word        | source start | out A  | out B  |
|-------------|--------------|--------|--------|
| vocabulary  | 39.560       | 16.952 | 11.952 |
| of          | 40.220       | 17.612 | 12.612 |
| millions,   | 40.400       | 17.792 | 12.792 |
| (end)       | 40.700       | 18.092 | 13.092 |

### "unknown word"
| word     | source start | out A  | out B  |
|----------|--------------|--------|--------|
| unknown  | 42.140       | 19.532 | 14.532 |
| word.    | 42.540       | 19.932 | 14.932 |
| (end)    | 42.760       | 20.152 | 15.152 |

## BUILD (range start 61.52; offset A +20.2500, B +15.2500)

### "chops text into tokens"
| word     | source start | out A  | out B  |
|----------|--------------|--------|--------|
| chops    | 62.940       | 21.670 | 16.670 |
| text     | 63.260       | 21.990 | 16.990 |
| into     | 63.620       | 22.350 | 17.350 |
| tokens,  | 63.810       | 22.540 | 17.540 |
| (end)    | 64.239       | 22.969 | 17.969 |

### "straw and berry"
| word    | source start | out A  | out B  |
|---------|--------------|--------|--------|
| straw   | 69.840       | 28.570 | 23.570 |
| and     | 70.180       | 28.910 | 23.910 |
| berry.  | 70.340       | 29.070 | 24.070 |
| (end)   | 70.660       | 29.390 | 24.390 |

Note: 'berry.' actually stops acoustically at source 70.61 (out A 29.340 / B 24.340);
the ASR box end 70.66 is a slight overrun.

## NEW_COMPONENT (range start 79.28; offset A +29.4583, B +24.4583)

### "token ID numbers"
| word      | source start | out A  | out B  |
|-----------|--------------|--------|--------|
| token     | 81.680       | 31.858 | 26.858 |
| ID        | 82.120       | 32.298 | 27.298 |
| numbers,  | 82.430       | 32.608 | 27.608 |
| (end)     | 82.800       | 32.978 | 27.978 |

### "only ever heard spoken"
| word     | source start | out A  | out B  |
|----------|--------------|--------|--------|
| only     | 86.580       | 36.758 | 31.758 |
| ever     | 86.820       | 36.998 | 31.998 |
| heard    | 87.040       | 37.218 | 32.218 |
| spoken.  | 87.400       | 37.578 | 32.578 |
| (end)    | 87.680*      | 37.858 | 32.858 |

*Acoustic end. The ASR box runs to 88.24 but that overlaps the excluded false start's
onset region — do NOT cue anything off the ASR end here (see edl reason).

## TOKENS (range start 102.84; offset A +38.2083, B +33.2083)

### "measured in tokens"
| word      | source start | out A  | out B  |
|-----------|--------------|--------|--------|
| measured  | 105.220      | 40.588 | 35.588 |
| in        | 105.500      | 40.868 | 35.868 |
| tokens.   | 105.660      | 41.028 | 36.028 |
| (end)     | 106.120      | 41.488 | 36.488 |

### "the only unit the model actually reads"
| word      | source start | out A  | out B  |
|-----------|--------------|--------|--------|
| the       | 106.620      | 41.988 | 36.988 |
| only      | 106.840      | 42.208 | 37.208 |
| unit      | 107.160      | 42.528 | 37.528 |
| the       | 107.420      | 42.788 | 37.788 |
| model     | 107.540      | 42.908 | 37.908 |
| actually  | 107.940      | 43.308 | 38.308 |
| reads.    | 108.420      | 43.788 | 38.788 |
| (end)     | 108.750      | 44.118 | 39.118 |

## PAYOFF (range start 111.34; offset A +44.1667, B +39.1667)

### "chunks with ID numbers"
| word      | source start | out A  | out B  |
|-----------|--------------|--------|--------|
| chunks    | 113.350      | 46.177 | 41.177 |
| with      | 113.800      | 46.627 | 41.627 |
| ID        | 114.020      | 46.847 | 41.847 |
| numbers.  | 114.240      | 47.067 | 42.067 |
| (end)     | 114.580      | 47.407 | 42.407 |
