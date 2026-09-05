# Lessons from the EP27-29 brainrot batch (2026-09-04)

Additions to `LESSONS_EP20-26.md`; those rules all still apply.

1. **Listen to the recorded intro before building the title sticker.** The presenter changes
   the intro wording between script and recording ("...content moderation PIPELINES to Gen
   Alpha..."). Dump the INTRO range's transcript words (`transcripts/<src>.json` filtered to the
   EDL range) and build the sticker from that, not from the batch plan. EP29's sticker had to be
   rebuilt and the episode re-composited because of this. A cold open (EP27) has no intro at all:
   the sticker then rides the hook overlay from 0.0s and `check_overlay_timing`'s "0.00s lead"
   flag is expected.

2. **The presenter's pasted "what I actually said" text carries his spellings.** ASR garbles
   ("lokenuanly", "Psy bow", "Blood was capping", "unk") are his coinages ("lowkenuinely",
   "Sybau", "Blud", "unc"). Patch `transcripts/<src>.json` word `text` before compositing
   (merge split words by extending `end` and deleting the follow-on word; remember the transcript
   has `spacing` entries between words, so "next word" is the next entry with `type == "word"`).

3. **Measure SFX audibility directly, not with `check_sfx_audible.py`.** The gain-fitted
   difference method false-flags half the cues. `tool/helpers/check_sfx_direct.py <ep-dir>`
   compares the 50ms peak of `sfx/sfx_track.wav` with `final_nosfx.mp4` in each cue's window;
   `--apply` lifts anything more than 3 dB under the voice to −2 dB (×4 cap), then re-run
   `build_sfx.py`. The loudness formula in `build_sfx` under-drives short transients (click, pop,
   shutter, sparkle, impact) by 10-17 dB, so expect ~2/3 of cues to get a boost. The FIRST
   target (−2 dB under the voice peak) was too loud for the user; the targets are now −8 dB
   for UI/stingers and −4 dB for voice memes. Do not `--apply` repeatedly on cues that have a
   neighbour within 1.5s: the neighbour sits in the window and the loop drives the cue to
   silence (the checker now skips those and says "overlap"; set them by hand).

3b. **Cue timing: land 30 ms BEFORE the word onset, not after.** The first cue lists were
   50-150 ms late on almost every spoken landing (written from caption chunk starts). Snap to
   the transcript word onset minus 0.03 s; voice-meme replies go at phrase end + 0.08 s. For
   visual landings (a slam, a stamp, a flinch) do not trust the batch-plan times: decode the
   overlay render around the cue and take the frame-diff peak (EP27's flinch scratch was 0.9 s
   late, EP28's SSE shutter 1.2 s early). Voice memes land on their first syllable
   (`ANCHOR` in build_sfx.py) — the swell heuristic put the 6-7 snippet's "seven" on the word
   and pre-rolled the "six".

3c. **Cut sound effects off.** A 2.8 s ding ring-out or a 4 s reveal sting smears into the
   next line. `DEFAULT_CUT` in build_sfx.py stops every long file 0.6-2.0 s after its landing
   with a 120 ms fade; per-cue `"cut"` overrides it (0 = play whole).

4. **`json.dump` of numpy floats truncates the file.** A `TypeError: float32 is not JSON
   serializable` mid-dump leaves a half-written `cues.json`. Cast to `float()` first, and keep
   the cue generator (`write_cues_27_29.py` pattern) so the file can be regenerated.

5. **HyperFrames takeover renders die under load.** 14-20s takeovers take 10-14 min and exit 255
   at frame ~345 if any other render or composite runs alongside. Builders that "arm a waiter"
   for a render that has already died never wake up: if `index.html` is newer than `render.webm`
   and no `hyperframes.mjs` process exists, render it yourself, alone, in the foreground
   (a foreground call that hits the tool timeout is moved to the background, not killed).

6. **Brainrot cast rules that held.** Real photos (Livvy Dunne, MrBeast, Kai Cenat, LaMelo) as
   circle/inset stickers with sponsor marks cropped; LaMelo 6-7 hands on every spoken
   "six seven"/"sixty-seven"; crude spoken words never printed on overlays (the user's own
   `SYBAU` chip is the one acronym allowed); tease chips dropped from every payoff.

7. **Gameplay strip (brainrot split-screen).** `render.py` takes `edl["gameplay"]` = {file,
   src_start, y, h, crop} and composites a muted, looped, cropped gameplay clip ABOVE the
   overlays and BELOW the captions. Put it at y=1300 (620px): the chin sits ~1200 on these
   takes and all overlay content ends by y=1280, so nothing is hidden; captions (margin-v 400,
   3px outline) land on the gameplay, which is the standard look. Vertical "no copyright"
   gameplay uploads on YouTube are 9:16 already; crop the band that holds the runner
   (Subway Surfers: source y 1000-1620; Minecraft parkour: y 650-1270). yt-dlp lives in
   `tool/.venv` (`python -m yt_dlp --download-sections "*10-160"`).
