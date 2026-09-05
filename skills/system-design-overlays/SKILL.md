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
   **Confirmed real failure: EP7 shipped its first cut with all 7 overlays as
   full-screen CSS/SVG takeovers — zero transparent formats, zero real images —
   despite this rule already existing in the skill at the time.** The rule existing
   isn't the same as it being checked; nobody ran the format-mix self-check until the
   user asked for variety directly, by which point 3 slots needed rebuilding from
   scratch. **Assign each beat's format (and whether it needs a real image, rule 6)
   during the planning pass (workflow step 2), before building anything** — write the
   whole episode's format-per-beat list up front and confirm it already spans ≥3
   formats, rather than defaulting every beat to the safest option (full-screen
   takeover) and hoping to catch the mix at the end.
8. **Never position two visible elements independently without checking their resolved
   pixel ranges against EACH OTHER — not just against the caption band and the face.**
   The caption/face check (rule 5) covers collisions between an overlay and things
   *outside* it; this rule covers collisions *within* one composition's own elements,
   which is just as common and easy to miss. Two ways this happens, both confirmed real
   bugs, not hypotheticals:
   - **Different coordinate frames.** One element positioned `bottom: Npx` relative to a
     parent container, another positioned `top: Mpx` in a totally different (often
     outer/sibling) coordinate frame. Each number looks reasonable read in isolation, but
     nobody resolved both to absolute canvas pixels and compared them. (EP5's `slot_problem`:
     `#pay-btn` was `bottom: 44px` inside a `560px`-top, `460px`-tall card — resolving to
     `y: 892-976` — while `#err-text`, a sibling of the card, was hardcoded `top: 930px` in
     the outer frame. Nobody added it up; the button's own label text was covered by
     "NETWORK DROPPED THE RESPONSE" for the entire beat.)
   - **Insufficient margin between a small element and a much larger one, especially with
     glow/text-shadow.** A `margin-top` that separates two text boxes' CSS boxes by a
     positive number can still visually crowd/touch once font ascenders, glow blur radius,
     and text-shadow spread are accounted for — a small gap that "should" be enough on
     paper reads as touching on screen. (EP3's `slot_payoff`: a 34px intro line and a
     96px emphasis line only 22px apart — visually crowded against each other badly enough
     to misread as one merged sentence.)
   - **Fix / prevention:** for every element in a composition, compute its resolved
     absolute top/bottom in real canvas pixels (walk up the `position: absolute` ancestor
     chain, don't trust a number read out of context) and check it pairwise against every
     other simultaneously-visible element — not just the ones that look risky. When two
     elements must sit close together (an intro line before a big emphasis line, a button
     label near an error message), use a generously large explicit gap (40px+) rather than
     a small margin that "adds up" correctly on paper. Verify with a real extracted frame,
     the same as any other clearance check in this skill — computed CSS math has been wrong
     more than once even when it looked right on paper.
9. **A fix to an overlay's `index.html` does not exist in the shipped video until the
   downstream base composite is rebuilt from it — matching duration is not evidence a
   base is current.** `render.py`'s per-segment base render (`base_vN.mp4`) bakes in
   whatever overlay `render.webm` files existed at build time. If an overlay is fixed
   afterward (e.g. a caption-collision reposition) but a later step (an SFX remix, a
   music-removal pass) reuses an *existing* `base_vN.mp4` by filename instead of
   rebuilding fresh, the earlier fix silently never ships — even though the source file
   is correct, even though the fix was already verified against a *different*, fresher
   render at the time. This happened for real: EP6's payoff overlay was correctly
   repositioned and verified clean, but the SFX-retiming pass later reused a `base_v9.mp4`
   built two days *before* that fix, and the shipped video reverted to the broken
   position with nobody noticing because duration matched. **Before reusing any
   `base_vN.mp4` (or similar) for a downstream step, check whether ANY overlay's
   `index.html` or `render.webm` has a newer mtime than that base file** (e.g. `find
   animations -name "render.webm" -newer base_vN.mp4`) — if anything is newer, rebuild the
   base fresh via `render.py --build-subtitles` (with the episode's current caption flags)
   before doing anything downstream with it. When in doubt, just rebuild fresh — it's
   cheap, and reusing a same-duration file that "should" be current is exactly the trap
   that shipped this bug. **This also applies mid-build, not just to later sessions**: if
   you (or sub-agents you spawned) are still building/fixing overlays when you run the
   first full composite, one of them can still be mid-write — confirmed real case on EP10,
   where a `slot_new_component` sub-agent's fix-up render landed ~30s *after* the first
   `final.mp4` finished, silently shipping a pre-fix version. Re-run the `find ... -newer`
   freshness check immediately before the FINAL render you intend to ship (not just once
   at the start of the session) — if anything comes back, rebuild fresh again before
   moving on to SFX/final delivery.
10. **Format choice affects sequencing, not just visuals.** An opaque full-screen
    takeover placed *after* another overlay specifically to avoid hiding it (e.g. after
    a title card) delays its own content until that other overlay clears — there's no
    way to start it earlier without either hiding the thing underneath or accepting the
    wait. If a beat's content needs to appear as early as possible, consider whether it
    actually needs to be opaque at all — a transparent floating card or corner accent can
    run *simultaneously* with a preceding overlay (nothing to hide), landing its content
    much earlier. **Confirmed real case: EP7's hook held a real video demo that needed to
    appear right at the top of its beat.** As a full-screen opaque takeover it had to wait
    for the title card (2.766s) to clear first — the video didn't visibly start until
    ~2.85s in, which read as "too late." Converting it to a transparent card floating over
    live footage (no opaque bg-fill) let it start at output 0.0, simultaneous with the
    title, landing the video almost immediately — verified with an isolated title+hook-only
    test render to confirm no collision (title occupies the upper third of the frame; the
    card was sized/positioned to start below it).
11. **The "plain text over forehead/hair is fine, solid boxes/photos are not" allowance
    (rule 5) extends to simple graphic linework too, not just text.** A lightened
    outline/glow shape — transparent-ish fill (~30% opacity or less), border + glow only,
    no solid backing — reads the same as text on this kind of footage and can sit over the
    hair, not just in whatever sliver of pure clear background sits above the hairline.
    **Confirmed real case: EP7's build-beat node-chip banner** was originally confined to
    the ~200px of genuinely clear ceiling measured on a real frame (grid-measured: hair
    tips start around y=200-220 on this footage) and read as "way too high"/cramped on
    review even though it had zero technical collision. Lightening the chip fill from
    solid dark (`rgba(10,14,22,0.88)`) to translucent (`rgba(6,10,18,0.32)`) let the whole
    band move ~150-350px lower, landing naturally over the hair instead of pinned to the
    very top edge — a *design* fix (rebalancing solidity vs. position), not a repositioning
    fix alone. If a graphic reads as awkwardly placed but isn't actually colliding with
    anything, consider whether it's fighting for space it doesn't need to fight for because
    it's more visually "solid" than it needs to be.
12. **Every overlay must fade out before its own declared duration ends, AND consecutive
    overlays' enable-windows must be contiguous (zero gap) — a beat should never expose a
    frame of bare live footage between two overlays.** Two distinct failure modes, both
    confirmed real, usually occurring together: (a) an overlay's content stays fully opaque
    right up to its own `data-duration` cutoff with no fade tween at all, so it hard-cuts
    straight from opaque content to whatever's behind it; (b) the EDL's `overlays` array
    leaves a small gap (tens to a few hundred ms) between one overlay's
    `start_in_output+duration` and the next one's `start_in_output`, during which nothing is
    composited at all. Individually each is minor; together they read as "flashes for a
    second, then cuts to me, then cuts to something else" — exactly as jarring as it sounds,
    and worse when it lands on a climactic line. **Confirmed real case: EP11's PROBLEM beat
    ended on a fully-opaque "BOTTLENECK" stamp with zero fade-out, followed by a 170ms EDL
    gap before BUILD started** — a live-face flash landing right on the episode's punchline.
    Auditing the rest of that episode found the same missing-fade-out bug in 3 of its other
    5 content overlays. **Fix, applied to every overlay in the episode, not just the one
    reported:** add a tail fade (`#content-all` opacity → 0) finishing shortly before the
    composition's own native duration, then extend that overlay's `data-duration` (both the
    HTML file and the EDL) so its enable-window end lands exactly on the next overlay's
    `start_in_output` — zero gap, verified via `next_start - this_start` arithmetic, not
    eyeballed. Re-render and re-verify by compositing the actual rebuilt overlay onto a real
    base-footage frame at the transition point, not just by reading the timeline numbers.
    **Confirmed real follow-on failure, from actually shipping this fix on EP11: fading out
    "finishes shortly before the composition's own native duration" is itself the bug if
    you leave any buffer at all.** The first fix left a 70-360ms gap between when each
    fade-out finished (fully transparent) and the overlay's extended duration/EDL end —
    reasoning it was "safe padding before the hard cutoff." It is not safe: with nothing
    else compositing during that window, it *is* the live-footage flash, just relocated
    to a few hundred ms earlier. **The fade must finish at *exactly* the overlay's true
    end, zero buffer** — shift the fade's start time later (same duration, same speed) so
    it lands precisely on the boundary, don't just cap it "shortly before." **This was
    caught late because it was checked by sampling frames every 50-100ms and eyeballing —
    a 3-6 frame gap (125-250ms at 24fps) is invisible at that sampling density.** Verify
    any transition-gap fix by exporting *every frame* across the transition window
    (`ffmpeg ... -vf fps=<source fps>`) and confirming none of them is a bare/empty
    composite — not a handful of spot samples. **A second, related bug found during that
    same frame-by-frame re-check: even at zero gap, 1-2 frames read as near-total black**
    at every transition — not a missing-composite gap, but the *incoming* overlay's own
    entrance: a full-screen takeover's `#bg-fill` (a static, very dark gradient) is opaque
    from local frame 0, while its actual content (header/card/glow) doesn't start fading
    in until 0.05-0.15s later, so there's a brief window showing only a plain near-black
    background right as the viewer's eye was adjusted to a bright lit face. Fix: start
    each overlay's primary entrance element at local time 0 (not 0.05-0.15s), and never
    give a background-fill element its own slow fade-in (if `#bg-fill` fades in at all,
    keep it under ~0.05-0.08s — a background should be there instantly, only foreground
    content needs a graceful reveal).
13. **Never animate SVG `rotation` (or any transform-origin-dependent property) on an
    element whose own geometry has a degenerate bounding box** — most commonly a `<line>`
    where `x1 === x2` (zero width) or `y1 === y2` (zero height), like a clock/gauge hand.
    **Confirmed real case: EP11's expiry-clock hand**, an SVG `<line>` rotated via GSAP
    `rotation`, warped into a hooked/curled shape and nearly vanished at several points in
    its sweep — confirmed via raw PNG snapshot (not a video-compression artifact). The
    standard fix (passing `transformOrigin` explicitly on the tween, in case GSAP's
    auto-detected pivot was degenerating to the shape's bbox center instead of the intended
    CSS-declared point) did **not** resolve it, meaning the cause runs deeper than origin
    auto-detection into this renderer's SVG-transform handling generally — don't assume
    that fix will work here even though it's the textbook answer. **Robust fix: don't
    rotate the element at all.** Tween a plain numeric angle on a JS object and set the
    line's endpoint attributes (`x2`/`y2`, or equivalent) directly every frame via
    `Math.sin`/`Math.cos` in an `onUpdate` callback — this only ever writes plain SVG
    coordinates and can never be affected by transform-origin ambiguity of any kind. This
    is deterministic (pure trig, no `Math.random()`/`Date.now()`) so it's safe for
    HyperFrames' rendering model. Prefer this pattern from the start for any rotating
    hand/needle/pointer element, rather than reaching for GSAP `rotation` and finding out
    at review time.
14. **A "genuinely clear" position check applies to the frame edges themselves, not just
    to the face/caption zones** — this recurs even on full-screen opaque takeovers with no
    live footage to avoid. **Confirmed real case: EP11's AI_ANGLE split comparison** had its
    top title pinned at `top: 40px` (2% down a 1920px frame) — nothing to collide with
    (opaque background, no face), yet it still read as "way too high, gets cut off,"
    because real playback contexts (platform UI chrome, safe-area conventions) expect
    meaningfully more top breathing room than "technically not clipped by our own canvas."
    Treat ~150-200px as the practical minimum top margin for hero text even in a fully
    opaque composition, and check it by eye against a real rendered frame — "nothing else
    is there" is not the same as "it looks right."

## Measure it on the rendered file. Do not trust CSS, and do not trust the linter.

Everything below was learned by shipping wrong overlays that passed every check. The single
highest-value habit in this skill is: **decode the rendered `.webm` and measure pixels.**
CSS arithmetic and `npx hyperframes check` both pass compositions that are visibly broken.

**VP9 alpha lives in a side channel, and this bites everyone exactly once.**
`ffprobe` reports `pix_fmt=yuv420p` on every overlay in this series, including ones that are
provably transparent. The real signal is the stream tag `alpha_mode=1`. And you **must**
decode with `-c:v libvpx-vp9` — the default decoder silently drops the alpha plane, so a
transparent overlay measures as fully opaque and a working fade measures as a hard cut.
Three separate sub-agents reached the wrong conclusion from `pix_fmt` in one batch.

```
ffprobe -v error -select_streams v:0 -show_entries stream_tags=alpha_mode -of default=nw=1:nk=1 render.webm
ffmpeg -v error -c:v libvpx-vp9 -i render.webm -vf "alphaextract,signalstats,\
metadata=print:key=lavfi.signalstats.YMAX:file=-" -f null -
```

Note `file=-` — `metadata=print` writes to the log, which `-v error` suppresses. Without it
you get an empty result and conclude the file is unreadable.

**The colour plane is garbage where alpha is 0.** To ask "what does this overlay actually put
behind the captions", composite it over black first (`color=black` + `overlay`), which weights
colour by alpha. Measuring the colour plane directly reports every transparent overlay as a
blinding white wash.

**A format is what it MEASURES as, not what you called it.** A "photo card" or "panel" whose
stacked background wash + glow blobs + vignette push rendered alpha near 1.0 across the frame
IS a takeover, and it silently breaks the episode's format mix and takeover cap. No lint
catches it — every individual rule is satisfied. Measure mean alpha; a genuine non-takeover
shows live footage at 25-40% in the open areas. Corollary: once footage really shows through,
type that used to sit on a wash now sits on live video — strengthen its `text-shadow` in the
same pass.

**Distinguish a shutter flash from a sustained wash by DURATION, not peak.** A 2-5 frame white
flash is EP4's own transition technique and legitimately whites out the caption band. A peak
measurement alone cannot tell it from a defect; count how many frames exceed the threshold.

**Check junctions, not just slots.** Per-slot fade checks miss rule 12's actual failure, which
lives at `this.start + this.duration` vs `next.start` in the COMPOSITED output. Export every
frame across each boundary at the output frame rate and confirm none is bare footage or
near-black:
`ffmpeg -ss <t-0.15> -t 0.5 -i final.mp4 -vf fps=24 j_%02d.png`. Spot samples every 50-100ms
miss a 3-6 frame gap entirely.

**Beware metrics that under-report what you are looking for.** Two real own-goals in one batch:
a fade check using max-alpha flagged three healthy slots as "hard cuts" (the 30fps overlay is
resampled to 24fps, so the final high-alpha frame is often never sampled); and an SFX
audibility check run at 8 kHz declared a shimmer inaudible because everything above 4 kHz had
been discarded — the same cue measured 0.80x baseline at 8 kHz and 3.27x at 32 kHz. When a
check says something is wrong, confirm the check before rebuilding the thing.

## Renderer traps (in addition to rules 13-14)

- **A `box-shadow`/glow reaches ~1.6x its blur radius past the element edge**, not half and not
  1.0x. `reach = edge + offset - 1.6*blur`. A 14px blur at `top:190px` puts non-zero alpha on
  row 178. Budget the whole thing near y=180/y=1280 and verify on decoded pixels.
- **Tweening `filter` from a computed `none` renders the element SOLID BLACK** for its first
  frames — GSAP reads the from-value as `brightness(0)`. Declare an explicit identity filter in
  CSS (`filter: grayscale(0) brightness(1)`) and repeat it in the `fromTo` from-vars. Live risk
  on any desaturate/contrast-cut/blur transition.
- **An SVG `<filter>` defaults to `x=-10% y=-10% width=120% height=120%`, and `feTurbulence`
  is a GENERATOR that fills the whole region regardless of input.** A panel-confined grain
  layer therefore paints noise ~20% past its element on every side — one shipped grain into the
  caption band, invisible to CSS arithmetic. Pin the region: `x="0%" y="0%" width="100%"
  height="100%"` or `filterUnits="userSpaceOnUse"`.
- **Nesting fading ancestors MULTIPLIES their opacities**, so a three-layer fade squares or
  cubes the curve and reaches zero early, leaving dead frames. Fade one layer per visible leaf.
- **But a transformed child can keep compositing at full strength while its faded ancestor
  blacks out** — ancestor opacity is not applied uniformly to transformed descendants. So fade
  the leaf that carries the transform, never a wrapper above it.
- **Per-leaf fading composites as `1-(1-a)^n`.** With n opaque leaves, a tween at 21% renders at
  60-76% on screen. A back-loaded ease (`power*.in`) therefore strands the overlay visibly high
  at the enable-window cut; front-load it (`power*.out`) so the last stored frame is near zero.
  This is the direct consequence of the "one fade per leaf" rule and the two must be read
  together.

## This shoot's framing: "land it on the chest" is often impossible

Grid-measure every beat, but expect: mid shots have the brow ~y=760 and chin ~y=1215; tight
close-ups have the chin at **y=1370-1430**, i.e. BELOW the y=1280 content limit, with the
shirt line inside the caption band. On those there is no chest band at all. Options, in order:
a side column (x>=850 or x<=330), an upper band above the brow, converting to a takeover if the
episode's budget of 2 has room, or an argued minimal overlap — stated in the report, never
silent. An honest overlap beats a silent one.

## A/B hook variants

When one episode ships two cuts differing only by the intro take: build every composition
ONCE and share it; only the EDL `start_in_output` values and the SFX cue times differ, by the
delta between the two intro takes. **Give each variant its own caption file** — `render.py
--subtitles-out master.A.ass` — because `--build-subtitles` otherwise writes a hardcoded
`master.ass` and recompositing one variant against the other's leftover file misaligns every
caption in the episode without changing its duration.

## TikTok-native title box (the intro treatment)

The intro of each episode carries a TikTok-style text sticker instead of the house title
card. Reference implementation:
`episodes/ep19-likecounts/animations/slot_tiktok_title/` — copy it rather than rebuilding.

**It REPLACES `slot_title`, it does not join it.** The boxes occupy the same top-left region
as the house card's accent-bar block; running both collides. Swap the EDL entry, leave
`slot_title/` on disk, and note the swap so it can be reverted in one line.

**Wording is fixed per hook variant. Use verbatim:**

| spoken hook | title text | boxes |
|---|---|---|
| "prepping/preparing you for your system design interview" | `MASTERING SYSTEM` / `DESIGN:` / `EPISODE X` | 3 |
| "exploring really cool tech" | `RLLY COOL TECH:` / `EPISODE X` | 2 |

Note the cool-tech line is **abbreviated — "RLLY", no leading "EXPLORING"**. EP19-B shipped
with the older longer wording (`EXPLORING / REALLY COOL TECH:`) and was deliberately not
re-rendered, so it is the one file that does not match this table.

**The title must match that variant's SPOKEN hook.** On episodes with A/B cuts, each variant
needs its own composition — one shared title would contradict the narration on screen and
defeat the point of testing the hooks against each other.

**Construction:**

- **Each wrapped line is its own white rounded box**, not one box behind the block. That
  per-line raggedness is the single thing that makes it read as a native sticker rather than
  a broadcast lower-third. Author the line breaks; `white-space: nowrap` so they can never
  re-wrap.
- 82px Inter 800, black on white, `border-radius: 18px`, padding ~26/34px, `gap: 14px`,
  centred via a flex column with `align-items: center` so each box hugs its own text.
- **Placement: measure, then sit over the hair and the background, clear of the face.** On
  EP19's intro (hair top ~490, brow ~883, chin ~1279) the stack at y=250-680 overlaps the
  neon sign and hair exactly like the reference while clearing the brow by ~200px. A solid
  box over hair is fine here and is what the reference does; over facial features it is not.
- Hold it through the intro narration and fade before the hook beat (EP19: 0.000-7.400, with
  the hook at 9.000/8.167 — comfortably clear in both variants).

**Two checker traps this format hits specifically:**

- A genuinely static sticker — which is what a real TikTok text box is — makes the motion
  linter report **"Timeline did not advance under seek; every green verdict on this run is
  unreliable."** Give the hold an imperceptible drift (scale 1.000 -> 1.010 over the hold,
  `ease:"none"`); ~9px across the widest box, invisible at 1x, and it restores every other
  verdict on the run.
- CSS `transform: scale()` on the stack plus a GSAP **`.to()`** on scale trips
  `gsap_css_transform_conflict` — GSAP overwrites the whole CSS transform. `fromTo` is
  exempt, so write the drift as a `fromTo` with an explicit start.


## TikTok's UI safe zone — the horizontal limit

The `y=180-1280` band protects against OUR burned-in captions. It says nothing about
TikTok's own chrome, which is drawn over the video at playback and which no render of ours
can show. **Full detail, sources and the shipped-batch audit: `SAFE_ZONE.md`.**

| | zone | status |
|---|---|---|
| **DANGER** | `x >= 900`, `x <= 60`, `y >= 1600`, `y <= 140` | every source agrees |
| **CAUTION** | `x >= 800`, `y >= 1400` | source-dependent; a coin flip across devices |

**Usable content band: `x=60-900, y=180-1280` — 840 x 1100, centred at `x=480`, NOT
`x=540`.** Design to `x <= 860`. Same exemptions as the y-band: `#bg-fill`, `#vignette`,
full-bleed photos and full-frame effect layers may cross; text, UI and graphics may not.
A push-in expands x too, and about x=480 now — resolve the composed worst case on BOTH axes.

**Two phrasings that put the entire EP14-19 batch into the rail. Do not reintroduce them:**

- *"the main graphic should occupy the centre 780-900px of the 1080px width"* — centred on
  540 that is x=90-990 or x=140-940, both under the rail. **Always state an x-band, never a
  width plus an implied centre**; a width hides its own bounds.
- *"a tall narrow side column at x>=850 or x<=330"* — this was the recommended escape hatch
  for tight close-ups with no chest band, and `x>=850` IS the action rail. **Side columns go
  LEFT (x=60-330) only.** A right column would have to end by x=860, which leaves too little
  width to be worth it; prefer an upper band, a takeover, or an argued minimal overlap.

**The captions are the bigger encroachment, and no overlay check can see them** — they are
composited last by ffmpeg. At the EP14-19 settings (font 74 / lr 190 / MarginV 350) the band
is `x 190-890`, bottom `y=1570` always, and 3-line chunks occur in 7 of 8 episodes — so it
runs 50-170px into the bottom UI zone in every episode. The knobs are coupled: widening the
margins forces more wraps, which pushes the band top up into the y<=1280 overlay floor.
Burned across all 8 EP14-19 caption files and measured clean on all three constraints:
**`--caption-font-size 60 --caption-margin-lr 220 --caption-margin-v 400`** (text x 220-860).
`64/190/400` also measures clean if bigger text matters more than the x<=860 target.
**Burn any candidate before adopting it** — estimation picked `64/220/400`, which looks
identical on paper to `64/190/400` and actually breaches: the narrower box wraps a chunk to
four lines and puts 17 frames above y=1280 on EP17. It changes the caption look, so confirm
before switching.

**Verify on the rendered file:** `tool/helpers/check_safe_zone.py <render.webm>`. It
composites over black (VP9 keeps colour where alpha is 0, so raw-alpha checks lie) and
judges by DURATION, not peak — a 2-5 frame shutter flash whitens the whole frame, and both a
peak test and a `cropdetect` pass will call every takeover a full-frame violation.


## Talking-head zoom

Gradual centered drift, not a punch: `zoom: {mode:"slow", from, to, focal_x:540, focal_y:960}`.
Two things that make it read as intentional rather than cheap:

- **Alternate direction per segment** (`+-+-`), so each range starts at the scale the previous
  one ended on. The drift is then continuous across every cut instead of snapping back to 1.0
  at each edit.
- **Cap the magnitude against the overlays' measured clearances.** A centered zoom displaces a
  point by `distance_from_centre * (Z-1)`. With overlays placed against measured face positions
  at clearances as tight as 40px, **1.045 is about the ceiling** — it costs the tightest case
  ~13px, where render.py's 1.12 default would cost ~35px and push graphics into the face.
  Verify segment durations are unchanged afterward; if they are, every overlay cue and caption
  still lands.

## SFX

- **Every file must be trimmed of leading silence.** `build_sfx.py` hard-refuses anything over
  20ms and will kill the whole render pass. `silenceremove=start_periods=1:start_threshold=
  -45dB:start_silence=0:detection=peak`. This is separate from `impact_offset`, which handles
  sounds whose peak arrives after their onset.
- **Set volume from measured loudness, not by ear-guessing.** A sourced set can span 30+ dB
  mean level, so a flat per-cue volume buries the quiet ones and lets the bass hits dominate.
  Partially normalise (k~0.6) toward a target, then override deliberately.
- **Voice memes are wanted on this channel.** One per episode, placed where the meme's words
  match the narration rather than merely where a hit belongs. Trim hard — they download as
  12-18s clips and some peak a full second in, which would start them inside the previous beat.
  Give them a ~1.25x volume bump (speech competing with speech). Crude clips are out.
- **Verify audibility by differencing the mixed track against the no-SFX track with a fitted
  gain, at 32 kHz.** Comparing peak levels between the two proves nothing — `loudnorm`
  renormalises the whole mix, so peaks go DOWN after adding SFX.

## Helper tools (in `tool/helpers/`)

Use these instead of re-deriving them:
`words.py` (word-level lookup for cut edges and payoff-word sync) · `find_dead_air.py`
(acoustic range ends — ASR word boxes overrun the audio badly on this shoot) ·
`fix_windows.py` (output-timeline beat windows on render.py's real 24fps grid,
`ceil(nominal*24)/24`) · `check_overlay_timing.py` (overlay vs its beat) ·
`check_overlay_files.py` (existence / declared-vs-actual duration / staleness) ·
`check_fade.py` (entrance + fade on the rendered alpha plane) · `check_caption_band.py`
(what each overlay actually composites behind the captions) · `build_sfx.py`.


## Workflow

1. Read the EDL. Compute each beat's output-timeline start/end from the cumulative sum of
   range durations. This tells you how much room exists, not how much you must fill.
2. For each beat, sketch: the composition archetype/**format** (rule 7), what real image
   (if any) anchors it (rule 6), and — most importantly — the **two-plus-phase story** it
   tells and what the transition beat between phases looks like (rule 3). If you can't
   articulate a phase 2, the concept probably needs more thought before building. **Write
   down the whole episode's format-per-beat list right here and confirm it already spans
   ≥3 formats before building anything** — don't default every beat to full-screen
   takeover and hope to catch the mix later (rule 7's confirmed EP7 failure was caught
   only after 3 slots needed rebuilding).
3. Build, lint (`npm run check`), render each slot.
4. Update the EDL's `overlays` array so each overlay's `start_in_output`/`duration` places
   it sensibly within its beat (starts shortly after the beat begins; doesn't need to run
   to the beat's end — see rule 1).
5. Composite + remix per the normal `render.py` pipeline.
6. Run the tool suite: `check_overlay_files.py`, `check_fade.py`, `check_caption_band.py`,
   `check_overlay_timing.py`. Then check the JUNCTIONS on the composited output.
7. Re-run the freshness check (rule 9) IMMEDIATELY before the final render, not once at the
   start — it caught a composite built against an overlay that had re-rendered 12 minutes
   earlier, in this batch.

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
  episode fails rule 7. Run this at the *planning* stage (workflow step 2), not only at
  the end — checking it after every slot is already built means failing it costs a
  rebuild, not a plan change (rule 7's confirmed EP7 case).
- **Placement-feel audit, separate from the collision check above (rule 11):** even a
  graphic with zero technical collision can still read as awkwardly placed — extract a
  frame and actually look at it, don't just confirm the pixel math cleared. If something
  looks cramped or pinned to an edge, check whether it's more visually "solid" than it
  needs to be before concluding it just needs to move (rule 11).
- **Internal-collision audit (rule 8):** for every beat, list every visible text/graphic
  element with its resolved absolute pixel range (not the raw CSS number — walk the
  ancestor chain), and check each pair for overlap or a suspiciously small gap (<30px
  between a small and a large element). Don't skip elements that "look fine" individually.
- **Base-freshness check (rule 9):** before reusing any existing `base_vN.mp4` for a
  downstream step (SFX remix, music pass, anything that isn't a full fresh composite),
  run `find animations -name "render.webm" -newer <base file>` (and the same for
  `index.html`) — if anything comes back, the base is stale; rebuild fresh via
  `render.py --build-subtitles` before proceeding. Note this in your report either way
  (confirmed fresh, or rebuilt because stale).
- **Transition-gap audit (rule 12):** list every beat's overlay `start_in_output+duration`
  next to the following beat's `start_in_output` — any positive gap is a bare-live-footage
  flash waiting to happen. For each overlay, also confirm it has an actual fade-out tween
  ending at *exactly* its own native duration, zero buffer (a fade that finishes early
  just relocates the flash, it doesn't remove it — confirmed real regression on EP11).
  Also confirm the *incoming* overlay's primary content starts at local time 0, not
  0.05-0.15s in, and that any background-fill fade-in is near-instant (<0.08s) — a slow
  background reveal reads as a near-black flash of its own. Fix all of it together, then
  **verify by exporting every single frame across each transition window at native frame
  rate** (`ffmpeg ... -vf fps=<source fps>`, not spot samples every 50-100ms — a 3-6 frame
  gap is invisible at that sampling density, which is exactly how EP11's first "fix"
  shipped still broken) and confirm none of them is bare-live-footage or near-total-black.
- **Rotating-element audit (rule 13):** for any hand/needle/pointer/gauge animated via
  GSAP `rotation`, check whether the rotated element's own geometry is degenerate (a
  `<line>` with `x1===x2` or `y1===y2`, or similar zero-width/height shape). If so, don't
  trust it just because `npm run check`'s motion linter passed — render a few frames
  mid-sweep (a `hyperframes snapshot` at 3-4 timestamps across the rotation's active
  window) and look at them directly. If it warps or vanishes, switch to the trig/onUpdate
  pattern in rule 13 rather than tweaking transformOrigin values and hoping.
- **Format-is-measured audit:** for every non-takeover slot, measure mean alpha on the
  rendered file and confirm live footage is genuinely visible. A stack of "subtle" full-frame
  layers adds up to an opaque one.
- **Junction audit:** export every frame at the output frame rate across each overlay
  boundary in the COMPOSITED file and confirm none is bare footage or near-black.
- **Tease-chip grep by ELEMENT** (`class="tease`, `id="tease`, `<span>Next`) across every
  composition — the words never appear literally (`&mdash;` + CSS uppercase).
- **SFX audibility** by gain-fitted difference at 32 kHz, never by comparing peaks.
- Before concluding a check has found a defect, confirm the CHECK is sound — a max-alpha fade
  test and an 8 kHz audibility test each produced false failures in this batch.
- Report all findings before presenting the result — if something's off, fix it first.
