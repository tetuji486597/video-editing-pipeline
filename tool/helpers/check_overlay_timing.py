#!/usr/bin/env python3
"""Audit overlay start times against the beat they belong to.

The failure this catches: an overlay whose content resolves while the presenter is
still on the PREVIOUS beat. EP17 shipped with its hook overlay at 2.800s while the
HOOK beat did not begin until 6.750 -- so a "DECLINED" card and a 40ms figure were
on screen during the series intro. That happened because the no-intro house pattern
(title 0->2.766, hook at 2.800) was applied to an episode that has a recorded intro.

A slot named slot_<beat> is expected to sit inside the beat window whose name it
matches. Ranges are already trimmed to speech, so beat_start IS speech onset.

Rules:
  - an overlay must start AT OR AFTER its beat's start (else it pre-empts the words)
  - it should start ~0.6-2.0s in, so the narration establishes the idea first
  - it should not run past its beat's end by more than ~1.0s

Usage: check_overlay_timing.py <edl.json>
"""
import json, sys, re

# A fixed maximum lead was wrong. An overlay should land its key visual ON the words
# that state the idea, and in a long beat those words can arrive several seconds in --
# EP16's counter overlay ticks 1-2-3 and belongs where he says "one, two, three", not
# 0.8s into the beat. So "late" is judged as a FRACTION of the beat, not in seconds.
LEAD_MIN = 0.25          # below this it fires before the idea is established
LEAD_FRAC_MAX = 0.50     # starting past the beat's halfway point is genuinely late
TAIL_SLACK = 1.0         # how far it may run past its beat's end


def merged_beats(beats):
    """Merge continuation ranges into one window.

    A beat recorded across several takes appears as NEW_COMPONENT / NEW_COMPONENT_B /
    NEW_COMPONENT_C. They are one beat editorially, so an overlay spanning them is
    correct, not an overrun -- treating them separately produced false positives.
    """
    out = {}
    for name, (s, e) in beats.items():
        root = re.sub(r"_[A-Z]$", "", name)
        if root in out:
            out[root] = [min(out[root][0], s), max(out[root][1], e)]
        else:
            out[root] = [s, e]
    return out


def beat_for_slot(name, beats):
    key = re.sub(r"^slot_", "", name).upper()
    return key if key in beats else None


def main():
    d = json.load(open(sys.argv[1], encoding="utf-8"))
    raw = d.get("_beat_windows_output_timeline")
    if not raw:
        print("  no beat windows in EDL"); return
    beats = merged_beats(raw)
    overlays = d.get("overlays", [])
    title_end = next((o["start_in_output"] + o["duration"]
                      for o in overlays if "slot_title" in o["file"]), 0.0)
    problems = 0
    for idx, o in enumerate(overlays):
        name = o["file"].split("/")[1]
        s, dur = o["start_in_output"], o["duration"]
        if name == "slot_title":
            print(f"  {name:22s} {s:7.3f}-{s+dur:7.3f}  (title card, exempt)")
            continue
        # the first content overlay cannot begin before the title card clears, so a
        # large lead there is a structural consequence of the house pattern, not late timing
        blocked_by_title = (s <= title_end + 0.10)
        b = beat_for_slot(name, beats)
        if not b:
            print(f"  {name:22s} {s:7.3f}  ?? no matching beat"); continue
        bs, be = beats[b]
        lead = s - bs
        end_over = (s + dur) - be
        flags = []
        beat_len = be - bs
        if lead < 0:
            flags.append(f"STARTS {-lead:.2f}s BEFORE its beat -- pre-empts the narration")
        elif lead < LEAD_MIN:
            flags.append(f"only {lead:.2f}s lead (want >={LEAD_MIN})")
        elif lead > beat_len * LEAD_FRAC_MAX and not blocked_by_title:
            flags.append(f"starts {100*lead/beat_len:.0f}% into its beat (late)")
        if end_over > TAIL_SLACK:
            flags.append(f"runs {end_over:.2f}s past its beat")
        status = "  ".join(flags) if flags else "ok"
        if flags:
            problems += 1
        print(f"  {name:22s} {s:7.3f}-{s+dur:7.3f}  beat {b} {bs:7.3f}-{be:7.3f}  lead {lead:+6.2f}  {status}")
    print(f"  --> {problems} timing problem(s)" if problems else "  --> all overlays land inside their beat")


if __name__ == "__main__":
    main()
