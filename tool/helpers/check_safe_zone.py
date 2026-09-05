#!/usr/bin/env python3
"""Check every overlay's CONTENT against TikTok's UI safe zone.

The y=180/y=1280 band this pipeline enforces protects against the BURNED-IN captions. It
says nothing about TikTok's own chrome, which is drawn over the video at playback:

  - RIGHT: the action rail -- profile bubble, like, comment, bookmark, share, sound disc.
  - BOTTOM: username, caption/description (expands to ~4 lines), sound tag, scrubber.
  - TOP: search icon, Following / For You tabs, device notch.
  - LEFT: a thin margin.

Published figures vary by source and shift with app versions, so two tiers are used
(margins triangulated across checksafe.zone, creamate.ai and kreatli.com):

  DANGER  x >= 900, x <= 60, y >= 1600, y <= 140   every source agrees this is covered
  CAUTION x >= 800, y >= 1400                      some sources; a coin flip across
                                                   devices and app versions

Reports the DEPTH content reaches, not a yes/no, because depth is what is comparable to
the limit and what tells you how much a fix has to move.

Three traps this must not fall into, all three of which produced a worthless audit here
before the tool was right:

  1. Measure COMPOSITED-OVER-BLACK luminance, not raw alpha. VP9 stores colour separately
     from alpha, so a fully transparent region still carries bright colour data.
  2. Judge by DURATION, not peak. A 2-5 frame white shutter flash whitens the ENTIRE frame.
     Any peak-based measure -- and any `cropdetect` pass, which accumulates -- then reports
     every full-screen takeover as a full-frame violation. Only sustained content counts.
  3. Do not average over the whole zone. The action rail is 180px wide; an 81px-deep solid
     white box inside it averages down to nothing against the 99px of empty rail beside it.
     Probe NARROW STRIPS and report the deepest one that is lit.

     The general form, which has now bitten this project three separate ways: A SUMMARY
     STATISTIC OVER A REGION LARGE RELATIVE TO THE FEATURE DILUTES THE FEATURE. Same class
     of error as measuring SFX audibility at 8 kHz when the cue lives above 4 kHz, and as
     using mean rather than max alpha to test a fade. Before trusting any check, ask what
     the statistic averages over and whether the thing being looked for survives it.

Usage: check_safe_zone.py <render.webm> [...]
"""
import re
import subprocess
import sys
from pathlib import Path

W, H = 1080, 1920
BRIGHT = 200        # text/UI-grade luminance, not a background gradient
DIM = 90            # anything readable at all
SUSTAIN = 0.10      # <=10% of frames reads as a transition flash, not placement
STRIP = 30

RIGHT_STRIPS = [(x, STRIP) for x in range(780, W, STRIP)]
LEFT_STRIPS = [(x, STRIP) for x in range(0, 90, STRIP)]


def strip_frac(path, x, w, thresh):
    """Fraction of frames with content above `thresh` in a vertical strip."""
    r = subprocess.run(
        ["ffmpeg", "-v", "error",
         "-f", "lavfi", "-i", f"color=black:s={W}x{H}",
         "-c:v", "libvpx-vp9", "-i", str(path),
         "-filter_complex",
         f"[0:v][1:v]overlay=shortest=1,crop={w}:{H}:{x}:0,signalstats,"
         "metadata=print:key=lavfi.signalstats.YMAX:file=-",
         "-f", "null", "-"], capture_output=True, text=True)
    v = [float(m) for m in re.findall(r"YMAX=([0-9.]+)", r.stdout + r.stderr)]
    if not v:
        return None
    return sum(1 for a in v if a > thresh) / len(v)


def main():
    rail = edge = left = 0
    for arg in sys.argv[1:]:
        p = Path(arg)
        label = f"{p.parent.parent.parent.name}/{p.parent.name}"
        if not p.exists():
            print(f"{label:44s} MISSING")
            continue

        # deepest lit strip on each side, at both thresholds
        deep_bright = deep_dim = None
        for x, w in RIGHT_STRIPS:
            if (f := strip_frac(p, x, w, BRIGHT)) and f > SUSTAIN:
                deep_bright = (x + w, f)
            if (f := strip_frac(p, x, w, DIM)) and f > SUSTAIN:
                deep_dim = (x + w, f)
        left_x = None
        for x, w in LEFT_STRIPS:
            if (f := strip_frac(p, x, w, BRIGHT)) and f > SUSTAIN:
                left_x = (x, f)
                break

        notes = []
        if deep_bright and deep_bright[0] > 900:
            notes.append(f"DANGER text/UI reaches x={deep_bright[0]} "
                         f"({deep_bright[1]*100:.0f}% of frames)")
            rail += 1
        elif deep_dim and deep_dim[0] > 900:
            notes.append(f"dim content only reaches x={deep_dim[0]} (background-grade)")
        elif deep_bright and deep_bright[0] > 860:
            notes.append(f"caution text/UI reaches x={deep_bright[0]} (past the x<=860 target)")
            edge += 1
        if left_x:
            notes.append(f"DANGER text/UI reaches x={left_x[0]} on the left")
            left += 1

        print(f"{label:44s} {'  '.join(notes) if notes else 'clear'}")

    print(f"\n{rail} slot(s) with text/UI in the right rail (x>=900), "
          f"{edge} past the x<=860 target only, {left} in the left margin (x<=60)")
    print("NOTE: this cannot see the burned-in captions -- they are composited later by "
          "ffmpeg.\n      Check those separately; see SAFE_ZONE.md.")


if __name__ == "__main__":
    main()
