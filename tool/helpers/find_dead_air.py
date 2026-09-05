#!/usr/bin/env python3
"""Find dead air RELATIVE to each file's own speech level.

Why not silencedetect: it takes an ABSOLUTE dB threshold. Room tone varies hugely
between shooting locations, and render.py's loudnorm pass amplifies whatever floor
exists. On the EP14-19 shoot the "silence" sits at -35..-44 dB while speech is at
-13 dB -- so a -34 dB silencedetect finds NOTHING while a viewer plainly hears four
seconds of nothing. That is exactly how a 4.4s hole shipped in EP18.

Why not the transcript: ElevenLabs Scribe pads word boxes. EP18's hook has
So[72.04] ... you[76.43] where "So" is boxed as a 4.4-second word, so a
next.start - prev.end gap check reads ~0 and misses it. EP19's intro had the same
shape at a range edge.

This measures short-window RMS, establishes the file's own speech level from the
loud half of the distribution, and reports every stretch sitting a long way under it.

Usage: find_dead_air.py <media> [min_seconds] [drop_db]
"""
import subprocess, sys, re

WIN = 0.10  # seconds per RMS window


def rms_windows(path):
    out = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", path, "-af",
         f"astats=metadata=1:reset={max(1,int(WIN*100))},ametadata=print:key=lavfi.astats.Overall.RMS_level",
         "-f", "null", "-"],
        capture_output=True, text=True).stderr
    vals, t = [], []
    cur_t = None
    for line in out.splitlines():
        m = re.search(r"pts_time:([0-9.]+)", line)
        if m:
            cur_t = float(m.group(1)); continue
        m = re.search(r"RMS_level=(-?[0-9.]+|-inf)", line)
        if m and cur_t is not None:
            v = m.group(1)
            vals.append(-120.0 if v == "-inf" else float(v))
            t.append(cur_t); cur_t = None
    return t, vals


def main():
    path = sys.argv[1]
    min_s = float(sys.argv[2]) if len(sys.argv) > 2 else 0.7
    drop = float(sys.argv[3]) if len(sys.argv) > 3 else 18.0

    t, v = rms_windows(path)
    if not v:
        print("  (no RMS data)"); return

    # the file's own speech level = median of its louder half
    s = sorted(v)
    speech = s[int(len(s) * 0.75)]
    floor = speech - drop

    runs, start = [], None
    for i, x in enumerate(v):
        if x < floor and start is None:
            start = t[i]
        elif x >= floor and start is not None:
            if t[i] - start >= min_s:
                runs.append((start, t[i]))
            start = None
    if start is not None and t[-1] - start >= min_s:
        runs.append((start, t[-1]))

    print(f"  speech level {speech:.1f} dB | flagging stretches below {floor:.1f} dB for >={min_s}s")
    if not runs:
        print("  CLEAN - no dead air"); return
    total = sum(b - a for a, b in runs)
    for a, b in runs:
        print(f"    DEAD  {a:7.2f} - {b:7.2f}   ({b-a:.2f}s)")
    print(f"  {len(runs)} stretch(es), {total:.2f}s total")


if __name__ == "__main__":
    main()
