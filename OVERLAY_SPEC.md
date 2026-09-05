# Shared overlay build spec — "System Design in 60 Seconds"

Written during the EP14-19 rebuild but **not scoped to it** — this is the standing
build spec for any episode's overlays. The `system-design-overlays` skill carries the
generalizable rules and the verification methods; this file carries the concrete
per-slot requirements a builder needs open while writing markup.

Read this in full before writing any composition. Everything here is non-negotiable
unless your own brief explicitly overrides it.

## Scaffolding

Create the slot dir, then copy `package.json`, `hyperframes.json` from
`C:\Users\gordo\video-editing-pipeline\episodes\ep13-ratelimiting\animations\slot_title\`
and write a `meta.json` of `{"id":"<slot>","name":"<slot>"}`. Set `name` in package.json too.

## Render

From inside the slot dir, **always with these flags** — the default opens many visible
Chrome windows on this machine and actively disrupts the user:

```
npx --yes hyperframes@0.7.68 check
npx --yes hyperframes@0.7.68 render . --format webm -o render.webm --workers 1 --no-browser-gpu
ffprobe -v error -show_entries format=duration -of csv=p=0 render.webm
```

`check` must pass with **0 errors**. Do your layout arithmetic on paper BEFORE rendering —
every render cycle costs the user a burst of windows. Aim to render once.

## Required HyperFrames patterns

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<div id="root" data-composition-id="main" data-start="0" data-duration="D"
     data-width="1080" data-height="1920">
  <section id="scene" class="clip" data-start="0" data-duration="D" data-track-index="1">…</section>
</div>
<script>
  gsap.defaults({ lazy: false });
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });
  window.__timelines["main"] = tl;
</script>
```

- Every timed element needs `data-start`, `data-duration`, `data-track-index` AND `class="clip"`.
- `html, body { width:1080px; height:1920px; overflow:hidden; background: transparent; }`
- Any opaque fill or full-bleed photo lives on a CHILD div — never on `#root` or `.clip`.
- **DETERMINISTIC ONLY.** No `Math.random()`, no `Date.now()`, no `new Date()`, no runtime
  network fetches. A local image file on disk is fine. Hard-code every scatter/jitter/
  position as a literal array.
- Font: `font-family: Inter, sans-serif;`. Use a monospace stack
  for IDs, codes, params and counters — it is what makes a technical UI read as real.
  **Write the stack as `"JetBrains Mono", Menlo, monospace` — name JetBrains Mono FIRST.**
  Do NOT lead with `ui-monospace`: the renderer's font compiler aliases `menlo` / `sf mono` /
  `consolas` to JetBrains Mono but leaves `ui-monospace` unmapped, so a stack beginning with
  it silently falls through and every "monospace" run renders proportional in Inter. This is
  invisible in digit columns (sans figures are tabular anyway) and only shows in letters.
  Confirm it worked in the check log — it should report
  `Fetched N font face(s) for "JetBrains Mono"` — and by measuring that two equal-length
  character runs produce identical pixel extents.
- **Never tween `innerText`.** GSAP numerically interpolates it and renders garbage like
  `"0.9546 / 4"`. Use pre-rendered stacked digit spans crossfaded with zero-duration
  `tl.set` swaps — which is also seek-safe.

## Layout — hard limits

> **2026-08-28 tightening (direct user feedback on the EP20-26 batch: a hook panel
> pinned at y≈28 "will likely be cropped out — make sure all overlays stay within some
> margin of the outside border").** The working content band for text/UI is now
> **x=70-870, y=200-1280** — the top limit moved from 180 to 200 and the left from 60
> to 70. Same exemptions as ever (`#bg-fill`, vignette, full-bleed photos, full-frame
> effect layers). Audit on decoded pixels, not CSS.

1. **Nothing renders below y=1280 or above y=180.** Burned-in captions occupy roughly
   y=1306-1570 in the WORST case, not y=1330 as earlier drafts of this file said.
   Measured for the EP14-19 batch by generating every episode's `master.ass` and
   resolving the widest chunk: at `--caption-font-size 74` with `--caption-margin-lr
   190` the usable text width is 700px, the longest chunk in the batch (EP17's
   "TRANSACTION AGAINST THAT BASELINE") wraps to 3 lines, and 3 lines at ~88px
   line-height above a `MarginV: 350` anchor puts the band top at
   1920-350-3*88 = **1306**. That leaves only **26px** of clearance above the y=1280
   limit -- so y=1280 is a hard floor with almost nothing to spare, not a soft
   guideline. Do not creep past it, and re-run this measurement if the caption size,
   MarginV or margin-lr ever change again.
   Usable content band is **y=180-1280**. `#bg-fill`, `#vignette`, full-bleed photos and
   full-frame effect layers (flash, grain, glitch bands) are exempt; all text, UI and
   graphics are not.
2. **A camera push-in EXPANDS your bounds.** A naive 180-1280 band scaled 1.06-1.09 about
   the frame centre resolves to roughly 130-1319 and breaks BOTH limits. Either set
   `transform-origin` to your content band's own centre and shrink the design band (e.g.
   230-1230), or resolve the extremes explicitly. **Report the arithmetic.** If you also
   apply a snap-zoom or shake, resolve the COMPOSED worst-case scale, not just the push-in.
