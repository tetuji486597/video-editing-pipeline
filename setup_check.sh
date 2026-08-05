#!/usr/bin/env bash
# Reports what's missing to edit episodes in this repo on a fresh machine.
# Run this after cloning, before attempting any edit. Exits 0 even if things
# are missing — it's a report, not a gate.

set -u
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ok=0; warn=0; missing=0

pass() { printf "  \033[32m✓\033[0m %s\n" "$1"; ok=$((ok+1)); }
fail() { printf "  \033[31m✗\033[0m %s\n" "$1"; missing=$((missing+1)); }
note() { printf "  \033[33m!\033[0m %s\n" "$1"; warn=$((warn+1)); }

echo "== python + tool/ venv =="
if command -v python3 >/dev/null; then
  pass "python3 found ($(python3 --version 2>&1))"
else
  fail "python3 not found — install it (e.g. brew install python)"
fi
if [ -d "$REPO_ROOT/tool/.venv" ]; then
  pass "tool/.venv already set up"
else
  note "tool/.venv missing — run: cd tool && python3 -m venv .venv && .venv/bin/pip install -e ."
fi

echo
echo "== ffmpeg (must have libass for captions) =="
FFMPEG_BIN="$(command -v ffmpeg || true)"
if [ -z "$FFMPEG_BIN" ]; then
  fail "ffmpeg not found on PATH — install it (e.g. brew install ffmpeg)"
else
  if ffmpeg -version 2>&1 | grep -q "enable-libass"; then
    pass "ffmpeg has libass ($FFMPEG_BIN) — subtitles filter will work"
  else
    fail "ffmpeg at $FFMPEG_BIN was NOT built with --enable-libass — the 'subtitles' filter does not exist with this build, captions will silently fail to burn in"
    if [ -x "/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg" ]; then
      note "found /opt/homebrew/opt/ffmpeg-full/bin/ffmpeg — prioritize it on PATH: export PATH=\"/opt/homebrew/opt/ffmpeg-full/bin:\$PATH\""
    else
      note "on macOS, try: brew install ffmpeg-full  (or any ffmpeg build with --enable-libass)"
    fi
  fi
fi

echo
echo "== Node / HyperFrames CLI =="
if command -v node >/dev/null; then
  pass "node found ($(node --version))"
  if command -v npx >/dev/null; then
    pass "npx found — HyperFrames CLI installs on first use (needs internet, fetches Google Fonts too)"
  else
    fail "npx not found — reinstall Node (npx ships with it)"
  fi
else
  fail "node not found — install Node.js (HyperFrames renders won't run without it)"
fi

echo
echo "== Secrets (intentionally excluded from git) =="
if [ -f "$REPO_ROOT/tool/.env" ] && grep -q "ELEVENLABS_API_KEY=.\+" "$REPO_ROOT/tool/.env" 2>/dev/null; then
  pass "tool/.env has an ElevenLabs key"
else
  note "no ElevenLabs API key set — only needed if transcribing NEW footage (EP1/EP4 transcripts are already committed under episodes/*/transcripts/). Add one to tool/.env as ELEVENLABS_API_KEY=..."
fi

echo
echo "== system-design-overlays skill (must be registered locally, git doesn't do this) =="
SKILL_SRC="$REPO_ROOT/skills/system-design-overlays/SKILL.md"
SKILL_DST="$HOME/.claude/skills/system-design-overlays/SKILL.md"
if [ -f "$SKILL_DST" ] && diff -q "$SKILL_SRC" "$SKILL_DST" >/dev/null 2>&1; then
  pass "system-design-overlays skill registered and matches this repo's copy"
elif [ -f "$SKILL_DST" ]; then
  note "system-design-overlays skill is registered but OUT OF DATE vs this repo — re-copy: mkdir -p ~/.claude/skills/system-design-overlays && cp \"$SKILL_SRC\" \"$SKILL_DST\""
else
  note "system-design-overlays skill not registered — Claude Code can't load it via the Skill tool until it's copied into ~/.claude/skills/: mkdir -p ~/.claude/skills/system-design-overlays && cp \"$SKILL_SRC\" \"$SKILL_DST\""
fi

echo
echo "== Optional: media-use / HeyGen (only needed to source new stock images/music) =="
if command -v heygen >/dev/null; then
  pass "heygen CLI found"
else
  note "heygen CLI not found — only needed if sourcing new stock photos/BGM via the media-use skill"
fi

echo
echo "== Optional: gh CLI (only needed to push changes back to GitHub) =="
if command -v gh >/dev/null && gh auth status >/dev/null 2>&1; then
  pass "gh CLI authenticated"
else
  note "gh not installed or not authenticated — only needed to push"
fi

echo
echo "-------------------------------------------"
echo "$ok ok, $warn to review, $missing missing"
if [ "$missing" -gt 0 ]; then
  echo "Fix the ✗ items above before rendering."
fi
