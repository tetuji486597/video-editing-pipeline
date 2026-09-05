# Lessons from the EP20-26 batch (2026-08-28) — read before the next batch

Everything below was learned the hard way in one build-and-three-feedback-round cycle.
The renderer traps are also condensed into `OVERLAY_SPEC.md` (which overlay builders
read in full); this file carries the fuller story and the process-level lessons.

## Gordon's standing directives from this batch (non-negotiable)

1. **Graphics must NEVER block text.** Not captions, not the composition's own text.
   Shipped twice in one batch: EP23's container box sat on the meme-card quote for all
   of act 1; EP26's player bar crossed "reconnecting…". Direct quote: "graphics should
   never block text."
2. **ALWAYS leave a margin from the video border.** Direct quote after the SECOND
   top-left-corner shipment: "there should ALWAYS be some margin from the border for
   the overlays in the video. STOP putting graphics so close to the border."
   The band is **x 70-870, y 200-1280** for all text/UI (bg-fill/vignette/full-bleed
   exempt). `tool/helpers/check_margins.py` is the authoritative audit — run it on
   EVERY slot's render.webm before compositing. Two agent-run audits false-passed
   corner-pinned content; do not accept an agent's "clear" without this script.
3. **Title stickers are horizontally CENTERED** (stack centered on x=540, measured
   539.5 on rendered frames), widest box ending by x<=870.
4. **SFX need real variety.** 13-19 DISTINCT sounds per episode, no repeated sound
   within an episode (a deliberate rhythmic triplet is the exception, and even then
   vary the samples). Rotate the whole library: ding, riser, swoosh_elec/double/deep,
   pop_balloon/pop_bubble, bass_hit, impact_trim, shutter, whoosh_trim — not just
   click/swoosh/pop every time.
5. **Zooms: strong (1.08) and butter-smooth**, focal on the face (eye line 540,730).

## Renderer traps discovered this batch (beyond OVERLAY_SPEC's existing list)

- **A `fromTo` property present ONLY in the from-vars is silently dropped by the
  seek-based renderer** — especially across `repeat` iterations. The element renders
  with that property at its CSS base value. Real case: EP22's arrow pulse dot had
  `y: 353` in from-vars only; it rendered 353px above its path, at the frame's top
  edge, teleporting frame to frame. **Every x/y/scale you set in from-vars must also
  appear in the to-vars** (same value = a constant tween) — and give animated
  elements an explicit CSS `left/top` base so a dropped transform degrades gracefully.
  A regex sweep found 24 such hazards across 12 slots; sweep for this pattern in any
  new batch (`fromTo(...{...x/y...}, {...missing...})`, including helper functions
  whose target is a variable, which a quoted-string grep misses).
- **A missing `class` attribute collapses an absolutely-positioned layout to the
  frame's top-left corner** — the CSS block silently never applies, the children
  resolve against #root, and every label double-draws at y~0. This shipped TWICE in
  one episode (EP26 slot_hook, then slot_payoff which reused the same markup).
  When a bug is found in one slot, **grep the whole episode (all episodes) for the
  same pattern before calling it fixed** — the payoff was sitting there broken while
  the hook got repaired. A cheap lint: diff CSS-declared classes against markup
  `class=` usage (mind JS-created elements).
- **ffmpeg `crop` freezes `iw`/`ih` at init** — its x/y expressions ARE re-evaluated
  per frame, but against the INITIAL input size, not the current frame's. An
  iw-based crop offset after an animated `scale` silently pins the crop at its first
  value and the zoom anchors to the top-left corner ("it's zooming into the left").
  Write animated-crop offsets in terms of `t`, replicating the scale stage's exact
  trunc-to-even quantization so offset and size never disagree (that mismatch is
  also THE source of zoom judder: motion arrives as irregular 0-2.5px lurches).
  Verify with a synthetic crosshair video: a mark at the focal point must stay
  pinned (measured (539.5, 730.0) across the whole zoom after the fix; per-frame
  motion <=0.24px). The full story is in `build_punch_zoom_filter`'s docstring.
- **`alimiter` defaults to `level=true`, which re-normalizes its OUTPUT back toward
  full scale** — as a ceiling it is a no-op-that-lies unless you pass `level=false`.
