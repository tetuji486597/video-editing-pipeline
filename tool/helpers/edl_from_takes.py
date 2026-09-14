#!/usr/bin/env python3
"""Build an episode EDL from a take spec, measuring every cut edge acoustically.

Why: EP27-29's EDLs were hand-measured range by range (acoustic onset vs ASR start,
acoustic end vs padded ASR box). That is the right method and it is mechanical, so
this does it for a whole episode at once and writes the same edl.json shape
(ranges with quote/reason/zoom, alternating slow zoom about the eye line).

Spec (JSON):
  {"episode": "ep30-abtesting", "source_key": "ep30",
   "source": "C:/.../Teleprompter-....mp4", "transcript": "transcripts/ep30.json",
   "focal": [540, 730], "zoom": 1.08,
   "takes": [ {"beat": "INTRO", "first": 1.92, "last": 3.74},  ... ] }

`first` = ASR start of the first kept word (or a time just before it); `last` = ASR
start of the LAST kept word (any time inside that word works). The script:
  - snaps `first` to the word whose box contains/starts at it, then finds the acoustic
    onset searching back up to 0.6s from the ASR start (RMS rising through floor+8 dB),
    start = onset - PRE (0.12s), never earlier than the previous speech tail.
  - finds the last word, then the acoustic END: first 120ms stretch below the threshold
    after the ASR box start, capped at box end + 0.7s (sighs/throat-clears after a take
    are excluded by the cap), end = tail + POST (0.12s).
Writes episodes/<ep>/edl.json and prints the range table. Run fix_windows.py --write
afterwards to stamp the output-timeline beat windows, then beats_md.py for beats.md.

Usage: edl_from_takes.py <spec.json> [--grade '<ffmpeg filter>']
"""
import json, subprocess, sys, os
import numpy as np

SR = 8000
WIN = 0.02
PRE, POST = 0.12, 0.12
GRADE = ("eq=contrast=1.15:saturation=1.05,colorbalance=rs=-0.04:gs=0.02:bs=0.05:rm=0.01:gm=0.0:"
         "bm=-0.01:rh=0.06:gh=0.02:bh=-0.06,vignette=angle=0.7,unsharp=5:5")


def rms_env(path):
    b = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-vn", "-ac", "1", "-ar", str(SR),
                        "-f", "f32le", "-"], capture_output=True).stdout
    a = np.frombuffer(b, np.float32)
    n = int(WIN * SR)
    m = len(a) // n
    env = 20 * np.log10(np.sqrt(np.mean(a[:m * n].reshape(m, n) ** 2, axis=1)) + 1e-9)
    return env


def main():
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    grade = GRADE
    if "--grade" in sys.argv:
        grade = sys.argv[sys.argv.index("--grade") + 1]
    ep_dir = os.path.join("episodes", spec["episode"])
    tr = json.load(open(os.path.join(ep_dir, spec["transcript"]), encoding="utf-8"))
    words = [w for w in tr["words"] if w.get("type", "word") == "word"]
    env = rms_env(spec["source"])
    speech = np.percentile(env[env > -80], 85)
    floor = np.percentile(env[env > -80], 20)
    thr = floor + 8.0
    print(f"speech {speech:.1f} dB  floor {floor:.1f} dB  threshold {thr:.1f} dB")
    zoom = float(spec.get("zoom", 1.08))
    fx, fy = spec.get("focal", [540, 730])
    ranges = []
    for i, tk in enumerate(spec["takes"]):
        fw = next(w for w in words if w["end"] >= tk["first"] - 0.01 and w["start"] >= tk["first"] - 0.3)
        lw = max((w for w in words if w["start"] <= tk["last"] + 0.01), key=lambda w: w["start"])
        # acoustic onset: walk back from ASR start while env stays above threshold, up to 0.6s
        s_i = int(fw["start"] / WIN)
        lo = max(0, int((fw["start"] - 0.6) / WIN))
        onset_i = s_i
        # first find a quiet point before the word, then the first loud window after it
        j = s_i
        while j > lo and env[j] > thr:
            j -= 1
        onset_i = j + 1 if env[j] <= thr else s_i
        onset = onset_i * WIN
        prev_quiet = j * WIN
        start = max(onset - PRE, prev_quiet)
        # acoustic end
        e_from = int(lw["start"] / WIN)
        cap = int((lw["end"] + 0.7) / WIN)
        k = e_from
        tail = None
        while k < min(cap, len(env) - 6):
            if all(env[k:k + 6] <= thr):
                tail = k * WIN
                break
            k += 1
        if tail is None:
            tail = min(lw["end"] + 0.15, cap * WIN)
            note_end = "no 120ms dead-air inside the cap; used ASR box end + 0.15"
        else:
            note_end = f"acoustic tail {tail:.2f} vs ASR '{lw['text']}' box end {lw['end']:.2f}"
        end = tail + POST
        quote = " ".join(w["text"] for w in words if fw["start"] <= w["start"] <= lw["start"])
        z_from, z_to = (1.0, zoom) if i % 2 == 0 else (zoom, 1.0)
        ranges.append({
            "source": spec["source_key"], "start": round(start, 3), "end": round(end, 3),
            "beat": tk["beat"], "quote": quote,
            "reason": tk.get("why", "Last complete take of this beat.") +
                      f" Acoustic onset {onset:.2f} vs ASR '{fw['text']}' start {fw['start']:.2f} "
                      f"(delta {fw['start'] - onset:+.2f}); {note_end}. Start = onset - {PRE}, end = tail + {POST}.",
            "zoom": {"mode": "slow", "from": z_from, "to": z_to, "focal_x": fx, "focal_y": fy},
        })
        print(f"  {tk['beat']:<14} {start:8.3f} -> {end:8.3f}  ({end - start:5.2f}s)  '{fw['text']}' .. '{lw['text']}'")
    edl = {
        "version": 1,
        "sources": {spec["source_key"]: spec["source"]},
        "ranges": ranges,
        "grade": grade,
        "overlays": [],
        "subtitles": "master.ass",
        "_variant": spec.get("variant_note", "Single variant."),
        "_zoom_note": f"Slow face-anchored zoom about ({fx},{fy}), magnitude {zoom}, alternating per range "
                      "so the drift is continuous across cuts (render.py supersampled zoom chain).",
        "_edge_note": "Every range START/END measured acoustically by edl_from_takes.py (20ms RMS, "
                      "threshold = 20th-percentile floor + 8 dB): start = onset - 0.12s, end = first "
                      "120ms dead-air after the last word + 0.12s, capped at the ASR box end + 0.7s so "
                      "sighs and throat-clears after a take are excluded.",
    }
    out = os.path.join(ep_dir, "edl.json")
    json.dump(edl, open(out, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print("wrote", out, "total", round(sum(r["end"] - r["start"] for r in ranges), 2), "s")


if __name__ == "__main__":
    main()
