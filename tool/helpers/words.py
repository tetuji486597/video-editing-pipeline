#!/usr/bin/env python3
"""Print word-level ASR entries in a time window.

Two things this is for:
  1. Snapping EDL cut edges to real word boundaries (Hard Rule 6).
  2. Finding the output-timeline timestamp of an overlay's payoff word, so the
     overlay's key visual lands ON the words that state the idea.

Scribe pads word boxes (see find_dead_air.py) -- a word's `end` is NOT where the
audio stops. Use this for boundaries and ordering; measure range ENDS acoustically.

Usage:
  words.py <transcript.json> <start> <end>
  words.py <transcript.json> --find "phrase to locate"
"""
import json
import sys


def load(path):
    d = json.load(open(path, encoding="utf-8"))
    words = d["words"] if isinstance(d, dict) and "words" in d else d
    return [w for w in words if w.get("type", "word") == "word"]


def main():
    path = sys.argv[1]
    words = load(path)

    if sys.argv[2] == "--find":
        needle = " ".join(sys.argv[3:]).lower().strip()
        toks = needle.split()
        n = len(toks)
        for i in range(len(words) - n + 1):
            run = [words[i + k]["text"].lower().strip(".,?!\"'") for k in range(n)]
            if run == [t.strip(".,?!\"'") for t in toks]:
                print(f"MATCH  {words[i]['start']:.3f} -> {words[i+n-1]['end']:.3f}")
                for k in range(n):
                    w = words[i + k]
                    print(f"    {w['start']:8.3f} {w['end']:8.3f}  {w['text']}")
        return

    lo, hi = float(sys.argv[2]), float(sys.argv[3])
    prev_end = None
    for w in words:
        if w["end"] < lo or w["start"] > hi:
            continue
        gap = "" if prev_end is None else f"  gap={w['start'] - prev_end:+.3f}"
        print(f"{w['start']:8.3f} {w['end']:8.3f}  {w['text']!r}{gap}")
        prev_end = w["end"]


if __name__ == "__main__":
    main()
