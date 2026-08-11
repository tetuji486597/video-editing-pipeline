# EP5 — Why You Never Get Charged Twice (video-use edit)

## Session 1 — 2026-08-03

**Strategy:** Single source recording (`ep5.mp4`, 2160x3840). Script given verbatim by Gordon;
matched each beat to the cleanest full take from the packed transcript (several beats had 2-3
retakes — picked the one that ran the whole line clean rather than a flubbed/cut-off attempt).
Total runtime 50.54s, close to the script's own "~45s" estimate.

**Visual metaphor (one thread across the episode):** a claim-check / coat-check ticket stub
("ADMIT ONE · 012345") standing in for the idempotency key — introduced in BUILD as the
key attached to a payment request, logged into an old leather ledger in NEW_COMPONENT
("first time seen"), then shown twice side-by-side in a second NEW_COMPONENT overlay to
land the actual payoff: same ticket number in, same result out, charged exactly once.
6 overlays total (title, hook, build, ledger, dedup, payoff) — no fullscreen takeovers this
time, all bottom-band or compact card compositions, varied between single-object (build,
ledger) and two-up comparison (dedup) layouts.

**Decisions:**
- Reused the established grade recipe and ASS word-highlight captions (`--caption-margin-v
  280`, matching the now-settled series default — see `STYLE.md` in the video-editing-pipeline
  repo).
- Fresh trap BGM (`bgm_002.wav`, "modern trap beat, deep 808 bass, crisp hi-hats, dark melodic
  loop") — explicitly re-resolved rather than reusing EP1/EP4's track; the first resolve call
  actually returned an ambient/underscore track by semantic-match coincidence, caught by
  checking the manifest description before committing to it.
- SFX: reused 5 already-downloaded myinstants.com clips from EP1/EP4 (record scratch, wrong
  buzzer, vine boom, camera shutter, correct ding — see `sfx/SFX_NOTES.md`) rather than
  downloading fresh ones, to avoid adding new untracked myinstants downloads for the same
  copyright-caveat reason already flagged in EP1.
- Punch-zoom on the HOOK, focal point measured fresh from this footage (520, 615 on the
  1080x1920 canvas) — this presenter sits noticeably higher/closer in frame (beanie, tighter
  crop) than EP1/EP4's footage, confirming focal point does NOT transfer between episodes
  and must be re-measured every time.

**Reasoning log:**
- The stock "claim-check ticket" image resolved via `media-use` came back as an illustrated
  sports-event ticket ("BOARS VS SHARKS — CENTRAL STADIUM — $30"), which would read as
  confusing/off-topic at full size. Fixed by cropping to just the generic "ADMIT ONE / 012345"
  stub half — keeps the ticket metaphor without the irrelevant branding. Worth remembering:
  inspect a resolved stock asset for baked-in text/branding before compositing it in full.
- First full-pipeline render surfaced a real collision: the hook overlay's bottom-band text
  (designed against the *old* lower caption position) overlapped the captions now that they
  sit at `MarginV: 280`. Root cause — every bottom-band overlay convention from EP1/EP4 was
  built before that margin change; nothing had re-checked bottom-band vertical budget against
  the new, higher caption zone. Fixed by moving all bottom-band overlays (hook, build, dedup,
  payoff) further up (`top: ~1030-1150px` instead of `~1210-1260px`) and re-verified with actual
  frame extractions at each overlay's on-screen moment, not just a lint pass. **This same
  vertical-budget check should happen automatically on any future episode** — the lint check
  doesn't catch overlay-vs-caption overlap, only overlay-vs-its-own-container overflow.
- Separately, the first cut of the `ledger` overlay used a centered full-panel layout (like
  EP4's `slot_problem`) — at this footage's framing, that landed the ledger book directly over
  the presenter's mouth like a mask. Rebuilt as a compact bottom-band composition (book +
  text side-by-side) instead. Lesson: a centered/full-panel layout that worked on one
  episode's footage can collide with the face on a different presenter framing — check an
  actual frame before committing to that layout, don't assume it transfers either.
- All cut boundaries verified via `timeline_view.py` waveform+frame strips (5 boundaries
  checked) — clean silence gaps at every cut, no clipped words, no audio pops.

**Outstanding:**
- Standing caveat: music/SFX levels (0.55 for SFX, 0.13/0.30 duck envelope for music) are
  estimated, not confirmed by ear against the final loudnorm pass.
- Deliverable: `/Users/gordon.jin/Downloads/edit_ep5/preview_final.mp4` (50.54s, `--preview`
  quality). Final CRF-20 pass pending sign-off.
