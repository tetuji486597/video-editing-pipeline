# ep24-kubernetes — beat windows + payoff-word timings (OUTPUT timeline)

Derived from the stamped `_beat_windows_output_timeline` in edl.A.json / edl.B.json
(fix_windows.py 24fps ceil grid). Word times are ElevenLabs Scribe word boxes mapped
into each variant's output timeline: `out = window_start + (src - range_start)`.
Remember Scribe pads word ENDS on this shoot (see edl reasons); starts are trustworthy,
ends can run long — the two flagged in the table are the proven offenders.

Variant A total 55.083s | Variant B total 53.917s. Content after INTRO is the same
cut in both variants; every B time = A time − 1.1667s.

## INTRO

- Window A: **0.0000 – 5.7917**  (5.7917s)
- Window B: **0.0000 – 4.6250**  (4.6250s)
- (different takes per variant: A = source 33.56–39.35 interview framing, B = source 13.42–18.02 cool-tech framing)

## HOOK

- Window A: **5.7917 – 11.7083**  (5.9166s)
- Window B: **4.6250 – 10.5417**  (5.9167s)

| phrase | source (src s) | A out start–end | B out start–end |
|---|---|---|---|
| three AM | 84.140–84.740 | 6.962–7.562 | 5.795–6.395 |
| no engineer wakes up | 84.940–85.980 | 7.762–8.802 | 6.595–7.635 |
| already handled it | 87.000–88.000 | 9.822–10.822 | 8.655–9.655 |
| Here's how | 88.040–89.760 | 10.862–12.582 | 9.695–11.415 | (ASR boxes 'how.' to src 89.76; true acoustic end src 88.75 = A 11.572 / B 10.405)

<details><summary>word-by-word</summary>

| word | src | A out | B out |
|---|---|---|---|
| three | 84.140–84.320 | 6.962–7.142 | 5.795–5.975 |
| AM | 84.360–84.740 | 7.182–7.562 | 6.015–6.395 |
| no | 84.940–85.010 | 7.762–7.832 | 6.595–6.665 |
| engineer | 85.160–85.520 | 7.982–8.342 | 6.815–7.175 |
| wakes | 85.560–85.760 | 8.382–8.582 | 7.215–7.415 |
| up | 85.820–85.980 | 8.642–8.802 | 7.475–7.635 |
| already | 87.000–87.270 | 9.822–10.092 | 8.655–8.925 |
| handled | 87.300–87.580 | 10.122–10.402 | 8.955–9.235 |
| it. | 87.620–88.000 | 10.442–10.822 | 9.275–9.655 |
| Here's | 88.040–88.190 | 10.862–11.012 | 9.695–9.845 |
| how. | 88.240–89.760 | 11.062–12.582 | 9.895–11.415 |

</details>

## PROBLEM

- Window A: **11.7083 – 21.0000**  (9.2917s)
- Window B: **10.5417 – 19.8333**  (9.2916s)

| phrase | source (src s) | A out start–end | B out start–end |
|---|---|---|---|
| hundreds of containers | 96.280–97.300 | 12.218–13.238 | 11.052–12.072 |
| by hand is impossible | 99.040–100.380 | 14.978–16.318 | 13.812–15.152 |
| restarts crashes | 101.060–101.940 | 16.998–17.878 | 15.832–16.712 |
| scales under load | 102.300–103.080 | 18.238–19.018 | 17.072–17.852 |
| dead hardware | 104.320–104.940 | 20.258–20.878 | 19.092–19.712 |

<details><summary>word-by-word</summary>

| word | src | A out | B out |
|---|---|---|---|
| hundreds | 96.280–96.620 | 12.218–12.558 | 11.052–11.392 |
| of | 96.660–96.800 | 12.598–12.738 | 11.432–11.572 |
| containers | 96.820–97.300 | 12.758–13.238 | 11.592–12.072 |
| by | 99.040–99.180 | 14.978–15.118 | 13.812–13.952 |
| hand | 99.220–99.560 | 15.158–15.498 | 13.992–14.332 |
| is | 99.600–99.770 | 15.538–15.708 | 14.372–14.542 |
| impossible. | 99.780–100.380 | 15.718–16.318 | 14.552–15.152 |
| restarts | 101.060–101.460 | 16.998–17.398 | 15.832–16.232 |
| crashes? | 101.500–101.940 | 17.438–17.878 | 16.272–16.712 |
| scales | 102.300–102.580 | 18.238–18.518 | 17.072–17.352 |
| under | 102.640–102.780 | 18.578–18.718 | 17.412–17.552 |
| load? | 102.840–103.080 | 18.778–19.018 | 17.612–17.852 |
| dead | 104.320–104.480 | 20.258–20.418 | 19.092–19.252 |
| hardware? | 104.540–104.940 | 20.478–20.878 | 19.312–19.712 |

</details>

## BUILD

- Window A: **21.0000 – 28.2500**  (7.2500s)
- Window B: **19.8333 – 27.0833**  (7.2500s)

