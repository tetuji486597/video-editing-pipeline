# EP32 — How apps survive a server catching fire (replication + failover)

Source: `C:/Users/gordo/Downloads/drive-download-20260905T030037Z-…/Teleprompter-2026-04-09_21-20-35.mp4 (folder -1-001)`. Single deliverable `final.mp4` (44.04s).

## Edit decisions
- **Recorded intro:** "Explaining replication in 30 seconds." The presenter never says the episode number; the title sticker carries `EPISODE 32` on top anyway (user request).
- **The countdown gag (user request):** he promises 30 seconds and the episode runs longer, so a stopwatch chip (`animations/slot_countdown/render.webm`, made by `tool/helpers/make_countdown.py`) counts 30 → 0 over the whole remaining video, i.e. slowly. It starts at the INTRO end and sits top-right (x 690-870, y 205-305) on top of every overlay; every content slot keeps that corner clear (`tool/helpers/check_reserve.py`).
- **Takes:** last complete attempt per beat; every range edge measured acoustically by `tool/helpers/edl_from_takes.py` (the per-range `reason` in `edl.json` records onset/tail vs ASR). Beat windows stamped by `fix_windows.py`; `beats.md` lists every word in output time.
- **Captions:** ASR patched where it was wrong (see Notes); otherwise verbatim as spoken.

## Ranges
| beat | source | out window |
|---|---|---|
| INTRO | 8.10-10.42 | 0.000-2.333 |
| HOOK | 15.70-21.42 | 2.333-8.083 |
| PROBLEM | 26.62-33.94 | 8.083-15.417 |
| BUILD | 40.48-48.24 | 15.417-23.208 |
| NEW_COMPONENT | 103.78-117.96 | 23.208-37.417 |
| PAYOFF | 141.74-148.36 | 37.417-44.042 |

## Overlays
| slot | start | dur |
|---|---|---|
| slot_tiktok_title | 0.000 | 2.333 |
| slot_hook | 2.600 | 5.400 |
| slot_problem | 8.500 | 6.900 |
| slot_build | 15.900 | 7.100 |
| slot_new_component | 23.500 | 13.500 |
| slot_payoff | 37.700 | 4.800 |
| slot_countdown | 2.333 | 41.708 |

Builder note: EP32 overlays (built 2026-09-05). Formats in beat order: sticker (INTRO) / corner accent (HOOK, upper-left, real githubstatus.com capture inset) / TAKEOVER (PROBLEM) / motion graphic (BUILD, upper band) / TAKEOVER (NEW_COMPONENT) / transparent band (PAYOFF, upper band, status capture callback) = 4 distinct, 2 takeovers, no adjacent repeat. Windows: title 0.000-2.333 (fade ends on the INTRO end); hook 2.600-8.000 (lead 0.27; fire on 'dies' @rel 0.40, 'nobody noticed' @1.85, REPLICATION @3.10, FAILOVER @3.98); problem 8.500-15.400 (lead 0.42; rows fill by 'machine', blackout on 'fails' @1.52, DOWN @2.24, rows->ash + counter to 0 over 'lost data for good' 3.5-4.64); build 15.900-23.000 (lead 0.48; followers on 'live copies' @0.85/1.45, crown on 'leader' @3.80, writes @4.30-5.20, FOLLOWERS @5.60, pulse on 'copy every change' @6.20); new_component 23.500-37.000 (lead 0.29; flames on 'dies' @0.45, flatline on 'notices' @1.25, crown hop on 'promotes' @1.90, FAILOVER + flash @3.90, reroute @5.05-5.65, '< 5s' on 'seconds' @6.75, read arrows on 'serve reads' @8.2-8.6, spare badges on 'redundancy' @11.15-11.65); payoff 37.700-42.500 (lead 0.28; 'waste?' @0.92, shield + 'saved you' on 'saves you' @2.16-2.34, status page @2.70; no tease chip). Gap audit: title->hook 0.267s (deliberate, hook lead), hook->problem 0.500s, problem->build 0.500s, build->new_component 0.500s, new_component->payoff 0.700s, payoff->end 1.542s; every render fades to alpha 0 at exactly its declared duration (check_

All renders: `check_margins` clear (three slots in the batch needed a nudge and re-render: EP33 new_component headline 64→54px, EP34 dh_name/payoff left 70→78px), `check_overlay_files` 0 problems, `check_overlay_timing` inside beat, countdown-reserve probe clear (takeover shutter flashes excepted).

## Audio
`sfx/cues.json`: 13 cues / 13 distinct, word-anchored by `tool/helpers/cues_from_words.py` (onset −30 ms), gains fitted by `check_sfx_direct.py --apply` (−8 dB stingers / −4 dB voice memes), overlapping cues set by hand. Final peak −1.76 dBFS.

## Notes
- Transcript: "takes the rights" → "writes".
- The overlay builders were cut off by an API session limit after rendering; the coordinator ran the final audits, fixes, composites and SFX.
