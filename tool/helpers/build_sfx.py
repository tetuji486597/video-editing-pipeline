#!/usr/bin/env python3
"""Build an episode's SFX track from a cue list, then mix it onto the composite.

Why this exists: the per-episode ffmpeg filtergraphs were hand-written each time,
which is how a cue with 1.25s of leading silence shipped in EP13 (the flood hit
fired over a second late because the source file started silent). This asserts the
invariant instead of relying on remembering it.

Cue list format (JSON):
  {"video": "final_nosfx.mp4", "out": "final.mp4", "cues": [
     {"at": 4.70, "sfx": "ding",    "vol": 0.55, "why": "hook: 2ms lands"},
     {"at": 9.32, "sfx": "whoosh_trim", "vol": 0.45, "why": "problem: fast-forward"}
  ]}

Every referenced sfx is checked for leading silence before use -- a stinger whose
transient is not at t=0 lands late no matter how correct its timestamp is.

Optional per-cue "cut": seconds AFTER the landing (`at`) at which the sound is faded out
(120ms fade). You do not have to play a whole sound effect: a 2.8s ding ring-out or a
4s reveal sting smears over the next line. DEFAULT_CUT below gives every known long file
a sensible tail; a cue's own "cut" overrides it, and "cut": 0 means play it whole.

Usage: build_sfx.py <episode-dir> <cues.json>
"""
import json, subprocess, sys, os

# Seconds after the landing to stop each sound (EP27-29 user feedback: "you don't always
# have to play the whole sound effect"). Files not listed play whole.
DEFAULT_CUT = {
    "tt_correct_ding": 0.8, "tt_notif_trim": 0.9, "tt_whoosh": 0.8, "whoosh_trim": 0.7,
    "tt_sparkle_trim": 1.0, "tt_error_glitch": 0.8, "tt_wrong_buzzer": 0.7, "tt_vine_boom": 1.0,
    "swoosh_deep": 0.6, "swoosh_double": 0.7, "impact_trim": 0.9, "bass_drop": 1.0,
    "bass_hit": 0.9, "riser": 0.35, "ding": 0.9, "tt_keyboard_trim": 1.2,
    "br_amongus_reveal": 1.5, "br_amongus_sus": 1.2, "br_skibidi_toilet": 1.4,
    "br_gigachad": 1.5, "br_tung_sahur": 2.0, "br_touch_grass": 1.8, "br_fanum_tax": 1.8,
    "br_monkey_screech": 1.0, "br_electric_zap": 0.6, "br_rizz": 1.0, "br_aura_minus1000": 1.5,
    "br_tralalero": 1.0, "br_sybau": 1.5, "br_touch_grass": 1.3,
}
FADE = 0.12

# Where a file LANDS, in seconds from its start, for files the percussive/swell heuristic
# gets wrong: a voice meme lands when it starts talking (its loudest syllable can be 1.3s
# in -- br_six_seven's "seven" -- which pre-rolled the "six" a beat early on EP27-29), and
# a musical sting lands on its drop. Measured from 100ms RMS envelopes.
ANCHOR = {
    "br_six_seven": 0.72, "br_six_seven_voice": 0.1, "br_amongus_reveal": 0.9,
    "br_amongus_sus": 0.9, "br_gigachad": 0.8, "br_touch_grass": 0.05, "br_aura_minus1000": 0.6,
    "br_rizz": 0.0, "br_sybau": 0.1, "br_tralalero": 0.0, "br_fanum_tax": 0.1,
    "br_skibidi_toilet": 0.0, "br_tung_sahur": 0.0, "br_monkey_screech": 0.2,
    "br_electric_zap": 0.0, "br_fries_in_bag": 0.0, "br_erm_sigma": 0.0,
    "br_what_the_skibidi": 0.0, "tt_bruh": 0.0,
}

SHARED = os.path.join(os.path.dirname(__file__), "..", "..", "sfx_shared")


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                 "format=duration", "-of", "csv=p=0", p],
                                capture_output=True, text=True).stdout.strip())


def impact_offset(p):
    """Seconds from a file's start to the moment it audibly LANDS.

    The leading-silence check below is necessary but not sufficient: it only looks at
    the head of the file. A stinger is not always transient-first --

        bass_hit      full energy at t=0          impact 0.00s   (percussive)
        shutter       full energy at t=0          impact 0.00s   (percussive)
        swoosh_deep   near-silent 0.2s, peaks 0.9 impact ~0.65s  (swell)
        buildup       ramps for 2.0s              impact ~0.90s  (riser)
        riser         ramps for 2.2s              impact ~1.50s  (riser)

    Delaying every cue by its timestamp alone therefore puts the audible impact of a
    swell up to ~1.5s late -- the same defect as EP13's impact_trim, just measured
    from the other end of the file. So a cue's `at` means "when the sound LANDS", and
    the delay applied is at - impact_offset.

    Anchoring on the first crossing of half-max is right for a percussive sound and
    WRONG for a ramp: a riser keeps climbing well past that point, so first-crossing
    put EP17's riser 1.12s late (measured on the built track, not assumed). The two
    cases need different anchors, so classify first:

      first crossing of half-max is in the first 15% of the file  -> percussive,
        the attack IS the landing; anchor on that crossing
      otherwise                                                   -> swell/ramp,
        it lands when it peaks; anchor on the peak

    This keeps bass_hit at 0.05s (full energy from t=0, broad sustain after) instead
    of mistaking its long sustain for a ramp and pre-rolling it 1.35s.
    """
    import struct, wave, tempfile
    w = os.path.join(tempfile.gettempdir(), "_sfx_impact.wav")
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", p,
                    "-ac", "1", "-ar", "8000", w, "-y"], check=True)
    with wave.open(w) as f:
        n = f.getnframes()
        a = struct.unpack(f"<{n}h", f.readframes(n))
    win = 400  # 50ms at 8kHz
    env = [sum(abs(x) for x in a[i:i + win]) / win for i in range(0, n - win, win)]
    if not env:
        return 0.0
    step = win / 8000.0
    total = len(env) * step
    peak_i = max(range(len(env)), key=lambda i: env[i])
    half = env[peak_i] * 0.5
    first = next((i for i, e in enumerate(env) if e >= half), 0) * step
    return first if total and first / total < 0.15 else peak_i * step


