# EP13 — "Why You Get 'Too Many Requests'" (rate limiting / token bucket)

Built via the video-use + HyperFrames pipeline, following STYLE.md conventions.
**First episode in this repo built on Windows** — see the porting notes below.

## Source & take selection

Source: `C:/Users/gordo/Downloads/13.mp4` — 2160x3840 HEVC, 30fps, 2m42s, mono 48k.
Same 9:16 aspect as the 1080x1920 output canvas, so scaling is a clean uniform 0.5x
(no crop offset). **Raw footage is unbacked-up** — README documents EP1's as already
lost; a second copy should exist somewhere before this episode is considered safe.

531 words / 27 phrases transcribed via ElevenLabs Scribe. The tape contains 4 hook
takes, 5 attempts at NEW_COMPONENT (with an audible sigh at 80.02 after the third
collapses), and 3 payoff takes. PROBLEM, BUILD and AI_ANGLE are each a single clean
first-time delivery.

7 ranges, 51.4s predicted / 51.52s actual on the concatenated base.

### Notable take decisions

- **HOOK is take 4, not take 3.** Take 3 (15.16) is clean and was the obvious pick,
  but its final word "requests?" carries 1.8s of trailing dead air vs 0.64s on take 4.
  Take 4 also runs continuously into the "Well, the app is defending itself" tag, so
  hook + tag come from one unbroken delivery with a natural 0.66s beat between them.
