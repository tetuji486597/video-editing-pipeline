# EP29 — Who reads your skibidi posts (BRAINROT EDITION)

Source: `C:\Users\gordo\Downloads\drive-download-20260904T054818Z-1-001\ep29.mp4`. Single deliverable
`final.mp4` (63.63s). No A/B hook variants for the brainrot batch.

## Edit decisions
- **Intro re-recorded as "Explaining content moderation PIPELINES to Gen Alpha in thirty
  seconds."** The first sticker cut dropped "pipelines"; it was rebuilt to match the recording:
  `EXPLAINING CONTENT / MODERATION PIPELINES / TO GEN ALPHA / IN 30 SECONDS` (4 boxes at 44px, widest
  ~633px, centred on x=540, y 210-590, clear of the brow at ~690).
- **Last complete attempt per beat wins**; see `beats.md` / `takes_packed.md` and each range's
  `reason` in `edl.json`.
- **Recorded words beat the script.** The transcript garble "lokenuanly" is the user's own
  coinage `lowkenuinely` (from his pasted lines) and "Livvy Dunn" is spelled `Livvy Dunne` —
  both patched in `transcripts/ep29.json`. The recorded gag is a Livvy Dunne post, not the
  scripted Botticelli painting, so the overlays use the real Livvy Dunne 2025 photo (CC BY-SA)
  and the Botticelli spare is unused. "Is it subhuman? You're cooked", "goofy ahh ones",
  "gets a little more based" are captioned as spoken.
- Ranges: INTRO, HOOK 3.25-9.08, PROBLEM 9.08-18.75, BUILD 18.75-27.63, NEW_COMPONENT
  27.63-44.71, AI_ANGLE 44.71-55.50, PAYOFF 55.50-63.63 (output times; source times in
  `edl.json`). Slow zoom 1.0↔1.08 alternating per range about (540,730).

## Overlays (7 slots, 2 takeovers)
| slot | format | out start | dur | gap after |
|---|---|---|---|---|
| slot_tiktok_title | centred sticker | 0.000 | 3.2 | 0.65 |
| slot_hook | half-panel: POSTS PER DAY counter stacking to 1,000,000,000, MrBeast avatar counting on his fingers and giving up, Trippi Troppi buried under post cards, `help` sign, Skibidi Toilet on "skibidi posts" | 3.850 | 5.2 | 0.60 |
| slot_problem | TAKEOVER: SLOW stadium of Trippis vs FAST BUT DUMB Bombardiro judge; real Livvy post → gavel → BOOTED; WRONG, human un-boots with a green check, SKILL ISSUE stamp | 9.650 | 9.1 | 0.55 |
| slot_build | translucent band: funnel, posts pour, real Instagram community-guidelines notice as reference + EXACT COPY, Among Us SUS chip, Tung Tung Tung Sahur bat knocks ×3 (24.65/24.88/25.11), trash chute → fries bag on "fries in the bag" | 19.300 | 8.9 | 1.80 |
| slot_new_component | TAKEOVER: EVERY POST GETS A SCORE, Ballerina Cappuccina spinning, four meters, score dial (trig needle), gigachad STAYS / toast COOKED, 67% + `idk chat` + LaMelo hands, HUMAN lane to Kai Cenat, ROBOT LEARNS loop, BASED meter +1 | 30.000 | 14.7 | 1.20 |
| slot_ai_angle | transparent band: HUMAN IN THE LOOP, ROBOT giant pile vs HUMAN goofy ones, VOLUME / VIBES bars | 45.900 | 9.5 | 0.90 |
| slot_payoff | photo card: the un-booted Livvy post with a green check, PEOPLE DO THE HARD ONES, Among Us `YOU` crewmate on "NPC"; no tease chip | 56.300 | 7.3 | — |

All seven renders: `check_margins` clear, `check_overlay_files` 0 problems, `check_fade` ok,
`check_overlay_timing` all inside beat. Every junction is a deliberate ≥0.5s gap. The
new_component render is slow (10-14 min) and died twice at frame ~345 when other renders ran
alongside — render it alone.

Assets: `assets/ATTRIB.md` + `episodes/ATTRIBUTIONS_EP27-29.md` (Livvy Dunne, MrBeast, Kai Cenat,
LaMelo Ball photos from Wikimedia; Instagram notice; Trippi Troppi, Bombardiro, Ballerina
Cappuccina, Tung Tung Tung Sahur, Skibidi Toilet, Among Us).

## Gameplay strip (user request: "subway surfer / minecraft parkour gameplay")
`edl.json["gameplay"]`: Subway Surfers (src 75s in), muted, cropped to 1080x620 and composited at y=1300-1920, ABOVE
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

`sfx/cues.json`: 33 cues, 33 distinct (bass drop, bubble pops, wrong buzzer, skibidi toilet,
swoosh, error glitch, notif, stamp, "erm what the sigma", correct ding, shutter, whoosh, amongus
sus, tung sahur, swoosh_deep, "fries in the bag", ding, gigachad, bass hit, record scratch, 6-7
snippet, swoosh_double, sparkle, bruh, riser, rizz, impact, amongus reveal...). Gains fitted from
file loudness, then 21 cues boosted from the direct SFX-vs-voice measurement (see EP27
project.md); only the camera shutter at 17.95s stays ~5 dB under the voice peak (its mean is
above the voice). Final peak −1.75 dBFS (after pass 2). `br_amongus_reveal` at 62.6s runs past the video end
by design (clipped by the mix).

## Caveats
- The sticker was rebuilt after the first composite; `final.mp4` is from the second composite
  (verified on the frame at 1.5s).
- Uncensored spoken words ("subhuman", "gyatt") stay in captions; on-screen overlay text is PG-13.
