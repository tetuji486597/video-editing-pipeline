---
name: system-design-overlays
description: Design and verify motion-graphic overlays for "System Design in 60 Seconds" episodes (video-use + HyperFrames pipeline). Load this before building or regenerating any episode's animations/ overlays. Modeled on EP4's overlays (the confirmed gold standard) — multi-phase mini-narratives, full-screen atmospheric takeovers, realistic UI recreations — with numeric self-checks, not just a vibe check.
---

# System Design overlay system

This skill went through two rounds of feedback. Round 1 (on EP3): overlays were **too
infrequent, too small, too short-lived, and not creative/aesthetic enough** — confirmed by
measurement, not just impression (EP3 originally covered ~55% of runtime, with one 16.1s
beat covered for only 7.5s). Round 2: overlays needed **real images from the web** (not
just custom shapes) and **format variance within one episode** (not always a transparent
band over live footage). Round 3, the most important: Gordon pointed at **EP4 (the CAPTCHA
episode) specifically** as the standard to emulate for presentation and pacing —
`/Users/gordon.jin/Downloads/edit_ep4/animations/slot_new_component/` and `slot_problem/`
are the reference implementations. Read this skill, but when in doubt, go read those two
files directly — they're worth more than any paragraph here.

## The EP4 case study (read the source, this is a summary)

EP4's `new_component` (the CAPTCHA grid, 7.9s) and `problem` (the sign-up form under bot
attack, 5.6s) overlays share a recipe that's richer than a "big card with a stat" — study
it before building anything:

- **Full-screen opaque takeover as the default for a conceptual/product moment**, not the
  exception. Both compositions fill the entire 1080x1920 canvas with a dark atmospheric
  background (`radial-gradient` base + 1-2 colored glow blobs + a vignette) — the
  talking-head footage is fully replaced for that beat, captions still burn on top. This
  reads as a produced cutaway, not a decoration on top of the shot.
- **A realistic UI/product recreation as the hero element**, not an abstract diagram. The
  CAPTCHA grid looks like an actual "select all squares with traffic lights" challenge
  (real street-intersection photo, amber grid lines, checkmark badges). The sign-up form
  looks like an actual product screenshot (rounded card, field labels, a real "Sign Up"
  button). This is why they read as high-production rather than a slide.
- **A two-phase (or more) mini-narrative inside one overlay, with a transition beat between
  phases.** The CAPTCHA composition: Phase 1 builds the challenge (header → reference chip
  → grid fades in → tiles get selected one by one, staggered → checkmarks pop in), then a
  **shutter-flash transition** (~0.06s white flash + a desaturate hit) at the phase
  boundary, then Phase 2 pays it off (the grid dims/recedes, data-flow lines draw from each
  selected tile into a glowing "AI eye" icon, traveling data packets loop along the lines,
  a "TRAINING_DATA.JPG" tag and an "OBJECT DETECTED / traffic_light / confidence 0.98"
  detection card land). The sign-up form does the same trick with a calm state and a
  swarming-red-glow "under attack" state. **This is the single biggest lever** — one overlay
  that visually dramatizes two beats of an idea (the setup AND the twist/consequence) reads
  as far richer than the same runtime spent on one flat reveal-and-hold.
- **Continuous motion throughout, never fully static.** A slow camera push-in
  (`scale: 1 → 1.09` over the whole 7.9s) runs underneath everything else. Selected tiles
  have a breathing amber glow (`yoyo: true, repeat: 7`). The AI eye's glow pulses
  (`yoyo, repeat: 4`). Nothing just sits there once revealed — there's always a subtle
  ambient animation layered on top of the main reveals.
- **Real sourced images embedded as functional UI detail, not as the whole-frame hero.**
  The CAPTCHA's grid photo and reference-icon thumbnail are real images, but they're
  inset into designed chrome (rounded corners, borders, glow) — the photo is a component
  of the UI, not a full-bleed background with text laid over it. (Photo-anchored
  full-bleed treatments, like EP3's hook, are also valid — this is a second, distinct
  pattern worth alternating with, not a replacement for it.)
- **Color-codes each phase/state.** Amber for the CAPTCHA-challenge phase, cyan for the
  AI/data-collection phase. Blue glow for the calm form, red glow for the swarm-attack
  state. Color shift is itself part of how the phase transition reads.