- **NEW_COMPONENT is a splice**, confirmed with the user. Take 4 (108.87) is the ONLY
  one of five containing the scripted "until it refills" clause, but it aborts one
  sentence later on "This allows short bursts but caps...". Spliced to the clean
  completion at 125.57, which is also the better read ("Fair to real users" vs take
  2's "which is fair to real users"). Cut lands after "refills." (ends 118.28); that
  edge is padded only +40ms because the aborted "This" onset sits just 80ms later.
  Verified on the rendered draft: waveform decays smoothly into the join with no pop
  spike, filmstrip shows continuous framing.
- **Payoff blooper NOT used.** Take 1 (141.46) inverts the line into "So a bucket is a
  token" — a usable blooper, and STYLE.md's EP7 correction says it would have to
  precede the clean line. User declined; kept the clean cut.
- **AI_ANGLE trailing air.** Final word "untouched." is timestamped to 140.78 but
  acoustically lands ~139.3 — up to 1.3s of dead air kept to respect Hard Rule 6
  (never cut inside a word). Revisit if it drags on review.

## Windows porting notes (this repo is macOS-native throughout)

Three real breakages, all fixed:

1. **`setup_check.sh` reports `python3` missing** — false alarm. Windows has Python
   3.10.6 as `python` (and 3.12.7 via the `py` launcher / anaconda). Built the venv
   with `python` and installed via `.venv/Scripts/pip`, not the README's
   `.venv/bin/pip`.
2. **`UnicodeEncodeError` on every helper that prints a `→`.** The Windows console
   defaults to cp1252, which cannot encode U+2192, so `render.py` crashed before
   extracting anything and `pack_transcripts.py` crashed after writing its file
   (making it look like it had succeeded). Fix: run helpers with
   `PYTHONIOENCODING=utf-8`. Not patched in-tree — it's an environment issue.
3. **Caption burn-in failed — `render.py:759`.** The subtitles filter escaped the
   drive colon but left Windows backslashes in the path, and ffmpeg's filtergraph
   parser reads `\` as an escape character (`C:\Users\...` → `\U`, `\g`, `\v` get
   eaten). **Patched in-tree**: normalize separators to forward slashes *before*
   escaping the colon. This is a no-op on POSIX so it does not affect the Mac.
   This is exactly the "captions silently fail" class STYLE.md warns about, except
   here it errored loudly instead.

## Face measurement — DOES NOT match the skill's documented values

Grid-measured on this footage at native scale (`drawgrid` at 108x100px on a
1080x1920-scaled frame), per skill rule 5's instruction to confirm per-shot:

| Feature | This footage | skill's stated value |
|---|---|---|
| hair tips | ~y=100 | ~y=200-220 |
| eyes | ~y=830 | — |
| mouth | ~y=1180-1240 | ~y=980-1080 |
| chin | ~y=1300-1330 | ~y=1080-1200 |

Everything sits **~150-200px lower** than the skill documents — this shot is framed
tighter/lower than EP4's. The consequence is significant: the 3-line caption zone
begins at y≈1330 and the chin sits at y≈1300-1330, so **there is effectively zero
clear vertical space between the chin and the caption band.** Skill rule 5's
preferred fix pattern (1) — "reposition the offending element up into the gap" — is
simply unavailable on this episode.

**Therefore: full-screen opaque takeovers are the default for any content-bearing
overlay here**, per rule 5's fix pattern (2). The one transparent format that remains
legitimately available is rule 11's translucent outline/glow linework over the *hair*
region (y≈150-560), which is a large genuinely-clear area on this shot.

## Overlay format mix (assigned at planning stage per rule 7)

| Beat | Format | Two-phase story |
|---|---|---|
| HOOK | full-screen takeover | login button mashed → red 429 toast slams in |
| PROBLEM | photo-anchored takeover + screen-shake | calm server → firehose flood, tips over |
| BUILD | transparent linework over hair (rule 11) | empty bucket → tokens drip in |
| NEW_COMPONENT | full-screen, realistic API UI | token spent / 200 OK → bucket empty / 429 |
| AI_ANGLE | split-screen comparison | flat limit throttles all → learned model spares humans |
| PAYOFF | real-photo full-bleed | payoff line → "next: why feeds never end" |

4 distinct formats — satisfies rule 7's ≥3 requirement. Signature colour is **amber**
(#f59e0b), the token/bucket thread; distinct from EP4's red/orange and EP6's teal.

**Screen-shake is confirmed-approved by the user for the PROBLEM beat.** STYLE.md
lists screen-shake as explicitly untested, so this is the series' first — flag it on
review.

**Note on EP4 as reference:** EP4's `slot_problem` fades out at 4.2s "leaving dead-air
tail" (line 412-413). Skill rule 12 was added *later* and reverses this — the fade
must finish at *exactly* the overlay's declared duration, zero buffer. Follow rule 12,
not EP4's tail timing.

## Overlay windows (output timeline)

| Slot | Window | Dur | Gap to next |
|---|---|---|---|
| title | 0.000–2.766 | 2.766 | +0.034 |
| hook | 2.800–6.200 | 3.400 | +1.000 |
| problem | 7.200–13.000 | 5.800 | +2.600 |
| build | 15.600–19.900 | 4.300 | +1.800 |
| new_component | 21.700–29.900 | 8.200 | +6.700 |
| ai_angle | 36.600–42.600 | 6.000 | +2.800 |
| payoff | 45.400–49.800 | 4.400 | — |

Rule 1 (breathing room) and rule 12 (contiguous, zero gap) appear to conflict. Resolved
empirically against the shipped episodes rather than by reading: ep4/ep5/ep6 all run
**49–54% coverage with multi-second deliberate gaps** (1.7s–9.1s), and all three share an
identical `title 0→2.766, hook 2.800→…` handoff. So rule 12 targets *small accidental*
gaps (its EP11 case was 170ms), not intentional breathing room. Every gap above is ≥1.0s
except that same house-standard 34ms title→hook handoff.

That empirical check also dissolved a rule-10 tension: the hook overlay does not need to
be transparent to land early, because the house pattern already starts it at 2.800.

## Reference-frame gotchas found this session (all cost real time)

- **Fast seek (`-ss` before `-i`) on VP9-with-alpha returns blank frames.** Nearly
  reported two non-existent "overlay is empty" defects. Audits must decode without
  seeking, or select frames by index.
- **ffmpeg's `color=` source defaults to 25fps.** Silently understated frame counts on
  30fps overlays — rule 12's "export every frame at native fps" check is worthless if
  the reference clock is wrong. Pass `r=30` explicitly.
- **`ffprobe` reports `yuv420p` on a correctly transparent overlay.** The default vp9
  decoder drops the alpha plane; `-c:v libvpx-vp9` reports `yuva420p`. This is the same
  behaviour the README's headline customization exists to work around. Do not use plain
  ffprobe as a transparency gate.
- **The `movie=` filter chokes on the Windows drive colon**, exactly like `render.py:759`
  did. Use `-vf format=yuv420p,signalstats,metadata=print` on a normal input instead.
- **`signalstats` silently emits nothing on RGB input** (e.g. a PNG). Needs
  `format=yuv420p` first, or it looks like the measurement failed.
- **A non-empty final frame is CORRECT, not a bug.** If the fade finishes exactly at the
  declared duration (rule 12), the last rendered frame at `dur − 1/30` is still ~11%
  visible. A fully-cleared last frame would mean the fade landed early — the actual bug.

## Cross-cutting bug found by the slot_problem build

A repeating `fromTo` whose **final render lands after a completed fade tween wins the DOM
write**, stranding the element visible. Green phase-1 streaks stayed lit under the red
firehose for ~2.8s; invisible at downscaled preview, only caught by cropping full-res.
Fix: make repeating tweens fully complete before the fade starts.

**The same pattern exists in shipped EP6** at
`episodes/ep6-websockets/animations/slot_problem/index.html:148` —
`{duration: 0.6, repeat: 3, yoyo: true}` starting at 4.8 runs to 7.2s, overshooting that
clip's 5.8s end. Not fixed here (out of scope for EP13) but worth a look.

Audited the ep13 slots for it: the surviving long repeats (`slot_hook:378` `#toast`
boxShadow to 5.50s vs 3.4s clip; `slot_new_component:832` `#bucket-glow` to 9.20s vs 8.2s)
all animate **children** of `#content-all`, while every fade targets `#content-all`
itself. Parent opacity multiplies, so a truncated child tween cannot strand content.

