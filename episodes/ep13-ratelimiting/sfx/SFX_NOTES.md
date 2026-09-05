# SFX sourcing & usage — EP13 ("Why You Get 'Too Many Requests'")

All four stingers sourced from myinstants.com, downloaded via direct `curl` with a
browser user-agent (the site 403s generic fetchers — `WebFetch` does not work, plain
`curl -A "Mozilla/5.0 ..."` does). Same copyright caveat as EP1/EP4/EP6: licensing on
myinstants.com content is unclear, so these files are kept local and are **not**
committed to the video-editing-pipeline git repo. Re-download if rebuilding.

Search technique that worked: `curl -s -A "<UA>" "https://www.myinstants.com/en/search/?name=<query>"`
then `grep -o 'media/sounds/[^"]*\.mp3'` to find the direct media path, then `curl` that
same path (same UA) into `sfx/<name>.mp3`.

## Catalog

| File | Source slug | Native dur | Used as |
|---|---|---|---|
| `drip.mp3` | `water-droplet-drip` | 0.496s | token drips (BUILD) |
| `stamp.mp3` | `papers-please-stamp` | 0.509s | 429 slams (HOOK, NEW_COMPONENT) |
| `ding.mp3` | `correct-ding2` | 1.328s | resolved motif (PAYOFF) |
| `impact.mp3` | `zapsplat_..._whoosh_into_impact_..._29904` | 7.908s | server flood (PROBLEM) |
| `impact_trim.mp3` | — | 1.600s | trimmed from `impact.mp3`, 0.25s tail fade |

`impact.mp3` at 7.9s native is far too long for a single hit; trimmed to 1.6s with
`-t 1.6 -af "afade=t=out:st=1.35:d=0.25"`. `silencedetect` confirmed no leading silence,
so the transient sits at t=0 and the trim needs no offset.

## Cue placement

Following the EP6 convention: **each cue's onset sits at its triggering GSAP call, not
mid-animation and not on settle** — the hit anticipates the pop. Output timestamps are
derived from each overlay's own timeline comments plus that slot's `start_in_output` in
`edl.json`, not guessed from the script.

| Beat | Overlay local landing beat | Output | SFX | Vol | Why |
|---|---|---|---|---|---|
| HOOK | shutter flash / 429 toast slam @ local 1.76 | **4.56** | stamp | 0.6 | Verified frame at 4.56 catches the white shutter flash mid-fire with the counter frozen at 8 — the toast slams immediately after. |
| PROBLEM | flood transition @ local 1.90 | **9.10** | impact_trim | 0.55 | Verified frame still shows `42 req/s HEALTHY` — the cue anticipates the flood by a frame, which is the intended convention. Slightly lower volume; it is the longest cue and sits under narration. |
| BUILD | 6 token drips @ local 1.95/2.25/2.55/2.85/3.15/3.45 | **17.55, 17.85, 18.15, 18.45, 18.75, 19.05** | drip ×6 | 0.5 | Exactly 0.30s apart, matching the composition's deliberately even drip spacing — the "steady rate" is the point of the beat. Verified frame at 17.55 shows the first token in flight above the bucket. Quietest cue since it fires six times. |
| NEW_COMPONENT | hero `429` slam @ local 4.80 | **26.50** | stamp | 0.6 | Reuses the same stamp as HOOK deliberately — a recurring "rejected" motif across the two 429 moments. Verified frame shows `BUCKET EMPTY → THROTTLED` with the hero numeral just beginning its scale-in. |
| PAYOFF | hero line lands | **48.10** | ding | 0.6 | Moved later from an initial 47.65: the verification frame at 47.65 showed only the warmed photo with no type yet, so the cue would have fired into empty frame. 48.10 lands as "A BUCKET OF TOKENS" arrives. Matches the series' recurring "resolved" ding on the closing tagline (EP1/EP3/EP4/EP5/EP6). |

AI_ANGLE deliberately carries **no cue** — its transition is a soft panel-ignite rather
than an impact, and the two stamps plus the drip cluster already sit close by. Adding a
sixth hit there would crowd the back half.

Cue spacing: all cues are ≥4s apart except the intentional 0.30s drip cluster.

## Mixing

- Per-clip `volume` applied **before** delay/mix (see table). `adelay=<ms>:all=1` for
  placement, then `amix=inputs=10:duration=longest:normalize=0`.
- `sfx_track.wav` — 48kHz stereo, 49.43s (last cue 48.10 + ding 1.33s), peak **-4.94 dB**.
- Final mix: `[0:a][1:a]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-2:LRA=11`.
- **`loudnorm` is used instead of `alimiter` deliberately.** STYLE.md records that on this
  very episode `alimiter` still let the AAC-encoded output peak positive (+0.05 to
  +0.08 dB) even at `limit=0.7:attack=1`, because a sample-peak limiter cannot account
  for the overshoot AAC encoding adds afterwards. `loudnorm`'s `TP` target is designed to
  survive lossy encoding.
- **Result: peak `-0.762 dB`** — negative, so no clipping. (Verified with
  `ffmpeg -i <final> -af astats -f null - 2>&1 | grep "Peak level dB"`; a positive number
  would mean it clipped.)
- Video is passed through with `-c:v copy` — only the audio is rebuilt, so the composite
  is not re-encoded.

## No music bed

Per STYLE.md (2026-08-08), background music is removed entirely across the series. This
mix is narration + overlays + captions + SFX only. Do not re-add a music layer without
asking.
