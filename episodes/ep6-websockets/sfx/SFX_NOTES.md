# SFX sourcing & usage — EP6 ("How WhatsApp Delivers in 1 Second")

All three stingers sourced from myinstants.com (downloaded via direct `curl` with a
browser user-agent — the site 403s generic fetchers without one). Same copyright
caveat as EP1/EP4: licensing on myinstants.com content is unclear, so these files are
kept local and are **not** committed to the video-editing-pipeline git repo.

**Retimed 2026-08-08, music removed entirely.** The original timestamps below were set
against an earlier version of these overlays; several were substantially rebuilt since
(full-screen takeovers, repositioned payoff content for caption clearance) and the old
cues drifted off their actual visual hits. New timestamps are derived directly from each
overlay's GSAP timeline (its own "TRANSITION"/landing-beat comments and code) plus the
EDL's `start_in_output` for that slot — not re-guessed from the script. Coverage was also
extended from 3 to 5 beats (BUILD and PAYOFF previously had none) to match the rest of
the series' convention of one landing-beat hit per produced overlay, reusing the existing
3-file catalog rather than downloading anything new.

| Beat | Overlay local landing beat | Output timestamp | SFX | Why |
|---|---|---|---|---|
| HOOK | `#transition-flash` fires @ local 1.3s (the arc-ping's arrival flash, message reaching Earth) | **4.10s** | Vine Boom | Old cue (~3.10s) targeted an earlier composition's punch-word timing that no longer exists in this shape; retimed to the literal "arrival" impact, just ahead of the "1 SECOND." text landing (local 1.7s) so the emphasis still reads as attached to the punchline. |
| PROBLEM | battery drain tween bottoms out @ local 4.7s (12%, "DRAINS BATTERY." visible) | **13.44s** | Sad Trombone | Old cue (13.24s) was already close — the composition's battery countdown is now a continuous tween rather than discrete steps, but the worst-point timing barely moved. Verified frame shows 17% and falling, reading clearly as the "pathetic" low point. |
| BUILD | `#flash` fires @ local 1.55s (failed-handshake red glow → persistent-connection teal glow) | **21.55s** | Vine Boom (reused) | New cue — this beat had no stinger before. The literal "fix arrives" moment, verified against a frame showing "THE OLD HANDSHAKE" fading as the YOU↔SERVER connection line begins drawing. |
| NEW_COMPONENT | `#tick2` (second checkmark) pops in @ local 5.05s, "RECONNECTED" status already showing | **35.11s** | Correct Answer ding | Old cue (33.76s) was close in concept but ~1.35s early against the current code's actual tick2 onset. Retimed to land exactly on the checkmark's trigger frame. |
| PAYOFF | `#punch-word` ("KEEP THE LINE OPEN.") begins its reveal @ local 0.12s | **48.42s** | Correct Answer ding (reused) | New cue — this beat had no stinger before. Reusing `correct_ding` here matches the rest of the series' convention of a recurring "resolved" motif on the closing tagline (see EP1/EP3/EP4/EP5's own payoff beats). |

Each cue's onset is placed right at its triggering GSAP call, not mid-animation or on
settle — verified by extracting a frame at the exact output timestamp for all five and
confirming the targeted visual event is either mid-flash or just beginning its reveal
(the same "hit anticipates the pop" convention used across the other episodes).

**Music removed entirely** — `sfx_track_v2.wav` is mixed directly onto the narration/
caption/overlay video (`base_v9.mp4`) with no `music_final.wav` layer.

## Mixing notes

- Levels: `volume=0.6` applied per-clip before delay/mix (estimated, not confirmed by ear).
- `sad_trombone` trimmed to 2.0s via `atrim` (native ~3.55s); `correct_ding` trimmed to
  1.3s at both placements (native ~2.95s — a longer source clip than other episodes'
  copy of the same file). `vine_boom` (native ~1.25s) plays untrimmed at both placements.
- All five cues are spaced 4s+ apart — no overlaps.
