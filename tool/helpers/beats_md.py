#!/usr/bin/env python3
"""Write episodes/<ep>/beats.md: every spoken word of every range in OUTPUT-timeline seconds.
word_out = word.start - range.start + window.start (Hard Rule 5), windows from fix_windows.py.
Overlay builders read this to land visuals on words. Usage: beats_md.py <episode-dir>"""
import json, sys, os
ep = sys.argv[1]
edl = json.load(open(os.path.join(ep, "edl.json"), encoding="utf-8"))
wins = edl.get("_beat_windows_output_timeline") or {}
out = ["# Beats -- output-timeline word times", "",
       "Columns: out start / out end (ASR box end, an upper bound) / word. Windows from fix_windows.py.", ""]
total = 0.0
for i, r in enumerate(edl["ranges"]):
    src = r["source"]; tr = json.load(open(os.path.join(ep, "transcripts", src + ".json"), encoding="utf-8"))
    words = [w for w in tr["words"] if w.get("type", "word") == "word" and r["start"] <= w["start"] < r["end"]]
    w = wins.get(r["beat"]) if isinstance(wins, dict) else None
    w0 = (w[0] if isinstance(w, list) else w.get("start")) if w else total  # fix_windows writes {beat: [start, end]}
    dur = r["end"] - r["start"]
    out.append(f"## {r['beat']}  -- output {w0:.3f} -> {w0 + dur:.3f} ({dur:.2f}s)  source {r['start']:.2f} -> {r['end']:.2f}")
    out.append(""); out.append("| out start | out end | word |"); out.append("|---|---|---|")
    for w in words:
        out.append(f"| {w['start'] - r['start'] + w0:.2f} | {min(w['end'], r['end']) - r['start'] + w0:.2f} | {w['text']} |")
    out.append("")
    total = w0 + dur
open(os.path.join(ep, "beats.md"), "w", encoding="utf-8").write("\n".join(out))
print("wrote", os.path.join(ep, "beats.md"), f"({len(edl['ranges'])} ranges, ends {total:.3f}s)")
