# EP28 — Why ChatGPT types so slow (BRAINROT EDITION)

Source: `C:\Users\gordo\Downloads\drive-download-20260904T054818Z-1-001\ep28.mp4`. Single deliverable
`final.mp4` (61.96s). No A/B hook variants for the brainrot batch.

## Edit decisions
- **Intro re-recorded as "Explaining streaming to Gen Alpha in thirty seconds."** The title
  sticker matches it: `EXPLAINING STREAMING / TO GEN ALPHA / IN 30 SECONDS` (3 boxes, 44px so the
  widest line stays under 660px, centred on x=540). INTRO range is the last complete take
  (22.60-25.75 source); the attempt at 9.60 is incomplete.
- **Last complete attempt per beat wins**; see `beats.md` / `takes_packed.md` and the per-range
  `reason` fields for the acoustic onset/offset choices.
- **Recorded words beat the script.** The transcript's "Psy bow." was merged into the user's
  spelling `Sybau.` in `transcripts/ep28.json`. "raw dogging", "backshots", "LARPing",
  "legiterally", "bed rot" are captioned as spoken. The recorded number is sixty-seven seconds
  everywhere (script said 20s in places) — overlays use 1:07 / 67.
- Ranges: INTRO 22.60-25.75, HOOK, PROBLEM, BUILD, NEW_COMPONENT, PAYOFF (source times in
  `edl.json`). Slow zoom 1.0↔1.08 alternating per range about (540,730).

## Overlays (6 slots, 2 takeovers)
| slot | format | out start | dur | gap after |
|---|---|---|---|---|
| slot_tiktok_title | centred sticker | 0.000 | 3.1 | 1.30 |
| slot_hook | half-panel ChatGPT chat card typing "chat is this real 6 7 skibidi", Tralalero sprinting under the caret, `idk yet` bubble on "doesn't know the end yet", mic drop on "from the dome" | 4.400 | 9.3 | 1.30 |
| slot_problem | TAKEOVER: blank tab + spinner, Trippi Troppi with "??", stopwatch to 1:07 with LaMelo 6-7 pops, tab smashed and window flies off, grass strip + TOUCH GRASS chip, SYBAU slam | 15.000 | 9.6 | 1.60 |
| slot_build | transparent motion graphic: MODEL chip → chute → phone, nine Chimpanzini each carrying one word chip, ONE PIPE / OPEN chips | 26.200 | 7.9 | 0.50 |
| slot_new_component | TAKEOVER: SSE one-way pipe vs CHAT two-way (Skibidi Toilet ↔ Cameraman), Among Us NPC, ONE WAY ONLY slam, real DevTools event-stream capture (`assets/sse_devtools_capture.png` + `sse_capture.txt` rows), FIRST WORD 0.5s / WHOLE THING 1:07, LaMelo pop, AURA meter | 34.600 | 20.5 | 0.60 |
| slot_payoff | corner chip: first word `chat` solid, rest ghosted; bed-with-phone on "bed rot"; no tease chip | 55.700 | 4.8 | — |

All six renders: `check_margins` clear, `check_overlay_files` 0 problems, `check_fade` ok,
`check_overlay_timing` all inside beat. The WHOLE THING stamp's left edge measures x=79 on the
composite (inside the x≥70 rule but tight — nudge right if the margin rule ever tightens).
`check_safe_zone` reports strip artefacts on the two takeovers (pixel-probed: nothing in x<60).

Assets: `assets/ATTRIB.md` + `episodes/ATTRIBUTIONS_EP27-29.md`. LaMelo is a head-only circle
sticker so the jersey sponsor marks are cropped out. The DevTools capture is a real
`stream.wikimedia.org` event-stream response.

## Gameplay strip (user request: "subway surfer / minecraft parkour gameplay")
`edl.json["gameplay"]`: Minecraft parkour (src 10s in), muted, cropped to 1080x620 and composited at y=1300-1920, ABOVE
the overlays (so the takeovers do not swallow it) and BELOW the captions. The strip only ever
covers the shirt (chin ~1200). Source clips: `shared_assets/brainrot/gameplay/` (150s cuts of
"no copyright" vertical gameplay uploads, see ATTRIBUTIONS_EP27-29.md). Takeover content stays
above y=1280 so nothing is hidden; captions keep their 3px outline over the moving background.

## Audio
**SFX pass 2 (user feedback: "some of the sfx are too loud... timing not always the best...
you don't always have to play the whole sound effect").** Gains re-fitted to −8 dB under the
voice peak for UI/stinger cues and −4 dB for voice memes (was −2 dB). Cue times snapped to the
landing word's onset minus 30 ms (they were 50-150 ms late), voice memes to the phrase end
+80 ms, and visual-driven cues to the frame-diff peak of the overlay render
(`tool/helpers/sfx_visual_events.py`; see LESSONS_EP27-29.md). Long tails are now cut by
`DEFAULT_CUT` in build_sfx.py (120 ms fade), and voice memes land on their first syllable via
`ANCHOR`. `cues.json` is the source of truth now; do not regenerate it from the batch script.

`sfx/cues.json`: 31 cues, 29 distinct (typing loop, bruh, sheesh, riser, wrong buzzer, error
glitch, 6-7 snippet ×3 on each "sixty-seven", swoosh_elec/pops per word launch, sparkle, shutter,
whoosh, ding, bass drop, click, vine boom...). Gains fitted from file loudness, then 16 cues
boosted from the direct SFX-vs-voice measurement (see EP27 project.md). Final peak −1.75 dBFS (after pass 2).
