# EP27 — Netflix has a robot that breaks Netflix (BRAINROT EDITION)

Source: `C:\Users\gordo\Downloads\drive-download-20260904T054818Z-1-001\ep27.mp4` (4K, single take file,
several attempts per beat). Single deliverable `final.mp4` (52.79s). No A/B hook variants for the
brainrot batch.

## Edit decisions
- **Cold open, no "Explaining X to Gen Alpha" intro.** The presenter never records an intro for this
  episode; the recording starts on "Six, seven. Okay, so Netflix has a robot..." so the TikTok
  title sticker (`NETFLIX HAS A ROBOT / THAT BREAKS NETFLIX / ON PURPOSE`) sits over the hook
  itself (0.0-6.37s) and fades with the hook overlay. `check_overlay_timing` flags the hook's
  0.00s lead — that is the cold open, not a mistake.
- **Last complete attempt per beat wins** ("usually my last attempt is the best one"), see
  `beats.md` / `takes_packed.md` for the per-beat take table and the acoustic onset/offset
  reasoning in each EDL range's `reason`.
- **Recorded words beat the script.** Captions come from the ElevenLabs transcript with the
  user's own spellings patched in `transcripts/ep27.json`: `Blood was capping` → `Blud`,
  `types like an unk` → `unc`. Everything else is verbatim as spoken ("Among Us three AM",
  "low-key also Ws", "Ohio of boxes").
- Ranges (source → output): HOOK 4.28-10.64, PROBLEM 17.13-28.62, BUILD 33.22-44.05,
  NEW_COMPONENT 85.10-103.93, PAYOFF 108.51-113.72. Slow zoom 1.0↔1.08 alternating per range
  about the eye line (540,730).

## Overlays (6 slots, 2 takeovers)
| slot | format | out start | dur |
|---|---|---|---|
| slot_tiktok_title | centred sticker, 3 boxes | 0.000 | 6.367 (fades with hook) |
| slot_hook | corner cutouts: PRODUCTION rack + real Chaos Monkey logo, Chimpanzini yanks a cable, LaMelo 6-7 pop on "six seven" | 0.000 | 6.367 |
| slot_problem | TAKEOVER: smug NEVER GOES DOWN slide with Skibidi Toilet → 3:00 AM, Tung Tung Tung Sahur as the pager, PROD DOWN, aura counter | 8.200 | 10.0 |
| slot_build | upper-band UI: CHAOS MONKEY chip, ALL GOOD dashboard stays green while one server gets the red X, 2:00 PM clock, Kai Cenat sipping | 20.700 | 8.7 |
| slot_new_component | TAKEOVER: CHAOS ENGINEERING quest log (GUESS → KILL ONE BOX → WATCH), LUNCH clock, FOUND ONE stamp, Bombardiro bombs an Ohio of boxes | 29.400 | 18.067 |
| slot_payoff | day/night card BREAK IT YOURSELF FIRST, monkey by day / sleeping by night, no tease chip | 48.025 | 4.767 |

The build → new_component junction is a deliberate zero-gap cut at 29.40s (build fades to alpha 0
by 29.37, takeover starts 29.40) — checked frame by frame on the composite, no flash. All six
renders: `check_margins` clear, `check_overlay_files` 0 problems, `check_fade` ok.

Assets: `assets/ATTRIB.md` + `episodes/ATTRIBUTIONS_EP27-29.md` (Chaos Monkey logo, Chimpanzini,
Skibidi Toilet, Tung Tung Tung Sahur, Bombardiro, LaMelo Ball, Kai Cenat, Among Us crewmate).

## Gameplay strip (user request: "subway surfer / minecraft parkour gameplay")
`edl.json["gameplay"]`: Subway Surfers (src 3s in), muted, cropped to 1080x620 and composited at y=1300-1920, ABOVE
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

`sfx/cues.json`: 27 cues, 27 distinct sounds (monkey screech, 6-7 snippet, vine boom, bruh,
tung-tung-tung knocks ×3, error glitch, bass drop, record scratch, sparkle, per-checkbox clicks,
wrong buzzer, sheesh, bass hit...). Cue gains were fitted twice: first by the file-loudness
formula, then boosted per cue from a direct measurement of the SFX track against the voice track
(`tool/helpers/check_sfx_direct.py`: 50ms peak of the cue vs the voice in the same 0.8s window; anything
more than 3 dB under the voice was raised to −2 dB, capped at ×4). Final peak −1.79 dBFS (after pass 2) after
loudnorm TP −2 (AAC overshoot leaves ~1 dB headroom).

## Not done / caveats
- The user's script line "Diabolical work" had a `br_diabolical` voice-meme candidate; it is
  deliberately unused (the spoken line already carries it).
- Spoken "Diddy party" / "unalive" are left uncensored in captions (recorded words win; on-screen
  overlay text stays PG-13).
