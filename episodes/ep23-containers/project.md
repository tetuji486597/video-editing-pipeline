# ep23 -- why everyone ships in containers (Docker)

## Session -- 2026-08-28 (EP20-26 batch)

**Batch context.** Built in the EP20-26 batch (2026-08-28) per `BATCH_PLAN_EP20-26.md`.
Cuts measured acoustically (find_dead_air + words.py); windows stamped by fix_windows.py.
Captions: NEW safe-zone settings **60/220/400** (`--caption-font-size 60 --caption-margin-lr
220 --caption-margin-v 400`), per SAFE_ZONE.md's burned-clean recommendation -- first batch
to adopt them. Zoom: slow centered 1.045 alternating. SFX: sfx_shared TikTok set, cues in
`sfx/cues.A.json`/`cues.B.json`, mixed by build_sfx.py; audibility verified by gain-fitted
32kHz difference (tool/helpers/check_sfx_audible.py, new this batch -- its control windows
must be cue-free AND it under-reports under non-scalar chains like limiters; confirm flags
with a clean forward control before believing them).

**Variants.** A = interview (48.208s), B = cool tech (48.042s, -0.1667s -- 4 frames).

**Overlays.** hook works-on-my-machine R.I.P. half-panel / problem version-mismatch
takeover / build pack-into-box motion-gfx (clicks per chip on runtime/libraries/settings)
/ runs half-panel with Phippy (CNCF art, CC-BY-4.0) hopping laptop->teammate->cloud on the
words / vm VM-vs-container takeover / payoff full-bleed REAL container-ship photo
(Wikimedia CC BY-SA, branding-free sunset silhouette). slot_tiktok_title_b's EDL duration
was corrected to the true file length 4.766 (one-frame quantization).

**SFX.** Voice meme tt_emotional_damage on the phrase's R.I.P.; stamp.mp3 on the lid;
swoosh triplet on the hops (middle one bumped to 0.68 after QC). Finals: A -1.17dB,
B -1.67dB peaks.


## Session -- 2026-08-28 (feedback pass: text-blocking, margins, centered titles, zoom, SFX variety)

Applied Gordon's five notes across the whole batch; ALL 14 finals re-composited.
1. **Graphics never block text.** EP23 slot_hook: the container box had no hidden frame-0
   state (fromTo immediateRender:false left it parked over the card text from t=0) --
   redesigned, box hidden until the drop, lands on the card's empty shoulder;
   pixel-verified zero text occlusion across all frames. EP26 slot_hook: root cause was a
   missing class="card" (both tiles collapsed to the top-left corner, labels double-drawn
   at y~28, bar crossing 'reconnecting') -- rebuilt as two tiles y230-580 with per-tile
   labels and separated rows.
2. **Border margins.** New standing rule: text/UI within x70-870, y200-1280. Audited every
   slot on decoded pixels; fixed EP20 slot_tokens (top 190->215+), EP23 slot_build lid-flap
   (x894->x<=859), EP24 slot_control kicker (y187->212+), all four EP23/24 titles (y190->210),
   EP26 titles + hook.
3. **Titles centered.** All 14 stickers now flex-centered on x=540 (measured 539.5 on
   rendered frames), fonts trimmed so the widest box ends <=870.
4. **Zoom smooth + stronger.** render.py's zoom chain rebuilt (see build_punch_zoom_filter's
   jitter note): the old animated-scale/continuous-offset rounding mismatch caused the
   shake; now supersampled 2x with the crop offset derived from the frame's actual
   quantized size. Magnitude 1.045 -> 1.08, focal moved to the eye line (540,730) so the
   stronger zoom barely displaces the face against overlay clearances (EP22 slot_sign
   still nudged up 25px for headroom). Extraction is ~5x realtime now -- composites must
   run serially.
5. **SFX variety.** Cue lists rebuilt: 13-19 DISTINCT sounds per episode, zero repeats
   within an episode; ding/riser/swoosh_elec/swoosh_double/swoosh_deep/pop_balloon/
   pop_bubble/bass_hit/impact_trim/shutter/whoosh_trim rotated in. Volume formula
   recovered from the shipped table: vol = 0.45 * 10^(0.6*(-18-mean)/20), clamp [.15,.95].
   All mixes re-verified (peaks -1.17..-1.82 dB; audibility by gain-fitted 32kHz diff, with
   clean-control re-probes for every flag -- the checker self-contaminates on ring-y
   neighbours and on offset-anchored sounds like riser/swoosh_deep).
EP21-B note: still needs its custom mix chain (dip at 51.08-51.32, dynamic loudnorm,
+0.85dB makeup, 192k alimiter level=false) -- the standard build_sfx path still AAC-rings
at the payoff plosive; final -15.55 LUFS vs A's -15.25, peak -1.82.

### Addendum (same day): zoom focal bug -- all 14 finals re-rendered again
Gordon spotted the zoom drifting LEFT instead of into the face. Root cause (crosshair-
verified): in ffmpeg's `crop` filter, `iw`/`ih` inside the x/y expressions are FROZEN at
init and do not track a size-changing input, so the offset stayed at its initial value and
the zoom anchored to the top-left corner. This was also the residual "shake": the animated
scale moves in whole-pixel quantized steps, and with the offset not moving in lockstep the
motion arrived as irregular 0-2.5px lurches. Fix in render.py (see
build_punch_zoom_filter's docstring): offset now computed from the same time expression
with the same trunc quantization as the scale -- crosshair pinned at (539.5, 730.0) across
the whole zoom, per-frame motion <=0.24px. Video re-rendered for every variant; audio
STREAM-COPIED from the verified finals (`-map 0:v -map 1:a -c copy`, the STYLE.md
visual-only-change path), so all peaks/mixes are bit-identical to the verified pass.

### Addendum (feedback round 3): stray-dot + corner-collapse sweep, margin hard-gate
Gordon flagged EP22's arrow dot rendering at the frame top (root cause: fromTo props
present only in from-vars are DROPPED by the seek renderer, esp. under repeat) and EP26's
payoff still corner-collapsed (same missing-class bug as its hook -- the earlier fix was
never swept across sibling slots). Fixed both, then swept ALL compositions: 24 from-only
x/y hazards across 12 slots hardened (prop repeated in to-vars + CSS base positions), and
a new authoritative audit (tool/helpers/check_margins.py, decoded pixels) caught 4 more
border grazes (ep20/21/26 build chips, ep22 sign panel top) -- all nudged inside
x70-870/y200-1280. Every episode except EP23 re-composited (video-only; audio
stream-copied). Full write-up: LESSONS_EP20-26.md (now step 3 in CLAUDE.md's reading
list); renderer traps added to OVERLAY_SPEC.md rules 8-10.
