# EP6 — "How WhatsApp Delivers in 1 Second"

Built via the video-use + HyperFrames pipeline, following the conventions confirmed in
STYLE.md (video-editing-pipeline repo) from EP1/EP4.

## Source & take selection

Source: `/Users/gordon.jin/Downloads/ep6.MP4` — **720x1280**, notably lower-res than
EP1/EP3/EP4/EP5's 2160x3840 footage. Same aspect ratio (9:16) as the 1080x1920 output
canvas, so scaling to output is a clean uniform 1.5x upscale (no crop offset). Bumped
`unsharp` luma amount 0.5→0.8 and lowered grain `noise` 7→6 in the grade filter chain to
compensate for upscale softness slightly — not rigorously A/B tested against the
original values, worth a look if the final output reads soft.

Five beats cut from a single source file, each beat picked as the cleanest complete
take (see `edl.json` `reason` fields) — PROBLEM and BUILD each had an aborted first
attempt that cuts off mid-sentence; used the clean retakes instead.

## Face-anchor for punch-zoom (HOOK beat only)

Measured directly from this footage rather than reusing EP1/EP4's (540, 730) — this
presenter's hairstyle gives much more headroom, so the eye line sits noticeably higher
in frame. Used an `ffmpeg drawgrid` pixel-ruler overlay on a native-resolution frame:
eyes at native (360, 375) on 720x1280 → scaled to the 1080x1920 canvas by the same 1.5x
factor → **focal point (540, 563)**. Confirmed via before/after grid-frame comparison
that the eyes stay locked in place through the zoom.

## Overlay concept — single metaphor thread

One visual thread across the whole episode: a **teal "open line" motif** (two nodes
connected by a glowing line) that pays off the script's own words ("keep the line
open"). Signature color is teal/emerald (#14b8a6), distinct from EP1's blue and EP4's
red/orange.

- **slot_hook** — paper-plane icon + a small dashed arc between two pulsing dots
  ("send" traveling across distance), punch word "1 SECOND."
- **slot_problem** — a repeating chat-bubble ("Any new messages?") pulsing 3x with a
  battery icon stepping down each cycle (100%→64%→28%) — visualizes "wasteful, slow,
  drains battery" without extra narration. Accent color orange (distinct from the
  teal thread) since this is the "old/bad way" beat.
- **slot_build** — the open-line motif's first appearance: two nodes ("YOU" / "SERVER")
  connected by a line that draws in once and then pulses steadily (contrast against
  PROBLEM's on/off flicker).
- **slot_new_component** — the biggest build: a WhatsApp-style chat bubble with a
  single gray checkmark + a queue-tray icon ("HELD IN QUEUE" / "RECEIVER OFFLINE"),
  then at ~3.7s a phase change — tray fades, status flips to "RECONNECTED", a second
  checkmark joins the first — directly recreating the script's own line, "your single
  grey tick becoming two."
- **slot_payoff** — the open-line motif reprised in miniature under "KEEP THE LINE
  OPEN." (no literal "next episode" text, matching the EP1/EP4 convention where the
  payoff overlay is purely a visual callback — the narration/captions already carry
  the tease verbally).

No emoji icons anywhere; all icons are hand-built SVG. No stock photos sourced for
this episode — the strongest visuals here were literal UI recreations (chat bubble,
checkmarks, battery), same reasoning as EP4's CAPTCHA-grid/signup-form overlays.

## Bug caught during self-check (fixed before finalizing)

First render of `slot_new_component` had its punch-word text ("GREY TICK BECOMES
TWO.") overlapping the captions — both landed in the same vertical band. Caught by
extracting an actual frame at that timestamp (not just checking the lint tool, which
has no cross-composition awareness of caption position). Fixed by moving the
punch-word up (`top: 380px → 250px`) and shrinking it slightly (68px → 56px font).
Re-rendered and re-verified with a fresh frame extraction — clean separation now.

## Music & SFX

- **Music**: HeyGen catalog, "dark trap instrumental beat, minimal 808 bass, tech
  focused" — a fresh track from EP1/EP3/EP4/EP5 per house convention. 44s source
  looped once (2s triangle crossfade) to cover the 56.94s runtime, ducked to a
  constant background level (`volume=0.16`). See `.media/index.md`.
- **SFX**: three myinstants.com stingers — `vine_boom.mp3` on the "1 SECOND" hook
  punch, `sad_trombone.mp3` on the battery's final/most-drained step in PROBLEM,
  `correct_ding.mp3` on the second-checkmark "delivered" moment in NEW_COMPONENT.
  Downloaded via direct `curl` with a browser user-agent (myinstants.com 403s
  WebFetch/generic fetchers without one). See `sfx/SFX_NOTES.md`.

## Verification

Self-checked with frame extractions at the title card, the hook zoom (confirmed eyes
stay locked), each beat's overlay (confirmed no overlay/caption collisions after the
fix above), and the payoff. Final duration 57.08s (base render) matches EDL
`total_duration_s` (56.94s) within loudnorm/encoding rounding, matching the pattern
seen on EP1/EP4.

## Output

`preview_final.mp4` — 1080x1920, 57.08s.
