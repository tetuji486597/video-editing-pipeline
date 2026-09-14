# video-editing-pipeline — agent instructions

This repo is a portable copy of the "System Design in 60 Seconds" editing setup — see
`README.md` for the layout (`tool/` = customized video-use, `episodes/` = per-episode
EDL + HyperFrames configs).

## On first use in a session (fresh clone, or any time you're unsure the environment is set up)

1. Run `./setup_check.sh` from the repo root and report the results to the user before
   attempting any render. It checks for the things that don't travel via git: the
   `tool/.venv`, an `ffmpeg` build with libass (captions silently fail without it — this
   has bitten this project before), Node/npx for the HyperFrames CLI, and the
   ElevenLabs/HeyGen credentials (intentionally excluded from git).
2. Walk the user through fixing anything marked missing (✗) — don't just report and
   stop. Warnings (!) are only blocking if the task actually needs that piece (e.g. the
   ElevenLabs key only matters if transcribing new footage; EP1/EP4 already have
   transcripts committed). This includes registering the `system-design-overlays` skill
   into `~/.claude/skills/` if `setup_check.sh` reports it missing or out of date — git
   does not populate that directory, so a fresh clone never has it registered until this
   copy step runs.
3. Read `LESSONS_EP20-26.md`, `LESSONS_EP27-29.md` and `LESSONS_EP30-35.md` — the hard-won rules from the EP20-26 batch (border
   margins x70-870/y200-1280, graphics-never-block-text, centered title stickers,
   SFX variety expectations, the seek-renderer fromTo trap, the frozen-`iw` crop trap,
   the audio chain traps). These came from direct user feedback; re-breaking them
   costs a full batch re-render.
4. Read `WRITING_RULES.md` before writing or rewriting ANY script or on-screen text — the
   de-AI rules (no "it's not X, it's Y", no em dashes in narration, no rules of three,
   no slogan payoffs). Direct user feedback; applied across the whole script doc.
5. Read `STYLE.md` before making any editorial decision (title/caption placement,
   music/SFX choices, overlay design, zoom behavior) — it's the confirmed-good defaults
   for this series, not a starting guess.
6. **Before building or regenerating any episode's overlays specifically**, load the
   `system-design-overlays` skill (via the Skill tool, once registered per step 2) and
   read `episodes/ep4-captcha/animations/slot_new_component/` and `slot_problem/` — EP4
   is the confirmed gold-standard reference for overlay presentation and pacing, cited
   directly in the skill. Read the source, not just the skill's summary of it.

## Daily editing

Read `tool/SKILL.md` for the render workflow and `tool/helpers/` for the actual scripts.
Each episode under `episodes/` has its own `project.md` with reasoning/decisions specific
to that episode — read it before changing that episode's edit.
