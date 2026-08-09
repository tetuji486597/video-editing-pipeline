"""Render a video from an EDL.

Implements the HEURISTICS render pipeline in the correct order:

  1. Per-segment extract with color grade + 30ms audio fades baked in
  2. Lossless -c copy concat into base.mp4
  3. If overlays or subtitles: single filter graph that overlays animations
     (with PTS shift so frame 0 lands at the overlay window start)
     and applies `subtitles` filter LAST → final.mp4

Optionally builds a master SRT from the per-source transcripts + EDL
output-timeline offsets, applies the proven force_style (2-word
UPPERCASE chunks, Helvetica 18 Bold, MarginV=35).

Usage:
    python helpers/render.py <edl.json> -o final.mp4
    python helpers/render.py <edl.json> -o preview.mp4 --preview
    python helpers/render.py <edl.json> -o final.mp4 --build-subtitles
    python helpers/render.py <edl.json> -o final.mp4 --no-subtitles
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    from grade import get_preset, auto_grade_for_clip  # same directory
except Exception:
    def get_preset(name: str) -> str:
        return ""

    def auto_grade_for_clip(video, start=0.0, duration=None, verbose=False):  # type: ignore
        return "eq=contrast=1.03:saturation=0.98", {}


# -------- Subtitle style (bold-overlay, proven at 1920×1080 and 1080×1920) --
#
# MarginV is NOT taste — it is a platform safe-zone rule.
# TikTok / IG Reels / Shorts UI (caption, username, music, right-rail actions)
# covers roughly the bottom ~25–30% of a 1080×1920 frame. Captions placed near
# the bottom edge get clipped or obscured by the UI. libass auto-scales the
# render canvas relative to PlayResY=288, so MarginV=90 lands the caption
# baseline roughly 30% up from the bottom on any aspect — clear of the UI on
# every major vertical-video platform. Do not drop this below ~75 without a
# specific reason.
SUB_FORCE_STYLE = (
    "FontName=Helvetica,FontSize=18,Bold=1,"
    "PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BackColour=&H00000000,"
    "BorderStyle=1,Outline=2,Shadow=0,"
    "Alignment=2,MarginV=90"
)

# -------- Helpers ------------------------------------------------------------


def run(cmd: list[str], quiet: bool = False) -> None:
    if not quiet:
        print(f"  $ {' '.join(str(c) for c in cmd[:6])}{' …' if len(cmd) > 6 else ''}")
    subprocess.run(cmd, check=True)


def resolve_grade_filter(grade_field: str | None) -> str:
    """The EDL's 'grade' field can be a preset name, a raw ffmpeg filter, or 'auto'.

    Returns the filter string to embed into the per-segment -vf chain.
    For 'auto', returns the sentinel "__AUTO__" which is resolved per-segment.
    """
    if not grade_field:
        return ""
    if grade_field == "auto":
        return "__AUTO__"
    # Preset names are short identifiers, filter strings contain '=' or ','.
    if re.fullmatch(r"[a-zA-Z0-9_\-]+", grade_field):
        try:
            return get_preset(grade_field)
        except KeyError:
            print(f"warning: unknown preset '{grade_field}', using as raw filter")
            return grade_field
    return grade_field


def resolve_path(maybe_path: str, base: Path) -> Path:
    """Resolve a path that may be absolute or relative to `base`."""
    p = Path(maybe_path)
    if p.is_absolute():
        return p
    return (base / p).resolve()


# -------- HDR → SDR tone mapping (HLG / PQ sources) --------------------------
#
# iPhone defaults to HLG HDR in Rec.2020 (and many mirrorless cameras ship PQ).
# If the source is HDR and we only downconvert bit depth (yuv420p10le → yuv420p)
# without tone-mapping, the output is 8-bit but still carries HLG/PQ transfer
# metadata. Players that honor the metadata (screen recorders, most social
# upload re-encodes) interpret 8-bit values in an HDR container and the result
# looks oversaturated / blown out. QuickTime on macOS can hide this locally —
# screen recording and uploaded renders cannot.
#
# Fix: detect HDR via color_transfer and prepend a zscale+tonemap chain to the
# vf graph so the output is clean Rec.709 SDR.

HDR_TRANSFERS = {"smpte2084", "arib-std-b67"}  # PQ (HDR10) and HLG

TONEMAP_CHAIN = (
    "zscale=t=linear:npl=100,"
    "format=gbrpf32le,"
    "zscale=p=bt709,"
    "tonemap=tonemap=hable:desat=0,"
    "zscale=t=bt709:m=bt709:r=tv,"
    "format=yuv420p"
)


def is_hdr_source(video: Path) -> bool:
    """Return True if the source uses a PQ or HLG transfer function."""
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=color_transfer",
             "-of", "default=noprint_wrappers=1:nokey=1", str(video)],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip() in HDR_TRANSFERS
    except subprocess.CalledProcessError:
        return False


def is_portrait_source(video: Path) -> bool:
    """Return True if the video's height > width (portrait / vertical)."""
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=width,height",
             "-of", "csv=p=0", str(video)],
            capture_output=True, text=True, check=True,
        )
        w, h = map(int, out.stdout.strip().split(","))
        return h > w
    except Exception:
        return False


