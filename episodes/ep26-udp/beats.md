# EP26 (UDP + jitter buffers) — beat windows and payoff-word timings

All times in seconds on the OUTPUT timeline (render.py's 24fps extract grid, as stamped by
`fix_windows.py`). Word spans are ASR word boundaries from `transcripts/ep26.json`, converted
per variant via `output = window_start + (source_time - range_start)`; two ends are
acoustic-capped where Scribe's box runs past the measured speech end (noted inline).

**MISSPEAK (both variants):** the intro says "episode 25" — this is episode 26. Every intro
take on the shoot has the wrong number; kept deliberately, see `_misspeak_note` in the EDLs.

Everything after INTRO is **0.7083s earlier in B** (B's intro take is shorter: 5.625s vs 6.333s).

## INTRO
- Window A: 0.0000 – 6.3333  (6.3333s)
- Window B: 0.0000 – 5.6250  (5.6250s)
- Quote A: "This is episode 25 of prepping you for your system design interview. Today, we'll be talking about UDP and jitter buffers."
- Quote B: "This is episode 25 of Exploring Really Cool Tech. Today, we'll be talking about UDP and jitter buffers."

## HOOK
- Window A: 6.3333 – 12.2083  (5.8750s)
- Window B: 5.6250 – 11.5000  (5.8750s)
- Quote: "So YouTube almost never glitches. Your video calls glitch constantly. Weirdly, the call is doing it on purpose."

| phrase | A start | A end | B start | B end |
|---|---|---|---|---|
| "never glitches" | 7.453 | 8.233 | 6.745 | 7.525 |
| "glitch constantly" | 9.093 | 9.793 | 8.385 | 9.085 |
| "doing it on purpose" (end acoustic-capped; ASR boxes 'purpose.' to 42.52, past the cut) | 11.003 | 12.023 | 10.295 | 11.315 |

## PROBLEM
- Window A: 12.2083 – 24.8333  (12.6250s)
- Window B: 11.5000 – 24.1250  (12.6250s)
- Quote: "Remember the takes and receipts from the URL episode? Reliable delivery means waiting for lost data to be resent, which is fine for a video file, but it's useless for a live call. A word from two seconds ago re-arriving now helps nobody."

| phrase | A start | A end | B start | B end |
|---|---|---|---|---|
| "waiting for lost data" | 16.528 | 17.448 | 15.820 | 16.740 |
| "useless for a live call" | 20.028 | 21.028 | 19.320 | 20.320 |
| "helps nobody" | 23.888 | 24.628 | 23.180 | 23.920 |

## BUILD
- Window A: 24.8333 – 30.8750  (6.0417s)
- Window B: 24.1250 – 30.1667  (6.0417s)
- Quote: "So live calls use UDP. Fire the packets and never look back. No receipts, no resends, no waiting."

| phrase | A start | A end | B start | B end |
|---|---|---|---|---|
| "UDP" | 26.213 | 26.633 | 25.505 | 25.925 |
| "never look back" | 27.933 | 28.613 | 27.225 | 27.905 |
| "no receipts, no resends, no waiting" | 28.773 | 30.693 | 28.065 | 29.985 |

## JITTER
- Window A: 30.8750 – 36.4583  (5.5833s)
- Window B: 30.1667 – 35.7500  (5.5833s)
- Quote: "Your device keeps a tiny jitter buffer, a fraction of a second of audio to smooth out packets arriving unevenly."

| phrase | A start | A end | B start | B end |
|---|---|---|---|---|
| "tiny jitter buffer" | 31.855 | 32.585 | 31.147 | 31.877 |
| "arriving unevenly" (end acoustic (ASR 149.18)) | 35.255 | 36.195 | 34.547 | 35.487 |

## ROBOT
- Window A: 36.4583 – 46.2083  (9.7500s)
- Window B: 35.7500 – 45.5000  (9.7500s)
- Quote: "If a packet is lost, it isn't re-requested. The moment is skipped or papered over. That's the robot voice. The trade is deliberate. For live conversation, being on time beats being complete."

| phrase | A start | A end | B start | B end |
|---|---|---|---|---|
| "isn't re-requested" | 37.838 | 38.678 | 37.130 | 37.970 |
| "skipped or papered over" | 39.338 | 40.358 | 38.630 | 39.650 |
| "robot voice" | 41.138 | 41.738 | 40.430 | 41.030 |
| "on time beats being complete" (end acoustic (ASR 158.98)) | 44.618 | 46.028 | 43.910 | 45.320 |

## AI_ANGLE
- Window A: 46.2083 – 53.8333  (7.6250s)
- Window B: 45.5000 – 53.1250  (7.6250s)
- Quote: "Modern calls soften the damage with AI, models that reconstruct the missing milliseconds and strip background noise, so small losses become inaudible."

| phrase | A start | A end | B start | B end |
|---|---|---|---|---|
| "reconstruct the missing milliseconds" | 48.828 | 50.518 | 48.120 | 49.810 |
| "strip background noise" | 50.768 | 51.768 | 50.060 | 51.060 |

## PAYOFF
- Window A: 53.8333 – 63.0833  (9.2500s)
- Window B: 53.1250 – 62.3750  (9.2500s)
- Quote: "Netflix delivers the past perfectly. A call delivers the present imperfectly, because late is worse than flawed. Next, we'll look at the company that pays people to break its own website."

| phrase | A start | A end | B start | B end |
|---|---|---|---|---|
| "past perfectly" | 54.953 | 55.673 | 54.245 | 54.965 |
| "present imperfectly" | 56.853 | 57.873 | 56.145 | 57.165 |
| "late is worse than flawed" | 58.433 | 59.523 | 57.725 | 58.815 |
