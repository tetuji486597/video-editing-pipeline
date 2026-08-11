# EP3 — "How Uber finds a driver in seconds" — session notes

Source: `/Users/gordon.jin/Downloads/ep3.mp4` (2160x3840, 151.7s raw). Built following the
same pipeline as EP1/EP4 and the confirmed conventions in `STYLE.md` (top-left title,
MarginV 280 captions, ducked trap BGM, myinstants SFX, measured punch-zoom focal point).

## Strategy

Six beats (HOOK, PROBLEM, BUILD, NEW_COMPONENT, AI_ANGLE, PAYOFF_NEXT) matching the given
script exactly. One continuous visual metaphor thread across the overlays: **indexing
physical space** — a location-ping icon (hook) → brute-force scan list (problem) → a
literal quadtree splitting on-screen (build) → a 5x5 neighbor-highlight grid + geohash
prefix string (new component) → a rising demand-prediction chart (AI angle) → the
"Index space, not just data." tagline card (payoff). Each overlay uses its own accent
color (cyan/red/green/amber/purple/blue) per STYLE.md's "vary color per concept" rule —
none reused from EP1/EP4's palettes.

## Take selection

All six beats had multiple retakes in the raw footage. Verified via `timeline_view.py`
waveform+frame inspection (not just the packed transcript text) before locking in:
- HOOK: three short phrases (37.06-46.26) confirmed as one natural continuous
  take-through via waveform — no retake gap.
- AI_ANGLE: first delivery (94.08-100.46) was an abandoned take (long silence after);
  the second delivery (106.72-116.84) flows directly into the closing line with only a
  breath between — used that one.
- PAYOFF_NEXT: three attempts total; the last (142.72-150.44) is the only one that's a
  single clean continuous burst on the waveform — used that, not the first two partials.

Final cut list and reasoning per range: see `edl.json`.

## Zoom

Measured the actual eye position on this footage directly (grid-overlay frame at
1080x1920 scale) rather than assuming EP1/EP4's numbers transferred — landed on
`focal_x: 545, focal_y: 725`, which happens to be very close to EP1/EP4's (540, 730):
same presenter, similar camera distance and framing. Applied to HOOK only (landing on
"How?"), not to every beat — EP1's precedent (zoom on hook only) rather than EP4's
(zoom on every beat), since the "punchier hooks" request that originally introduced this
effect was about hooks specifically, not a standing per-beat rule.

## Music + SFX

- BGM: sourced fresh via `media-use`/HeyGen catalog (query: "modern trap beat
  instrumental, driving hi-hats, confident tech explainer background") — a new track,
  not reused from EP1/EP4. 47s source, crossfade-looped to cover the full 63.56s runtime,
  ducked to 0.32 under dialogue (0.5 during the title/hook lead-in), faded out over the
  last ~3s.
- SFX: reused EP1/EP4's already-downloaded myinstants.com stingers (no new downloads
  this session) but picked thematically per this episode's specific beats — see
  `sfx/SFX_NOTES.md` for the full mapping and reasoning per placement.

## Verification

Self-eval pass: full-res frame extractions at the title card, each of the 6 overlay
windows, and a caption frame — all confirmed legible, correctly positioned (no
face/overlay/caption collisions), and matching STYLE.md's confirmed defaults. Waveform
spot-check at the first SFX hit (HOOK, ~8.6s) shows a clean punctuation layer, no
visible clipping. Did not do a full ±1.5s cut-boundary pixel-diff pass on every one of
the 5 internal cuts (time-boxed) — worth a closer look if any cut reads as jumpy on
playback.

## Output

`preview_final.mp4` — 63.76s, 1080x1920, graded + zoomed + captioned + music/SFX mixed.

## Flag for review

- BUILD overlay's quadtree-split animation is fast (splits complete within ~0.6s of
  screen time); may be worth slowing down if it reads as too quick on a real playback
  rather than frame-by-frame inspection.
- SFX levels (0.55 relative to narration) are an estimate by ear against the render, not
  a measured target — same caveat as every prior episode's SFX notes.
