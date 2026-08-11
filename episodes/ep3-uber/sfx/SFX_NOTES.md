# EP3 trending SFX — sourcing + usage reference

Reused from EP1/EP4's already-downloaded myinstants.com catalog (same licensing caveat as
those episodes' notes — see EP1's `sfx/SFX_NOTES.md` for the general sourcing method).
No new downloads this episode; each pick below is a thematic reuse chosen to fit this
episode's beats specifically, not a copy-paste of EP1/EP4's placements.

## Catalog — what each one is commonly used for

| File | Sound | Commonly used for | Feel |
|---|---|---|---|
| `suspense_strike.mp3` | Suspense string hit | A mystery/question beat — "wait, how?" | Orchestral stinger, native 3.07s, trimmed to 1.8s |
| `wrong_buzzer.mp3` | Game-show wrong-answer buzzer | The naive approach failing/not scaling | Harsh buzz, 1.06s |
| `vine_boom.mp3` | "Vine Boom" | A dramatic reveal/impact beat | Bass hit, 1.25s |
| `mind_blown.mp3` | "mind = blown" | A clever-trick reveal — "wait, that's smart" | Vocal exclamation, native 8.93s, trimmed to 2.0s |
| `over_9000.mp3` | "It's Over 9000!!" | Escalation — things scaling up further | Shouted exclamation, native 2.64s, played ~full (trimmed to 2.6s) |
| `correct_ding.mp3` | Correct Answer (game-show ding) | Resolution/"solved" moment — recurring series motif for payoff beats (same use as EP1/EP4) | Bright upward chime, 1.27s |

## How this episode (EP3 — Uber driver matching / geospatial indexing) used them

**Retimed 2026-08-08** — this episode's overlays went through three full regeneration
rounds since the original SFX pass (concept rebuild → real-images/format-variance pass →
caption-collision-driven pass that converted several overlays to full-screen takeovers and
shifted their internal content). Old timestamps were re-derived from the script/narration
and had drifted off the actual visual hits. New timestamps come directly from each
overlay's own GSAP timeline (the specific `fromTo`/`.to()` call that lands its hero
element), plus the EDL's `start_in_output` offset for that slot.

| Beat | Overlay local landing beat | Old timestamp | New timestamp | SFX | Why |
|---|---|---|---|---|---|
| HOOK | `#s2` "200ms" stat pops in @ local 1.0s | ~8.6s | **3.85s** | Vine Boom (was Suspense Strike) | The hook overlay has no "How?" text moment — its one real hit is the "200ms" stat popping in with a back-out bounce. Old cue landed in the overlay's fade-out tail, matched to spoken "How?" rather than anything on screen. |
| PROBLEM | live counter maxes out + `#e1` "BUT IT'S A DISASTER" pops @ local 8.8s | ~18.3s | **18.25s** | Wrong Buzzer (unchanged) | Already well-placed — barely moved. The counter finishing its climb to 50,000 and the "disaster" emphasis landing together is the clear hit. |
| BUILD | quadtree level-3 split completes + `#e1` emphasis pops @ local 4.7s | ~28.7s | **25.90s** | Suspense Strike (was Vine Boom) | Old cue was ~2.8s late — past the recursion completing, into the idle ambient-pulse hold. Retimed to the actual "IGNORING THE ENTIRE REST" reveal moment. |
| NEW_COMPONENT | `#e1` "SAME PREFIX = NEARBY." pops @ local 10.3s (stage B) | ~37.7s | **39.90s** | Mind Blown (unchanged) | Old cue landed mid-way through the hash-string characters still typing in, before the actual prefix-match payoff text appears. Retimed to the real "aha" moment. Stage A (naive-vs-indexed split-screen) was considered for a second cue but skipped to avoid cluttering the episode's longest beat. |
| AI_ANGLE | `#e1` "SURGE + ETA." pops @ local 5.4s | ~45.9s | **51.10s** | Over 9000 (unchanged) | Old cue fired right as the chart line was still drawing in (local ~0), well before either callout or the emphasis text had landed. Retimed to the actual escalation payoff. |
| PAYOFF | `#e1` tagline pops @ local 0.6s | ~57.0s | **56.50s** | Correct Answer ding (reused) | Already close — barely moved. Series-recurring "resolved" motif. |

**Music removed entirely** (2026-08-08, per direction) — `sfx_track_v2.wav` is mixed
directly onto the narration/caption/overlay video with no `music_final.wav` layer.

All six new timestamps were verified by extracting a real frame at each exact output
timestamp from the rendered final and confirming the targeted visual event is actually
occurring there (not just computed from the timeline arithmetic).

## Mixing notes

- All six mixed at `volume=0.6` relative to narration (same estimate-by-ear approach as
  before, not measured against a target LUFS).
- Longer source clips (mind_blown, over_9000, suspense_strike) trimmed via `atrim` to
  their first 1.8-2.6s so they punctuate the beat instead of ringing into the next line.
- Built via one `ffmpeg -filter_complex` pass: `atrim` (where needed) → `volume=0.6` →
  `adelay=<ms>|<ms>` per clip → `amix=inputs=6:duration=longest:normalize=0` →
  `sfx_track_v2.wav`, then mixed onto the narration video with a second `amix` (no music
  input) to produce the final render.
