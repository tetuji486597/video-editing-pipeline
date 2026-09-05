# EP28 — Why ChatGPT types so slow (SSE, brainrot edition) — beats

Single variant, `edl.json`, no overlays yet. Output-timeline windows are on render.py's 24fps
extract grid (stamped by `fix_windows.py`). Word times below are OUTPUT timeline =
window_start + (word.start - range.start), from the ASR word boxes; starts are reliable, ends
are Scribe-padded (measure acoustically before syncing anything to a word END).

Total duration: **61.9583s**

## INTRO  — output 0.000 → 3.167  (source 22.60–25.75, 3.167s)

> Explaining streaming to Gen Alpha in thirty seconds.

| phrase | output start | output end | source start |
|---|---|---|---|
| Explaining streaming | 0.200 | 1.160 | 22.800 |
| Gen Alpha | 1.340 | 1.940 | 23.940 |
| thirty seconds | 2.160 | 2.860 | 24.760 |

## HOOK  — output 3.167 → 13.708  (source 31.62–42.15, 10.542s)

> You know how ChatGPT yaps one word at a time? Like, chat, is this real or is bro LARPing? Turns out it legiterally doesn't know the end of the sentence yet. Bro straight freestyling from the dome.

| phrase | output start | output end | source start |
|---|---|---|---|
| one word at a time | 4.907 | 5.747 | 33.360 |
| is this real | 6.417 | 7.047 | 34.870 |
| LARPing | 7.647 | 8.027 | 36.100 |
| legiterally | 9.127 | 9.847 | 37.580 |
| freestyling | 12.227 | 12.827 | 40.680 |
| from the dome | 12.867 | 13.527 | 41.320 |

## PROBLEM  — output 13.708 → 24.625  (source 50.25–61.16, 10.917s)

> So the AI makes one word at a time, and a long answer takes, like, sixty-seven seconds to finish. If you had to look at a blank screen for sixty-seven seconds, we would close the tab and might even touch grass. Like bro, Psy bow.

| phrase | output start | output end | source start |
|---|---|---|---|
| sixty-seven seconds | 16.798 | 17.638 | 53.340 |
| sixty-seven seconds | 19.438 | 20.308 | 55.980 |
| close the tab | 20.978 | 21.418 | 57.520 |
| touch grass | 22.158 | 22.798 | 58.700 |
| Psy bow | 23.738 | 25.318 (ASR, over-boxed) / **24.468 acoustic** | 60.280 |

Note: Scribe boxes 'bow.' as 60.62-61.86 but the audio hits floor at 61.01 (every threshold); the real end of the word is output 24.468, 157ms before the cut at 24.625. Do not sync anything to the ASR end.

## BUILD  — output 24.625 → 34.125  (source 66.40–75.88, 9.500s)

> So instead of raw dogging the whole answer, the server just backshots each word to your phone the second it pops out. There's one pipe, and it stays open, and words keep falling down it.

| phrase | output start | output end | source start |
|---|---|---|---|
| raw dogging | 25.365 | 25.905 | 67.140 |
| backshots | 27.665 | 28.285 | 69.440 |
| one pipe | 31.065 | 31.505 | 72.840 |
| stays open | 31.785 | 32.305 | 73.560 |
| falling down it | 33.225 | 33.985 | 75.000 |

## NEW_COMPONENT  — output 34.125 → 55.125  (source 126.02–146.98, 21.000s)

> That pipe is called server-sent events, SSE, and the thing about it is it only goes in one direction, from the server down to you. The chat app episode had a pipe that went both ways, but you talk back in a chat. Here you're just an NPC listening, so one way is fine. And the sneaky part is the first word shows up in, like, half a second, so your brain goes, "Oh, that was fast," even though the whole thing still took sixty-seven seconds. It's basically continuous aura farming.

| phrase | output start | output end | source start |
|---|---|---|---|
| server-sent events | 34.985 | 35.705 | 126.880 |
| SSE | 35.925 | 36.205 | 127.820 |
| one direction | 37.785 | 38.235 | 129.680 |
| both ways | 41.105 | 41.505 | 133.000 |
| NPC listening | 43.605 | 44.345 | 135.500 |
| half a second | 47.865 | 48.385 | 139.760 |
| that was fast | 49.725 | 50.245 | 141.620 |
| sixty-seven seconds | 51.825 | 52.745 | 143.720 |
| aura farming | 54.445 | 54.895 | 146.340 |

## PAYOFF  — output 55.125 → 61.958  (source 149.68–156.50, 6.833s)

> So give people the first word right away instead of making them bed rot until the last one. Next, we'll look at who's reading a billion posts a day.

| phrase | output start | output end | source start |
|---|---|---|---|
| first word right away | 56.005 | 56.825 | 150.560 |
| bed rot | 57.685 | 58.125 | 152.240 |
| billion posts | 60.705 | 61.365 | 155.260 |

## Edge audit (find_dead_air.py at -12/-18/-25 dB below speech level, cross-checked with words.py)

| beat | acoustic onset | ASR first-word start | start pad | acoustic tail | ASR last-word end | end pad |
|---|---|---|---|---|---|---|
| INTRO | 22.76 (breath from 22.51) | 22.80 | 160ms | 25.60 | 25.46 (under-boxed 140ms) | 150ms |
| HOOK | 31.76-31.79 | 31.74 | 160ms | 41.94-42.03 | 41.98 | 120-210ms |
| PROBLEM | 50.35 (breath from 50.13) | 50.38 | 100ms | 60.84-61.01 | **61.86 (over-boxed 850ms)** | 150ms |
| BUILD | 66.49-66.54 | 66.56 | 120ms | 75.67-75.73 | 75.76 | 150ms |
| NEW_COMPONENT | 126.12 | 126.15 | 100ms | 146.77-146.88 | 146.79 | 100-210ms |
| PAYOFF | 149.78 (inhale from 149.42) | 149.84 | 100ms | 156.22-156.37 | 156.25 | 130ms |

No cut lands inside a word. All pads within 30-200ms of the nearest acoustic edge (HOOK/NEW_COMPONENT quoted as a span because the -12 and -25 dB floors disagree by ~100ms on where the tail ends).

## Internal dead air (>0.8s) — NONE

Largest silences inside a kept range: 0.53s between 'seconds.' and 'It's' (NEW_COMPONENT, the kept breath before the tag line), 0.49s after 'LARPing?' (HOOK), 0.43s after 'fine.' (NEW_COMPONENT), 0.32s after 'grass.' (PROBLEM). All are phrase breaths; nothing needs a trim.

## Zoom

slow mode, focal (540,730), alternating 1.0->1.08 / 1.08->1.0 per range starting at 1.0 on INTRO, so scale is continuous across every cut. No overlays yet; re-check clearances against the zoom displacement if any are added.
