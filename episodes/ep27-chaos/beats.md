# EP27 beats -- output-timeline word times

Source: `edl.json` (windows stamped by `fix_windows.py`, 24fps ceil grid). 
word_out = word_source_start - range_start + window_start. Word END column is the ASR box end mapped the same way -- 
Scribe pads box ends on this shoot, so treat END as an upper bound and START as the sync point.

Total duration: 52.7917s


## HOOK  -- output 0.0000 -> 6.3750  (6.3750s)   source 4.28 -> 10.64

| phrase | source start | out start | out end (ASR box) |
|---|---|---|---|
| Six, | 4.460 | 0.180 | 0.480 |
| seven. | 4.800 | 0.520 | 1.000 |
| break Netflix | 8.240 | 3.960 | 4.580 |
| on purpose | 8.920 | 4.640 | 5.520 |
| what the skibidi | 9.860 | 5.580 | 6.220 |

## PROBLEM  -- output 6.3750 -> 17.8750  (11.5000s)   source 17.13 -> 28.62

| phrase | source start | out start | out end (ASR box) |
|---|---|---|---|
| never goes down | 19.600 | 8.845 | 9.605 |
| Among Us | 21.480 | 10.725 | 11.205 |
| three AM | 21.980 | 11.225 | 11.825 |
| crashing out | 25.520 | 14.765 | 15.805 |
| capping | 26.920 | 16.165 | 16.505 |
| aura loss | 27.820 | 17.065 | 17.705 |

## BUILD  -- output 17.8750 -> 28.7083  (10.8333s)   source 33.22 -> 44.05

| phrase | source start | out start | out end (ASR box) |
|---|---|---|---|
| cook it ourselves | 34.600 | 19.255 | 19.975 |
| Chaos Monkey | 36.660 | 21.315 | 22.145 |
| unplugs a server | 37.980 | 22.635 | 23.495 |
| middle of the day | 39.120 | 23.775 | 24.365 |
| diabolical | 42.340 | 26.995 | 27.625 |
| let him cook | 43.460 | 28.115 | 28.655 |

## NEW_COMPONENT  -- output 28.7083 -> 47.5417  (18.8334s)   source 85.10 -> 103.93

| phrase | source start | out start | out end (ASR box) |
|---|---|---|---|
| chaos engineering | 86.440 | 30.048 | 30.948 |
| unalive this box | 88.490 | 32.098 | 32.978 |
| slime out | 90.880 | 34.488 | 34.878 |
| W rizz | 93.480 | 37.088 | 37.648 |
| found out at lunch | 96.500 | 40.108 | 40.848 |
| Diddy party | 98.240 | 41.848 | 42.708 |
| yeeting | 100.420 | 44.028 | 44.338 |
| Ohio of boxes | 102.560 | 46.168 | 48.388 (ASR pad -- acoustic end of speech is source 103.81 = out 47.418; the beat window ends 47.542) |

## PAYOFF  -- output 47.5417 -> 52.7917  (5.2500s)   source 108.51 -> 113.72

| phrase | source start | out start | out end (ASR box) |
|---|---|---|---|
| break your own stuff | 108.780 | 47.812 | 48.652 |
| can't break you at night | 110.260 | 49.292 | 50.092 |
| types like an unk | 112.840 | 51.872 | 52.632 (acoustic end source 113.60 = out 52.632, agrees) |

## Notes

- Internal dead air: none >0.8s in any range. Longest internal gaps are the 0.43s breath inside BUILD
  (source 35.41-35.84, out ~20.07-20.50, between "ourselves." and "That robot's") and the 0.36s turn
  inside PROBLEM after "three AM," (source 22.61-22.97, out ~11.86-12.22).
- Edge flags: ASR "Six," starts 110ms LATE (acoustic onset 4.33 vs ASR 4.46); ASR "boxes." is boxed
  1.50s long (103.28-104.78) against an acoustic end of 103.81. All other edges agree with the ASR
  within 60ms. See each range's "reason" in edl.json.
