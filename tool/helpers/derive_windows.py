#!/usr/bin/env python3
"""Re-derive an EDL's output-timeline beat windows from the ACTUAL rendered segments.

Why this exists: render.py extracts at 24fps and every segment quantizes to that
grid, so a beat window computed by summing (end - start) in the source domain is
wrong by up to a frame per segment and drifts cumulatively. ep13's edl.json records
the case where skipping this put every downstream cue 70ms off.

Also maps source-domain word timestamps into the output timeline (Hard Rule 5:
output_time = word.start - segment_start + segment_offset) so an overlay's key
visual can be landed on the word that states the idea.

Usage:
  derive_windows.py <edl.json> [--write]          # show / patch beat windows
  derive_windows.py <edl.json> --at <src_time>    # map a source time to output
"""
import json
import subprocess
import sys
from pathlib import Path


def probe(p):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout.strip())


def segments(edl_path):
    """Return [(beat, src_start, src_end, out_start, out_end)] from real clip durations."""
    edl = json.loads(edl_path.read_text(encoding="utf-8"))
    d = edl_path.parent
    clips = sorted((d / "clips_draft").glob("seg_*.mp4"))
    if not clips:
        clips = sorted((d / "clips_graded").glob("seg_*.mp4"))
    if len(clips) != len(edl["ranges"]):
        sys.exit(f"{len(clips)} clips vs {len(edl['ranges'])} ranges -- render a draft first")

    out, t = [], 0.0
    for r, c in zip(edl["ranges"], clips):
        dur = probe(c)
        out.append((r["beat"], r["start"], r["end"], t, t + dur))
        t += dur
    return edl, out, t


def main():
    edl_path = Path(sys.argv[1]).resolve()
    edl, segs, total = segments(edl_path)

    if "--at" in sys.argv:
        src = float(sys.argv[sys.argv.index("--at") + 1])
        for beat, ss, se, os_, oe in segs:
            if ss <= src <= se:
                print(f"{src:.3f} (source) -> {src - ss + os_:.3f} (output)   in {beat}")
                return
        sys.exit(f"{src} falls in no kept range")

    print(f"{edl_path.parent.name}/{edl_path.name}   total {total:.3f}s")
    windows = {}
    for beat, ss, se, os_, oe in segs:
        nominal = se - ss
        real = oe - os_
        windows[beat] = [round(os_, 3), round(oe, 3)]
        print(f"  {beat:16s} out {os_:7.3f} - {oe:7.3f}  ({real:5.2f}s)"
              f"   drift {real - nominal:+.3f}")

    if "--write" in sys.argv:
        edl["_beat_windows_output_timeline"] = windows
        edl["_windows_note"] = (
            "Derived from the ACTUAL rendered segment durations (ffprobe on clips_draft), "
            "not from summed source ranges -- render.py extracts at 24fps and each segment "
            "quantizes to that grid.")
        edl["total_duration_s"] = round(total, 3)
        edl_path.write_text(json.dumps(edl, indent=2), encoding="utf-8")
        print("  -> written")


if __name__ == "__main__":
    main()
