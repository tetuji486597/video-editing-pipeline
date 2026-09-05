#!/usr/bin/env python3
"""Verify each SFX cue is audible in the final mix.

Method (validated on EP19, see episodes/ep19-likecounts/project.md): difference the
mixed track against the no-SFX track with a FITTED gain, at 32 kHz -- loudnorm
renormalises the whole mix so comparing peaks proves nothing, and an 8 kHz
downsample discards shimmer content above 4 kHz (a real cue measured 0.80x at 8 kHz
vs 3.27x at 32 kHz).

For each cue: fit gain g on a 1.5s control window ending 0.3s before the cue
(least-squares final ~ g*nosfx), then report
    ratio = RMS(final - g*nosfx in cue window) / RMS(final - g*nosfx in control)
ratio >= 1.5 -> clearly audible; 1.2-1.5 borderline; < 1.2 flag as inaudible.

Usage: check_sfx_audible.py <episode-dir> <cues.json>
"""
import json, os, subprocess, sys
import numpy as np

SR = 32000


def load(path):
    p = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR),
         "-f", "f32le", "-"], capture_output=True)
    return np.frombuffer(p.stdout, dtype=np.float32)


def main():
    ep_dir, cues_path = sys.argv[1], sys.argv[2]
    spec = json.load(open(cues_path))
    final = load(os.path.join(ep_dir, spec["out"]))
    nosfx = load(os.path.join(ep_dir, spec["video"]))
    n = min(len(final), len(nosfx))
    final, nosfx = final[:n], nosfx[:n]

    def rms(x):
        return float(np.sqrt(np.mean(x * x))) if len(x) else 0.0

    # Control windows must be CUE-FREE: a control that overlaps a neighbouring cue
    # inflates the baseline and flags a healthy cue as inaudible (first version of
    # this tool did exactly that on EP25 -- three false BADs, all from cue-bleed).
    all_at = sorted(c["at"] for c in spec["cues"])

    def clean_control(at):
        # walk backwards in 0.25s steps to find a 1.5s window >=0.9s clear of every cue
        for back in np.arange(0.3, min(at, 12.0), 0.25):
            lo, hi = at - back - 1.5, at - back
            if lo < 0:
                break
            if all(hi <= a - 0.9 or lo >= a + 2.5 for a in all_at):
                return int(lo * SR), int(hi * SR)
        # fallback: quietest assumption -- window right before the cue
        return int(max(0, at - 1.8) * SR), int((at - 0.3) * SR)

    bad = 0
    for c in spec["cues"]:
        at = c["at"]
        c0, c1 = clean_control(at)
        w0, w1 = int(max(0, at - 0.05) * SR), int(min(n / SR, at + 0.9) * SR)
        c0 = max(0, c0)
        ctrl_f, ctrl_n = final[c0:c1], nosfx[c0:c1]
        if len(ctrl_f) < SR // 2 or rms(ctrl_n) == 0:
            g = 1.0
        else:
            g = float(np.dot(ctrl_f, ctrl_n) / np.dot(ctrl_n, ctrl_n))
        base = rms(ctrl_f - g * ctrl_n) or 1e-9
        cue = rms(final[w0:w1] - g * nosfx[w0:w1])
        ratio = cue / base
        verdict = "OK " if ratio >= 1.5 else ("~? " if ratio >= 1.2 else "BAD")
        if ratio < 1.2:
            bad += 1
        print(f"  {verdict} {at:7.2f}s {c['sfx']:<18} ratio {ratio:5.2f}x  ({c['why'][:52]})")
    print(f"{'ALL AUDIBLE' if bad == 0 else str(bad) + ' cue(s) FLAGGED'} -- {os.path.basename(cues_path)}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
