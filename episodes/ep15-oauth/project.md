# ep15-oauth — How sign-in with Google works (OAuth)

## Session — 2026-08-20 (EP14-19 batch rebuild)

**Context.** This is a REBUILD, not a first pass. An earlier build of EP14-19 was snapshotted
to `_overlay_snapshots/2026-08-20_pre-richness-rebuild/` and its live episode dirs removed.
That batch drew three rounds of feedback, all recorded in `OVERLAY_SPEC.md`: overlays
presented "too much information in too short of time", then read as "too sparse", then
"not enough variation in presentation format", plus "not enough real, relevant images --
the dictionary for the DNS is not exactly the image that best applies". The old
`index.html` files were treated as the ANTI-reference; only their downloaded images were
harvested, and four were rejected outright as visual puns (keys / dictionary-page / mask /
cables).

**Cut.** Takes chosen from the packed transcript, every range end measured ACOUSTICALLY with
`find_dead_air.py` rather than off the ASR word box. That mattered: Scribe boxed EP18's
premise "So" as a 4.38-second word and EP19's opening "This" as 2.65s, so padding off the
ASR end would have shipped dead silence at those range heads.

**Output-timeline math.** Beat windows are derived on render.py's real 24fps extract grid
(`ceil(nominal*24)/24`, verified against all 29 rendered segments), not by summing source
ranges -- see ep13's `_trim_note` for the session where skipping that put every downstream
cue 70ms off. `tool/helpers/fix_windows.py` does this and is the authority; the EDL is
authoritative over `BATCH_PLAN_EP14-19.md` for every start/duration.

**New tooling added this session** (all in `tool/helpers/`): `words.py` (word-level lookup
for cut edges and payoff-word sync), `fix_windows.py`, `check_overlay_files.py`
(existence / declared-vs-actual duration / staleness), `check_fade.py` (entrance + fade
measured on the rendered alpha plane), `check_caption_band.py` (what each overlay actually
composites behind the burned-in captions). `render.py` gained `--subtitles-out` so A/B
variants cannot share one caption file.

**Six renderer traps found and added to OVERLAY_SPEC.md this session:** box-shadow reaches
~1.6x its blur radius (EP13's shipped title card breaches y=180 by this rule); tweening
`filter` from a computed `none` renders solid black; an SVG `<filter>` defaults to a 120%
region and `feTurbulence` fills all of it (painted grain into the caption band); nesting
fading ancestors multiplies opacities; a transformed child keeps compositing while its
faded ancestor blacks out; and per-leaf fading composites as 1-(1-a)^n, so a back-loaded
ease that reads as 21% in the tween renders at 60-76% on screen.

**Audits run, on rendered pixels not CSS arithmetic.** Caption band: 0 slots with a
sustained bright wash (the only bright peaks are 2-5 frame shutter flashes, EP4's own
technique). Tease chips: 0 across all 47 compositions, grepped by element
(`class="tease`, `id="tease`, `<span>Next`) since the words never appear literally.
Freshness (rule 9) re-checked immediately before every final render -- it caught EP18
compositing against a `slot_response` that had re-rendered 12 minutes earlier.

### Episode-specific

**Beats (6):** HOOK / PROBLEM / BUILD / NEW_COMPONENT / SCOPE / PAYOFF. 46.333s.
**Formats:** half-panel, TAKEOVER, transparent, TAKEOVER, motion-gfx, half-panel.

**Take notes.** Hook is take 4 of 4 and the only one delivering the hook and the "That's
called OAuth" tag as one unbroken line; the others break ~0.6s before the tag or abort.

**Real images.** `slot_new_component` uses a REAL Google OAuth consent screen from Google's
own published developer documentation. Two other images from that same page were rejected
because they show a real account address and avatar. `slot_hook` uses a real logged-out app
login screen (Wikimedia, public domain) cropped to exclude the host product's wordmark.
**`keys.jpg` from the old snapshot is rejected** -- the spec names it as the metaphor failure.


## Session — 2026-08-21 (zoom + TikTok SFX pass)

Cuts, overlays, captions and EDL timings are UNCHANGED from the 2026-08-20 build. Only two
things moved.

**Gradual centered zoom.** Every range now carries `zoom: {mode: "slow"}` with focal
**(540, 960)** — the exact frame centre, deliberately not render.py's (540, 730) eye-line
default. Direction alternates per segment (`+-+-`), so each range starts at the scale the
previous one ended on and the drift is continuous across every cut rather than snapping back
to 1.0 at each edit. Magnitude is capped at **1.045**: a centered zoom displaces a point by
distance_from_centre*(Z-1), and these overlays were placed against measured face positions
with clearances as tight as 40px, so 4.5% costs the tightest ~13px while render.py's 12%
default would cost ~35px and push graphics into the face. Segment durations are byte-identical
after the zoom, which is why every overlay cue and caption still lands.

**TikTok SFX.** The previous set was too limited (EP13 shipped 10 cues from 4 distinct
sounds); each episode now uses 8-10 distinct sounds from a 22-file TikTok set, including one
voice meme per episode. See `sfx_shared/TIKTOK_SFX_NOTES.md` for what each sound means, the
measured-loudness volume calibration, and the hard requirement that every file be trimmed of
leading silence (build_sfx REFUSES >20ms, which killed the first render pass).

**Verification note worth keeping.** Checking SFX audibility by comparing peak levels between
final.mp4 and final_nosfx.mp4 proves NOTHING — loudnorm renormalises the whole mix, so peaks
go *down* after adding SFX. The working method is to difference the two tracks with a fitted
gain, and it must run at **32 kHz, not 8 kHz**: a shimmer lives above 4 kHz, so an 8 kHz
downsample discards it and reports an audible cue as silent (measured 0.80x vs 3.27x on the
same cue). All 78 cues across the eight deliverables verify audible at 32 kHz.
