#!/usr/bin/env bash
# Rule 9 gate: refuse to composite if any overlay source is newer than its render.
#
# The failure this prevents is documented in the overlay skill: a sub-agent still
# fixing overlays while the coordinator composites, so a pre-fix render ships and
# nobody notices because the duration matches. It happened on EP6 for real, and it
# nearly happened again on EP18 — the check was RUN but only printed, and the
# composite proceeded past three stale slots.
#
# Usage:  check_fresh.sh <episode-dir>   # exits non-zero if anything is stale
set -u
DIR="${1:-.}"
stale=0
for s in "$DIR"/animations/slot_*; do
  [ -d "$s" ] || continue
  name=$(basename "$s")
  if [ ! -f "$s/render.webm" ]; then
    printf "  MISSING  %-24s no render.webm\n" "$name"; stale=$((stale+1)); continue
  fi
  newer=$(find "$s" \( -name 'index.html' -o -name '*.jpg' -o -name '*.png' \) -newer "$s/render.webm" 2>/dev/null)
  if [ -n "$newer" ]; then
    printf "  STALE    %-24s source newer than render\n" "$name"; stale=$((stale+1))
  else
    printf "  fresh    %-24s\n" "$name"
  fi
done
if [ "$stale" -gt 0 ]; then
  echo
  echo "REFUSING TO COMPOSITE: $stale slot(s) stale. Re-render them first."
  exit 1
fi

# An EDL overlay duration MUST equal its rendered clip length. Shortening the EDL
# value to fix a beat overrun truncates the clip mid-fade -- a hard cut from partial
# opacity to bare footage, which is the rule-12 flash. The only way to shorten an
# overlay is to re-render it shorter.
mismatch=0
for edl in "$DIR"/edl.json "$DIR"/edl_a.json "$DIR"/edl_b.json; do
  [ -f "$edl" ] || continue
  while IFS='|' read -r rel dur; do
    [ -n "$rel" ] || continue
    f="$DIR/$rel"
    [ -f "$f" ] || continue
    real=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
    if awk -v a="$dur" -v b="$real" 'BEGIN{exit !((a-b>0.02)||(b-a>0.02))}'; then
      printf "  MISMATCH %-30s edl=%.3f render=%.3f\n" "$(basename $(dirname $rel))" "$dur" "$real"
      mismatch=$((mismatch+1))
    fi
  done < <(python -c "
import json,sys
d=json.load(open(r'$edl',encoding='utf-8'))
for o in d.get('overlays',[]): print(o['file']+'|'+str(o['duration']))
" 2>/dev/null)
done
if [ "$mismatch" -gt 0 ]; then
  echo
  echo "REFUSING TO COMPOSITE: $mismatch overlay duration(s) do not match their render."
  echo "Shortening an EDL duration truncates the clip mid-fade. Re-render instead."
  exit 1
fi
echo "all slots fresh and durations match - safe to composite"