3. Hero words/numerals **>= 110px** (a single hero glyph like a status code: >= 140px).
   The main graphic should fill the usable width defined in rule 5 — it is the subject of
   the frame, not an accent. **Express it as an x-band, never as "a width, centred."**
   "the centre 780-900px of 1080" sounds safe and resolves to x=90-990 or x=140-940; both
   sit under TikTok's action rail. That phrasing is how the entire EP14-19 batch ended up
   in the rail, so it has been removed.
4. **Pairwise collision check.** For every pair of simultaneously-visible elements, resolve
   BOTH to absolute canvas pixels by walking the `position:absolute` ancestor chain — never
   trust a raw CSS number read in isolation. A child at `bottom:44px` inside a parent at
   `top:560px; height:460px` resolves to y=892-976 and WILL collide with a sibling
   hardcoded at `top:930px` in the outer frame. Confirm no overlap and >= 40px separation.
   A small kicker sitting close above a large hero line is the classic failure: a 22px gap
   between a 34px label and a 96px headline reads as one merged sentence. Report the
   arithmetic. Elements that never co-occur in time are fine — say so and give the times.
5. **Nothing renders right of x=900 or left of x=60 — TikTok draws its own UI there.**
   The y=180-1280 band in rule 1 protects against OUR burned-in captions. It says nothing
   about TikTok's chrome, which is composited over the video at playback and which no
   render of ours can show. On the right: the action rail — profile bubble, like, comment,
   bookmark, share, spinning sound disc. On the left: a thin margin. Published figures vary
   by source and drift between app versions, so triangulate and use two tiers:

   | | zone | status |
   |---|---|---|
   | **DANGER** | `x >= 900`, `x <= 60`, `y >= 1600`, `y <= 140` | every source agrees TikTok covers this |
   | **CAUTION** | `x >= 800`, `y >= 1400` | some sources; a coin flip across devices and app versions |

   Sources: checksafe.zone (right 280px, bottom 520px, top 140px; safe rect x 40-800,
   y 180-1400), creamate.ai (right 180px, bottom 400px, left 60px, top 140px),
   kreatli.com (~1080x1420 text-safe; "if text or faces touch the right third they are at
   risk"). They disagree by ~100px on the right and ~120px on the bottom, which is what the
   two tiers encode — do not pick one source and call it settled.

   **Usable content band is therefore x=60-900, y=180-1280 — 840 x 1100, centred at
   x=480, NOT x=540.** That 60px leftward shift is 5.5% of frame width, imperceptible, and
   is what lets a hero graphic keep its size instead of being shrunk. Design to `x <= 860`
   so a nudge or a push-in does not spend the whole margin. Same exemptions as rule 1:
   `#bg-fill`, `#vignette`, full-bleed photos and full-frame effect layers may cross it;
   all text, UI and graphics may not.

   **A camera push-in expands x too** (rule 2), and about `x=480` now, not the frame
   centre. Resolve the composed worst case on BOTH axes and report the arithmetic.

   Verify on the rendered file, not the CSS: `tool/helpers/check_safe_zone.py <render.webm>`.

## This shoot's framing: "land it on the chest" is often impossible

Measured independently by several slots on the EP14-19 footage, in output-canvas pixels
(the drafts are 720x1280 -- multiply by 1.5). The framing varies a lot shot to shot, so
**always grid-measure your own beat**; these are here so you know what to expect, not to
be trusted directly:

- Mid shots: hair top ~y=385, eyebrows ~y=760, chin ~y=1215.
- Tight close-ups (EP14's BUILD beat): hair top ~y=290, mouth ~y=1160-1270,
  **chin bottom ~y=1370-1430.**

On the tight shots the chin sits *below* the y=1280 content limit and the shirt line lands
inside the caption band, so **the gap between "below the chin" and "above the captions" is
zero or negative — there is no chest band to land on at all.** Do not silently shrink a
panel into space that does not exist. The options that actually work, in order:

1. **A side column — LEFT ONLY, x=60-330.** A tall narrow panel clears the head entirely
   and suits list/feed content natively. **A right-hand column is no longer available**: the
   old advice here said "x>=850 or x<=330", and x>=850 is precisely TikTok's action rail
   (rule 5). EP14's BUILD slot took that advice and resolved to x=850.5-1081.5, sitting
   under the like and comment buttons for the whole beat. A right column is only usable if
   it ends by x=860, which on a 1080 canvas leaves too little width to be worth it —
   so go left, or pick option 2/3/4.
2. **An upper band above the brow line.** Everything above ~y=760 leaves eyes, nose and
   mouth unobscured. Works on mid shots; on close-ups the clear ceiling can be as little as
   100px, which forces a sub-110px headline — say so rather than breaking the limit.
3. **Convert to a full-screen opaque takeover** — but only if the episode's takeover budget
   (max 2) has room. Check the format plan before choosing this.
4. **Accept minimised coverage and state it.** If nothing else fits, cover the mouth/chin
   rather than the eyes, keep the fill translucent, and report exactly what is covered and
   why the alternatives failed. An honest, argued overlap beats a silent one.

## Timing — hard rules

- **Primary entrance begins at local t=0**, and must NOT be at opacity 0 on frame 0. On an
  opaque takeover whose background is already up, invisible content reads as a black flash.
  Start it around 0.5 opacity and animate up. `#bg-fill` must be present instantly (no
  fade-in, or under 0.08s).
- **The final fade-out must FINISH at exactly the declared duration, zero buffer.** For a
  5.8s slot: `…, 5.5)` with `duration: 0.3`. Not "shortly before" — a fade that lands early
  just relocates the bare-frame flash earlier.
- **Every repeating tween (`repeat:`/`yoyo:`) must fully COMPLETE before the fade starts.**
  A repeating tween whose final render lands after a completed fade wins the DOM write and
  strands the element visible. This is a confirmed real bug in this pipeline. Compute each
  one's true end: `start + (repeat+1)*duration + repeatDelay*repeat`.
- **A plain `tl.to(target, {opacity:0})` fade can silently FAIL to render.** The renderer
  seeks a paused timeline and screenshots immediately, so a tween that must read its start
  value from the DOM can miss the write. Two builds hit this independently. Use `fromTo`
  with an explicit `{opacity:1}` start plus `gsap.defaults({lazy:false})`. Also note that
  ancestor opacity is NOT applied uniformly to transformed descendant layers, so fading a
  wrapper can fade only part of a composition.
  **Verify the fade on the ACTUAL RENDERED FILE, not the lint harness** —
  `check --at --snapshots` has reported a broken fade as working. Say in your report how
  you verified it.
- `fromTo` defaults to `immediateRender: true`, which applies the from-vars at build time
  and can leave elements visible during an earlier phase. Pass `immediateRender: false` on
  any `fromTo` that starts after t=0.
- Never `ease: "linear"`. `power3.out` for reveals, `sine.inOut` for ambient/continuous,
  `power4.out` for slams and impacts.
- **Never reveal two independent new elements simultaneously** — the eye cannot track both.
  Stagger everything.

## Information density and duration — READ THIS FIRST, IT IS THE #1 NOTE

Direct feedback on the first pass of these episodes: **"the overlays present too much
information in too short of time."** That is now the primary constraint. An overlay that
is technically correct but unreadable at 1× is a failed overlay.

**One idea per overlay.** The overlay is not a transcript of the narration and must not
try to carry every clause the presenter says. Pick the single thing that beat is about and
show only that. If you cannot say what the one idea is in a short phrase, the design is
not ready.

One idea does **not** mean one act. It means one idea, *dramatized* — see the next section.

## The biggest lever: two acts with a turn between them

This is the single highest-value structural choice, and dropping it is what flattened the
last batch. Compare, from this repo:

```
EP4  slot_new_component :  PHASE 1 challenge builds  →  shutter flash @3.0s  →  PHASE 2 the reveal
EP17 slot_new_component :  REVEAL 1 · 2 · 3 · 4 · 5 · 6  →  hold
```

Both have a similar number of tweens. The first tells a story with a turn; the second is a
list. EP4's CAPTCHA assembles tile by tile, a white shutter flash cuts, and then the grid
recedes while data-flow lines draw from each selected tile into a glowing AI eye with
packets travelling along them — the setup AND its consequence, in one overlay.

**Ask: does this beat have a turn?** A setup and a consequence, a calm state and a broken
one, a thing and what it becomes. If yes, build both halves and put a real transition beat
between them — a shutter flash, a desaturate hit, a sweep, a colour phase-shift. Colour-code
the two phases so the shift itself carries the turn.

If the beat genuinely has no turn — a payoff that holds one strong image, a single running
counter — then one act is correct. Do not manufacture a second phase to satisfy this rule.
A held photo card with a slow drift is a legitimate and welcome contrast.

**There are TWO budgets and they move in OPPOSITE directions.** An earlier version of this
file had a single budget that charged 1.2s for every "distinct visual element". That priced
*motion* as a cost, so the cheapest way to comply was one card, one headline, two chips,
hold — and every overlay in the batch collapsed into that shape. The user's verdict on the
result: **"the overlays are too sparse."** Their original complaint was never about things
happening on screen; it was about text and numbers to process. Keep these separate.

**Budget 1 — TEXT AND NUMBERS. Tight. This is the one that was right.**
- **One** headline, **6 words maximum**.
- **At most two** supporting labels, ~3 words each.
- **At most two** numbers on screen at any instant. Not two per phase — two at a time.
- Anything beyond that gets cut, not shrunk.
- A long code string, URL or hash counts as *one* number, and only if it is the subject.

**Budget 2 — VISUAL EVENTS. Generous. Spend here.**
Things that move, assemble, fill in, travel, pulse or transition are **not charged**. A grid
filling in tile by tile, packets running along a path, a UI assembling itself, a colour
phase-shift — these carry the idea without adding a word to read. This is where richness
comes from and there is no cap on it.

**Duration = reading time of the TEXT only:**
- **0.4s per word** the viewer must actually read, plus
- **1.2s per element that must be READ AND UNDERSTOOD** (a labelled value, a named node) —
  NOT per element that merely appears or moves, plus
- **1.0s settle** so the final state is held, not snatched away.

Take the LARGER of that and 4.5s. If the text doesn't fit the beat, **cut text** — never
speed up the reveal, and never cut motion to buy time.

**Do NOT stretch an overlay to cover its beat.** EP4's `new_component` runs 7.9s inside a
16.7s beat — about 45% coverage — and it is the series gold standard. A rich 45%-coverage
overlay beats a thin 95%-coverage one. Padding a composition to fill a beat is what makes
it feel sparse. This also keeps overlays from overrunning short beats.

**Stagger with real gaps.** Two elements appearing 0.15s apart read as simultaneous. Leave
**at least 0.6s** between successive reveals, and hold the final composed state for the
full settle before any fade begins.

**Land the key visual on the words.** Your brief gives the narration for the beat. The
moment the overlay's main idea resolves should coincide with the phrase that states it —
not 3 seconds early while the presenter is still on the previous sentence.

## Format variety — vary it deliberately, per episode

Direct feedback, given twice: **the overlays don't have enough variation in presentation
format.** This has not yet been fixed — under the old single budget every format degenerated
into the same dark card with a headline, whatever it was nominally called.

**What actually differentiates a format is the HERO OBJECT, not the frame shape.** A
recognizable UI recreation reads as a produced cutaway; an abstract panel with chips reads as
a slide, no matter whether it is half-screen or full-screen. Decide what the hero object IS
first — a real screen, a photograph, a diagram, a counter — then pick the frame that suits it.

**Write the episode's format plan before building any slot**, list it in your report, and
make it genuinely varied. Do not use the same format twice in a row, and do not use
full-screen opaque takeover more than twice in one episode. Draw from:

1. **Full-screen opaque takeover** — the footage is fully replaced. Reserve this for the
   episode's one or two densest conceptual beats. It is the heaviest option, not the default.
2. **Half-screen panel** — the graphic occupies the upper OR lower half; the presenter stays
   visible in the other half. Excellent for "here's the thing I'm describing" moments.
3. **Transparent band / lower-third** — linework and type over live footage, no opaque fill.
   Translucent fills (≤0.32 alpha), border + glow for definition.
4. **Corner accent** — a small chip or counter in one corner, footage otherwise untouched.
   Good for a single number or a running state.
5. **Static photo card** — a real sourced photograph presented as a held card with a short
   caption. Deliberately still: no animation beyond a slow drift and the entrance. A quiet
   beat is a legitimate and welcome contrast.
6. **Full-bleed photo scene** — a real photograph fills the frame with type over it.
7. **Motion graphic** — an animated diagram where the motion IS the explanation.

**A format is what it MEASURES as, not what you called it.** A "photo card", "panel" or
"transparent band" whose rendered alpha sits near 1.0 across the frame IS a full-screen
takeover, and it silently breaks the episode's committed format mix and takeover cap. No
lint catches this -- `check` passes happily, because every individual rule is satisfied.
**Confirmed real case this batch: EP14's `slot_payoff` first render measured 0.91-1.00
alpha across the whole frame** from the combined weight of a background wash, two glow
blobs and a vignette, which would have made it EP14's THIRD takeover against a cap of two.
It was caught only by decoding the rendered `.webm`'s alpha plane and measuring mean
coverage, then fixed by lightening the wash/glows/vignette to 0.66-0.73 in the open areas
(live footage genuinely visible at 27-34%). **Verify non-takeover formats by measuring
alpha on the rendered file**, not by asserting you did not add a `#bg-fill` -- a stack of
"subtle" full-frame layers adds up to an opaque one. Note the corollary: once footage
really is showing through, type that used to sit on a wash now sits on live video, so
strengthen its `text-shadow` in the same pass.

**Use real photographs more often.** They were under-used in the first pass. A real image
grounds an abstract idea faster than any diagram — a phone, a crowd, a keyboard, a server
rack, a printed page. Reach for one whenever the beat has a physical analogue, and follow
the sourcing rules below.

## Renderer traps found the hard way — read these, they WILL bite

1. **`tl.set()` at position 0 never fires.** The renderer screenshots a paused timeline
   without advancing it, so anything you establish with a `set` at t=0 is simply absent on
   frame 0. **Frame-0 state must come from CSS**, not from a timeline `set`.
2. **Two `set`s on the same property at the same position render the boundary frame blank.**
   The classic case is a stacked-digit counter: `set(".digit", {opacity:0})` plus
   `set("#digit-3", {opacity:1})` at the same time produces a one-frame flicker on *every*
   increment. Fix: only touch the OUTGOING element — hide the previous digit and show the
   next as two different targets, never a blanket hide-all plus a show-one at the same
   position.
3. **`repeat: 2, yoyo: true` ends at the PEAK, not the base.** An even iteration count runs
   up/down/up and leaves the element at its animated value — a "breathe" built this way
   holds a full-strength glow forever. **Use an odd `repeat` for yoyo tweens** so they land
   back on the base value. This is separate from (and in addition to) the rule that a
   repeating tween must finish before the fade.
4. **`fromTo` applies its start values at BUILD time** unless you pass
   `immediateRender: false`. One build stamped a `blur(9px)` start onto frame 0 and rendered
   its first 2.3 seconds fully blurred. Pass `immediateRender: false` on every `fromTo` that
   begins after t=0 — no exceptions.
5. **Tweening `filter` from a computed `none` flashes the element solid BLACK.** GSAP
   interpolates the from-value as `brightness(0)`, so an element that should ease into
   `grayscale(1) brightness(0.62)` renders as a black rectangle for its first frames. The
   lint harness does not catch it -- it was found on a composited frame after shipping a
   visible black box in a rendered slot this batch. **Fix: declare an explicit identity
   filter in CSS (`filter: grayscale(0) brightness(1)`) and repeat it in the `fromTo`
   from-vars**, so the tween never starts from `none`. Same class of trap as the
   `tl.set`-at-0 and even-`repeat`-yoyo bugs.
6. **Never put a light/bright background behind the caption band.** The burned-in captions
   are white with a black outline and an amber highlight word, designed for dark footage. An
   overlay that fills the frame with a light wash creates no *collision* — the existing rules
   all concern collisions — but drops the amber word to the weakest contrast in the series.
   If your composition needs a light panel (a light-mode UI recreation, a paper texture),
   **confine it to the content band and let the dark background show below ~y=1240**, e.g. via
   a `mask-image: linear-gradient(to bottom, #000 0 1180px, transparent 1300px)`. Verify by
   cropping the caption band at native resolution, not by eyeballing a downscaled frame.
7. **A `box-shadow`/glow reaches ~1.6x its blur radius past the element edge, not half
   and not 1.0x.** Measured empirically on rendered pixels: `top_reach = element_top + offsetY -
   blur`. A 6px bar at `top:190px` with `box-shadow: 0 2px 14px` puts faint but non-zero
   alpha on rows **178-181**, breaching the y=180 limit even though the arithmetic
   "blur/2 = 7px" said it cleared. Budget the whole blur radius when an element sits near
   y=180 or y=1280, and verify by probing the decoded alpha plane row by row rather than
   trusting the CSS numbers. A second slot then measured alpha 4/255 as far as **1.6x**
   the blur past the edge (a Gaussian tail does not stop at the nominal radius), so
   budget `1.6 * blur` when an element sits near y=180 or y=1280 and verify on decoded
   pixels regardless. **Note `episodes/ep13-ratelimiting/animations/slot_title/`
   ships `0 0 18px 2px`, which resolves to y=170 and DOES breach the limit** - do not copy
   its shadow values when using it as a structural reference.
8. **A `fromTo` property present ONLY in the from-vars is silently DROPPED by the
   seek-based renderer** — especially across `repeat` iterations — and the element
   renders with that property at its CSS base value. Confirmed real case: EP22's
   arrow pulse dot carried `y: 353` in from-vars only and rendered at the frame's
   TOP EDGE, 353px off its path, teleporting between frames. **Every x/y/scale in a
   from-vars object must be repeated in the to-vars** (same value = constant tween),
   and every GSAP-positioned element needs an explicit CSS `left/top` base. Sweep new
   compositions for this pattern including helper functions with variable targets.
9. **A missing `class` attribute silently collapses an absolutely-positioned layout
   into the frame's top-left corner** (the CSS never applies; children resolve
   against #root; labels double-draw at y~0). Shipped TWICE in one episode (EP26
   hook, then payoff which reused the markup). After fixing any such bug, grep every
   sibling slot for the same pattern — and lint CSS-declared classes against markup
   `class=` usage. The catch-all: run `tool/helpers/check_margins.py` on every
   render.webm — corner-collapsed content always breaches the margin band.
10. **An element that animates in later is NOT offscreen before its tween starts.**
   With `immediateRender: false` it sits at its CSS REST position from frame 0 —
   EP23's container box rested exactly on top of its card's text for the whole first
   act ("graphics should never block text", direct feedback). Elements entering
   later must be hidden at rest (CSS `opacity: 0`) or based off-canvas, and the
   pairwise-collision audit must include frame-0 rest states, not just designed
   positions.
11. **`ease: "none"` is permitted where constant velocity is genuinely the point** (a scroll
   that must not decelerate, a spinner). The ban is on `"linear"` as a lazy default for
   reveals — it is not a ban on constant motion where the physics demand it.

## Style

- Dark atmospheric background: a `radial-gradient` base plus 1-2 coloured glow blobs plus a
  `#vignette` radial overlay. Not a flat CSS colour.
- A static deterministic `feTurbulence` SVG grain at ~0.03-0.05 opacity over the frame —
  it breaks gradient banding.
- Continuous motion: a slow camera push-in under everything, and ambient life (breathing
  glows, a blinking cursor) so nothing sits perfectly static once revealed.
- Realistic UI chrome where the beat calls for it: rounded cards (~20-24px radius), 1-2px
  borders at low alpha, window headers, monospace values. This realism is what makes a
  composition read as high-production rather than as a slide.
- **NO emoji.** Hand-built SVG, realistic CSS UI recreations, or real sourced photos only.
- **Never animate GSAP `rotation` on an SVG element with a degenerate bounding box** — a
  `<line>` with `x1===x2` or `y1===y2` (a clock hand, a gauge needle, a scale beam, a radar
  sweep). It warps and vanishes in this renderer, and passing `transformOrigin` does NOT fix
  it. Instead tween a plain numeric angle on a JS object and write the endpoint coordinates
  via `Math.sin`/`Math.cos` in an `onUpdate` callback, or rotate a wrapper that has real
  width and height.

## Real images — REQUIRED

The user asked for real images from the web explicitly. Every episode must contain some.

- WebSearch for a directly-fetchable URL (Unsplash / Pexels / Wikimedia direct file URLs
  work well), then `curl -L -A "Mozilla/5.0" <url> -o assets/<name>.jpg`.
- **Verify each**: `ffprobe assets/<name>.jpg` must report sane dimensions — not a 0-byte
  file and not an HTML error page.
- **RELEVANCE IS THE FIRST TEST, AND IT IS WHERE THE LAST BATCH FAILED.** Direct user
  feedback: *"there are not enough real, relevant images — the dictionary for the DNS is not
  exactly the image that best applies."* A photo of a printed directory is a *metaphor* for
  DNS. A photo of keys is a metaphor for OAuth. Metaphors teach nothing and read as stock.

  **For a software concept, the most relevant image is almost always the real software.**
  A real OAuth consent screen beats keys. A real browser address bar or `dig` output beats a
  phone book. A real declined-payment notification beats a photo of a card reader. EP19's
  real Instagram post works precisely because it IS the thing being discussed.

  Before accepting an image ask: *is this the actual thing the beat is about, or a visual
  pun about it?* If it is a pun, go back and find the real thing.

- **Deliberate product screenshots ARE wanted; incidental branding is not.** These are two
  different rules and the old wording conflated them, which would reject the very screenshots
  this series needs:
  - **Wanted:** a real UI captured on purpose because it is the subject — a consent screen,
    a shortener, an address bar, a real post. Capture with the browser MCP or source directly.
  - **Reject:** branding that leaked in by accident and is not the subject — a university
    name in the corner of a stock photo (this shipped once and had to be cropped), a
    photographer's watermark, a random logo on a wall.
  - **Reject identifiable faces of private individuals.** A public figure whose post is the
    subject of the beat is fine and is what the user asked for.
- Embed photos either as a full-bleed hero scene or inset inside designed UI chrome — both
  are valid, but a photo behind a card must be dimmed enough that the card stays the hero.
- **Legibility over a photograph is a real risk.** Use a scrim gradient behind type plus a
  multi-layer `text-shadow`; never rely on the photo happening to be dark where text lands.
  Verify on a native-resolution crop, not a downscaled frame — the built-in contrast checker
  samples the CSS stack, not `<img>` pixels, so it structurally cannot catch this.
- If you genuinely cannot obtain an image after real attempts, say so LOUDLY in your final
  report. Do not silently ship a CSS-only composition where one was required.

## What your final report must contain, per slot

1. The phases and the transition beat between them, named.
2. Every real photo's source URL and confirmation it carries no legible branding.
3. Resolved absolute pixel ranges of every visible element.
4. Your pairwise collision arithmetic.
5. Push-in (and composed-scale) bounds arithmetic.
6. Confirmation nothing sits below y=1280 or above y=180.
7. Confirmation the fade finishes exactly at the declared duration, **and how you verified
   that on the rendered file**.
8. Confirmation no repeating tween outlives the fade.

Do not ask questions. If anything is ambiguous, pick the most obvious interpretation and
proceed.

## Never put a next-episode tease in the payoff overlay

`ep6-websockets/project.md` records the series convention, set on EP1/EP4: the payoff
overlay is a **purely visual callback**. No `Next — ...` chip, no pill, no kicker line.
The narration and captions already carry the tease verbally, so the chip is pure
duplication, and it is always the densest thing in the overlay — a full sentence
arriving on top of a headline that just landed.

This has now slipped through twice (EP17 and EP18 both shipped a chip after a pass that
was supposed to remove them all). Grepping for `Next` misses it: the markup writes the
dash as `&mdash;` and the text is uppercased in CSS, so the literal string never appears.
**Grep for the element, not the words** — `class="tease`, `id="tease`, `<span>Next`.

If you remove a tease, also remove anything that existed only to support it. EP18 had a
`#tease-scrim`, a static dark ellipse placed over the brightest part of the photograph.
With the pill gone it stopped being contrast support and became a smudge on the plate.
