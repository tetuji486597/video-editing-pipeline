# EP1 — Where Your Password Actually Goes (video-use edit)

## Session 1 — 2026-07-22

**Strategy:** Single continuous take-through of the script (HOOK → PROBLEM → BUILD → NEW_COMPONENT → PAYOFF_NEXT) stitched from 7 source ranges, with two retaken sections swapped in for the NEW_COMPONENT beat. Bold cinematic color grade (teal-shadow/warm-highlight split, vignette, sharpen, grain) applied per-segment. 8 HyperFrames motion-graphic overlays built around one recurring visual metaphor — a kitchen blender making a smoothie, standing in for password hashing — researched from real teaching analogies (rainbow tables, salting, one-way hashing) rather than invented cold. Bold-overlay captions (2-word uppercase chunks). Trap-style instrumental bed via the `media-use`/HeyGen pipeline, ducked under the two densest explanation beats with a swell into the outro.

**Decisions:**
- Take choices: HOOK uses the second delivery (12.10–18.64s) over the first (cleaner single breath, no gap before "run."). NEW_COMPONENT stitched from 3 ranges to avoid a "mixed and hacked" flub and a cut-off "bcrypt." retake.
- Grade: custom ffmpeg chain (not a video-use preset) — `eq` contrast/saturation + `colorbalance` teal-shadow/warm-highlight split + `vignette` + `unsharp` + `noise` grain — built to match the bold cinematic look from a prior Vyra episode.
- Overlay engine: HyperFrames (transparent alpha WebM), 8 slots built in parallel sub-agents against one shared brief (title, hook stamp, problem/danger, build/hashing, rainbow/attacker, salt/defense, bcrypt/tension, riddle/resolution). 2 of 8 are full-canvas takeovers (problem, rainbow); the rest are confined to a bottom band (y 1260–1870) because this footage's tight selfie framing leaves almost no headroom above the head — top-anchored placement (the Vyra-project default) does not work here.
- Music: sourced via the newly-installed `media-use`/HeyGen pipeline (this was the session's first real use of it — required installing + OAuth-authenticating the `heygen` CLI). Looped via a 0.5s crossfade (28s source → 55.5s), ducked 0.22→0.10 under BUILD and the salt explanation, swelling to 0.28 for the outro.

**Reasoning log:**
- Transcript alias mismatch: EDL used source id "EP1" but the cached transcript was named after the raw filename — `build_master_srt` produced 0 caption cues until the transcript was copied to `transcripts/EP1.json`.
- ffmpeg's default "vp9" decoder silently drops WebM's alpha side-channel (auto_scale fakes an opaque plane instead) — confirmed by direct testing. Fix: `render.py` now forces `-c:v libvpx-vp9` on any `.webm` overlay input. This is a durable fix to the shared helper, not a one-off workaround.
- This machine's default Homebrew `ffmpeg` has no `--enable-libass`, so the `subtitles` filter doesn't exist at all — `ffmpeg-full` (already installed, keg-only) has it. Render commands need `/opt/homebrew/opt/ffmpeg-full/bin` prioritized on PATH.
- First-pass bottom-band overlays (build/salt/bcrypt/riddle) used a semi-transparent glass look (`rgba(255,255,255,0.08)` fill / `0.5` stroke) that's nearly invisible against this footage's dark brown t-shirt — fixed by bumping to `0.22`/`0.92` opacity plus a dark drop-shadow halo on each icon's container, which is background-color-agnostic.
- video-use has no native background-music mixing step in `render.py` — built a standalone ffmpeg pass (seamless loop via `acrossfade`, piecewise-linear `volume` envelope for ducking, `amix` onto the final render) rather than extending the shared helper, since the ducking timings are specific to this episode's beats.

**Outstanding (session 1):**
- Music level was tuned by ear-estimate only (baseline 0.22 / ducked 0.10 / swell 0.28) — needs Gordon's by-ear confirmation and likely a re-tune, per the standing rule that volume never transfers cleanly across different source tracks.
- Final render (non-preview quality, CRF 20) not yet produced — current output is `--preview` quality (CRF 22). Pending Gordon's sign-off on the cut/overlays/music before the final pass.

## Session 2 — 2026-08-01

**Requests:** word-by-word caption highlighting; move captions lower; more creative overlays; pull real images from the web; add trending SFX from myinstants.com.

**Decisions:**
- Captions rebuilt as real ASS (not SRT) — `build_master_ass()` added to `render.py`. Word-highlight works by emitting one Dialogue event per word (full chunk text, only the active word color-tagged gold `&H00D7FF&`) rather than relying on ASS `\k` sweep semantics, which are ambiguous/inconsistent across renderers. PlayResX/Y set to the real output canvas (1080x1920) so MarginV is literal output pixels, not scaled through libass's SRT-conversion default (PlayResY=288) — much more predictable. Landed on `--caption-margin-v 60` (near the bottom edge) per "move it lower."
- Moving captions that low collided with the v1 bottom-band overlay zone (y 1260–1870) — resolved by shrinking/raising that zone to y 1210–1690 for all 4 partial slots (hook, build, salt, bcrypt, riddle), freeing a clean gap above the new caption position. Coordinated this across all affected slots before touching content.
- All 8 overlays rebuilt from scratch for "more creative + real images": each of the 6 conceptual slots (problem, build, rainbow, salt, bcrypt, riddle) now integrates 1-2 real photos sourced via the `media-use` skill's `resolve --type image` (HeyGen catalog) — e.g. a real prism dispersing light into an actual rainbow for the rainbow-tables beat, a real hourglass with a masked sand-fill reveal for bcrypt, a real sealed mason jar for the riddle payoff. Title and hook stayed typographic (not concept overlays, lower value to redo).
- Added 7 SFX stingers sourced from myinstants.com (Vine Boom, Wrong Answer Buzzer, Record Scratch, Suspense Strike, Correct Answer ding ×2, Bruh) at specific script beats — full sourcing/usage reference at `sfx/SFX_NOTES.md`. **Explicitly against this series' established "no brainrot" baseline** ([[vyra-no-brainrot-style]] from a prior Vyra episode rejected SFX stingers outright) — flagged the direction-reversal and the copyright risk (myinstants hosts ripped, non-royalty-free audio) before proceeding; Gordon confirmed he wants it anyway for this episode.

**Reasoning log:**
- Bugs independently caught and fixed by the overlay-rebuild sub-agents, worth knowing for future HyperFrames work: (1) GSAP `.fromTo()` defaults `immediateRender: true`, which snaps elements to their "from" state at timeline-build time instead of their scheduled position — collapsed 14 radiating particles into a static blob until `immediateRender: false` was added to each reused-base-state tween. (2) `mix-blend-mode` (multiply/screen) on a layer nested inside a fading-opacity ancestor produces color/alpha corruption artifacts when re-decoded from a transparent-alpha WebM — replaced with plain layered gradients. (3) A CSS `radial-gradient`/blurred-circle "aura" banded visibly (concentric rings, octagon posterization) under VP9 alpha encoding — fixed with a static SVG `feTurbulence` dither overlay at low opacity.
- Music + SFX mixing still isn't part of `render.py` — both are separate ffmpeg `amix` passes applied after `render.py`'s own output (narration + overlays + captions + loudnorm), each built once as a standalone track (`music_final.wav`, `sfx_track.wav`) then mixed in together in one final pass.

**Outstanding (session 2):**
- Same music-level caveat as session 1 (still ear-estimated). SFX levels (0.55-0.7 relative to narration) are equally unconfirmed by ear — flagged in `sfx/SFX_NOTES.md`.
- Deliverable: `/Users/gordon.jin/Downloads/edit/preview_v2_final.mp4` — still `--preview` quality. Final CRF-20 pass pending sign-off.
