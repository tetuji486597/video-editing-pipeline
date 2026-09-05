# EP12 — "How Google Search Is Instant Across Billions of Pages" (database indexes / B-trees)

Built via the video-use + HyperFrames pipeline, following STYLE.md conventions. Built on
Windows — see EP13's `project.md` for the porting notes (cp1252 `→` crashes, the
`render.py:759` backslash patch, `--workers 1 --no-browser-gpu` on renders).

## Source & take selection

Source: `C:/Users/gordo/Downloads/12.mp4` — 2160x3840 HEVC, 30fps, 2m17s, mono 48k.
Clean uniform 0.5x to the 1080x1920 output canvas. 487 words / 20 phrases via Scribe.
**Raw footage is unbacked-up** — same exposure as EP13.

6 ranges, 56.06s. **5 of 6 beats had a discarded earlier attempt** — a higher retake rate
than EP13:

- **HOOK** take 2/2 — take 1 is a one-word false start ("In,").
- **PROBLEM** only delivery, clean.
- **BUILD** take 2/2 — take 1 (30.92) stops after "a separate sorted structure" without
  reaching the B-tree or the book analogy.
- **NEW_COMPONENT** take 2/2 — take 1 (45.40) flubs "instead of **re**-reading every page"
  and aborts. The kept take is one continuous 16.45s delivery covering mechanism,
  trade-off AND rule-of-thumb, so no splice was needed (unlike EP13's NEW_COMPONENT).
- **AI_ANGLE** take **4/4** and the only complete one — take 1 stops at "extend this exact
  idea", take 2 is a stumble ("Vector databases, vector databases."), take 3 repeats
  "nearest neighbor search" across a break.
- **PAYOFF** take 2/2 — the earlier attempt fragments across a "we'll talk about how--"
  flub and would need a splice; this one lands both halves unbroken.

## Dead-air audit (applied proactively after the EP13 report)

Gordon flagged ~1.7s of dead silence at EP13's 0:42 mark. Root cause: **Scribe's word
boxes routinely overrun the actual audio**, so padding off the ASR end preserves silence.
Every EP12 range end was therefore measured acoustically with `silencedetect`, not trusted
from the transcript:

| Beat | Trailing air | Action |
|---|---|---|
| HOOK | +0.050s | keep |
| PROBLEM | +0.018s | keep |
| BUILD | +0.020s | keep |
| NEW_COMPONENT | +0.001s | keep |
| **AI_ANGLE** | **+0.387s** | **trimmed** — ASR boxes "fast." to 107.94, speech stops at 107.553; range ends at 107.63 |
| PAYOFF | none (speech runs to the end) | keep |

Internal gaps of 0.46-0.80s (HOOK, PROBLEM, BUILD, NEW_COMPONENT, PAYOFF) are natural
rhetorical beats and were kept. **Measurement trap:** pick a window that starts *after*
any internal pause or you measure the wrong gap — PROBLEM initially read as +1.015s of
trailing air because the window caught the pause before "it's hopeless."

## Face measurement — differs from EP13, measured not assumed

| Feature | EP12 | EP13 |
|---|---|---|
| hair tips | ~60 | ~100 |
| hairline | ~560 | ~580 |
| eyes | ~700 | ~830 |
| mouth | ~1010-1060 | ~1180-1240 |
| chin | **~1150** | **~1300** |

His chin sits ~150px higher here. EP13 had **zero** clearance between chin and the
caption zone (1330), forcing every content overlay to be a full-screen takeover. EP12 has
a usable **~180px band (1190-1310)**, which is what makes the transparent two-band payoff
possible. Confirms the skill's instruction to grid-measure per shot.

## Overlay format mix (assigned at planning stage per rule 7)

Signature colour **violet #8b5cf6** — distinct from EP13 amber, EP6 teal, EP4 red/orange,
EP1 blue.

| Beat | Window | Format | Two-phase story |
|---|---|---|---|
| title | 0.000-2.766 | transparent top-left | STYLE.md standard |
| hook | 2.800-6.300 | full-screen counter takeover | odometer to 1,000,000,000 → "FOUND IN 2 ms" |
| problem | 7.600-13.400 | full-screen table-scan takeover | row-by-row SEQ SCAN → fast-forward blur → HOPELESS |
| build | 15.900-20.700 | **real-photo-anchored** (book) | "a separate sorted structure" + B-tree → back-of-book index panel |
| new_component | 23.500-32.200 | data-viz B-tree takeover | 3-hop traversal, COMPARISONS 3 → balance-scale trade-off |
| ai_angle | 40.000-46.000 | embedding point-cloud takeover | cyan vector space → violet HNSW 4-hop traversal |
| payoff | 49.500-54.000 | **transparent two-band** over live footage | TOC motif (upper) + next-episode strip (lower) |

**5 distinct formats** — clears rule 7's ≥3. Gaps: title→hook +0.034 (house standard,
matches ep4/5/6/13); then +1.300 / +2.500 / +2.800 / +7.800 / +3.500. No small accidental
gaps. Coverage 36.07/56.06 = 64%.

