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
   transcripts committed).
3. Read `STYLE.md` before making any editorial decision (title/caption placement,
   music/SFX choices, overlay design, zoom behavior) — it's the confirmed-good defaults
   for this series, not a starting guess.

## Daily editing

Read `tool/SKILL.md` for the render workflow and `tool/helpers/` for the actual scripts.
Each episode under `episodes/` has its own `project.md` with reasoning/decisions specific
to that episode — read it before changing that episode's edit.
