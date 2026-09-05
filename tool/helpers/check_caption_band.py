#!/usr/bin/env python3
"""Measure what each overlay actually puts behind the burned-in caption band.

Two distinct failures live in this band, and neither is a *collision*, so none of the
geometry rules catch either one:

  1. STRAY INK -- a non-takeover overlay leaking graphics below y=1280. The usual cause
     is an SVG <filter> region: it defaults to x=-10% y=-10% width=120% height=120%, and
     `feTurbulence` is a GENERATOR that fills the whole region regardless of input, so a
     panel-confined grain layer paints ~20% past its element on every side. Confirmed
     real this batch: a panel grain painted noise down to y=1331, inside the band.
  2. A BRIGHT WASH -- captions are white with a black outline and an amber highlight
     word, designed for dark footage. A light region behind them drops the amber word to
     the worst contrast in the series. A full-screen takeover legitimately covers this
     band; it just has to stay DARK.

Measures max alpha and peak luminance inside y=1306-1570 across sampled frames, decoding
with libvpx-vp9 so the alpha side-channel is not dropped.

Usage: check_caption_band.py <render.webm> [...]
"""
import re
import subprocess
import sys
from pathlib import Path

TOP, HEIGHT = 1306, 264
ALPHA_STRAY = 8      # above this, the overlay is really painting in the band
LUMA_BRIGHT = 70     # above this, it is washing the band light


def probe_alpha(path):
    """Max alpha in the band -- how much the overlay paints there at all."""
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-c:v", "libvpx-vp9", "-i", str(path),
         "-vf", f"crop=1080:{HEIGHT}:0:{TOP},alphaextract,signalstats,"
                "metadata=print:key=lavfi.signalstats.YMAX:file=-",
         "-f", "null", "-"], capture_output=True, text=True)
    return [float(m) for m in re.findall(r"YMAX=([0-9.]+)", r.stdout + r.stderr)]


def probe_composited_luma(path):
    """Peak luminance the overlay actually CONTRIBUTES, by compositing it over black.

    Measuring the colour plane directly is meaningless here: VP9 stores colour and alpha
    separately, so fully-transparent regions still carry arbitrary (often bright) colour
    values. A transparent overlay would report luma ~250 and look like a bright wash when
    it paints nothing at all. Compositing over black weights colour by alpha, which is
    exactly what the burned-in captions will sit on top of.
    """
    r = subprocess.run(
        ["ffmpeg", "-v", "error",
         "-f", "lavfi", "-i", f"color=black:s=1080x{HEIGHT}",
         "-c:v", "libvpx-vp9", "-i", str(path),
         "-filter_complex",
         f"[1:v]crop=1080:{HEIGHT}:0:{TOP}[ov];[0:v][ov]overlay=shortest=1,"
         "signalstats,metadata=print:key=lavfi.signalstats.YMAX:file=-",
         "-f", "null", "-"], capture_output=True, text=True)
    return [float(m) for m in re.findall(r"YMAX=([0-9.]+)", r.stdout + r.stderr)]


def main():
    bad = 0
    for arg in sys.argv[1:]:
        p = Path(arg)
        label = f"{p.parent.parent.parent.name}/{p.parent.name}"
        if not p.exists():
            print(f"{label:44s} MISSING"); bad += 1; continue

        alphas = probe_alpha(p)
        lumas = probe_composited_luma(p)

        if not alphas or not lumas:
            print(f"{label:44s} unreadable"); bad += 1; continue

        a, y = max(alphas), max(lumas)
        # A 2-frame white shutter flash is EP4's own gold-standard transition technique
        # and legitimately whites out the whole frame, band included. A sustained bright
        # wash is the actual defect. Distinguish them by how long it lasts, not by peak.
        n_bright = sum(1 for v in lumas if v > LUMA_BRIGHT)
        frac = n_bright / len(lumas)

        flags = []
        if a > ALPHA_STRAY and frac > 0.10:
            flags.append(f"BRIGHT WASH behind captions -- luma {y:.0f} on "
                         f"{frac*100:.0f}% of frames")
        elif a > ALPHA_STRAY and n_bright:
            flags.append(f"brief bright peak (luma {y:.0f}, {n_bright}/{len(lumas)} "
                         "frames) -- reads as a shutter flash, ok")
        if any("WASH" in f for f in flags):
            bad += 1
        print(f"{label:44s} alpha_max={a:5.0f}  luma_max={y:5.0f}  "
              f"bright={n_bright:3d}/{len(lumas):3d}  "
              f"{'  '.join(flags) if flags else 'clear'}")

    print(f"\n{bad} slot(s) with a sustained bright wash behind the captions")


if __name__ == "__main__":
    main()