# -------- Punch zoom (Ken-Burns-style zoom in/out synced to a landing word) --


def build_punch_zoom_expr(
    at: float,
    scale: float = 1.18,
    in_dur: float = 0.28,
    hold_dur: float = 0.35,
    out_dur: float = 0.45,
) -> str:
    """Build an ffmpeg time expression Z(t) for a single punch-in/punch-out zoom.

    Ease-out-cubic on both the zoom-in (snaps toward `scale`, landing exactly at
    `at`) and the zoom-out (releases back to 1.0) — never linear, matches the
    "zoom punch" technique from the Vyra-era episodes. `at` is segment-local time
    (0 = this segment's own start), matching the EDL range's own local timeline.
    """
    t0 = at - in_dur
    t1 = at
    t2 = at + hold_dur
    t3 = t2 + out_dur
    ramp_in = f"(1+({scale}-1)*(1-pow(1-clip((t-{t0})/{in_dur},0,1),3)))"
    ramp_out = f"({scale}-({scale}-1)*(1-pow(1-clip((t-{t2})/{out_dur},0,1),3)))"
    return (
        f"if(lt(t,{t0}),1.0,"
        f"if(lt(t,{t1}),{ramp_in},"
        f"if(lt(t,{t2}),{scale},"
        f"if(lt(t,{t3}),{ramp_out},1.0))))"
    )


def build_punch_zoom_filter(
    zoom_expr: str,
    focal_x: float = 540,
    focal_y: float = 730,
    out_w: int = 1080,
    out_h: int = 1920,
) -> str:
    """scale-then-crop filter chain that zooms toward a fixed focal point (fx, fy)
    in the ORIGINAL out_w x out_h frame — that point stays at the same on-screen
    position throughout (e.g. eye level), everything else grows away from it.

    Derivation: after scaling by Z, the point that was at (fx, fy) moves to
    (fx*Z, fy*Z). To keep it on-screen at (fx, fy), the crop offset must be
    (fx*Z - fx, fy*Z - fy) = (fx*(Z-1), fy*(Z-1)). Since 0 <= fx <= out_w and
    Z >= 1, this is always within [0, out_w*(Z-1)] (the valid crop range) —
    no clamping needed.

    Note: this ffmpeg build's `crop` filter has no `eval` option at all — its
    x/y expressions are simply re-evaluated every frame against that frame's
    actual `iw`/`ih` (unlike `scale`, which needs `eval=frame` explicitly).
    """
    w_expr = f"trunc({out_w}*({zoom_expr})/2)*2"
    h_expr = f"trunc({out_h}*({zoom_expr})/2)*2"
    x_expr = f"{focal_x}*(({zoom_expr})-1)"
    y_expr = f"{focal_y}*(({zoom_expr})-1)"
    return (
        f"scale=w='{w_expr}':h='{h_expr}':eval=frame,"
        f"crop=w={out_w}:h={out_h}:x='{x_expr}':y='{y_expr}'"
    )


# -------- Per-segment extraction (Rule 2 + Rule 3) --------------------------


DENOISE_MODEL_DEFAULT = Path(__file__).resolve().parent.parent / "models" / "rnnoise" / "bd.rnnn"


