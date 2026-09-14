# EP34 — Sharing a secret while the whole world listens (Diffie-Hellman)

Source: `C:/Users/gordo/Downloads/drive-download-20260905T030037Z-…/Teleprompter-2026-04-09_21-38-44.mp4 (folder -1-002)`. Single deliverable `final.mp4` (61.92s).

## Edit decisions
- **Recorded intro:** "Explaining Diffie-Hellman in 30 seconds." The presenter never says the episode number; the title sticker carries `EPISODE 34` on top anyway (user request).
- **The countdown gag (user request):** he promises 30 seconds and the episode runs longer, so a stopwatch chip (`animations/slot_countdown/render.webm`, made by `tool/helpers/make_countdown.py`) counts 30 → 0 over the whole remaining video, i.e. slowly. It starts at the INTRO end and sits top-right (x 690-870, y 205-305) on top of every overlay; every content slot keeps that corner clear (`tool/helpers/check_reserve.py`).
- **Takes:** last complete attempt per beat; every range edge measured acoustically by `tool/helpers/edl_from_takes.py` (the per-range `reason` in `edl.json` records onset/tail vs ASR). Beat windows stamped by `fix_windows.py`; `beats.md` lists every word in output time.
- **Captions:** ASR patched where it was wrong (see Notes); otherwise verbatim as spoken.

## Ranges
| beat | source | out window |
|---|---|---|
| INTRO | 3.96-6.34 | 0.000-2.417 |
| HOOK | 11.50-20.50 | 2.417-11.417 |
| PROBLEM | 34.36-44.04 | 11.417-21.125 |
| BUILD | 48.96-59.12 | 21.125-31.292 |
| NEW_COMPONENT | 82.74-100.24 | 31.292-48.792 |
| DH_NAME | 109.62-115.58 | 48.792-54.792 |
| PAYOFF | 133.36-140.46 | 54.792-61.917 |

## Overlays
| slot | start | dur |
|---|---|---|
| slot_tiktok_title | 0.000 | 2.400 |
| slot_hook | 2.900 | 8.500 |
| slot_problem | 12.600 | 8.500 |
| slot_build | 21.900 | 9.300 |
| slot_new_component | 31.900 | 16.800 |
| slot_dh_name | 49.200 | 5.500 |
| slot_payoff | 55.200 | 5.000 |
| slot_countdown | 2.417 | 59.500 |

Builder note: Formats: sticker / half-panel (hook) / motion-gfx (problem, wire) / TAKEOVER (build, paint 1) / TAKEOVER (new_component, paint 2 + the real Wikipedia diagram) / corner (dh_name, real Edge padlock) / transparent band (payoff). Landings (output s): sticker 0-2.4 (INTRO ends 2.4167; fade ends 2.4). hook 2.9-11.4: halos on 'secret' 3.92, listeners on 'everyone in the room' 4.52, scribbles on 'listens to every word' 5.36, ??? turn on 'can't work it out' 8.28-8.35, browser bar on 'open a website' 10.64-10.9. problem 12.6-21.1: KEY chip on 'key' 13.34, screens wake on 'just met' 14.6, ghost key on 'agree on one' 16.1, wire on 'over a line' 16.8, clamp bites on 'tapping' 18.45, key travels on 'send the key' 19.34, copy climbs + headline on 'the tapper has it too' 20.1-20.9. build 21.9-31.2: yellow pours on 'paint' 22.38, PUBLIC on 'public color' 24.05, eye on 'everyone can see' 25.0, flash/hands/private pours on 'secretly mixes' 26.5-27.3, PRIVATE on 'private color' 27.6, cross-over on 'swap' 29.16, SWAP chip on 'in the open' 30.35. new_component 31.9-48.7: pours on 'adds their own private color' 32.4-33.0, match flash + '=' on 'final' 36.1, eye on 'eavesdropper' 37.0, swatches on 'saw the mixtures' 37.9-38.3, un-mix attempts on 'unmixing paint' 39.4-40.9, IMPOSSIBLE on 'impossible' 41.1-41.35, diagram card on 'real version uses math' 42.3, one-way glyph on 'one-way' 44.4, KEY chips on 'shared key' 46.3-46.5, empty wire on 'never once traveled the wire' 47.4-48.0. dh_name 49.2-54.7: 

All renders: `check_margins` clear (three slots in the batch needed a nudge and re-render: EP33 new_component headline 64→54px, EP34 dh_name/payoff left 70→78px), `check_overlay_files` 0 problems, `check_overlay_timing` inside beat, countdown-reserve probe clear (takeover shutter flashes excepted).

## Audio
`sfx/cues.json`: 17 cues / 17 distinct, word-anchored by `tool/helpers/cues_from_words.py` (onset −30 ms), gains fitted by `check_sfx_direct.py --apply` (−8 dB stingers / −4 dB voice memes), overlapping cues set by hand. Final peak −1.78 dBFS.

## Notes
- DH_NAME is its own beat ("That's Diffie-Hellman… milliseconds") taken from the second read; the HOOK ends on "website" before the sigh.
- The overlay builders were cut off by an API session limit after rendering; the coordinator ran the final audits, fixes, composites and SFX.
