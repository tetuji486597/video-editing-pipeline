# EP22 webhooks -- beat windows + payoff-word timings (OUTPUT timeline)

Derived from the stamped `_beat_windows_output_timeline` in edl.A.json / edl.B.json
(24fps extract grid, fix_windows.py --write) and the cached word-level transcript.
output_time = beat_window_start + (source_word_time - range_source_start).
Everything after INTRO is **1.125s earlier in B** (B's intro take is shorter: 4.4167s vs 5.5417s).

## INTRO
- window A: 0.0000 - 5.5417  |  window B: 0.0000 - 4.4167
- A source 42.36-47.9 (interview intro) | B source 10.4-14.8 (cool-tech intro)

## HOOK
- window A: 5.5417 - 10.2500  |  window B: 4.4167 - 9.1250
- source range 52.28-56.98 (same take both variants)
- **"the instant it happens"**  A 7.211 - 8.282  |  B 6.086 - 7.157
    - the          A   7.211 -   7.362   B   6.086 -   6.237
    - instant      A   7.402 -   7.682   B   6.277 -   6.557
    - it           A   7.742 -   7.822   B   6.617 -   6.697
    - happens      A   7.922 -   8.282   B   6.797 -   7.157
- **"without ever checking"**  A 8.322 - 9.202  |  B 7.197 - 8.077
    - without      A   8.322 -   8.562   B   7.197 -   7.437
    - ever         A   8.602 -   8.802   B   7.477 -   7.677
    - checking.    A   8.842 -   9.202   B   7.717 -   8.077
- **"That's called a webhook"**  A 9.362 - 10.102  |  B 8.237 - 8.977
    - That's       A   9.362 -   9.492   B   8.237 -   8.367
    - called       A   9.522 -   9.632   B   8.397 -   8.507
    - a            A   9.662 -   9.702   B   8.537 -   8.577
    - webhook.     A   9.722 -  10.102   B   8.597 -   8.977

## PROBLEM
- window A: 10.2500 - 18.7500  |  window B: 9.1250 - 17.6250
- source range 64.2-72.68 (same take both variants)
- **"anything new"**  A 13.300 - 14.080  |  B 12.175 - 12.955
    - "Anything    A  13.300 -  13.670   B  12.175 -  12.545
    - new?"        A  13.690 -  14.080   B  12.565 -  12.955
- **"thousands of wasted calls"**  A 16.030 - 17.180  |  B 14.905 - 16.055
    - thousands    A  16.030 -  16.390   B  14.905 -  15.265
    - of           A  16.430 -  16.530   B  15.305 -  15.405
    - wasted       A  16.570 -  16.850   B  15.445 -  15.725
    - calls        A  16.890 -  17.180   B  15.765 -  16.055
- **"one event"**  A 18.050 - 18.690  |  B 16.925 - 17.565
    - one          A  18.050 -  18.230   B  16.925 -  17.105
    - event.       A  18.290 -  18.690   B  17.165 -  17.565

## BUILD
- window A: 18.7500 - 24.6250  |  window B: 17.6250 - 23.5000
- source range 74.88-80.72 (same take both variants)
- **"flips the direction"**  A 19.550 - 20.410  |  B 18.425 - 19.285
    - flips        A  19.550 -  19.790   B  18.425 -  18.665
    - the          A  19.800 -  19.880   B  18.675 -  18.755
    - direction.   A  19.930 -  20.410   B  18.805 -  19.285
- **"hand the payment provider a URL"**  A 20.810 - 22.430  |  B 19.685 - 21.305
    - hand         A  20.810 -  20.970   B  19.685 -  19.845
    - the          A  21.010 -  21.110   B  19.885 -  19.985
    - payment      A  21.150 -  21.470   B  20.025 -  20.345
    - provider     A  21.510 -  21.870   B  20.385 -  20.745
    - a            A  21.890 -  21.970   B  20.765 -  20.845
    - URL          A  22.110 -  22.430   B  20.985 -  21.305
- **"call me when something happens"**  A 23.160 - 24.430  |  B 22.035 - 23.305
    - "Call        A  23.160 -  23.330   B  22.035 -  22.205
    - me           A  23.390 -  23.490   B  22.265 -  22.365
    - when         A  23.510 -  23.630   B  22.385 -  22.505
    - something    A  23.670 -  23.950   B  22.545 -  22.825
    - happens."    A  24.050 -  24.430   B  22.925 -  23.305

## POST
- window A: 24.6250 - 32.8750  |  window B: 23.5000 - 31.7500
- source range 83.14-91.39 (same take both variants)
- **"HTTP POST"**  A 27.665 - 28.785  |  B 26.540 - 27.660
    - HTTP         A  27.665 -  28.185   B  26.540 -  27.060
    - POST         A  28.305 -  28.785   B  27.180 -  27.660
- **"actually work to do"**  A 31.985 - 32.855  |  B 30.860 - 31.730
    - actually     A  31.985 -  32.225   B  30.860 -  31.100
    - work         A  32.285 -  32.475   B  31.160 -  31.350
    - to           A  32.475 -  32.625   B  31.350 -  31.500
    - do,          A  32.665 -  32.855   B  31.540 -  31.730

## SIGN
- window A: 32.8750 - 38.9583  |  window B: 31.7500 - 37.8333
- source range 91.39-97.44 (same take both variants)
- **"sign each call"**  A 35.785 - 36.385  |  B 34.660 - 35.260
    - sign         A  35.785 -  36.005   B  34.660 -  34.880
    - each         A  36.045 -  36.225   B  34.920 -  35.100
    - call.        A  36.265 -  36.385   B  35.140 -  35.260
- **"verify the signature"**  A 36.725 - 37.625  |  B 35.600 - 36.500
    - verify       A  36.725 -  37.045   B  35.600 -  35.920
    - the          A  37.085 -  37.165   B  35.960 -  36.040
    - signature    A  37.185 -  37.625   B  36.060 -  36.500
- **"really them"**  A 38.345 - 39.785  |  B 37.220 - 38.660
    - really       A  38.345 -  38.585   B  37.220 -  37.460
    - them.        A  38.625 -  39.785   B  37.500 -  38.660  (ASR box end 39.785 A / 38.660 B overruns the beat; acoustic end 38.805 A / 37.680 B)

## PAYOFF
- window A: 38.9583 - 45.7500  |  window B: 37.8333 - 44.6250
- source range 121.34-128.1 (same take both variants)
- **"the server calls you"**  A 40.538 - 41.338  |  B 39.413 - 40.213
    - The          A  40.538 -  40.618   B  39.413 -  39.493
    - server       A  40.658 -  40.898   B  39.533 -  39.773
    - calls        A  40.918 -  41.158   B  39.793 -  40.033
    - you.         A  41.238 -  41.338   B  40.113 -  40.213

## Notes for overlay/SFX cueing
- POST -> SIGN is a zero-gap split inside one take at source 91.39; SIGN's window starts exactly where POST's ends in both variants (no quantization slack: POST's 8.25s span is frame-exact at 24fps).
- 'them.' in SIGN: ASR boxes it to source 98.30 but the audio decays by 97.32; anything cued to that word should land on its onset (A 38.625 / B 37.500), not the box end.
- PAYOFF internal beat: the breath before 'Next,' sits at A ~44.13-44.44 / B ~43.01-43.32 on the output timeline (0.26s acoustic).
