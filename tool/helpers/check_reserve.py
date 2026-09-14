#!/usr/bin/env python3
"""Probe a render.webm for CONTENT inside a reserved box (default: the EP30-35 countdown corner
x 670-880, y 195-335). Two criteria: alpha > 8 (transparent compositions) and, for takeovers
whose opaque background legitimately fills the box, luma > 90 after compositing over black
(text/UI/glow). Prints both and a verdict. Usage: check_reserve.py <render.webm> [x0 y0 x1 y1]"""
import subprocess, sys, numpy as np
p = sys.argv[1]; x0, y0, x1, y1 = (int(v) for v in (sys.argv[2:6] or (670, 195, 880, 335)))
b = subprocess.run(["ffmpeg", "-loglevel", "error", "-c:v", "libvpx-vp9", "-i", p, "-vf", f"crop={x1-x0}:{y1-y0}:{x0}:{y0},format=rgba",
                    "-f", "rawvideo", "-pix_fmt", "rgba", "-"], capture_output=True).stdout
w, h = x1 - x0, y1 - y0; n = len(b) // (w * h * 4)
f = np.frombuffer(b[:n * w * h * 4], np.uint8).reshape(n, h, w, 4).astype(np.float32)
a = f[..., 3]; rgb = f[..., :3] * (a[..., None] / 255.0)
luma = 0.2126 * rgb[..., 0] + 0.7152 * rgb[..., 1] + 0.0722 * rgb[..., 2]
opaque = (a.mean(axis=(1, 2)) > 200).mean() > 0.5   # takeover: background fills the box
lit = (luma > 90).sum(axis=(1, 2)) > 12               # >12 px of bright content in a frame
alpha_hit = (a.max(axis=(1, 2)) > 8)
if opaque:
    verdict = "CLEAR (takeover bg only)" if not lit.any() else f"INTRUSION: bright content in {lit.mean()*100:.1f}% of frames, max luma {luma.max():.0f}"
else:
    verdict = "CLEAR" if not alpha_hit.any() else f"INTRUSION: alpha>8 in {alpha_hit.mean()*100:.1f}% of frames"
print(f"{p}: frames {n}  {'takeover' if opaque else 'transparent'}  {verdict}")