- **Grain/dither texture + vignette on every composition** — a static, deterministic
  `feTurbulence` filter at very low opacity, breaking up gradient banding and giving the
  dark backgrounds texture instead of reading as flat CSS.
- **Pacing/coverage is NOT maximized to fill the whole beat.** EP4's overlays actually
  cover only ~45-55% of their beat's duration (e.g. `new_component` runs 7.9s inside a
  16.7s beat) — measured, not assumed. What makes this feel complete rather than sparse is
  that the produced moment itself is dense and multi-phase; the remaining talking-head time
  reads as intentional breathing room between produced beats, not a gap. **Don't chase a
  coverage percentage at the expense of density** — a rich 45%-coverage overlay beats a
  thin 95%-coverage one. See rule 1 below for how this replaces the old flat-percentage
  mandate.

## Hard rules

1. **Every beat gets ONE produced overlay moment — but don't maximize its length, maximize
   its density.** No beat should be left with zero overlay, and no overlay should be a
   thin single-stage reveal stretched to fill time. Target: the overlay's own runtime
   should be dense enough that a viewer could not tell it was cut short — i.e. it has a
   real beginning/middle/end (see rule 3) — even if that runtime is well under the beat's
   full duration. EP4's ~45-55% per-beat coverage with rich multi-phase content is the
   reference, not a ceiling — a longer or shorter overlay is fine as long as it's dense
   throughout. Compute beat boundaries from the EDL's cumulative range durations (output
   timeline) so you know how much room exists, but the goal is a well-paced produced
   moment followed by clean breathing room, not wall-to-wall coverage.
2. **Size: bias toward large, dominant treatments.** Primary hero numbers/words ≥90px
   font-size. Graphic/UI elements should be large enough to read as the main subject of
   the frame, not a corner accent — EP4's form card and CAPTCHA grid both occupy roughly
   the center 700-900px of the 1080px width. Full-screen takeovers (rule 7) are the
   strongest way to guarantee this.
3. **Multi-phase structure, not front-loaded-then-static.** Every overlay should have at
   least two distinct visual phases with a transition beat between them (a flash, a color
   shift, a scale/recede move) — see the EP4 case study above. A single build-up with no
   payoff/twist phase is the most common way an overlay reads as thin even when it's
   technically "long enough."
4. **Creativity: no template reuse across beats in the same episode.** Don't repeat the
   same composition archetype for every beat. Vary color per beat/phase (see case study).
   No emoji icons (hand-drawn SVG, realistic UI recreations, or real sourced photos only).
5. **Never break the caption clearance — or the presenter's face.** The caption band
   (`MarginV: 350`, `--caption-font-size 74`, `--caption-margin-lr 190` on a 1080x1920
   canvas, worst-case footprint roughly y=1300-1920 for a 3-line wrap — these values climb
   over time, always confirm the current ones in `render.py`/`STYLE.md` rather than
   trusting this paragraph) must stay clear of overlay content with a visible gap — measure
   it, don't assume. On any overlay where live footage remains visible (not a full-screen
   takeover), the same discipline applies to the presenter's face: a photo card's bottom
   edge landing across the mouth/chin, or a chart line/callout box sitting on the nose or
   mouth, reads as broken even though it never touches a caption. Grid-measure the actual
   face position for that specific shot (this footage typically runs the mouth
   ~y=980-1080, chin ~y=1080-1200 — confirm per-shot, don't assume it transfers) and either
   extend a photo card past the chin or insert a spacer so graphic elements land on the
   chest, not the face. Plain text with a strong shadow overlapping the forehead/hair is
   fine (established convention) — solid boxes/lines/photos on facial features are the
   specific thing to avoid. **Fix patterns, in order of preference:** (1) if there's real
   vertical space between the face and the caption zone, just reposition the offending
   element(s) up; (2) if there isn't — common once a graphic needs to be bigger than
   ~150px tall, since the gap between "below the chin" and "above the caption" is often
   under 100px on this footage — convert the whole overlay to a full-screen opaque
   takeover instead (dark `radial-gradient` `#bg-fill` + `#vignette`, content recentered
   in the vertical-middle, clear of both constraints — more robust than fine-tuning a
   transparent band); (3) if a composition connects fixed SVG coordinates to a moving
   element (e.g. data-flow lines from a grid to an icon), moving just one endpoint breaks
   the line's geometry — recompute every connected coordinate together (including any
   "recede" scale/translate transform on the source content) and verify with real
   rendered frames, not arithmetic alone.