def extract_segment(
    source: Path,
    seg_start: float,
    duration: float,
    grade_filter: str,
    out_path: Path,
    preview: bool = False,
    draft: bool = False,
    zoom_filter: str | None = None,
    denoise_model: Path | None = None,
) -> None:
    """Extract a cut range as its own MP4 with grade + 30ms audio fades baked in.

    `-ss` before `-i` for fast accurate seeking. Scale to 1080p from 4K.
    Portrait sources (height > width) are scaled by height to preserve orientation.

    Quality ladder:
      - final (default): 1080p libx264 fast CRF 20
      - preview:         1080p libx264 medium CRF 22 (evaluable for QC)
      - draft:           720p libx264 ultrafast CRF 28 (cut-point check only)
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    portrait = is_portrait_source(source)
    if draft:
        scale = "scale=-2:1280" if portrait else "scale=1280:-2"
    else:
        scale = "scale=-2:1920" if portrait else "scale=1920:-2"

    vf_parts: list[str] = []
    if is_hdr_source(source):
        vf_parts.append(TONEMAP_CHAIN)
    vf_parts.append(scale)
    if grade_filter:
        vf_parts.append(grade_filter)
    if zoom_filter and not draft:
        # zoom applied after grade (like a camera move over already-graded film);
        # skipped in draft mode — draft is for cut-point checks, not visual QC
        vf_parts.append(zoom_filter)
    vf = ",".join(vf_parts)

    # 30ms audio fades at both edges (Rule 3) — prevent pops
    fade_out_start = max(0.0, duration - 0.03)
    af_parts: list[str] = []
    if denoise_model is not None:
        # RNNoise (ML speech denoiser) before the fades — a highpass first strips
        # sub-80Hz rumble/handling noise that isn't speech-band, then RNNoise
        # discriminates voice from room noise (confirmed via measured RMS: on a
        # real quiet-vs-speech A/B, ~26dB noise-floor drop vs ~19dB on speech, a
        # real ~7dB SNR gain — not just a uniform volume cut like ffmpeg's
        # built-in afftdn, which showed near-zero differential in the same test).
        af_parts.append(f"highpass=f=80,arnndn=m='{denoise_model}'")
    af_parts.append(f"afade=t=in:st=0:d=0.03,afade=t=out:st={fade_out_start:.3f}:d=0.03")
    af = ",".join(af_parts)

    if draft:
        preset, crf = "ultrafast", "28"
    elif preview:
        preset, crf = "medium", "22"
    else:
        preset, crf = "fast", "20"

    cmd = [
        "ffmpeg", "-y",
        "-ss", f"{seg_start:.3f}",
        "-i", str(source),
        "-t", f"{duration:.3f}",
        "-vf", vf,
        "-af", af,
        "-c:v", "libx264", "-preset", preset, "-crf", crf,
        "-pix_fmt", "yuv420p", "-r", "24",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-movflags", "+faststart",
        str(out_path),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def extract_all_segments(
    edl: dict,
    edit_dir: Path,
    preview: bool,
    draft: bool = False,
    denoise_model: Path | None = None,
) -> list[Path]:
    """Extract every EDL range into edit_dir/clips_graded/seg_NN.mp4.
    Returns the ordered list of segment paths.

    If the EDL `grade` is "auto", analyze each segment range with
    `auto_grade_for_clip` and apply a per-segment subtle correction.
    Otherwise, apply the same preset/raw filter to every segment.
    """
    resolved = resolve_grade_filter(edl.get("grade"))
    is_auto = resolved == "__AUTO__"
    clips_dir = edit_dir / (
        "clips_draft" if draft else ("clips_preview" if preview else "clips_graded")
    )
    clips_dir.mkdir(parents=True, exist_ok=True)

    ranges = edl["ranges"]
    sources = edl["sources"]

    seg_paths: list[Path] = []
    print(f"extracting {len(ranges)} segment(s) → {clips_dir.name}/")
    if is_auto:
        print("  (auto-grade per segment: analyzing each range)")
    for i, r in enumerate(ranges):
        src_name = r["source"]
        src_path = resolve_path(sources[src_name], edit_dir)
        start = float(r["start"])
        end = float(r["end"])
        duration = end - start
        out_path = clips_dir / f"seg_{i:02d}_{src_name}.mp4"

        if is_auto:
            seg_filter, _stats = auto_grade_for_clip(src_path, start=start, duration=duration, verbose=False)
        else:
            seg_filter = resolved

        note = r.get("beat") or r.get("note") or ""
        print(f"  [{i:02d}] {src_name}  {start:7.2f}-{end:7.2f}  ({duration:5.2f}s)  {note}")
        if is_auto:
            print(f"        grade: {seg_filter or '(none)'}")

        zoom_filter = None
        if r.get("zoom"):
            z = r["zoom"]
            zoom_expr = build_punch_zoom_expr(
                at=float(z["at"]),
                scale=float(z.get("scale", 1.18)),
                in_dur=float(z.get("in_dur", 0.28)),
                hold_dur=float(z.get("hold_dur", 0.35)),
                out_dur=float(z.get("out_dur", 0.45)),
            )
            zoom_filter = build_punch_zoom_filter(
                zoom_expr,
                focal_x=float(z.get("focal_x", 540)),
                focal_y=float(z.get("focal_y", 730)),
            )
            print(f"        zoom: punch to {z.get('scale', 1.18)}x at t={z['at']}s (local)")

        extract_segment(
            src_path, start, duration, seg_filter, out_path,
            preview=preview, draft=draft, zoom_filter=zoom_filter,
            denoise_model=denoise_model,
        )
        seg_paths.append(out_path)

    return seg_paths


# -------- Lossless concat ----------------------------------------------------


def concat_segments(segment_paths: list[Path], out_path: Path, edit_dir: Path) -> None:
    """Lossless concat via the concat demuxer. No re-encode."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    concat_list = edit_dir / "_concat.txt"
    concat_list.write_text("".join(f"file '{p.resolve()}'\n" for p in segment_paths))

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_list),
        "-c", "copy",
        "-movflags", "+faststart",
        str(out_path),
    ]
    print(f"concat → {out_path.name}")
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    concat_list.unlink(missing_ok=True)


