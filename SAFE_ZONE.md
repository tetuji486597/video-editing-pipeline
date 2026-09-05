# TikTok UI safe zone — where overlays may NOT go

Written 2026-08-24, after EP14-19 shipped. **This is a forward-looking spec change**; the
eight delivered files were NOT re-rendered.

## The zones

TikTok composites its own interface over the video at playback. Nothing we render can show
it, so it has to be a hard geometric constraint rather than something to eyeball.

  RIGHT   action rail — profile bubble, like, comment, bookmark, share, sound disc
  BOTTOM  @username, description (expands to ~4 lines), sound ticker, scrubber, nav bar
  TOP     search icon, Following / For You tabs, device notch
  LEFT    a thin margin

Published figures disagree and drift between app versions, so two tiers:

| | zone | status |
|---|---|---|
| **DANGER** | `x >= 900`, `x <= 60`, `y >= 1600`, `y <= 140` | every source agrees |
| **CAUTION** | `x >= 800`, `y >= 1400` | source-dependent; a coin flip across devices |

Sources: checksafe.zone (right 280, bottom 520, top 140; safe rect x 40-800, y 180-1400);
creamate.ai (right 180, bottom 400, left 60, top 140); kreatli.com (~1080x1420 text-safe,
"if text or faces touch the right third they are at risk"). They differ by ~100px on the
right and ~120px on the bottom. Do not pick one and call it settled.

**Usable content band: x=60-900, y=180-1280 — 840 x 1100, centred at x=480, not x=540.**
Design to `x <= 860`. Exemptions match the y-band's: `#bg-fill`, `#vignette`, full-bleed
photos and full-frame effect layers may cross; text, UI and graphics may not.

## Root cause — two lines in this spec, not 35 separate mistakes

1. `OVERLAY_SPEC.md` rule 3 said the main graphic should occupy **"roughly the centre
   780-900px of the 1080px width."** Centred on 540 that is x=90-990 or x=140-940. Both are
   under the rail. **A width plus an implied centre hides its own bounds** — the rule is now
   an absolute x-band.
2. The framing section's first escape hatch for close-ups was **"a tall narrow panel at
   x>=850 or x<=330."** `x>=850` IS the action rail. That is why EP14's BUILD panel reaches
   x=1080. The right-hand option is removed; left columns only.

## Audit of the shipped batch — measured, not estimated

`tool/helpers/check_safe_zone.py`, on decoded pixels, overlay composited over black,
counting only content that PERSISTS (a 2-5 frame shutter flash whitens the whole frame).
Reports how deep text/UI-grade content (luma > 200) actually reaches.

**Of 49 compositions: 35 put text/UI past x=900, 2 sit exactly at the
caution edge, 12 are clear.**

Depth distribution (px reached): {930: 6, 960: 6, 990: 14, 1020: 5, 1050: 3, 1080: 1}

| slot | reaches | into rail | % of frames |
|---|---|---|---|
| `ep14-infinitescroll/slot_build` | **x=1080** | 180px | 93% |
| `ep16-urlshortener/slot_build` | **x=1050** | 150px | 71% |
| `ep19-likecounts/slot_tradeoff` | **x=1050** | 150px | 20% |
| `ep14-infinitescroll/slot_hook` | **x=1050** | 150px | 14% |
| `ep19-likecounts/slot_tiktok_title` | **x=1020** | 120px | 96% |
| `ep18-urlrequest/slot_hook` | **x=1020** | 120px | 92% |
| `ep14-infinitescroll/slot_ai_angle` | **x=1020** | 120px | 50% |
| `ep17-fraud/slot_outlier` | **x=1020** | 120px | 48% |
| `ep18-urlrequest/slot_problem` | **x=1020** | 120px | 25% |
| `ep19-likecounts/slot_tiktok_title_b` | **x=990** | 90px | 96% |
| `ep15-oauth/slot_hook` | **x=990** | 90px | 95% |
| `ep18-urlrequest/slot_payoff` | **x=990** | 90px | 92% |
| `ep14-infinitescroll/slot_payoff` | **x=990** | 90px | 62% |
| `ep15-oauth/slot_payoff` | **x=990** | 90px | 62% |
| `ep15-oauth/slot_build` | **x=990** | 90px | 59% |
| `ep14-infinitescroll/slot_problem` | **x=990** | 90px | 48% |
| `ep16-urlshortener/slot_scale` | **x=990** | 90px | 45% |
| `ep19-likecounts/slot_new_component` | **x=990** | 90px | 41% |
| `ep16-urlshortener/slot_payoff` | **x=990** | 90px | 39% |
| `ep18-urlrequest/slot_response` | **x=990** | 90px | 35% |
| `ep15-oauth/slot_scope` | **x=990** | 90px | 31% |
| `ep16-urlshortener/slot_problem` | **x=990** | 90px | 21% |
| `ep16-urlshortener/slot_hook` | **x=990** | 90px | 18% |
| `ep17-fraud/slot_feature_store` | **x=960** | 60px | 91% |
| `ep15-oauth/slot_problem` | **x=960** | 60px | 76% |
| `ep15-oauth/slot_new_component` | **x=960** | 60px | 63% |
| `ep18-urlrequest/slot_title` | **x=960** | 60px | 54% |
| `ep14-infinitescroll/slot_new_component` | **x=960** | 60px | 12% |
| `ep17-fraud/slot_hook` | **x=960** | 60px | 11% |
| `ep19-likecounts/slot_build` | **x=930** | 30px | 85% |
| `ep19-likecounts/slot_payoff` | **x=930** | 30px | 79% |
| `ep17-fraud/slot_payoff` | **x=930** | 30px | 73% |
| `ep17-fraud/slot_problem` | **x=930** | 30px | 36% |
| `ep18-urlrequest/slot_tcp_tls` | **x=930** | 30px | 35% |
| `ep17-fraud/slot_ai_angle` | **x=930** | 30px | 18% |

