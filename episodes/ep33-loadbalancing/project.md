# EP33 — The traffic cop in front of every big app (load balancing)

Source: `C:/Users/gordo/Downloads/drive-download-20260905T030037Z-…/Teleprompter-2026-04-09_21-28-50.mp4 (folder -1-001)`. Single deliverable `final.mp4` (52.54s).

## Edit decisions
- **Recorded intro:** "Explaining load balancers in 30 seconds." The presenter never says the episode number; the title sticker carries `EPISODE 33` on top anyway (user request).
- **The countdown gag (user request):** he promises 30 seconds and the episode runs longer, so a stopwatch chip (`animations/slot_countdown/render.webm`, made by `tool/helpers/make_countdown.py`) counts 30 → 0 over the whole remaining video, i.e. slowly. It starts at the INTRO end and sits top-right (x 690-870, y 205-305) on top of every overlay; every content slot keeps that corner clear (`tool/helpers/check_reserve.py`).
- **Takes:** last complete attempt per beat; every range edge measured acoustically by `tool/helpers/edl_from_takes.py` (the per-range `reason` in `edl.json` records onset/tail vs ASR). Beat windows stamped by `fix_windows.py`; `beats.md` lists every word in output time.
- **Captions:** ASR patched where it was wrong (see Notes); otherwise verbatim as spoken.

## Ranges
| beat | source | out window |
|---|---|---|
| INTRO | 0.98-3.46 | 0.000-2.500 |
| HOOK | 8.66-15.24 | 2.500-9.083 |
| PROBLEM | 20.54-31.16 | 9.083-19.708 |
| BUILD | 48.18-57.36 | 19.708-28.917 |
| NEW_COMPONENT | 74.82-90.54 | 28.917-44.667 |
| PAYOFF | 120.84-128.70 | 44.667-52.542 |

## Overlays
| slot | start | dur |
|---|---|---|
| slot_tiktok_title | 0.000 | 2.500 |
| slot_hook | 3.050 | 6.300 |
| slot_problem | 9.350 | 10.300 |
| slot_build | 20.150 | 8.800 |
| slot_new_component | 29.450 | 15.000 |
| slot_payoff | 44.950 | 5.200 |
| slot_countdown | 2.500 | 50.042 |

Builder note: EP33 overlays (built 2026-09-04). Formats in beat order: sticker (INTRO), transparent crowd band (HOOK), TAKEOVER (PROBLEM), motion graphic (BUILD), TAKEOVER (NEW_COMPONENT), corner card (PAYOFF) = 4 distinct, 2 takeovers, no adjacent repeat. Every duration is on the 30fps grid and every fade lands on alpha 0 at the slot's own end. Junction audit: title 0.00-2.50 (= INTRO end) | gap 0.55 | hook 3.05-9.35 | ZERO-GAP junction | problem 9.35-19.65 | gap 0.50 | build 20.15-28.95 | gap 0.50 | new_component 29.45-44.45 | gap 0.50 | payoff 44.95-50.15 | bare tail 2.39s to 52.54 (spoken tease only, no chip). Leads: hook 0.55 into HOOK, problem 0.27 into PROBLEM, build 0.44 into BUILD, new_component 0.53 into NEW_COMPONENT, payoff 0.28 into PAYOFF. Landings (output s): hook counter 1,000,000 at 3.85, cop glyph on 'traffic cop' 6.60, five servers lit on 'before they ever arrived' 8.10-8.55; problem melt on 'melts' 9.72-10.5, 50-grid shutter slam on '50' 11.65, 'identical copies' headline 11.85, arrows seek on 'new problem' 13.70, dogpile on 'pick badly' 16.57, thud 17.41, 'buried' label 18.10, 'idle' 18.65; build fleet on 'whole fleet' 20.75-21.65, first request holds on 'hits it first' 22.30-23.90, deals on 'deals them out' 23.90-25.45, ROUND ROBIN on 'round robin' 25.85, 'one for you' deals 26.60 / 27.45, 'back around' 28.23; new_component stacks fill 30.75-31.9, first route on 'fewest' 32.00, LEAST CONNECTIONS on 'connections' 32.75, real samwho sim inset on 'pile up' 34.35, heartbe

All renders: `check_margins` clear (three slots in the batch needed a nudge and re-render: EP33 new_component headline 64→54px, EP34 dh_name/payoff left 70→78px), `check_overlay_files` 0 problems, `check_overlay_timing` inside beat, countdown-reserve probe clear (takeover shutter flashes excepted).

## Audio
`sfx/cues.json`: 14 cues / 14 distinct, word-anchored by `tool/helpers/cues_from_words.py` (onset −30 ms), gains fitted by `check_sfx_direct.py --apply` (−8 dB stingers / −4 dB voice memes), overlapping cues set by hand. Final peak −0.72 dBFS.

## Notes
- Transcript: the padded boxes "...A" and "requests....Smarter" were split so the BUILD/NEW_COMPONENT ranges start on the real "A" / "Smarter" onsets (restart takes).
- The overlay builders were cut off by an API session limit after rendering; the coordinator ran the final audits, fixes, composites and SFX.