6. **Use real images from the web, not just custom shapes/vectors/charts** — but embed
   them as functional detail inside designed UI chrome (a thumbnail, a grid photo, an
   inset), per the EP4 case study, as at least as often as using them as a full-bleed
   background. Source via the `media-use` skill's HeyGen catalog or the web directly.
   Prefer generic/stock-safe imagery over real branded screenshots (recurring lesson:
   EP5's sourced "ticket" image came back with unrelated event branding baked in and had
   to be cropped down) — the goal is a real image grounding the concept, not a specific
   trademarked UI, unless the user has asked for that brand by name.
7. **Vary the overlay format itself within one episode.** Full-screen opaque takeover
   (EP4's default, and the strongest option for a conceptual/product moment) is
   encouraged, not just "allowed." Within a single episode, mix genuinely different
   overlay *formats* across beats — draw from at least 3 of: (a) full-screen opaque
   takeover with a realistic UI/product recreation, (b) a real-photo-anchored full-bleed
   scene, (c) a transparent corner/band accent over live footage, (d) a split-screen or
   before/after comparison, (e) a data-viz/chart takeover. Format variance is scoped
   per-episode — episodes don't need to match each other's specific format mix.

## Workflow

1. Read the EDL. Compute each beat's output-timeline start/end from the cumulative sum of
   range durations. This tells you how much room exists, not how much you must fill.
2. For each beat, sketch: the composition archetype (rule 7), what real image (if any)
   anchors it (rule 6), and — most importantly — the **two-plus-phase story** it tells and
   what the transition beat between phases looks like (rule 3). If you can't articulate a
   phase 2, the concept probably needs more thought before building.
3. Build, lint (`npm run check`), render each slot.
4. Update the EDL's `overlays` array so each overlay's `start_in_output`/`duration` places
   it sensibly within its beat (starts shortly after the beat begins; doesn't need to run
   to the beat's end — see rule 1).
5. Composite + remix per the normal `render.py` pipeline.

## Self-check before calling it done (run this, report the findings)

- **Density audit:** for each beat, confirm the overlay has a real multi-phase structure
  (name the phases and the transition beat) — not just "yes it has an overlay."
- **Coverage report (informational, not a hard gate):** overlay duration ÷ beat duration,
  per beat. Report it for visibility, but don't treat a number below 85% as a failure by
  itself — judge density (above) instead. Flag it only if a beat has NO overlay at all.
- **Size spot-check:** extract one frame per beat at its visual peak and confirm the
  primary element reads as large/dominant.
- **Caption-clearance and face-clearance audit — check across each beat's FULL duration,
  not one frame.** This is the check most likely to give a false pass if done lazily.
  Extract frames at multiple timestamps spanning each overlay's entire on-screen run
  (start, ~25%, ~50%, ~75%, near-end) and confirm a visible gap to both the caption band
  and (if live footage is visible) the presenter's face at every one of them — crop tight
  and grid-measure if it looks close, don't eyeball a full 1920px frame. Captions change
  word-by-word every ~0.3-0.5s and overlay animations evolve continuously, so a collision
  can exist for only part of a beat and be completely invisible in a single sample frame.
  This exact mistake shipped 15 real collisions across 4 episodes (EP3/4/5/6) after a
  caption size/position/width change — every one was only checked at one frame originally,
  and every one was only colliding during a different portion of its beat's runtime. See
  rule 5's fix patterns for how they were resolved (reposition, full-screen-takeover
  conversion, or SVG-coordinate recompute).
- **Real-image audit:** count real sourced images per episode and note whether each is
  used full-bleed or embedded as UI detail (both are valid; zero across a whole episode
  fails rule 6).
- **Format-mix audit:** list each beat's format. Fewer than 3 distinct formats in one
  episode fails rule 7.
- Report all findings before presenting the result — if something's off, fix it first.