| phrase | source (src s) | A out start–end | B out start–end |
|---|---|---|---|
| orchestrator | 107.520–108.100 | 22.170–22.750 | 21.003–21.583 |
| desired state | 108.880–109.620 | 23.530–24.270 | 22.363–23.103 |
| ten copies | 110.330–110.930 | 24.980–25.580 | 23.813–24.413 |
| makes reality match | 112.400–113.340 | 27.050–27.990 | 25.883–26.823 |

<details><summary>word-by-word</summary>

| word | src | A out | B out |
|---|---|---|---|
| orchestrator. | 107.520–108.100 | 22.170–22.750 | 21.003–21.583 |
| desired | 108.880–109.280 | 23.530–23.930 | 22.363–22.763 |
| state, | 109.360–109.620 | 24.010–24.270 | 22.843–23.103 |
| ten | 110.330–110.500 | 24.980–25.150 | 23.813–23.983 |
| copies | 110.600–110.930 | 25.250–25.580 | 24.083–24.413 |
| makes | 112.400–112.570 | 27.050–27.220 | 25.883–26.053 |
| reality | 112.660–113.000 | 27.310–27.650 | 26.143–26.483 |
| match. | 113.080–113.340 | 27.730–27.990 | 26.563–26.823 |

</details>

## CONTROL

- Window A: **28.2500 – 41.6667**  (13.4167s)
- Window B: **27.0833 – 40.5000**  (13.4167s)

| phrase | source (src s) | A out start–end | B out start–end |
|---|---|---|---|
| actual versus desired | 156.600–157.650 | 30.030–31.080 | 28.863–29.913 |
| container dies | 158.040–158.750 | 31.470–32.180 | 30.303–31.013 |
| machine fails | 159.780–160.380 | 33.210–33.810 | 32.043–32.643 |
| auto-scales up | 163.860–164.580 | 37.290–38.010 | 36.123–36.843 |
| air traffic controller that never sleeps | 166.040–167.900 | 39.470–41.330 | 38.303–40.163 |

<details><summary>word-by-word</summary>

| word | src | A out | B out |
|---|---|---|---|
| actual | 156.600–156.900 | 30.030–30.330 | 28.863–29.163 |
| versus | 156.920–157.200 | 30.350–30.630 | 29.183–29.463 |
| desired. | 157.220–157.650 | 30.650–31.080 | 29.483–29.913 |
| container | 158.040–158.380 | 31.470–31.810 | 30.303–30.643 |
| dies, | 158.420–158.750 | 31.850–32.180 | 30.683–31.013 |
| machine | 159.780–160.040 | 33.210–33.470 | 32.043–32.303 |
| fails, | 160.120–160.380 | 33.550–33.810 | 32.383–32.643 |
| auto-scales | 163.860–164.380 | 37.290–37.810 | 36.123–36.643 |
| up, | 164.480–164.580 | 37.910–38.010 | 36.743–36.843 |
| air | 166.040–166.160 | 39.470–39.590 | 38.303–38.423 |
| traffic | 166.200–166.440 | 39.630–39.870 | 38.463–38.703 |
| controller | 166.480–166.900 | 39.910–40.330 | 38.743–39.163 |
| that | 167.020–167.160 | 40.450–40.590 | 39.283–39.423 |
| never | 167.180–167.400 | 40.610–40.830 | 39.443–39.663 |
| sleeps. | 167.480–167.900 | 40.910–41.330 | 39.743–40.163 |

</details>

## AI_ANGLE

- Window A: **41.6667 – 49.0000**  (7.3333s)
- Window B: **40.5000 – 47.8333**  (7.3333s)

| phrase | source (src s) | A out start–end | B out start–end |
|---|---|---|---|
| GPU workloads | 173.400–174.310 | 44.797–45.707 | 43.630–44.540 |
| huge clusters | 175.900–176.720 | 47.297–48.117 | 46.130–46.950 | (ASR end src 176.72; acoustic sibilant tail to src 177.49 = A 48.887 / B 47.720)

<details><summary>word-by-word</summary>

| word | src | A out | B out |
|---|---|---|---|
| GPU | 173.400–173.820 | 44.797–45.217 | 43.630–44.050 |
| workloads | 173.860–174.310 | 45.257–45.707 | 44.090–44.540 |
| huge | 175.900–176.240 | 47.297–47.637 | 46.130–46.470 |
| clusters. | 176.260–176.720 | 47.657–48.117 | 46.490–46.950 |

</details>

## PAYOFF

- Window A: **49.0000 – 55.0833**  (6.0833s)
- Window B: **47.8333 – 53.9167**  (6.0834s)

| phrase | source (src s) | A out start–end | B out start–end |
|---|---|---|---|
| robot that babysits your servers | 179.460–181.040 | 50.090–51.670 | 48.923–50.503 |

<details><summary>word-by-word</summary>

| word | src | A out | B out |
|---|---|---|---|
| robot | 179.460–179.800 | 50.090–50.430 | 48.923–49.263 |
| that | 179.810–179.970 | 50.440–50.600 | 49.273–49.433 |
| babysits | 180.000–180.460 | 50.630–51.090 | 49.463–49.923 |
| your | 180.520–180.620 | 51.150–51.250 | 49.983–50.083 |
| servers. | 180.660–181.040 | 51.290–51.670 | 50.123–50.503 |

</details>

