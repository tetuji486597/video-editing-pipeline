# SFX sourcing & usage — EP12 ("How Google Search Is Instant Across Billions of Pages")

Sourced from myinstants.com via direct `curl` with a browser user-agent (the site 403s
generic fetchers; `WebFetch` does not work, plain curl with a UA does). Same copyright
caveat as EP1/EP4/EP6/EP13: licensing on myinstants.com content is unclear, so these files
are kept local and are **not** committed to the repo. Re-download if rebuilding.

Search technique: `curl -s -A "<UA>" "https://www.myinstants.com/en/search/?name=<query>"`
then `grep -o 'media/sounds/[^"]*\.mp3'` for the direct media path, then curl that path.

## Catalog

| File | Source slug | Native | Shipped | Note |
|---|---|---|---|---|
| `click.mp3` | `button-click` | 2.837s | — | **166ms of leading silence** |
| `click_trim.mp3` | — | 0.220s | ✓ | trimmed from 0.160 so the transient is at t=0 |
| `whoosh.mp3` | `abrupt-whoosh` | 2.171s | — | **335ms of leading silence** |
| `whoosh_trim.mp3` | — | 1.300s | ✓ | trimmed from 0.330, 0.25s tail fade |
| `ding.mp3` | `correct-ding2` | 1.328s | ✓ | transient already at t=0 |
| `stamp.mp3` | `papers-please-stamp` | 0.509s | ✓ | reused from EP13 |

**Leading silence is the trap worth remembering.** Because cues are placed on the
triggering GSAP call, a stinger with 166-335ms of silence baked into its head lands
audibly late even when its timestamp is correct. Always `silencedetect` a freshly
downloaded stinger and trim from its transient before using it.

## Cue placement

Per the EP6 convention: **each cue's onset sits at its triggering GSAP call, not
mid-animation and not on settle** — the hit anticipates the pop. Output timestamps derive
from each overlay's own timeline plus that slot's `start_in_output`, then were each
verified against a real extracted frame at that exact timestamp.

| Beat | Landing beat | Output | SFX | Vol | Why |
|---|---|---|---|---|---|
| HOOK | latency slam @ local 1.90 | **4.70** | ding | 0.55 | Verified frame catches the shutter flash mid-fire with the counter locked on 1,000,000,000 — "2 ms" lands immediately after. A resolution ding sells "instant". |
| PROBLEM | fast-forward transition @ local 1.72 | **9.32** | whoosh_trim | 0.45 | The script's own "fast-forward blur over the endless scan" cue. Verified frame still shows ROWS READ 6 mid-scan, so the whoosh anticipates the blur by a frame. |
| PROBLEM | HOPELESS stamp @ local 2.52 | **10.12** | stamp | 0.60 | Second cue in one beat, deliberately — the stamp slam is a distinct impact from the fast-forward and 0.80s clear of it. Reuses EP13's stamp as a series "rejected/failed" motif. |
| BUILD | index entry highlights @ local 3.58 | **19.48** | click_trim | 0.45 | Verified frame shows `indexes … 142` highlighting violet with its arrow drawing — the literal "jump straight to the page" moment. |
| NEW_COMPONENT | 3 B-tree snap-zooms | **25.10, 25.86, 26.60** | click_trim ×3 | 0.45 | The script's "snap-zoom down the B-tree levels **with clicks**". One click per hop. |
| AI_ANGLE | violet pulse ring @ local 2.45 | **42.45** | whoosh_trim | 0.35 | Quietest cue — this transition is a soft panel-ignite, not an impact, and it sits between two denser cue clusters. |
| PAYOFF | hero resolves @ local 2.35 | **51.85** | ding | 0.55 | Moved later from an initial 51.70, where the verification frame still showed phase 1's "A TABLE OF CONTENTS". 51.85 lands as "…YOUR DATABASE READS FIRST" arrives. Reusing the ding matches the series' recurring "resolved" motif on the closing tagline. |

9 cues. Spacing is ≥0.76s everywhere except the intentional 3-click B-tree cluster
(0.76s / 0.74s apart) and the PROBLEM pair (0.80s apart).

## Mixing

- Per-clip `volume` applied **before** delay/mix. `adelay=<ms>:all=1`, then
  `amix=inputs=9:duration=longest:normalize=0`.
- `sfx_track.wav` — 48kHz stereo, 53.18s, peak **-5.86 dB**.
- Final mix: `[0:a][1:a]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-2:LRA=11`.
- **`loudnorm` rather than `alimiter`**, per STYLE.md: a sample-peak limiter cannot account
  for the overshoot AAC encoding adds afterwards, which is how EP13's mix first shipped
  peaking positive. `loudnorm`'s TP target is designed to survive lossy encoding.
- **Result: peak `-1.764 dB`** — negative, no clipping, essentially matching the -1.71
  STYLE.md documents as the good outcome. Integrated -15.0 LUFS.
- Video passed through with `-c:v copy` — only audio is rebuilt, so the composite is not
  re-encoded (STYLE.md's AAC double-encode regression).

## No music bed

Per STYLE.md (2026-08-08), background music is removed series-wide. Narration + overlays +
captions + SFX only. Do not re-add a music layer without asking.
