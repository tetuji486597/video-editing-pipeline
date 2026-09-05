#!/usr/bin/env python3
"""Border-margin audit for overlay renders: text/UI must stay inside x70-870, y200-1280.

Why this exists: TWO separate margin audits by build agents false-passed compositions
whose content sat at the frame's very top-left (EP26 slot_hook at y~28, then EP26
slot_payoff at y~30 — the same collapsed-layout bug, missed twice). This script is the
authoritative check and it runs on RENDERED PIXELS:

- decodes with -c:v libvpx-vp9 (the default decoder silently drops the alpha plane),
- composites over black (VP9 keeps colour where alpha=0; raw colour reads lie),
- flags UI-grade content (luma > 120) outside the band, but only where it PERSISTS
  (>8% of frames) — 2-5 frame shutter flashes are a legitimate technique,
- reports the worst offending extents and the persistence so a human can judge.

Exemptions must be judged by eye: full-bleed photos / #bg-fill gradients may cross the
band. Anything that reads as text, chip, line-work or icon may not.

Usage: check_margins.py <render.webm> [...]
"""
import subprocess, sys
import numpy as np

W, H = 1080, 1920
X0, X1, Y0, Y1 = 70, 870, 200, 1280
LUMA, PERSIST = 120, 0.08


def audit(path):
    p = subprocess.run(
        ["ffmpeg", "-v", "error", "-c:v", "libvpx-vp9", "-i", path,
         "-filter_complex",
         f"color=black:s={W}x{H}:r=24[bg];[bg][0:v]overlay=shortest=1,format=gray",
         "-f", "rawvideo", "-"], capture_output=True)
    a = np.frombuffer(p.stdout, dtype=np.uint8)
    n = len(a) // (W * H)
    if n == 0:
        print(f"  {path}: DECODE FAILED")
        return True
    fr = a[:n * W * H].reshape(n, H, W)
    bright = fr > LUMA
    persist = bright.mean(axis=0)          # fraction of frames each pixel is lit
    hot = persist > PERSIST
    bad = False
    for name, mask in (("top y<%d" % Y0, hot[:Y0, :]),
                       ("bottom y>%d" % Y1, hot[Y1:, :]),
                       ("left x<%d" % X0, hot[:, :X0]),
                       ("right x>%d" % X1, hot[:, X1:])):
        if mask.any():
            ys, xs = np.where(mask)
            off = {"top": (0, 0), "bottom": (Y1, 0), "left": (0, 0), "right": (0, X1)}[name.split()[0]]
            worst = float(persist[:Y0, :].max() if name.startswith("top") else
                          persist[Y1:, :].max() if name.startswith("bottom") else
                          persist[:, :X0].max() if name.startswith("left") else
                          persist[:, X1:].max())
            print(f"  BREACH {name}: x {xs.min()+off[1]}-{xs.max()+off[1]} "
                  f"y {ys.min()+off[0]}-{ys.max()+off[0]}  persistence {worst:.0%}")
            bad = True
    if not bad:
        print("  clear")
    return bad


def main():
    any_bad = False
    for path in sys.argv[1:]:
        print(path)
        any_bad |= audit(path)
    sys.exit(1 if any_bad else 0)


if __name__ == "__main__":
    main()