def leading_silence(p):
    """Seconds of silence at the head of a file, 0.0 if it starts on its transient."""
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-af",
                          "silencedetect=n=-45dB:d=0.02", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    starts = [l for l in out.splitlines() if "silence_start" in l]
    ends = [l for l in out.splitlines() if "silence_end" in l]
    if not starts or not ends:
        return 0.0
    try:
        s0 = float(starts[0].split("silence_start:")[1].split()[0])
        e0 = float(ends[0].split("silence_end:")[1].split()[0])
    except (IndexError, ValueError):
        return 0.0
    return e0 if s0 < 0.02 else 0.0


def main():
    ep_dir, cue_path = sys.argv[1], sys.argv[2]
    cfg = json.load(open(cue_path, encoding="utf-8"))
    cues = sorted(cfg["cues"], key=lambda c: c["at"])
    video = os.path.join(ep_dir, cfg["video"])
    total = dur(video)

    ins, filts, labels, shifts = [], [], [], []
    for i, c in enumerate(cues):
        p = os.path.normpath(os.path.join(SHARED, c["sfx"] + ".mp3"))
        if not os.path.exists(p):
            sys.exit(f"missing sfx: {p}")
        lead = leading_silence(p)
        if lead > 0.02:
            sys.exit(f"REFUSING: {c['sfx']}.mp3 has {lead:.3f}s of leading silence -- "
                     f"the cue would land that late. Trim it from its transient first.")
        if c["at"] + dur(p) > total + 0.5:
            print(f"  warn: {c['sfx']} at {c['at']} runs past the video end ({total:.2f}s)")
        # `at` is when the sound must LAND, so back the start off by its impact offset
        imp = ANCHOR[c["sfx"]] if c["sfx"] in ANCHOR else impact_offset(p)
        delay = c["at"] - imp
        head_trim = 0.0
        if delay < 0:
            # cue is too early in the video for the swell to fit -- trim its head
            # rather than let it land late, and say so
            head_trim, delay = -delay, 0.0
            print(f"  note: {c['sfx']} at {c['at']:.2f}s needs {imp:.2f}s of pre-roll but "
                  f"only {c['at']:.2f}s exists; trimming {head_trim:.2f}s off its head")
        if imp > 0.02:
            shifts.append(f"{c['sfx']}-{imp:.2f}s")
        ins += ["-i", p]
        pre = f"atrim=start={head_trim:.3f},asetpts=PTS-STARTPTS," if head_trim else ""
        cut = c.get("cut", DEFAULT_CUT.get(c["sfx"], 0))
        if cut:
            # stop `cut` seconds after the LANDING: file time = impact offset + cut
            end = max(imp - head_trim + cut, FADE + 0.05)
            if end < dur(p) - head_trim - 0.01:
                pre += f"atrim=end={end:.3f},afade=t=out:st={end-FADE:.3f}:d={FADE},"
        filts.append(f"[{i}:a]{pre}volume={c.get('vol',0.5)},"
                     f"adelay={int(round(delay*1000))}:all=1[a{i}]")
        labels.append(f"[a{i}]")

    # Name the track after its cue file. A shared sfx_track.wav means an episode's
    # B variant silently overwrites A's track: the finals are still correct (each is
    # muxed before the next build runs) but any later check reads the wrong track and
    # reports phantom misalignment. Ask me how I know.
    stem = os.path.splitext(os.path.basename(cue_path))[0].replace("cues", "sfx_track")
    track = os.path.join(ep_dir, "sfx", stem + ".wav")
    os.makedirs(os.path.dirname(track), exist_ok=True)
    fg = ";".join(filts) + ";" + "".join(labels) + f"amix=inputs={len(cues)}:duration=longest:normalize=0[out]"
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", *ins,
                    "-filter_complex", fg, "-map", "[out]", "-t", f"{total:.3f}",
                    "-ar", "48000", "-ac", "2", track, "-y"], check=True)

    out = os.path.join(ep_dir, cfg["out"])
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", video, "-i", track,
                    "-filter_complex",
                    "[0:a][1:a]amix=inputs=2:duration=first:normalize=0,"
                    "loudnorm=I=-14:TP=-2:LRA=11[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", out, "-y"], check=True)

    peak = subprocess.run(["ffmpeg", "-hide_banner", "-i", out, "-af", "astats", "-f", "null", "-"],
                          capture_output=True, text=True).stderr
    pk = next((l.split(":")[-1].strip() for l in peak.splitlines() if "Peak level dB" in l), "?")
    kinds = sorted({c["sfx"] for c in cues})
    sh = ("  aligned: " + ", ".join(sorted(set(shifts)))) if shifts else ""
    print(f"  {os.path.basename(ep_dir):24s} {len(cues)} cues / {len(kinds)} distinct  "
          f"peak {pk} dB  -> {cfg['out']}{sh}")


if __name__ == "__main__":
    main()