## Output frame rate — 24fps, and the overlays are 30fps

`render.py:273` hardcodes `-r 24` on segment extraction. So the chain is: source 30fps →
extracted segments 24fps → HyperFrames overlays rendered at 30fps → final output 24fps.
Both the footage and the overlays get decimated. Every shipped episode went through this
same code path, so **this is the series' established output, not a regression** — but two
consequences are real:

- The 0.06s shutter-flash transitions the overlays use are ~1.4 frames at 24fps, so they
  land as a single-frame blip rather than a readable flash.
- 30fps is the norm for vertical social; 24 is a cinematic choice.

Changing it is one line, but it would make EP13 inconsistent with EP1-EP12. Left at 24
pending a decision. **This also invalidates frame-index arithmetic that assumes 30fps** —
an audit that selects frames by index against the composite must use 24, not the
overlays' native 30.

## Delivered

`final.mp4` — 1080x1920, 24fps, **51.54s**, 65 MB.
Peak **-0.762 dB** (negative = no clipping), integrated **-15.0 LUFS**.

Intermediates kept: `final_nosfx.mp4` (composite before the SFX mix), `preview.mp4` /
`preview_sfx.mp4` (QC pass), `cut_check.mp4` (cut verification, no overlays),
`base_draft.mp4`, `master.ass`, `verify/strips/*` (the audit contact sheets).

## Status

- [x] Transcript, packed takes, EDL, cut verified (draft render + waveform/filmstrip)
- [x] All 7 overlays built and rendered at exactly their specified durations
- [x] slot_problem rebuilt — rule-9 caught its index.html newer than its render
- [x] Rule-9 freshness re-checked immediately before the ship render: all 7 fresh
- [x] SFX: 4 sourced, 10 cues placed on triggering GSAP calls, verified against frames
- [x] Final composite + audit suite (see below)
- [x] Peak verified negative after the SFX remix

## Self-check audit results

- **Caption/face clearance — PASS.** All 7 overlays sampled at 5 points across their
  *entire* runs (start/25/50/75/95%), not one frame each. No overlay content enters the
  caption band at any sample. Contact sheets in `verify/strips/`.
