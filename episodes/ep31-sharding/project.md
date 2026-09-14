# EP31 — How databases hold a billion rows (sharding)

Source: `C:/Users/gordo/Downloads/drive-download-20260905T030037Z-…/Teleprompter-2026-04-09_21-11-43.mp4 (folder -1-001)`. Single deliverable `final.mp4` (48.50s).

## Edit decisions
- **Recorded intro:** "Explaining sharding in 30 seconds." The presenter never says the episode number; the title sticker carries `EPISODE 31` on top anyway (user request).
- **The countdown gag (user request):** he promises 30 seconds and the episode runs longer, so a stopwatch chip (`animations/slot_countdown/render.webm`, made by `tool/helpers/make_countdown.py`) counts 30 → 0 over the whole remaining video, i.e. slowly. It starts at the INTRO end and sits top-right (x 690-870, y 205-305) on top of every overlay; every content slot keeps that corner clear (`tool/helpers/check_reserve.py`).
- **Takes:** last complete attempt per beat; every range edge measured acoustically by `tool/helpers/edl_from_takes.py` (the per-range `reason` in `edl.json` records onset/tail vs ASR). Beat windows stamped by `fix_windows.py`; `beats.md` lists every word in output time.
- **Captions:** ASR patched where it was wrong (see Notes); otherwise verbatim as spoken.

## Ranges
| beat | source | out window |
|---|---|---|
| INTRO | 3.06-5.02 | 0.000-2.000 |
| HOOK | 11.46-17.26 | 2.000-7.833 |
| PROBLEM | 22.76-31.00 | 7.833-16.083 |
| BUILD | 53.30-59.52 | 16.083-22.333 |
| NEW_COMPONENT | 82.16-102.22 | 22.333-42.417 |
| PAYOFF | 130.60-136.68 | 42.417-48.500 |

## Overlays
| slot | start | dur |
|---|---|---|
| slot_tiktok_title | 0.000 | 2.000 |
| slot_hook | 2.500 | 5.300 |
| slot_problem | 8.300 | 7.700 |
| slot_build | 16.500 | 5.800 |
| slot_new_component | 22.800 | 19.500 |
| slot_payoff | 43.000 | 5.400 |
| slot_countdown | 2.000 | 46.500 |

Builder note: EP31 overlays (built 2026-09-04). Formats: sticker / half-panel / motion-gfx / TAKEOVER / transparent band / corner card (1 takeover). Windows (out s): title 0.000-2.000 (INTRO end, fade 1.72-2.00); hook 2.500-7.800 (lead 0.50, gap 0.50 after title); problem 8.300-16.000 (lead 0.47, gap 0.50); build 16.500-22.300 (lead 0.42, gap 0.50); new_component 22.800-42.300 (lead 0.47, gap 0.50); payoff 43.000-48.400 (lead 0.58, gap 0.70; ends 0.10 before the last frame). Every gap is a deliberate >=0.5s breath; every fade lands on alpha 0 at its declared duration. Landings (word onset -> overlay-local): hook 'hold all of Facebook' 3.60->1.10 meter+3B chip, 'break' 5.18->2.68 burst, 'pieces' 6.10->3.60 PIECES label; problem 'vertically' 9.03->0.73 arrow, 'CPU' 10.77->2.25 chip, 'RAM' 11.53->3.05 chip, 'hard ceiling' 13.13->4.88 bar slam, 'absurdly expensive' 14.17->5.9 $ stack, 'fast' 15.53->6.95 tip; build 'horizontally' 17.34->0.85 arrow, 'split' 19.34->2.84 shutter+split, 'many machines' 19.90->3.05-3.41 machines, 'each one' 20.88->4.30 SHARDS, 'slice' 21.62->4.95 kicker; new_component 'user ID' 23.39->0.6 underline, 'A through M' 27.11->4.3 A-M chip, 'Shard One' 28.49->5.7 flash, 'N to Z' 29.05->6.25, 'Shard Two' 30.19->7.4, 'reads and writes' 31.67->8.1 blips, 'add more machines' 35.19->12.4 rebalance, 'hard parts' 36.81->13.9 amber shift, 'spreads load' 38.31->15.5 hot shard, 'queries' 40.11->17.3 query card, 'several shards' 41.45->18.55 fan-out; payoff 'box any bigger' 43.38->0.

All renders: `check_margins` clear (three slots in the batch needed a nudge and re-render: EP33 new_component headline 64→54px, EP34 dh_name/payoff left 70→78px), `check_overlay_files` 0 problems, `check_overlay_timing` inside beat, countdown-reserve probe clear (takeover shutter flashes excepted).

## Audio
`sfx/cues.json`: 15 cues / 15 distinct, word-anchored by `tool/helpers/cues_from_words.py` (onset −30 ms), gains fitted by `check_sfx_direct.py --apply` (−8 dB stingers / −4 dB voice memes), overlapping cues set by hand. Final peak −1.09 dBFS.

## Notes
- Transcript: "Users Eight through M" → "A through M" (the letter).
- The overlay builders were cut off by an API session limit after rendering; the coordinator ran the final audits, fixes, composites and SFX.
