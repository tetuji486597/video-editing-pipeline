#!/usr/bin/env python3
"""Verify every overlay an EDL references actually exists and matches its declared duration.

Three failures this catches, all of which render a technically-valid video with a silently
wrong overlay:
  1. A missing render.webm -- render.py composites what it can and carries on.
  2. A render whose real duration differs from the EDL's `duration`. The EDL value drives
     the enable-window, so a short render leaves bare footage at the tail of the window and
     a long one gets cut off mid-animation, including its fade-out.
  3. A stale render.webm older than its own index.html -- the fix exists in source but was
     never rendered, so it is not in the shipped video (rule 9).

Usage: check_overlay_files.py <edl.json> [<edl.json> ...]
"""
import json
import subprocess
import sys
from pathlib import Path

TOL = 0.005


def probe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None


def main():
    problems = 0
    for arg in sys.argv[1:]:
        p = Path(arg).resolve()
        edl = json.loads(p.read_text(encoding="utf-8"))
        d = p.parent
        print(f"\n{d.name}/{p.name}")
        for o in edl.get("overlays", []):
            f = d / o["file"]
            name = o["file"].split("/")[-2] if "/" in o["file"] else o["file"]
            if not f.exists():
                print(f"  {name:22s} MISSING  {o['file']}")
                problems += 1
                continue
            actual = probe(f)
            declared = o["duration"]
            src = f.parent / "index.html"
            stale = src.exists() and src.stat().st_mtime > f.stat().st_mtime
            flags = []
            if actual is None:
                flags.append("UNREADABLE")
            elif abs(actual - declared) > TOL:
                flags.append(f"DURATION {actual:.3f} != {declared:.3f}")
            if stale:
                flags.append("STALE (index.html newer than render.webm)")
            status = "  ".join(flags) if flags else "ok"
            if flags:
                problems += 1
            print(f"  {name:22s} decl {declared:6.3f}  actual "
                  f"{actual if actual is None else f'{actual:6.3f}'}  {status}")

    print(f"\n{problems} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
