#!/usr/bin/env python3
"""Verify, on the RENDERED file, that each overlay's entrance and fade-out are correct.

This is rule 12's core check, and it has to be done on the rendered .webm because the
lint harness has reported a broken fade as working.

Two failures, both of which show up as a flash of bare footage or a black hole:
  ENTRANCE  frame 0 fully transparent  -> the overlay pops in late; on an opaque takeover
            a background-only frame 0 reads as a near-black flash right as the viewer's
            eye was adjusted to a lit face.
  FADE      last frame still opaque    -> the overlay hard-cuts instead of fading, or a
            repeating tween won the final DOM write and stranded content visible.

VP9 keeps alpha in a side channel, so `pix_fmt` reads yuv420p and the stream tag
`alpha_mode=1` is what actually tells you alpha exists. Decoding MUST use
`-c:v libvpx-vp9` or the alpha plane is silently dropped and every file looks opaque.

Usage: check_fade.py <render.webm> [<render.webm> ...]
"""
import re
import subprocess
import sys
from pathlib import Path


def alpha_series(path):
    """Mean alpha (0-255) per frame, in order."""
    # `metadata=print` writes to the log, which `-v error` suppresses -- without an
    # explicit `file=-` this returns nothing and every slot looks unreadable. And the
    # decoder MUST be forced to libvpx-vp9: the default vp9 decoder silently drops the
    # WebM alpha side-channel, so a fade reads as opaque-throughout.
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-c:v", "libvpx-vp9", "-i", str(path),
         "-vf", "alphaextract,signalstats,"
                "metadata=print:key=lavfi.signalstats.YMAX:file=-",
         "-f", "null", "-"],
        capture_output=True, text=True)
    return [float(m) for m in re.findall(r"YMAX=([0-9.]+)", r.stdout + r.stderr)]


def has_alpha(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream_tags=alpha_mode", "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True)
    return r.stdout.strip() == "1"


def main():
    bad = 0
    for arg in sys.argv[1:]:
        p = Path(arg)
        label = f"{p.parent.parent.parent.name}/{p.parent.name}"
        if not p.exists():
            print(f"{label:44s} MISSING"); bad += 1; continue
        if not has_alpha(p):
            print(f"{label:44s} NO ALPHA CHANNEL -- would composite fully opaque"); bad += 1; continue

        a = alpha_series(p)
        if not a:
            print(f"{label:44s} could not read alpha plane"); bad += 1; continue

        first, last = a[0], a[-1]
        peak = max(a)
        flags = []
        # Frame 0 must carry SOME visible content. Measured as max alpha, not mean:
        # a title card is mostly empty canvas, so its mean is near zero even when the
        # element is plainly visible.
        if first <= 1:
            flags.append(f"ENTRANCE frame0 max-alpha={first:.0f} (blank -- pops in late)")
        # A correct zero-buffer fade does NOT reach 0 on the last stored frame: the fade
        # lands exactly on the declared duration, and the last frame sits one frame
        # interval earlier, so a residual is expected and healthy. What we are actually
        # testing for is a HARD CUT -- content still near full strength at the end.
        if last > 0.5 * peak:
            flags.append(f"FADE last={last:.0f} vs peak {peak:.0f} (no fade -- hard cut)")
        # ...and that the tail is genuinely descending rather than flat.
        tail = a[-8:]
        if len(tail) >= 4 and tail[-1] > 0.9 * max(tail):
            flags.append("FADE tail not descending")
        if flags:
            bad += 1
        print(f"{label:44s} n={len(a):3d} frame0={first:6.0f} peak={peak:6.0f} "
              f"last={last:6.0f}  {'  '.join(flags) if flags else 'ok'}")

    print(f"\n{bad} problem(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
