# EP23 asset attributions & usage

Sources and licences as recorded at sourcing time (see `episodes/ATTRIBUTIONS_EP20-26.md`
for the batch-level log — this file records EP23's actual in-overlay usage).

| File | Source | Licence | Used in |
|---|---|---|---|
| `phippy_full.png` | github.com/cncf/artwork `other/phippy-and-friends/phippy_full.png` (linked from phippy.io) | phippy.io / CNCF, **CC-BY-4.0** | `animations/slot_runs/` — Phippy peeks out of the hopping container box (head visible above the box rim, body clipped behind the box front panel). Copy at `animations/slot_runs/assets/phippy_full.png`. |
| `captain_kube_full.png` | same repo | CC-BY-4.0 | not used in EP23 (reserved for EP24 payoff) |
| `zee_full.png` | same repo | CC-BY-4.0 | not used in EP23 |
| `goldie_full.png` | same repo | CC-BY-4.0 | not used in EP23 |
| `container_ship.jpg` | https://upload.wikimedia.org/wikipedia/commons/7/7d/Port_Jersey_container_ship_sunset_2018.jpg | **CC BY-SA 2.0**, Eric Kilby (via Flickr) — credit needed if ever published | `animations/slot_payoff/` — full-bleed hero, dimmed (brightness 0.62), masked off below ~y=1240, scrim + multi-layer text-shadow under the type. Pre-cropped 1080x1920 vertical band centred on the ship stern: `crop=2088:3712:1456:0,scale=1080:1920` → `animations/slot_payoff/assets/ship_crop.jpg`. |

Branding note: the ship's stern name ("HELSINKI BRIDGE") is faintly present in the source
at crop y≈1265 — that row sits inside the mask fade-out (1180→1300) and under the 0.62
brightness dim, and is not legible in the rendered frame (verified on a native-resolution
crop during the build). Container stacks read as silhouettes; no other marks.
