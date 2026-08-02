# video-editing-pipeline

Claude-Code-driven pipeline for producing the "System Design in 60 Seconds" TikTok
episodes: teleprompter talking-head footage in, a graded/captioned/scored vertical
video out.

## Layout

- **`tool/`** — a customized copy of [browser-use/video-use](https://github.com/browser-use/video-use)
  (EDL-based cut/grade/composite/caption renderer). Notable changes on top of upstream:
  - Forces `-c:v libvpx-vp9` on WebM overlay inputs — ffmpeg's default `vp9` decoder
    silently drops alpha, turning transparent HyperFrames overlays into solid black.
  - Real word-by-word caption highlighting (`build_master_ass` / `--caption-format
    ass-karaoke`) instead of ASS `\k` karaoke tags — one Dialogue event per word with
    only the active word color-tagged, avoiding ambiguous sweep-timing semantics.
  - A face-anchored "punch zoom" effect (`--zoom` entries in the EDL) — Ken-Burns-style
    zoom that zooms toward a fixed focal point (the presenter's eyes) rather than the
    frame's geometric center.
  - See `tool/SKILL.md` and `tool/install.md` for daily usage and setup.

- **`episodes/`** — per-episode source configs: the EDL (`edl.json`), the
  [HyperFrames](https://github.com/heygen-com/hyperframes) motion-graphic overlay
  compositions (`animations/<slot>/index.html`), word-level transcripts, SFX sourcing
  notes, and session notes (`project.md`). Raw footage and rendered video/audio output
  are intentionally excluded (regenerate via `tool/helpers/render.py`).
  - `ep1-password/` — "Where Your Password Actually Goes" (hashing/salting/bcrypt)
  - `ep4-captcha/` — "How Sites Know You're Not a Robot" (CAPTCHA/bot-detection)

## Rebuilding an episode

```bash
cd tool && python3 -m venv .venv && .venv/bin/pip install -e .
# then, from an episode's directory (with its own footage + transcripts alongside edl.json):
python3 ../../tool/helpers/render.py edl.json -o preview.mp4 --preview \
  --build-subtitles --caption-format ass-karaoke --caption-margin-v 280
```

Each `animations/<slot>/` composition is rendered separately via the HyperFrames CLI
(`npx hyperframes render --format webm -o render.webm`) before compositing.
