# EP5 trending SFX — sourcing + usage reference

Source: myinstants.com, same approach as EP1/EP4. All five clips here are reused from
those episodes' already-downloaded files (see EP1's `sfx/SFX_NOTES.md` for the general
sourcing method and the licensing caveat) rather than freshly downloaded — reuse keeps
the same trending-meme vocabulary consistent across the series without adding new
untracked myinstants.com downloads.

## Catalog — what each one is commonly used for

| File | Sound | Commonly used for | Feel |
|---|---|---|---|
| `record_scratch.mp3` | Record Scratch | A "wait, what?" rhetorical-question beat — needle-scratch stopping the moment cold. | Vinyl scratch, ~1s |
| `wrong_buzzer.mp3` | Game-show wrong buzzer | A bug/failure moment — something just went wrong. | Harsh buzzer, ~1.2s |
| `vine_boom.mp3` | Vine Boom | A dramatic reveal/statement landing with weight. | Deep bass hit, ~1s |
| `camera_shutter.mp3` | Camera Shutter | A snapshot/logging/"this just got recorded" moment (reused from EP4). | Sharp click, 0.88s |
| `correct_ding.mp3` | Correct Answer (game-show ding) | Resolution/"solved" moment — recurring series motif for payoff-style beats. | Bright upward chime, ~1.3s |

## How this episode (EP5 — idempotency keys) used them

**Retimed 2026-08-08** — the timestamps below were originally set against the script/
narration, but the overlays have since been rebuilt/repositioned (caption-collision
fixes moved `slot_hook`/`slot_payoff` text, `slot_problem` became a full-screen takeover,
and the old separate "dedup" concept was merged into `slot_ledger`). New timestamps are
derived directly from each overlay's own GSAP timeline — its documented/identifiable
"landing beat" local time — plus the EDL's `start_in_output` for that slot, not
re-guessed from the script. Music has also been removed entirely (no `music_final.wav`
in the mix anymore).

| Beat | Overlay local landing beat | Old ts | New ts | SFX | Why |
|---|---|---|---|---|---|
| HOOK | `#e1` "CHARGED ONCE." pops in @ local 0.55s | 4.9s | **3.35s** | Record Scratch | The "wait, only once?" twist landing. Old cue was 1.55s late relative to this overlay's actual reveal. |
| PROBLEM | both charge cards + "CHARGED TWICE." confirmed @ local ~4.3-4.6s | 17.4s | **10.52s** | Wrong Buzzer | Old cue (17.4s) fell in the dead-air gap between the problem overlay ending (12.7s) and the build overlay starting (18.96s) — synced to nothing at all. |
| BUILD | ticket + key-code fully settled @ local ~0.6s | 19.3s | **19.56s** | Vine Boom | Barely moved (+0.26s) — this overlay's internal timing hadn't drifted much; now nails the exact settle point instead of landing slightly before it. |
| NEW_COMPONENT (ledger, phase 1) | "stamp" lands @ local 1.0s (back.out ease) | 27.5s | **29.00s** | Camera Shutter | The "first time seen, logged" moment, now matched to the stamp's actual landing instant. |
| NEW_COMPONENT (ledger, phase 2) | "Not charged again." tagline starts to reveal @ local 4.75s | 32.0s | **32.75s** | Correct Answer ding | Small drift (+0.75s) — now lands exactly on the resolution tagline's onset instead of just before it. |

PAYOFF_NEXT still has no added stinger — the closing line ("Press it twice, pay once.")
is short and punchy enough on its own; a 6th sound in an ~8s beat still reads as overkill.

## Mixing notes

- Levels: `volume=0.6` applied per-clip before delay/mix (same estimate as before, not
  confirmed by ear against final loudnorm output).
- All five clips are short (<1.3s) one-shots, no trimming needed.
- Rebuilt as `sfx_track_v2.wav` via a single `ffmpeg -filter_complex` pass
  (`volume` + `adelay` per clip + `amix duration=longest`), then mixed directly onto
  `base_v6.mp4` (narration-only) with `amix duration=first` — no music track involved.
