# Editing conventions — "System Design in 60 Seconds"

Confirmed-good defaults for this series, learned across EP1 ("Where Your Password
Actually Goes") and EP4 ("How Sites Know You're Not a Robot"). Apply these as the
starting point on new episodes; don't re-derive them from scratch.

## Title card

- HyperFrames composition (`animations/slot_title/`), transparent background — the
  presenter's face stays visible underneath, it's never an opaque full-screen card.
- Anchored **top-left corner**: `#block { left: 70px; top: 190px; }` on a 1080x1920
  canvas. Not centered lower on the frame (too busy/dated-looking) and not flush
  against the very top edge (`top: 90px` sat too close to the frame edge).
- Minimal content only: a thin accent bar + small uppercase kicker (`SYSTEM DESIGN ·
  NN`) + bold headline. Earlier drafts also had a badge and a meta-line — cut those,
  they read as too verbose/cluttered.
- Held long enough to actually read (~2.7s), not a quick flash.

## Captions

- Real word-by-word highlighting: one Dialogue event per word, only the active word
  color-tagged (`{\c&H00D7FF&}WORD{\c&HFFFFFF&}`), rest in the style's default color.
  Do not use ASS `\k`/`\kf` karaoke tags — the sweep semantics are ambiguous and
  inconsistent across renderers.
- Author the `.ass` file's `PlayResX`/`PlayResY` to match the real output canvas
  (1080x1920), not libass's plain-SRT-conversion default (`PlayResY=288`). With real
  PlayRes set, `MarginV` is literal output pixels.
- Confirmed position: **`MarginV: 350`** (bumped from 280 across EP3/EP4/EP5/EP6, well
  above the bottom edge, clear of every graphic overlay checked so far — re-check this
  clearance any time overlays change, since overlay content is what actually varies
  per-episode, not the caption position).
- **Pitfall: small `MarginV` bumps are visually imperceptible.** Nudging 60→95→130
  (each +35px on a 1920px-tall canvas) produced a pixel-diffed shift of only ~15px per
  step — invisible at normal viewing scale. When asked to move captions, jump by a real
  fraction of the canvas height (10%+) and confirm with an actual pixel diff
  (`ffmpeg -filter_complex "blend=all_mode=difference,eq=contrast=5"` on same-timestamp
  frames from before/after), not just an eyeball check of one frame.
- **Line wrapping already works** — `WrapStyle: 0` is set in the `.ass` header, and
  libass auto-wraps any chunk that doesn't fit within `PlayResX` minus `MarginL`/`MarginR`
  (960px usable width at the current margins). Chunks are capped at 4 words
  (`max_words_per_chunk` in `build_master_ass`), so most stay on one line, but a chunk
  containing one long/hyphenated word (e.g. "CLICK-ALL-THE-TRAFFIC-LIGHTS") can wrap to
  3 lines — verified this renders safely (no clipping, no overlay collision) at
  `MarginV: 350`. If a future margin bump ever gets large enough to push a 3-line wrap
  off the top of frame, that's the case to check first.

## Music & SFX

- Background music: a ducked trap/beat-driven instrumental (rejected: lofi, generic
  corporate stock). Volume/ducking envelope is tuned per-episode, mixed in as a
  separate `amix` pass after `render.py`'s own output (narration + overlays + captions
  + loudnorm) — `render.py` itself has no native music-mixing step.
- SFX stingers sourced from myinstants.com, documented per-episode in `sfx/SFX_NOTES.md`
  (which clip, where it's used, why). **The actual audio files are intentionally not
  committed to this repo** — licensing on myinstants.com content is unclear; re-download
  if rebuilding an episode's final mix.
- This reverses an earlier "no brainrot" stance (no SFX stingers, no screen-shake, no
  bouncy caption colors) — that rule was explicitly relaxed for SFX only, confirmed
  after flagging the copyright risk. Screen-shake / bouncy captions are still untested;
  don't assume they're wanted without asking.

## Overlays (motion graphics)

**Load the `system-design-overlays` Claude Code skill before building or regenerating any
episode's overlays** (`~/.claude/skills/system-design-overlays/SKILL.md`, also vendored at
`skills/system-design-overlays/` in this repo) — it's the single source of truth, don't
duplicate its numbers here since it's been revised more than once. Currently modeled on
**EP4's overlays as the confirmed gold standard** (`edit_ep4/animations/slot_new_component/`
and `slot_problem/` — read the source, not just the summary): full-screen atmospheric
takeovers with realistic UI/product recreations, a two-plus-phase mini-narrative per overlay
with a transition beat (a flash, a color shift) between phases, continuous ambient motion,
real images embedded as UI detail. Coverage percentage is explicitly *not* the target to
maximize — EP4's overlays run only ~45-55% of their beat's duration; density and a real
beginning/middle/end matter more than filling time. Also still true: no template reuse
across beats in one episode, no emoji icons.
- No emoji icons — hand-drawn SVG icons or real sourced photos instead (via the
  `media-use` skill's HeyGen image catalog: a real prism/rainbow, a real hourglass with
  an actual rising-sand mask, a real mason jar, etc.).
- Research a real visual metaphor per concept before building (e.g. door = WebSocket,
  mailbox = queue) and let one metaphor thread evolve across a whole episode rather than
  a disconnected icon per beat.
- On-screen text needs real designed treatment (accent bar, highlighted keyword chip,
  icon) — not flat text with no styling.
- Bigger overlays make caption collisions more likely, not less — check every beat's
  overlay against the caption band (`MarginV: 350`, roughly y=1490-1920) with an actual
  frame extraction, not an eyeballed guess. This bit us for real once (EP6's queue beat).
- Punch-zoom (`"zoom": {"at": <seconds>, "scale": 1.2}` in an EDL range) should zoom
  toward the presenter's actual eye level, not the frame's geometric center — measure
  the real focal point from an actual frame of that footage (don't assume it transfers
  from a previous episode's framing) before hardcoding `focal_x`/`focal_y` in
  `build_punch_zoom_filter`.

## Verification discipline

- Don't trust a sub-agent's own alpha/transparency diagnosis unless it explicitly used
  the validated decode path (`-c:v libvpx-vp9` forced on WebM inputs — ffmpeg's default
  `vp9` decoder silently drops alpha and always reports "opaque"). Re-verify centrally
  before treating a reported alpha bug as real.
- For any position/size change requested as "a bit" or "more" — verify with an actual
  before/after comparison (pixel diff, or a full-resolution frame extraction with the
  same timestamp), not a single frame glanced at in isolation. See the caption-margin
  pitfall above — it's the same mistake in a different guise.

See `tool/README.md` for the render pipeline itself, and each episode's `project.md`
for episode-specific reasoning logs and outstanding items.
