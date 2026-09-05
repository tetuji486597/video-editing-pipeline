#!/usr/bin/env python3
"""Patch every EDL's output-timeline beat windows onto render.py's real 24fps grid.

render.py extracts each segment with -r 24, so a segment's rendered duration is
ceil(nominal_seconds * 24) / 24 -- NOT the raw (end - start). Summing raw ranges
drifts by up to a frame per segment, cumulatively. ep13's edl.json records the
session where skipping this left every downstream cue 70ms off.

The ceil rule is verified against the actual rendered clips whenever a
clips_draft/ directory is present (--verify), so this stays honest rather than
assumed. Analytic derivation matters for the A/B variants: both write to the same
clips_draft/, so the second render clobbers the first variant's clips and only one
of them could ever be measured directly.

Usage: fix_windows.py <edl.json> [<edl.json> ...] [--write] [--verify]
"""
import json
import math
import subprocess
import sys
from pathlib import Path

FPS = 24


def quantized(nominal):
    return math.ceil(round(nominal * FPS, 6)) / FPS


def probe(p):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout.strip())


def main():
    paths = [Path(a) for a in sys.argv[1:] if not a.startswith("--")]
    write = "--write" in sys.argv
    verify = "--verify" in sys.argv
    bad = 0

    for p in paths:
        edl = json.loads(p.read_text(encoding="utf-8"))
        clips = sorted((p.parent / "clips_draft").glob("seg_*.mp4")) if verify else []
        measurable = len(clips) == len(edl["ranges"])

        windows, t = {}, 0.0
        print(f"\n{p.parent.name}/{p.name}")
        for i, r in enumerate(edl["ranges"]):
            dur = quantized(r["end"] - r["start"])
            windows[r["beat"]] = [round(t, 4), round(t + dur, 4)]
            line = f"  {r['beat']:16s} {t:7.3f} - {t + dur:7.3f}  ({dur:5.3f}s)"
            if measurable:
                actual = probe(clips[i])
                ok = abs(actual - dur) < 0.001
                line += f"   measured {actual:.3f} {'ok' if ok else 'MISMATCH'}"
                if not ok:
                    bad += 1
            print(line)
            t += dur

        if write:
            edl["_beat_windows_output_timeline"] = windows
            edl["total_duration_s"] = round(t, 4)
            edl["_windows_note"] = (
                "Output-timeline windows on render.py's real 24fps extract grid: each "
                "segment's rendered duration is ceil((end-start)*24)/24, not the raw source "
                "span. Verified against rendered clips where measurable. Overlay "
                "start_in_output values are derived from THESE numbers.")
            p.write_text(json.dumps(edl, indent=2), encoding="utf-8")
            print(f"  -> written, total {t:.3f}s")

    if bad:
        sys.exit(f"\n{bad} segment(s) disagreed with the ceil rule -- do not trust these windows")


if __name__ == "__main__":
    main()