# -------- Master SRT (Rule 5) ------------------------------------------------


PUNCT_BREAK = set(".,!?;:")


def _srt_timestamp(seconds: float) -> str:
    total_ms = int(round(seconds * 1000))
    h, rem = divmod(total_ms, 3600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _words_in_range(transcript: dict, t_start: float, t_end: float) -> list[dict]:
    out: list[dict] = []
    for w in transcript.get("words", []):
        if w.get("type") != "word":
            continue
        ws = w.get("start")
        we = w.get("end")
        if ws is None or we is None:
            continue
        if we <= t_start or ws >= t_end:
            continue
        out.append(w)
    return out


def build_master_srt(edl: dict, edit_dir: Path, out_path: Path) -> None:
    """Build an output-timeline SRT from per-source transcripts.

    - 2-word chunks (break on any punctuation in between)
    - UPPERCASE text
    - Output times computed as word.start - segment_start + segment_offset
    """
    transcripts_dir = edit_dir / "transcripts"
    sources = edl["sources"]

    entries: list[tuple[float, float, str]] = []
    seg_offset = 0.0

    for r in edl["ranges"]:
        src_name = r["source"]
        seg_start = float(r["start"])
        seg_end = float(r["end"])
        seg_duration = seg_end - seg_start

        tr_path = transcripts_dir / f"{src_name}.json"
        if not tr_path.exists():
            print(f"  no transcript for {src_name}, skipping captions for this segment")
            seg_offset += seg_duration
            continue

        transcript = json.loads(tr_path.read_text())
        words_in_seg = _words_in_range(transcript, seg_start, seg_end)

        # Group into 2-word chunks, break on punctuation
        chunks: list[list[dict]] = []
        current: list[dict] = []
        for w in words_in_seg:
            text = (w.get("text") or "").strip()
            if not text:
                continue
            current.append(w)
            # Break if the current text ends in punctuation or we hit 2 words
            ends_in_punct = bool(text) and text[-1] in PUNCT_BREAK
            if len(current) >= 2 or ends_in_punct:
                chunks.append(current)
                current = []
        if current:
            chunks.append(current)

        for chunk in chunks:
            local_start = max(seg_start, chunk[0].get("start", seg_start))
            local_end = min(seg_end, chunk[-1].get("end", seg_end))
            out_start = max(0.0, local_start - seg_start) + seg_offset
            out_end = max(0.0, local_end - seg_start) + seg_offset
            if out_end <= out_start:
                out_end = out_start + 0.4
            text = " ".join((w.get("text") or "").strip() for w in chunk)
            text = re.sub(r"\s+", " ", text).strip()
            # Strip trailing punctuation for cleaner uppercase look
            text = text.rstrip(",;:")
            text = text.upper()
            entries.append((out_start, out_end, text))

        seg_offset += seg_duration

    # Sort and write as SRT
    entries.sort(key=lambda e: e[0])
    lines: list[str] = []
    for i, (a, b, t) in enumerate(entries, start=1):
        lines.append(str(i))
        lines.append(f"{_srt_timestamp(a)} --> {_srt_timestamp(b)}")
        lines.append(t)
        lines.append("")
    out_path.write_text("\n".join(lines))
    print(f"master SRT → {out_path.name} ({len(entries)} cues)")


# -------- Master ASS with word-by-word karaoke highlight --------------------


def _ass_timestamp(seconds: float) -> str:
    total_cs = int(round(seconds * 100))
    h, rem = divmod(total_cs, 360000)
    m, rem = divmod(rem, 6000)
    s, cs = divmod(rem, 100)
    return f"{h:d}:{m:02d}:{s:02d}.{cs:02d}"


ASS_BASE_COLOUR = "&HFFFFFF&"   # white — unspoken/spoken-already words in the visible chunk
ASS_HILITE_COLOUR = "&H00D7FF&"  # gold (BGR) — the word being spoken right now


def build_master_ass(
    edl: dict,
    edit_dir: Path,
    out_path: Path,
    margin_v: int = 70,
    font_size: int = 58,
    margin_lr: int = 60,
    max_words_per_chunk: int = 4,
) -> None:
    """Build an output-timeline ASS file with real word-by-word karaoke highlight.

    Each chunk (up to `max_words_per_chunk` words, breaking on punctuation or a
    silence gap >= 0.4s) is emitted as N overlapping-free Dialogue events — one
    per word — showing the full chunk text with only the currently-spoken word
    tag-colored gold, the rest white. This sidesteps ASS \\k sweep-color
    ambiguity entirely: every frame's exact appearance is explicit.

    PlayResX/PlayResY are set to the actual output canvas (1080x1920), so
    MarginV is real output pixels, not scaled through libass's SRT-conversion
    default (PlayResY=288).
    """
    transcripts_dir = edit_dir / "transcripts"

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Helvetica,{font_size},{ASS_BASE_COLOUR},{ASS_BASE_COLOUR},&H00000000,&H00000000,1,0,0,0,100,100,1,0,1,3,0,2,{margin_lr},{margin_lr},{margin_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

    events: list[tuple[float, float, str]] = []
    seg_offset = 0.0

    for r in edl["ranges"]:
        src_name = r["source"]
        seg_start = float(r["start"])
        seg_end = float(r["end"])
        seg_duration = seg_end - seg_start

        tr_path = transcripts_dir / f"{src_name}.json"
        if not tr_path.exists():
            print(f"  no transcript for {src_name}, skipping captions for this segment")
            seg_offset += seg_duration
            continue

        transcript = json.loads(tr_path.read_text())
        words_in_seg = _words_in_range(transcript, seg_start, seg_end)

        # Group into small chunks, break on punctuation, word cap, or a gap >= 0.4s
        chunks: list[list[dict]] = []
        current: list[dict] = []
        prev_end: float | None = None
        for w in words_in_seg:
            text = (w.get("text") or "").strip()
            if not text:
                continue
            ws = w.get("start", seg_start)
            gap_break = prev_end is not None and (ws - prev_end) >= 0.4
            if gap_break and current:
                chunks.append(current)
                current = []
            current.append(w)
            ends_in_punct = text[-1] in PUNCT_BREAK
            if len(current) >= max_words_per_chunk or ends_in_punct:
                chunks.append(current)
                current = []
            prev_end = w.get("end", ws)
        if current:
            chunks.append(current)

        for chunk in chunks:
            n = len(chunk)
            out_starts = [max(0.0, w.get("start", seg_start) - seg_start) + seg_offset for w in chunk]
            out_ends = [max(0.0, w.get("end", seg_start) - seg_start) + seg_offset for w in chunk]
            words_upper = [re.sub(r"\s+", " ", (w.get("text") or "").strip()).upper() for w in chunk]

            for i in range(n):
                ev_start = out_starts[i]
                ev_end = out_starts[i + 1] if i + 1 < n else out_ends[i]
                if ev_end <= ev_start:
                    ev_end = ev_start + 0.12
                parts = []
                for j in range(n):
                    if j == i:
                        parts.append(f"{{\\c{ASS_HILITE_COLOUR}}}{words_upper[j]}{{\\c{ASS_BASE_COLOUR}}}")
                    else:
                        parts.append(words_upper[j])
                text = " ".join(parts)
                events.append((ev_start, ev_end, text))

        seg_offset += seg_duration

    events.sort(key=lambda e: e[0])
    lines = [header]
    for a, b, t in events:
        lines.append(
            f"Dialogue: 0,{_ass_timestamp(a)},{_ass_timestamp(b)},Default,,0,0,0,,{t}"
        )
    out_path.write_text("\n".join(lines) + "\n")
    print(f"master ASS → {out_path.name} ({len(events)} word-highlight events)")


# -------- Loudness normalization (social-ready audio) -----------------------


# Social-media standard: -14 LUFS integrated, -1 dBTP peak, LRA 11 LU.
# Matches YouTube / Instagram / TikTok / X / LinkedIn normalization targets.
LOUDNORM_I = -14.0
LOUDNORM_TP = -1.0
LOUDNORM_LRA = 11.0


def measure_loudness(video_path: Path) -> dict[str, str] | None:
    """Run ffmpeg loudnorm first pass and parse the JSON measurement.

    Returns a dict with measured_i, measured_tp, measured_lra, measured_thresh,
    target_offset, or None if measurement failed.
    """
    filter_str = (
        f"loudnorm=I={LOUDNORM_I}:TP={LOUDNORM_TP}:LRA={LOUDNORM_LRA}:print_format=json"
    )
    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-nostats",
        "-i", str(video_path),
        "-af", filter_str,
        "-vn", "-f", "null", "-",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    # loudnorm prints the JSON to stderr at the end of the run
    stderr = proc.stderr

    # Find the JSON block — loudnorm output contains a `{ ... }` block
    start = stderr.rfind("{")
    end = stderr.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    try:
        data = json.loads(stderr[start : end + 1])
    except json.JSONDecodeError:
        return None
    needed = {"input_i", "input_tp", "input_lra", "input_thresh", "target_offset"}
    if not needed.issubset(data.keys()):
        return None
    return data


def apply_loudnorm_two_pass(
    input_path: Path,
    output_path: Path,
    preview: bool = False,
) -> bool:
    """Run two-pass loudnorm on input_path, write normalized copy to output_path.

    Returns True on success, False if measurement failed (caller should fall
    back to copying the input unchanged).

    In preview mode, skips the measurement pass and uses a one-pass approximation
    for speed. Final mode always does the proper two-pass.
    """
    if preview:
        # One-pass approximation — faster, slightly less accurate.
        filter_str = f"loudnorm=I={LOUDNORM_I}:TP={LOUDNORM_TP}:LRA={LOUDNORM_LRA}"
        cmd = [
            "ffmpeg", "-y", "-hide_banner", "-nostats",
            "-i", str(input_path),
            "-c:v", "copy",
            "-af", filter_str,
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-movflags", "+faststart",
            str(output_path),
        ]
        print(f"  loudnorm (1-pass preview) → {output_path.name}")
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        return True

    # Full two-pass
    print(f"  loudnorm pass 1: measuring {input_path.name}")
    measurement = measure_loudness(input_path)
    if measurement is None:
        print("  loudnorm measurement failed — falling back to 1-pass")
        return apply_loudnorm_two_pass(input_path, output_path, preview=True)

    print(f"    measured: I={measurement['input_i']} LUFS  "
          f"TP={measurement['input_tp']}  LRA={measurement['input_lra']}")

    filter_str = (
        f"loudnorm=I={LOUDNORM_I}:TP={LOUDNORM_TP}:LRA={LOUDNORM_LRA}"
        f":measured_I={measurement['input_i']}"
        f":measured_TP={measurement['input_tp']}"
        f":measured_LRA={measurement['input_lra']}"
        f":measured_thresh={measurement['input_thresh']}"
        f":offset={measurement['target_offset']}"
        f":linear=true"
    )
    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-nostats",
        "-i", str(input_path),
        "-c:v", "copy",
        "-af", filter_str,
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-movflags", "+faststart",
        str(output_path),
    ]
    print(f"  loudnorm pass 2: normalizing → {output_path.name}")
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    return True


# -------- Final compositing (Rule 1 + Rule 4) -------------------------------


def build_final_composite(
    base_path: Path,
    overlays: list[dict],
    subtitles_path: Path | None,
    out_path: Path,
    edit_dir: Path,
) -> None:
    """Final pass: base → overlays (PTS-shifted) → subtitles LAST → out.

    If there are no overlays and no subtitles, just copy base to out.
    """
    has_overlays = bool(overlays)
    has_subs = subtitles_path is not None and subtitles_path.exists()

    if not has_overlays and not has_subs:
        # Nothing to do — just rename/copy base to final name
        run(["ffmpeg", "-y", "-i", str(base_path), "-c", "copy", str(out_path)], quiet=True)
        return

    inputs: list[str] = ["-i", str(base_path)]
    for ov in overlays:
        ov_path = resolve_path(ov["file"], edit_dir)
        if ov_path.suffix.lower() == ".webm":
            # ffmpeg's default "vp9" decoder silently drops the WebM alpha side-channel
            # (auto_scale then fakes a fully-opaque plane) — the libvpx-vp9 decoder
            # extracts it correctly. Required for any alpha-carrying overlay (e.g. HyperFrames).
            inputs += ["-c:v", "libvpx-vp9", "-i", str(ov_path)]
        else:
            inputs += ["-i", str(ov_path)]

    filter_parts: list[str] = []
    # PTS-shift every overlay so its frame 0 lands at start_in_output
    for idx, ov in enumerate(overlays, start=1):
        t = float(ov["start_in_output"])
        filter_parts.append(f"[{idx}:v]setpts=PTS-STARTPTS+{t}/TB[a{idx}]")

    # Chain overlays on top of base
    current = "[0:v]"
    for idx, ov in enumerate(overlays, start=1):
        t = float(ov["start_in_output"])
        dur = float(ov["duration"])
        end = t + dur
        next_label = f"[v{idx}]"
        filter_parts.append(
            f"{current}[a{idx}]overlay=enable='between(t,{t:.3f},{end:.3f})'{next_label}"
        )
        current = next_label

    # Subtitles LAST — Rule 1
    if has_subs:
        subs_abs = str(subtitles_path.resolve()).replace(":", r"\:").replace("'", r"\'")
        if subtitles_path.suffix.lower() == ".ass":
            # .ass carries its own complete style (incl. word-highlight color
            # overrides) — force_style would only override what it already declares.
            filter_parts.append(f"{current}subtitles='{subs_abs}'[outv]")
        else:
            filter_parts.append(
                f"{current}subtitles='{subs_abs}':force_style='{SUB_FORCE_STYLE}'[outv]"
            )
        out_label = "[outv]"
    else:
        # Rename the last overlay output to [outv] for consistency
        if has_overlays:
            filter_parts.append(f"{current}null[outv]")
            out_label = "[outv]"
        else:
            out_label = "[0:v]"

    filter_complex = ";".join(filter_parts)

    cmd = [
        "ffmpeg", "-y",
        *inputs,
        "-filter_complex", filter_complex,
        "-map", out_label,
        "-map", "0:a",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "copy",
        "-movflags", "+faststart",
        str(out_path),
    ]
    print(f"compositing → {out_path.name}")
    print(f"  overlays: {len(overlays)}, subtitles: {'yes' if has_subs else 'no'}")
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


# -------- Main ---------------------------------------------------------------


def main() -> None:
    ap = argparse.ArgumentParser(description="Render a video from an EDL")
    ap.add_argument("edl", type=Path, help="Path to edl.json")
    ap.add_argument("-o", "--output", type=Path, required=True, help="Output video path")
    ap.add_argument(
        "--preview",
        action="store_true",
        help="Preview mode: 1080p, medium, CRF 22 — evaluable for QC, faster than final.",
    )
    ap.add_argument(
        "--draft",
        action="store_true",
        help="Draft mode: 720p, ultrafast, CRF 28 — cut-point verification only.",
    )
    ap.add_argument(
        "--build-subtitles",
        action="store_true",
        help="Build master captions from transcripts + EDL offsets before compositing",
    )
    ap.add_argument(
        "--caption-format",
        choices=["srt", "ass-karaoke"],
        default="srt",
        help="srt: plain force_style chunks (default). ass-karaoke: real word-by-word "
             "color-highlight captions (master.ass), full styling incl. MarginV baked in.",
    )
    ap.add_argument(
        "--caption-margin-v",
        type=int,
        default=70,
        help="ass-karaoke only: bottom margin in real output pixels (PlayResY = output height).",
    )
    ap.add_argument(
        "--caption-font-size",
        type=int,
        default=58,
        help="ass-karaoke only: font size in real output pixels (PlayResY = output height).",
    )
    ap.add_argument(
        "--caption-margin-lr",
        type=int,
        default=60,
        help="ass-karaoke only: left/right margin in real output pixels — raise this to "
             "narrow the usable text width and force wrapping sooner (keeps lines shorter "
             "and more centered instead of spanning near-full-width).",
    )
    ap.add_argument(
        "--denoise",
        action="store_true",
        help="Apply RNNoise ML speech denoising (+ an 80Hz highpass) to each segment's "
             "audio before the fade edges, using the bundled model at "
             "helpers/../models/rnnoise/bd.rnnn. Confirmed via measured RMS to meaningfully "
             "separate voice from room noise (~7dB SNR gain), unlike ffmpeg's built-in "
             "afftdn which showed near-zero differential in the same test.",
    )
    ap.add_argument(
        "--denoise-model",
        type=Path,
        default=None,
        help="Path to an alternate RNNoise .rnnn model (defaults to the bundled model).",
    )
    ap.add_argument(
        "--no-subtitles",
        action="store_true",
        help="Skip subtitles even if the EDL references one",
    )
    ap.add_argument(
        "--no-loudnorm",
        action="store_true",
        help="Skip audio loudness normalization. Default is on (-14 LUFS, -1 dBTP, LRA 11).",
    )
    args = ap.parse_args()

    edl_path = args.edl.resolve()
    if not edl_path.exists():
        sys.exit(f"edl not found: {edl_path}")

    edl = json.loads(edl_path.read_text())
    edit_dir = edl_path.parent
    out_path = args.output.resolve()

    # 1. Extract per-segment (auto-grade per range if EDL grade is "auto")
    denoise_model_path = None
    if args.denoise:
        denoise_model_path = (args.denoise_model or DENOISE_MODEL_DEFAULT).resolve()
        if not denoise_model_path.exists():
            sys.exit(f"--denoise given but model not found: {denoise_model_path}")
    segment_paths = extract_all_segments(
        edl, edit_dir, preview=args.preview, draft=args.draft,
        denoise_model=denoise_model_path,
    )

    # 2. Concat → base
    if args.draft:
        base_name = "base_draft.mp4"
    elif args.preview:
        base_name = "base_preview.mp4"
    else:
        base_name = "base.mp4"
    base_path = edit_dir / base_name
    concat_segments(segment_paths, base_path, edit_dir)

    # 3. Subtitles: build if requested, resolve final path
    subs_path: Path | None = None
    if not args.no_subtitles:
        if args.build_subtitles:
            if args.caption_format == "ass-karaoke":
                subs_path = edit_dir / "master.ass"
                build_master_ass(edl, edit_dir, subs_path, margin_v=args.caption_margin_v, font_size=args.caption_font_size, margin_lr=args.caption_margin_lr)
            else:
                subs_path = edit_dir / "master.srt"
                build_master_srt(edl, edit_dir, subs_path)
        elif edl.get("subtitles"):
            subs_path = resolve_path(edl["subtitles"], edit_dir)
            if not subs_path.exists():
                print(f"warning: subtitles path in EDL does not exist: {subs_path}")
                subs_path = None

    # 4. Composite (overlays + subtitles LAST) → intermediate (pre-loudnorm) path
    overlays = edl.get("overlays") or []
    if args.no_loudnorm:
        # Composite directly to final output
        build_final_composite(base_path, overlays, subs_path, out_path, edit_dir)
    else:
        # Composite to a temp file, then run loudnorm → final output
        tmp_composite = out_path.with_suffix(".prenorm.mp4")
        build_final_composite(base_path, overlays, subs_path, tmp_composite, edit_dir)
        print("loudness normalization → social-ready (-14 LUFS / -1 dBTP / LRA 11)")
        apply_loudnorm_two_pass(tmp_composite, out_path, preview=args.draft)
        tmp_composite.unlink(missing_ok=True)

    size_mb = out_path.stat().st_size / (1024 * 1024)
    print(f"\ndone: {out_path} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
