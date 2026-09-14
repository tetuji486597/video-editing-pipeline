# Lessons from the EP30-35 batch (2026-09-05)

Additions to `LESSONS_EP20-26.md` and `LESSONS_EP27-29.md`; those still apply.

1. **Build the EDL with `tool/helpers/edl_from_takes.py`.** One spec per episode (beat, first
   word time, last word time, why) → acoustic onset/tail per range, alternating zoom, quote
   and reason fields, then `fix_windows.py --write` and `beats_md.py`. Six episodes took
   minutes instead of an afternoon of hand measurement. Watch the `last` hint: it must sit on
   the LAST kept word (a hint a word early drops the sentence end — EP30 "tell.", EP34 "fight").
   ASR pads a restart's first word into the previous one ("...A" spanning 2s, "requests....Smarter");
   split those boxes in the transcript so the range starts on the real onset and the caption
   shows the word. ASR can also box a spoken parenthetical as an `audio_event` (EP30
   "(meaning off by default)") — it then vanishes from captions; re-add it as timed words.

2. **The countdown gag is a coordinator overlay, not a builder slot.** `make_countdown.py`
   renders a 180x100 chip webm (30 → 0 over T−t0, ring drains continuously); render.py now
   takes `x`/`y` on an overlay entry, and the chip goes LAST in `overlays` so it rides above
   takeovers. Builders reserve the corner x≥670,y≤330; `check_reserve.py` verifies it on the
   render (takeover backgrounds are allowed there, bright content is not; 1-3 frame shutter
   flashes are fine — the chip sits on top).

3. **Render queue.** `tool/helpers/hf_render.sh <slot>` is a machine-wide 2-slot queue with a
   retry; six builders shared it with zero dead renders (EP27-29 lost several to overload).
   Throughput is the cost: ~35 renders took ~2.5 h. Builders must call it, never npx.

4. **Builders die at the API session limit; plan for the coordinator to finish.** All six
   builders were killed by a 429 session limit after their last render. Because every builder
   had already wired `overlays` into edl.json and rendered everything, the coordinator could
   run the audit suite itself (margins on 39 renders found 3 breaches the builders would have
   caught: an overflowing headline and two `left:70px` shadows) and finish. Keep the "wire the
   EDL as you go" instruction — it is what made the recovery cheap.

5. **`check_margins` catches text overflow that CSS width does not.** A `white-space:
   nowrap` headline wider than its box centres beyond it (EP33 "LEAST CONNECTIONS" at 64px
   spanned x 70-891 in a 740px box). Shrink the font, not the box.

6. **Word-anchored cue lists are fast and accurate.** `cues_from_words.py` resolves
   `{beat, phrase, sfx}` specs to output-time onsets (−30 ms) straight from the EDL and
   transcripts; 14-17 distinct sounds per episode, then `check_sfx_direct.py --apply` twice
   and hand-set the overlapping ones. Peaks landed at −0.7…−1.9 dBFS first time.
