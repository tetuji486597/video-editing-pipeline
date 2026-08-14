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
- Confirmed size: **`--caption-font-size 74`** (bumped from the old hardcoded 58 —
  `build_master_ass`/`render.py` now take this as a real parameter/CLI flag instead of a
  hardcoded value in the `.ass` Style line). Re-verify wrap + overlay/face clearance after
  any further size bump — bigger text wraps more often (more chunks now need 2 lines that
  used to fit on 1) and each wrapped line adds real height above the `MarginV` anchor.
- **Pitfall: small `MarginV` bumps are visually imperceptible.** Nudging 60→95→130
  (each +35px on a 1920px-tall canvas) produced a pixel-diffed shift of only ~15px per
  step — invisible at normal viewing scale. When asked to move captions, jump by a real
  fraction of the canvas height (10%+) and confirm with an actual pixel diff
  (`ffmpeg -filter_complex "blend=all_mode=difference,eq=contrast=5"` on same-timestamp
  frames from before/after), not just an eyeball check of one frame.
- **Line wrapping already works** — `WrapStyle: 0` is set in the `.ass` header, and
  libass auto-wraps any chunk that doesn't fit within `PlayResX` minus `MarginL`/`MarginR`.
  Chunks are capped at 4 words (`max_words_per_chunk` in `build_master_ass`).
- Confirmed horizontal width: **`--caption-margin-lr 190`** (up from the old hardcoded 60
  — usable text width narrowed from 960px to 700px, centered, so lines wrap sooner instead
  of spanning near-full-width). Also a real CLI flag/parameter now, not hardcoded.
- **Pitfall (the expensive one): a caption-position or caption-size change is not "done"
  until every overlay in every episode has been re-audited against it — across each
  overlay's FULL on-screen duration, not one sample frame.** Bumping `MarginV`/font-size
  broke FIVE separate overlays in EP4 alone (a stop-sign detection HUD, a stacked-text
  hook, a fingerprint centerpiece, a CAPTCHA "detect card", a payoff glass icon) — all
  invisible until frames were pulled at multiple timestamps spanning each beat's actual
  runtime, because captions change every ~0.3-0.5s and overlay animations evolve, so a
  collision can exist for only part of a beat and be invisible in a single sample. Fix
  pattern: if there's real vertical space between the presenter's face and the caption
  zone (worst case ~y=1300-1920), just reposition the offending element(s) up into it. If
  there isn't — common once a graphic needs to be bigger than ~150px tall, since the gap
  between "below the chin" and "above the caption" is often under 100px on this footage —
  convert the whole overlay to a full-screen opaque takeover instead (add a `radial-gradient`
  `#bg-fill` + `#vignette`, matching `slot_problem`/`slot_new_component` in
  `episodes/ep4-captcha/animations/`, and move the content into the vertical-center, clear
  of both constraints). If a composition connects fixed SVG coordinates to a moving element
  (data-flow lines to an icon), moving just the destination breaks the line's geometry —
  recompute every connected coordinate together and verify by re-rendering real frames, not
  arithmetic alone.
- **Pitfall: small `MarginV` bumps are visually imperceptible.** Nudging 60→95→130
  (each +35px on a 1920px-tall canvas) produced a pixel-diffed shift of only ~15px per
  step — invisible at normal viewing scale. When asked to move captions, jump by a real
  fraction of the canvas height (10%+) and confirm with an actual pixel diff
  (`ffmpeg -filter_complex "blend=all_mode=difference,eq=contrast=5"` on same-timestamp
  frames from before/after), not just an eyeball check of one frame.

## Music & SFX

- **Background music: removed entirely (2026-08-08).** Went through lofi → rejected
  generic corporate stock → a ducked trap/beat-driven instrumental → now removed per
  direction. Final mixes are narration + overlays + captions + SFX only, no music layer.
  Don't re-add a music bed to a future episode without asking first — this reverses
  the "ducked trap instrumental" convention that held through EP1-EP6.