- **Transition-gap (rule 12) — PASS.** Only sub-second boundary is title->hook at 34ms;
  frame-exact check shows the title fading over a face that was already visible beneath
  it, then the takeover landing. No bare-footage flash. All other gaps are 1.0-6.7s of
  deliberate breathing room.
- **Format mix (rule 7) — PASS, 4 distinct formats.** Full-screen takeover (hook,
  new_component) · photo-anchored takeover (problem) · transparent linework over live
  footage (build) · split-screen comparison (ai_angle) · real-photo full-bleed (payoff).
- **Real images (rule 6) — PASS, 2 sourced.** `slot_problem/assets/server.jpg` (server
  rack, embedded as atmospheric backdrop under a designed UI card) and
  `slot_payoff/assets/chaos.jpg` (traffic light-trails, full-bleed hero). Two candidates
  were rejected for legible building signage — the EP5 branding trap.
- **Density (rule 3) — PASS.** Every overlay has a named two-phase structure with an
  explicit transition beat; see each slot's agent report summarised above.
- **Coverage (informational).** 34.9s of overlay across 51.5s = 68%, higher than the
  49-54% of ep4/ep5/ep6 because this episode has 6 content beats rather than 5. Per-beat
  it ranges 55-98%. Rule 1 says judge density, not percentage.
- **Rotating-element (rule 13) — N/A.** No GSAP `rotation` on any degenerate-bbox SVG in
  any slot; confirmed in all six agent reports.

## NOT independently verified (agent-reported only) — read before trusting this episode

- **Rule 8 internal-collision arithmetic is entirely agent-reported.** Every slot's build
  agent produced resolved-pixel ranges and pairwise gaps; none of it was independently
  recomputed. Deliberate allocation of effort — the caption/face clearance and transition
  audits were done first-hand instead, because those are the failures with shipped
  precedent in this repo.
- **`slot_problem`'s content bounds were not independently measured.** It was checked only
  via its agent's report and the composite contact strip (which looked clean). It is also
  the riskiest slot to take on trust: it is the only one with screen-shake displacing
  content up to ±19.3px, and the only one that was rebuilt.
- **Open loose end in `slot_problem`:** its agent found `#endpoint`'s box (x 238-618)
  overlapping `#chip`'s box (x 602-842) by 16px. It judged this cosmetic (rendered glyph
  run ends at x≈453, so ~149px of real visual separation) and deliberately reverted its
  fix to keep `index.html` byte-identical to the render. That slot was then rebuilt
  anyway for staleness — so the fix *could* have been applied and shipped with a matching
  render, and wasn't. Worth closing next time that slot is touched.

## Carry-forward items affecting the repo, not just EP13

1. **`tool/helpers/render.py:759` is patched in-tree.** Windows path separators are now
   normalized to forward slashes before the drive-colon escape, because ffmpeg's
   filtergraph parser eats backslashes as escapes and caption burn-in failed outright.
   No-op on POSIX, so the Mac is unaffected — but the vendored copy of video-use is now
   modified and that should survive any future re-vendoring.
2. **A shipped episode may have a stranded element.** The repeating-`fromTo`-beats-fade
   bug documented above was located by the slot_problem agent in
   `episodes/ep6-websockets/animations/slot_problem/index.html:148` —
   `{duration: 0.6, repeat: 3, yoyo: true}` starting at 4.8 runs to 7.2s against that
   clip's 5.8s end. Scoped out of EP13 deliberately. Worth checking EP6's shipped output.

## Outstanding

- HyperFrames pins 0.7.68 (latest 0.7.111). Lint substitutes 'Helvetica Neue' → Inter;
  EP4 uses the same stack so aliasing is consistent series-wide.
- `impact.mp3` is 7.91s native and needs `atrim` to ~1.5-2s for the flood hit.
- `system-design-overlays` skill still not registered in `~/.claude/skills/` — the repo
  copy was read directly instead. Registering it is a user-config change, left alone.
- Windows: renders should use `--workers 1 --no-browser-gpu`. The default spawns one
  Chrome worker per core and each opens a **visible** window on this machine.
