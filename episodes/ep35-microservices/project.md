# EP35 — Monolith vs microservices, the real fight

Source: `C:/Users/gordo/Downloads/drive-download-20260905T030037Z-…/Teleprompter-2026-04-09_21-49-38.mp4 (folder -1-002)`. Single deliverable `final.mp4` (48.38s).

## Edit decisions
- **Recorded intro:** "Monolith versus microservices in 30 seconds." The presenter never says the episode number; the title sticker carries `EPISODE 35` on top anyway (user request).
- **The countdown gag (user request):** he promises 30 seconds and the episode runs longer, so a stopwatch chip (`animations/slot_countdown/render.webm`, made by `tool/helpers/make_countdown.py`) counts 30 → 0 over the whole remaining video, i.e. slowly. It starts at the INTRO end and sits top-right (x 690-870, y 205-305) on top of every overlay; every content slot keeps that corner clear (`tool/helpers/check_reserve.py`).
- **Takes:** last complete attempt per beat; every range edge measured acoustically by `tool/helpers/edl_from_takes.py` (the per-range `reason` in `edl.json` records onset/tail vs ASR). Beat windows stamped by `fix_windows.py`; `beats.md` lists every word in output time.
- **Captions:** ASR patched where it was wrong (see Notes); otherwise verbatim as spoken.

## Ranges
| beat | source | out window |
|---|---|---|
| INTRO | 10.22-13.04 | 0.000-2.833 |
| HOOK | 28.02-34.72 | 2.833-9.542 |
| PROBLEM | 52.18-61.64 | 9.542-19.042 |
| BUILD | 85.12-91.28 | 19.042-25.208 |
| NEW_COMPONENT | 96.16-112.80 | 25.208-41.875 |
| PAYOFF | 126.64-133.12 | 41.875-48.375 |

## Overlays
| slot | start | dur |
|---|---|---|
| slot_tiktok_title | 0.000 | 2.833 |
| slot_hook | 3.350 | 6.300 |
| slot_problem | 10.150 | 9.000 |
| slot_build | 19.650 | 6.400 |
| slot_new_component | 26.600 | 15.700 |
| slot_payoff | 42.800 | 4.800 |
| slot_countdown | 2.833 | 45.542 |

Builder note: EP35 overlays (built 2026-09-04). Formats in beat order: sticker (INTRO), half-panel VS card (HOOK), motion graphic block+DEPLOY (PROBLEM), TAKEOVER shatter (BUILD, the episode's only takeover), transparent band gauge/tangle/stamp (NEW_COMPONENT), corner stamp checklist (PAYOFF). Every slot except the sticker keeps the countdown reserve x>=670,y<=330 at alpha 0 (probed on decoded alpha, every frame). Landings (output s): hook VS badge 4.10; swarm 'thousands of services' 4.55-5.60; 'copying' chip+X 7.50/7.90 on 'making a mistake' 7.37-8.07; balance beam 8.50-8.85 on 'real trade-off' 8.67-9.39. problem block cells 10.50-11.72 on 'one big code base' 10.38-11.16; DEPLOY press 12.45 on 'single unit' 12.30-12.68; tick 13.15 on 'simple' 12.90; amber change cell 15.10 on 'one team's change' 14.76-15.22; red wave 15.90-16.70 on 'break everything' 15.74-16.63; heavy redeploy crawl 17.67-18.87 on 'deploy the whole thing every time' 17.40-19.00. build shatter 20.15 on 'split' 19.93-20.20; OWN TEAM + avatars 22.60-23.28 on 'a team owns each one' 22.42-23.28; deploy buttons 23.85 on 'deploys it' 23.70-24.10; OWN SCHEDULE + staggered presses 24.50-25.23 on 'own schedule' 24.60-25.05. new_component gauge climbs 27.75-29.25 on 'adds real complexity' 27.69-29.13; Amazon 2008 graph inset 28.35; packets 29.2-32.5 on 'every call crosses a network'; red X 31.45 on 'fail in new ways' 31.17-32.22; magnifier 32.5-34.05 on 'debugging gets much harder' 32.45-34.07; PEOPLE PROBLEM stamp 36.15 on 'organi

All renders: `check_margins` clear (three slots in the batch needed a nudge and re-render: EP33 new_component headline 64→54px, EP34 dh_name/payoff left 70→78px), `check_overlay_files` 0 problems, `check_overlay_timing` inside beat, countdown-reserve probe clear (takeover shutter flashes excepted).

## Audio
`sfx/cues.json`: 15 cues / 15 distinct, word-anchored by `tool/helpers/cues_from_words.py` (onset −30 ms), gains fitted by `check_sfx_direct.py --apply` (−8 dB stingers / −4 dB voice memes), overlapping cues set by hand. Final peak −1.74 dBFS.

## Notes
- PAYOFF starts on "So" after the sigh; PROBLEM is the second take (the first broke on "once team change").
- The overlay builders were cut off by an API session limit after rendering; the coordinator ran the final audits, fixes, composites and SFX.