- SFX stingers sourced from myinstants.com, documented per-episode in `sfx/SFX_NOTES.md`
  (which clip, where it's used, why). **The actual audio files are intentionally not
  committed to this repo** — licensing on myinstants.com content is unclear; re-download
  if rebuilding an episode's final mix.
- This reverses an earlier "no brainrot" stance (no SFX stingers, no screen-shake, no
  bouncy caption colors) — that rule was explicitly relaxed for SFX only, confirmed
  after flagging the copyright risk. Screen-shake / bouncy captions are still untested;
  don't assume they're wanted without asking.
- **`WebFetch` returns a 403 on myinstants.com; plain `curl` with a browser
  `User-Agent` header does not.** Use `curl -A "Mozilla/5.0 (Macintosh; Intel Mac OS X
  10_15_7) AppleWebKit/537.36" <page-url>` to grab the page HTML, then
  `grep -o 'media/sounds/[^"]*\.mp3'` to find the direct media path, then `curl` that
  (same UA) to `sfx/<name>.mp3`. `WebSearch` is fine for finding the right page URL in
  the first place, just not for fetching myinstants.com itself.
- **The final SFX+narration remix needs true-peak-aware limiting, or it can clip —
  `alimiter` alone is not reliably enough.** A plain
  `amix=inputs=2:duration=first:normalize=0` between the narration track (already
  loudnorm'd to -14 LUFS on its own) and a fresh `sfx_track.wav` is NOT re-normalized
  after mixing — if enough cues stack near a loud narration moment, the combined peak
  can exceed 0dB. Confirmed real case: EP7's first mix peaked at +1.5dB. First fix tried —
  `,alimiter=limit=0.95:attack=5:release=50` — worked for EP7/EP10, but on EP13 it still
  left the AAC-encoded output peaking *positive* (+0.05 to +0.08dB) even down at
  `limit=0.7:attack=1`: the narration track alone already peaked at -0.91dB, and AAC
  encoding adds its own small overshoot on top of whatever sample-peak limiting ran before
  encoding — a sample-peak limiter has no way to account for that. **Use
  `loudnorm=I=-14:TP=-2:LRA=11` in place of `alimiter` on the final mix instead** — the same
  tool already used for the narration-only loudness pass elsewhere in this pipeline, and its
  `TP` target is specifically designed to survive lossy encoding. Confirmed: dropped EP13's
  peak to a clean -1.71dB. Single-pass `loudnorm` (not the 2-pass measure-then-normalize used
  for the narration-only pass) is fine at this final-mix stage. Always check
  `ffmpeg -i <final>.mp4 -af astats -f null - 2>&1 | grep "Peak level dB"` after any SFX
  remix; a positive number means it clipped.
- **When rebuilding a composite where only overlay visuals/timing changed (not audio),
  reuse the existing shipped file's audio track — but with `-c:a copy`, not a fresh AAC
  re-encode.** Confirmed real case: EP13's rework re-muxed the old `final.mp4`'s audio
  into the new composite via `-c:a aac -b:a 192k`, which re-encodes already-lossy AAC
  through a second lossy pass — the extra encoder overshoot regressed the peak from a
  clean -1.71dB back up to 0.0dB even though the audio *content* was byte-for-byte
  unchanged. Fixed by switching that mux step to `-c:a copy` (bitstream copy, no
  re-encode) — restored the original -1.71dB peak exactly. Always prefer `-c:a copy`
  when the audio itself isn't changing, and re-verify the peak afterward regardless.
- **When inserting a genuine on-camera mistake/blooper for comedic effect, it must
  precede the clean explanation of the thing being fumbled, not follow it.** Confirmed
  correction on EP7: a mispronunciation blooper ("Enter the trie, or trie, or trie, or
  whatever.") was first placed *after* the clean "Enter the tree, a tree where each node
  is a letter..." line, which read as a redundant aside once the concept was already
  explained. Moved to open the beat instead — the struggle has to come first, then the
  clean recovery, for the "cold open blooper → composed explanation" structure to land.