**Real images: 1** — `slot_build/assets/book.jpg` (Unsplash, open book, no legible title/
author/publisher; only out-of-focus Cyrillic body copy, illegible at frame scale).

## The fade-rendering bug — found independently by two builds

**A `tl.to(target, {opacity: 0})` fade can silently fail to render in this renderer.** Two
EP12 slots hit it independently:

- `slot_ai_angle`: the fade never rendered at all — luminance sat flat through the last
  frame. The discriminator was that it was the only plain `.to()` among 33 tweens; every
  `fromTo` with explicit start values rendered fine. **The renderer seeks a paused
  timeline and screenshots immediately, so a tween that must read its start value from the
  DOM can miss the write.** Fixed with `fromTo` + explicit `{opacity:1}` start +
  `gsap.defaults({lazy:false})`.
- `slot_hook`: the fade had no measurable effect until ~3.37 of a 3.2→3.5 window, and
  measuring two regions separately showed **ancestor opacity is not applied uniformly to
  transformed descendant layers** (row-field fully black while the numeral held ~80%). A
  wrapper div changed nothing. Fixed with a top-most `#blackout` leaf.

**`check --at --snapshots` reported the fade working on the broken build**, so the lint
harness cannot catch this class — only re-rendering and measuring can.

**Verified NOT affected** (measured, not assumed): both title cards (EP12 and EP13) fade
correctly — they fade *leaf elements directly* rather than an ancestor wrapper. EP13's
`slot_ai_angle`, `slot_build`, `slot_payoff` and EP12's `slot_problem`, `slot_new_component`
all measured correct fades too. So the bug is conditional, not universal — which means
**every slot's fade must be verified empirically on the render, per slot.**

**Worth auditing, out of scope here:** `slot_hook`'s agent flagged that EP4's
`slot_new_component` — the repo's cited gold standard, referenced by the overlay skill's
rule 12 — uses `tl.to("#content-all",{opacity:0,duration:0.3},7.6)` over a `#scene` with a
scale transform and a filtered `#dither`, i.e. exactly the construction that measured
broken. **Its shipped fade-out may never have worked.**

## Verification gotchas hit this session

- **`select` preserves original PTS.** Compositing an overlay frame onto a base with
  `select=eq(n,X)` and no `setpts=PTS-STARTPTS` silently produces a frame with NO overlay
  — it looks exactly like a broken overlay. Same class as the pipeline's Hard Rule 4.
- **Flattening alpha onto an unspecified background misreads fades.** Decoding a
  transparent WebM without compositing over a known colour let ffmpeg flatten decreasing
  alpha onto a light default, which read as "the fade is going *brighter*". Always
  composite over an explicit colour (magenta reads best) before judging a fade.
- **SFX leading silence.** `click.mp3` carried 166ms and `whoosh.mp3` 335ms of leading
  silence. Since cues are placed on the triggering GSAP call, either would have landed
  audibly late. Always `silencedetect` a stinger and trim from its transient.

## Output frame rate — 24fps, and it matters MORE here than in EP13

`render.py:273` hardcodes `-r 24` on segment extraction. Source is 30fps, HyperFrames
renders every overlay at 30fps, output is 24fps — so both the footage and the overlays are
decimated. Every shipped episode went through this path, so it is the series' established
output, **but it is a real defect, not a style choice**, and EP12's overlays are more
frame-timing-sensitive than EP13's:

