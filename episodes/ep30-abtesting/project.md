# EP30 — How companies test on you without telling you (feature flags + A/B)

Source: `C:/Users/gordo/Downloads/drive-download-20260905T030037Z-…/Teleprompter-2026-04-09_21-05-50.mp4 (folder -1-001)`. Single deliverable `final.mp4` (48.83s).

## Edit decisions
- **Recorded intro:** "Explaining A/B testing in 30 seconds." The presenter never says the episode number; the title sticker carries `EPISODE 30` on top anyway (user request).
- **The countdown gag (user request):** he promises 30 seconds and the episode runs longer, so a stopwatch chip (`animations/slot_countdown/render.webm`, made by `tool/helpers/make_countdown.py`) counts 30 → 0 over the whole remaining video, i.e. slowly. It starts at the INTRO end and sits top-right (x 690-870, y 205-305) on top of every overlay; every content slot keeps that corner clear (`tool/helpers/check_reserve.py`).
- **Takes:** last complete attempt per beat; every range edge measured acoustically by `tool/helpers/edl_from_takes.py` (the per-range `reason` in `edl.json` records onset/tail vs ASR). Beat windows stamped by `fix_windows.py`; `beats.md` lists every word in output time.
- **Captions:** ASR patched where it was wrong (see Notes); otherwise verbatim as spoken.

## Ranges
| beat | source | out window |
|---|---|---|
| INTRO | 1.90-3.88 | 0.000-2.000 |
| HOOK | 8.82-13.10 | 2.000-6.292 |
| PROBLEM | 26.10-34.24 | 6.292-14.458 |
| BUILD | 39.66-45.92 | 14.458-20.750 |
| NEW_COMPONENT | 47.74-62.56 | 20.750-35.583 |
| AI_ANGLE | 64.68-71.52 | 35.583-42.458 |
| PAYOFF | 73.08-79.42 | 42.458-48.833 |

## Overlays
| slot | start | dur |
|---|---|---|
| slot_tiktok_title | 0.000 | 2.000 |
| slot_hook | 2.300 | 4.100 |
| slot_problem | 6.900 | 7.600 |
| slot_build | 15.000 | 5.500 |
| slot_new_component | 21.100 | 14.400 |
| slot_ai_angle | 36.000 | 6.300 |
| slot_payoff | 42.850 | 5.500 |
| slot_countdown | 2.000 | 46.833 |

Builder note: EP30 overlays (builder 2026-09-05). Formats: sticker / half-panel (two phones) / TAKEOVER (100% dial + user grid) / motion graphic (if(flag) card + toggle + real LaunchDarkly flag row) / TAKEOVER (1% ramp + KILL -> A|B split, phones, result table, DECISION) / transparent band (NEW MODEL chip + toggle + users pie + A/B bubbles) / photo card (real LD flag row, SHIPPED -> TURNED ON -> 1% pie). Landings (output s): hook diff rings 3.75 ('slightly different' 3.36-3.90), '?' 5.76 ('can tell' 5.76-6.14); problem 100% slam 8.10 ('hundred percent' 8.11-8.59), red cascade 10.29 ('broken' 10.19-10.49), EVERYONE GETS HIT 11.43 (11.33-12.19), ROLLBACK lever 13.32 ('rolling back' 13.15-13.69), sweat drop 13.90 ('painful' 13.95-14.39); build if/flag rows 15.35 ('wraps' 15.30-15.54), toggle 16.41 ('switch' 16.36), flip 17.01 ('flip' 16.96-17.22), 'no redeploy' 17.63 ('redeploying' 17.58-18.12), dark sweep 18.66 + 'OFF by default' 19.30 ('ships dark' 18.64-19.24); new_component ON+1% 21.55 ('one percent' 21.55-21.91), sparkline 22.60-24.10 ('watch the metrics' 22.59-23.35), ramp 5%/25% 24.60/24.98 ('ramp up' 24.59-25.05), KILL slam 26.20 ('kill' 26.21-26.31), phase shift 27.50 ('Show version A' 27.51), split wipe 28.37 ('half' 28.37-28.53), B wipe 29.27 ('version B' 29.27-29.77), table 30.45 ('Compare the numbers' 30.37-31.21), A/B TEST headline 31.97 ('A/B' 31.97), B lights 32.60, check 33.50 ('decisions' 33.51-33.97), DECISION stamp 34.67 ('actual numbers' 34.67-35.51); ai_angle toggle ON 3

All renders: `check_margins` clear (three slots in the batch needed a nudge and re-render: EP33 new_component headline 64→54px, EP34 dh_name/payoff left 70→78px), `check_overlay_files` 0 problems, `check_overlay_timing` inside beat, countdown-reserve probe clear (takeover shutter flashes excepted).

## Audio
`sfx/cues.json`: 15 cues / 15 distinct, word-anchored by `tool/helpers/cues_from_words.py` (onset −30 ms), gains fitted by `check_sfx_direct.py --apply` (−8 dB stingers / −4 dB voice memes), overlapping cues set by hand. Final peak −1.86 dBFS.

## Notes
- Transcript: the ASR boxed "(meaning off by default)" as an audio_event; replaced with four timed words so the caption reads the whole sentence.
- The overlay builders were cut off by an API session limit after rendering; the coordinator ran the final audits, fixes, composites and SFX.
