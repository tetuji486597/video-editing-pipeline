# EP4 — How Sites Know You're Not a Robot (video-use edit)

## Session 1 — 2026-08-01

**Strategy:** Stitched from TWO source recordings — `Teleprompter-2026-07-07_21-49-20.mp4` (HOOK/PROBLEM/BUILD/NEW_COMPONENT) and `Teleprompter-2026-07-07_21-53-04.mp4` (AI_ANGLE/PAYOFF_NEXT) — same sitting, same shirt/lighting, the cross-file cut is visually and audibly seamless. Gordon initially pointed me at the second file alone; it only contained the back half of the script, so I flagged the gap and he supplied the first file's name. Total runtime 68.1s (script's own "~45s" estimate undershoots — the takes themselves just run long).

**Visual metaphor (researched):** a security-checkpoint / two-way-mirror thread — bots swarm a signup form; an unseen "bouncer" watches behavioral signals before anyone's stopped; suspicious visitors get an ID check (CAPTCHA) that secretly generates AI training data; the arms race is forgers (AI) getting better, so defenses shift to behavior; the payoff returns to the two-way mirror, revealing the viewer was also the teacher. 2 full-canvas beats (problem, new_component — the episode's core "wait, I'm training AI?" reveal), 5 bottom-band accents (title, hook, build, ai_angle, payoff).

**Decisions:**
- Reused the bold cinematic grade recipe and the ASS word-highlight caption approach from EP1 (this episode is the second use of both, no changes needed).
- Fresh trap-style BGM track (different from EP1's, same genre/style per Gordon's direction) via `media-use`.
- Trending SFX again (per Gordon's "yes, same as EP1"): Mind Blown (hook twist), Danger Siren (bots attacking), Robotic Beep (invisible detection), Camera Shutter (CAPTCHA/ID-check reveal), Over 9000 (arms-race escalation joke), Correct Answer ding (reused motif, resolution). Full reference in `sfx/SFX_NOTES.md`.
- All 7 overlays built with real `media-use`-sourced photos: ant/insect swarm + login-form screenshot (problem), fingerprint macro (build), traffic-light + crosswalk aerial photos (new_component — the CAPTCHA grid), stop-sign photo with a CV bounding-box HUD (ai_angle), two-way-mirror/glass photo (payoff).

**Reasoning log:**
- Same transcript-alias-mismatch bug as EP1 hit again immediately (EDL used "EP4A"/"EP4B" aliases, transcripts were named after the raw filenames) — same fix (copy to match alias). This is clearly a recurring gotcha for any multi-source EDL; worth remembering to set the EDL source alias to match a transcript rename *up front* next time, not just after zero captions show up.
- Two of five overlay sub-agents (`problem`, `new_component`) independently flagged what they believed was a genuine local VP9-alpha-encoder limitation — content failing to fade to true transparency near the end of their clips, based on their own pixel/alpha inspection. Both were **false alarms**: verified directly by re-decoding with the already-known-correct method (`-c:v libvpx-vp9` forced on the input) and confirmed both clips fade to real transparency exactly as authored. The sub-agents' own ad hoc alpha checks were (most likely) using the default decoder, which — as established in EP1 — always reports fully opaque regardless of actual alpha data. Lesson: don't trust a sub-agent's own alpha/transparency diagnosis unless it explicitly used the `libvpx-vp9`-forced decode path; re-verify centrally before treating it as a real bug.
- One sub-agent (`ai_angle`) reported that a `feTurbulence` dither overlay — the "cheap insurance against VP9 banding" trick from EP1 — rendered as a solid visible gray block instead of a subtle 4%-opacity texture, and removed it rather than fight the artifact. Confirms this trick is not universally reliable; treat it as "try it, verify the actual rendered frame, remove if it doesn't survive" rather than a guaranteed fix.

**Outstanding:**
- Same standing caveat: music and SFX levels are estimated, not confirmed by ear.
- Deliverable: `/Users/gordon.jin/Downloads/edit_ep4/preview_final.mp4` — `--preview` quality. Final CRF-20 pass pending sign-off.