- `slot_problem`'s scan bar steps on a deliberately **mechanical 0.21s grid** — 6.3 frames
  at 30fps, 5.04 at 24fps. Non-integer, so the steps land on alternating frame offsets and
  the mechanical evenness that sells "painfully slow, one row at a time" is disturbed.
- `slot_hook`'s 10 odometer reels lock on a 30fps schedule, the last at 1.716s.
- The three B-tree snap-zoom clicks sit 0.76s / 0.74s apart, tuned at 30fps.
- Every fade was authored to finish exactly at `data-duration` and verified at 30fps; in
  the 24fps composite the last frame sits at `dur − 1/24`, so the zero-buffer property was
  confirmed against a different clock than the one that ships.

Changing it is one line in `render.py` **plus a full re-render** (~20 min), and it would
make EP12/EP13 the only episodes at 30fps. Left at 24 pending a decision.

**Corollary that already bit once:** a source-domain edit does not translate 1:1 to output.
Trimming 1.68s from EP13's AI_ANGLE produced a 1.610s output shift, because segments
quantize to the 24fps grid — see EP13's `edl.json` `_trim_note`. Re-derive downstream
overlay windows and SFX cues against the rendered output, never by carrying the
source-domain delta across arithmetically.

## Status

- [x] Transcript, packed takes, dead-air audit, EDL, cut verified (56.06s, 165 caption events)
- [x] All 7 overlays built, rendered at exact durations, individually verified on frames
- [x] Rule-9 freshness: all 7 fresh
- [x] SFX catalog: click_trim 0.22s, whoosh_trim 1.30s, ding 1.33s (all transients at t=0)
- [x] Composite + SFX placement (9 cues, each verified against a real frame) + audit suite

## Delivered

`final.mp4` — 1080x1920, 24fps, **56.14s**, 67 MB.
Peak **-1.764 dB** (negative = no clipping), integrated **-15.0 LUFS**, **no dead air**
anywhere at -34dB/0.5s.

Intermediates kept: `final_nosfx.mp4`, `cut_check.mp4` (cut verification, no overlays),
`base_draft.mp4`, `master.ass`, `verify/strips/*` (audit contact sheets).

## Self-check audit results

- **Caption/face clearance — PASS.** All 7 overlays sampled at 5 points across their
  *entire* runs, not one frame each. No overlay content enters the caption band at any
  sample. The transparent payoff was additionally composited over live footage and
  confirmed to keep the face zone (540-1190) completely clear across its full run.
- **Format mix (rule 7) — PASS, 5 distinct formats** (see table above).
- **Real images (rule 6) — PASS, 1 sourced** (`slot_build/assets/book.jpg`, full-bleed).
- **Density (rule 3) — PASS.** Every overlay has a named two-phase structure with an
  explicit transition beat.
- **Fade verification — PASS, empirically per slot.** Given the fade-rendering bug above,
  every slot's fade was verified on the actual render rather than trusted from the lint
  harness (which reported a broken fade as working).
- **Rule-9 freshness — PASS**, re-run immediately before the ship render: all 7 fresh.
- **Rotating-element (rule 13) — N/A.** No GSAP `rotation` on any degenerate-bbox SVG.
  The balance-scale beam specifically uses the trig/`onUpdate` pattern instead.
- **Coverage (informational).** 36.07/56.06 = 64%; per-beat 55-98%.

## NOT independently verified (agent-reported only)

- **Rule 8 internal-collision arithmetic is agent-reported**, not independently recomputed
  — same allocation as EP13. First-hand effort went to caption/face clearance, fade
  verification and the composite audit instead.
- **Two slots use `data-layout-allow-*` suppressions.** `slot_problem` (3 containers) and
  `slot_hook` (reel strips) suppressed layout-auditor findings, each with a stated
  rationale (clip-unaware `getBoundingClientRect` on scrolled/clipped content). I verified
  `slot_problem`'s visually and the suppression is legitimate — exactly one number renders
  with no ghosting. `slot_hook`'s I did not separately re-derive beyond its frame checks.