- **The native AAC encoder can overshoot ~3.5dB past ANY pre-encode ceiling on
  clipped/square-wave content.** A pre-encode WAV measuring a clean -2.0 dBTP decoded
  to +1.4dB after AAC. Two sources of such content: a broken myinstants download
  (`tt_hold_up.mp3` decoded to **+14.3 dBFS float peak** — always check a new file's
  float peak before cueing it) and hot plosives pushed into loudnorm's limiter.
  EP21-B needs a custom chain (surgical 200ms dip on the plosive, dynamic loudnorm,
  +0.85dB makeup, 192kHz-oversampled `alimiter=...:level=false`, then AAC) — see
  `episodes/ep21-kanonymity/project.md`.
- **Single-pass dynamic loudnorm can under-level by 1-2 LU on some streams** and its
  dynamic mode occasionally lets a true peak through. Always measure the DECODED
  final (`astats` + `loudnorm=print_format=json`) and match A/B variants' integrated
  loudness within ~0.3 LU so the hook test is fair.

## Animation-correctness rules (extending OVERLAY_SPEC)

- **An element that animates in later is NOT offscreen before its tween starts.**
  With `immediateRender:false` it sits at its CSS REST position from frame 0 — EP23's
  container box rested exactly on top of the card text for the whole first act.
  Elements that enter later must be hidden at rest (CSS `opacity: 0`) or based
  off-canvas, and the collision audit must include their rest positions.
- **The pairwise-collision audit must include every element's full trajectory AND its
  frame-0 rest state**, not just its "designed" position.

## Process lessons

- **Check the checker before believing a failure — or a pass.** This batch:
  the SFX-audibility checker false-flagged ~20 cues (control windows contaminated by
  neighbouring cues, by long ring-outs (bass_drop rings ~3.5s), by offset-anchored
  sounds (riser peaks 1.85s after onset — its own ramp occupies the "control"), and
  by non-scalar mix chains (a limiter breaks the fitted-gain assumption — verify
  those with direct band-RMS deltas instead). And two margin audits false-PASSED
  corner-pinned content. Every flag was resolved by an independent method before
  acting; every "clear" on something a human flagged deserves the same suspicion.
- **The SFX volume formula** actually used by the calibration table:
  `vol = 0.45 * 10^(0.6*(-18 - mean_dB)/20)`, clamped [0.15, 0.95], then the known
  manual overrides (bass-heavy <=0.45, voice memes x1.25, sparkle boosted).
- **When only visuals change, stream-copy the verified audio** into the new composite
  (`-map new:v -map old_final:a -c copy`) — bit-identical mixes, no re-verification,
  and it sidesteps the EP21-B AAC quirk. (STYLE.md already said this; it saved three
  full audio passes this batch.)
- **The supersampled zoom renders at ~5.5x realtime** (~27s per 5s segment). One
  variant fits a ~10-minute window; TWO CONCURRENT composites thrash and die.
  Composite serially, in foreground calls. Background jobs also got killed while
  agents had Chrome render batches running — assume ~10min/background job under load.
- **A/B variant conventions**: A = "prepping you for your system design interview",
  B = "Exploring Really Cool Tech"; build compositions once, share across variants;
  per-variant caption files; B's cues = A minus the intro delta. EP20 has no
  cool-tech take → B is a cold open whose sticker carries the hook text. EP26's
  intros all misspeak "episode 25" → corrected on screen by `slot_fix26`
  (`*EPISODE 26` / `he can't count`) popping exactly on the spoken "25" — Gordon
  approved this gag treatment for misspeaks.
- **Real data beats mockups** and Gordon consistently likes it: the real OpenAI
  tokenizer capture (with the real st|raw|berry split), the real
  `api.pwnedpasswords.com/range/CBFDA` response (1,972 suffixes, the real match
  count 2,266,543), real GH Actions runs, phippy.io art (CC-BY), real container-ship
  photo. Reject visual puns; capture the real software.
- **Sweep-by-pattern after every point fix.** The single most expensive mistake of
  this batch was fixing EP26's hook without grepping for the same broken markup in
  its sibling slots — Gordon found the payoff himself one feedback round later.
