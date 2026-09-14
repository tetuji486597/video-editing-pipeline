#!/usr/bin/env bash
# Render a HyperFrames slot through a machine-wide queue (max $HF_SLOTS concurrent, default 2).
# Why: EP27-29 takeover renders exit 255 at frame ~345 whenever 3+ renders (or a render plus a
# composite) run at once. Builders working in parallel must call THIS instead of npx directly.
# Usage: hf_render.sh <slot_dir>     (blocks until a queue slot is free, retries once on failure)
set -u
SLOT_DIR="$1"; MAX="${HF_SLOTS:-2}"
LOCKROOT="$(cd "$(dirname "$0")/../.." && pwd)/.hf_locks"; mkdir -p "$LOCKROOT"
got=""
while [ -z "$got" ]; do
  for i in $(seq 1 "$MAX"); do
    L="$LOCKROOT/slot$i"
    # stale lock: older than 40 minutes
    if [ -d "$L" ] && [ -n "$(find "$L" -maxdepth 0 -mmin +40 2>/dev/null)" ]; then rmdir "$L" 2>/dev/null; fi
    if mkdir "$L" 2>/dev/null; then got="$L"; break; fi
  done
  [ -z "$got" ] && sleep 15
done
trap 'rmdir "$got" 2>/dev/null' EXIT
cd "$SLOT_DIR" || exit 2
rm -rf .render.hf-transaction-* 2>/dev/null
for attempt in 1 2; do
  npx --yes hyperframes@0.7.68 render . --format webm -o render.webm --workers 1 --no-browser-gpu > render.log 2>&1
  rc=$?
  if [ $rc -eq 0 ] && [ -f render.webm ]; then tail -2 render.log; exit 0; fi
  echo "render attempt $attempt failed (rc=$rc) in $SLOT_DIR"; tail -3 render.log; sleep 10
done
exit 1
