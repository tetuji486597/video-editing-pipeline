#!/usr/bin/env python3
"""Render the "in 30 seconds" countdown chip as a small VP9-alpha webm.

EP30-35 gag (user request): the intro promises "in 30 seconds", the episode takes
longer, so a timer counts down from 30 to 0 over the WHOLE remaining video --
i.e. it runs slow. Displayed value = ceil(30 * (1 - (t - t0) / (T - t0))): 30 at t0,
0 exactly at the last frame. A thin ring drains continuously so the slowness is visible.

The chip is a TikTok-sticker-style white rounded box (matches the title boxes) with a
small clock glyph and bold digits, rendered at its own size (CHIP_W x CHIP_H) so the
webm is tiny; render.py places it with the overlay entry's "x"/"y".

Usage: make_countdown.py <out.webm> <duration_seconds> [--fps 30] [--from 30]
  The webm runs from 0 to duration; start it at t0 via start_in_output in the EDL.
"""
import sys, os, math, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont

CHIP_W, CHIP_H = 180, 100
FONTS = [r"C:\Windows\Fonts\ariblk.ttf", r"C:\Windows\Fonts\arialbd.ttf",
         "/System/Library/Fonts/Supplemental/Arial Black.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]


def font(size):
    for p in FONTS:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def frame(value_shown, frac_left, f_big):
    S = 2  # supersample for clean edges
    W, H = CHIP_W * S, CHIP_H * S
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # soft shadow
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([6 * S, 8 * S, W - 6 * S, H - 4 * S], radius=16 * S, fill=(0, 0, 0, 70))
    im.alpha_composite(sh)
    d.rounded_rectangle([6 * S, 6 * S, W - 6 * S, H - 6 * S], radius=16 * S, fill=(255, 255, 255, 255))
    # clock glyph: ring that drains clockwise
    cx, cy, r = 38 * S, CHIP_H * S // 2, 22 * S
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(200, 200, 200, 255), width=5 * S)
    if frac_left > 0:
        d.arc([cx - r, cy - r, cx + r, cy + r], start=-90, end=-90 + 360 * frac_left, fill=(17, 17, 17, 255), width=5 * S)
    d.ellipse([cx - 3 * S, cy - 3 * S, cx + 3 * S, cy + 3 * S], fill=(17, 17, 17, 255))
    ang = -90 + 360 * (1 - frac_left)
    hx = cx + int((r - 8 * S) * math.cos(math.radians(ang)))
    hy = cy + int((r - 8 * S) * math.sin(math.radians(ang)))
    d.line([cx, cy, hx, hy], fill=(17, 17, 17, 255), width=4 * S)
    # digits
    txt = str(value_shown)
    bbox = d.textbbox((0, 0), txt, font=f_big)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = 72 * S + (CHIP_W * S - 72 * S - 14 * S - tw) // 2 - bbox[0]
    ty = (H - th) // 2 - bbox[1] - 2 * S
    d.text((tx, ty), txt, font=f_big, fill=(17, 17, 17, 255))
    return im.resize((CHIP_W, CHIP_H), Image.LANCZOS)


def main():
    out = sys.argv[1]
    T = float(sys.argv[2])
    fps = int(sys.argv[sys.argv.index("--fps") + 1]) if "--fps" in sys.argv else 30
    start_val = int(sys.argv[sys.argv.index("--from") + 1]) if "--from" in sys.argv else 30
    f_big = font(int(46 * 2))
    n = int(round(T * fps))
    tmp = tempfile.mkdtemp(prefix="countdown_")
    cache = {}
    for i in range(n):
        t = i / fps
        frac_left = max(0.0, 1 - t / T)
        shown = math.ceil(start_val * frac_left - 1e-9)
        key = (shown, round(frac_left, 3))
        if key not in cache:
            cache[key] = frame(shown, frac_left, f_big)
        cache[key].save(os.path.join(tmp, f"f{i:05d}.png"))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", os.path.join(tmp, "f%05d.png"),
                    "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-b:v", "0", "-crf", "20", "-deadline", "good",
                    "-cpu-used", "4", "-auto-alt-ref", "0", out], check=True)
    for f in os.listdir(tmp):
        os.remove(os.path.join(tmp, f))
    os.rmdir(tmp)
    print(f"wrote {out}: {n} frames @ {fps}fps, {start_val} -> 0 over {T:.2f}s, chip {CHIP_W}x{CHIP_H}")


if __name__ == "__main__":
    main()