Left margin (`x <= 60`): **no slot EXCEEDS luma 200 there, but one sits exactly on the
line.** EP14 `slot_recycle`'s left strip measures peak luma 200 across 96% of frames and
its element box was built at x=30-76 — it fails the strict `> 200` test by a single luma
level, so it reads as "clear" above and should not. Treat it as a real left-margin
encroachment. EP16 `slot_redirect` (123) and EP19 `slot_approx_ok` (108) are genuinely dim
— background gradient bleed, which is exempt. Nothing else reaches x<=60. **Top and bottom are clean** — the
existing y=180-1280 rule already keeps overlays out of y<=140 and y>=1400. The problem axis
is RIGHT, and only RIGHT.

### The one with no free fix

EP14 `slot_build` reaches **x=1080 in 93% of frames** — the full width of the rail, the
worst in the batch. It was placed there deliberately: that beat is a tight close-up where
the chin bottom lands at y~1370-1430 and the shirt line is already inside the caption band,
so there is no chest band to land on. Leaving the rail costs either panel width or face
clearance. A genuine tradeoff, not an oversight.

`ep19/slot_tiktok_title` (x=1020, 96%) and `_b` (x=990, 96%) are next: the opaque white
sticker's widest line overhangs the rail for essentially the whole hold. If the title box
rolls out to EP14-18, **narrow the boxes to end by x=860 first** — this is the cheapest fix
in the batch, since it is one CSS change in one reference composition.

## The burned-in captions — the encroachment no overlay check can see

Captions are composited last by ffmpeg, so no pass over `animations/*/render.webm` shows
them. Measured by burning each episode's real `master.ass` onto black and probing regions:

**At the shipped settings (font 74 / margin-lr 190 / MarginV 350) the caption band sits
below y=1520 in 81-88% of frames — inside TikTok's description area, in every episode.**
It does clear the y<=1280 overlay floor and the x>=900 rail; the bottom is the only breach.

The knobs are coupled, not independent: widening `margin-lr` to clear x=800 narrows the
text, forcing more wraps, which pushes the band top UP into the y<=1280 overlay floor;
raising `MarginV` does the same. Measured across all 1280 caption chunks in the batch:

| font / lr / MarginV | worst chunk | band | x span | verdict |
|---|---|---|---|---|
| 74 / 190 / 350 (shipped) | 3 lines | 1306-1570 | 190-890 | in the bottom UI |
| 74 / 190 / 400 | 3 lines | 1256-1520 | 190-890 | collides with overlays |
| 64 / 190 / 400 | 3 lines | 1292-1520 | 190-890 | OK |
| 64 / 220 / 400 | 3 lines | 1292-1520 | 220-860 | OK |
| 58 / 190 / 400 | 2 lines | 1382-1520 | 190-890 | OK, but small |

**Two settings were burned across all 8 caption files and measured CLEAN on all three
constraints** (nothing above y=1280, nothing below y=1520, nothing past x=900):

| setting | text x span | vs the x<=860 target | note |
|---|---|---|---|
| **60 / 220 / 400** | 220-860 | **meets it** | recommended; font 74 -> 60 |
| 64 / 190 / 400 | 190-890 | 30px over | bigger text, right edge in the CAUTION band |

    --caption-font-size 60 --caption-margin-lr 220 --caption-margin-v 400

**Do not adopt a setting without burning it.** Font-metric estimation picked
`64/220/400`, which looks identical on paper to `64/190/400` — and it breaches: the
narrower 640px box wraps a chunk to FOUR lines, and 4 x 76px above a MarginV 400 anchor
tops out at y=1216, 64px through the overlay floor. Measured, that is 17 bad frames on
EP17 and 7 on EP19. The estimator only ever predicted a 3-line worst case.

EP19 also breaches y<=1280 by a frame or two **at the shipped settings**, so that one is
pre-existing rather than introduced by any change here.

checksafe.zone's more conservative `y >= 1400` bottom cannot be met at all without moving
captions into overlay space — unreachable by design, not an oversight.

**This visibly shrinks the captions across the series, so it is Gordon's call.**

## How to check

    python tool/helpers/check_safe_zone.py episodes/<ep>/animations/*/render.webm

Three traps, all of which produced a worthless audit here before the tool was right:

1. **Composite over black.** VP9 stores colour separately from alpha, so a fully
   transparent region still carries bright colour data. Raw-alpha checks lie.
2. **Judge by DURATION, not peak.** A 2-5 frame white shutter flash whitens the entire
   frame. Peak-based measures — and any `cropdetect` pass, which accumulates — then report
   every full-screen takeover as a full-frame violation. The first version of this tool did
   exactly that and its output was worthless.
3. **Do not average over the zone.** The rail is 180px wide; an 81px-deep solid white box
   averages down to nothing against the empty rail beside it. The second version of this
   tool did that and classified EP19's opaque title sticker — 120px into the rail for 96%
   of its hold — as "thin/edge only". Probe narrow strips; report the deepest lit one.
