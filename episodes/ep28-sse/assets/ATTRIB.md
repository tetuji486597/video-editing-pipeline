# EP28 (SSE, brainrot edition) — asset usage and attribution

Every file below was ffprobe-verified before use (dimensions / pix_fmt in the table). Full
sourcing detail for the shared brainrot cast lives in `episodes/ATTRIBUTIONS_EP27-29.md`;
this file records what EP28's overlays actually USE and where.

| file | probe | source / licence | used in |
|---|---|---|---|
| `tralalero_tralala_render.png` | 583x581 rgba | stealabrainrot.fandom.com (Steal a Brainrot game-model render; AI-fan-art character, no rights-holder — Gordon: don't worry about rights for these) | `slot_hook` — the shark sprints under the typing line (130px, flipped to run right) |
| `trippi_troppi_render.png` | 383x651 rgba | stealabrainrot.fandom.com render | `slot_problem` — the confused user staring at the spinner (act 1), then dropped onto the grass (act 2); two `<img>` instances of the same file |
| `chimpanzini_bananini_render.png` | 504x476 rgba | stealabrainrot.fandom.com render | `slot_build` — nine monkeys, one word chip each, sprinting down the ONE PIPE chute |
| `lamelo_ball_allstar2022.jpg` -> `lamelo_67_sticker.png` | 2415x3242 yuvj444p -> 600x600 rgba | https://commons.wikimedia.org/wiki/File:LaMelo_Ball_(cropped).jpg — CC BY 2.0, Erik Drost. Cutout made by us: head-only circle crop (radius 440px about (1085,520)) with a white sticker ring; the crop deliberately excludes the jersey sponsor marks (KIA / Jumpman / NBA logo) that sit lower in the photo — no legible branding in the sticker. Public figure, the 6-7 meme IS him. | `slot_problem` (two pops, on each spoken "sixty-seven"), `slot_new_component` (one pop) |
| `amongus_red_crewmate_transparent.png` | 150x198 rgba | among-us.fandom.com (Innersloth sprite) | `slot_new_component` — the `NPC` at the bottom of the SSE pipe (shown at 140x185, <1x, no upscale) |
| `skibidi_toilet_transparent.png` | 678x1048 rgba | skibidi-toilet.fandom.com (DaFuq!?Boom! character render) | `slot_new_component` — yapping on top of the CHAT pipe |
| `cameraman_skibidi_normal_transparent.png` | 263x434 rgba | skibidi-toilet.fandom.com render | `slot_new_component` — yapping back at the bottom of the CHAT pipe (110x182, <1x) |
| `sse_devtools_capture.png` | 1554x873 rgb24 | our own headless-Chromium capture of https://stream.wikimedia.org/v2/stream/recentchange (public Wikimedia EventStreams SSE endpoint); the DevTools-style chrome is ours, the headers/chunks are real | `slot_new_component` act 2 — inset in a browser window, scrolled from the `content-type: text/event-stream` header to the chunk list |
| `sse_capture.txt` | text, 14 chunks | same endpoint via fetch()+ReadableStream | `slot_new_component` — the extra chunk rows 3-9 are the REAL events 3-9 from this file (event/data lines, sizes = byte length of each block, arrival offsets from each event's own meta.timestamp relative to chunk 2's +0.154s) |

Not used (available in `assets/`): `ballerina_cappuccina_*`, the `*_scene.png` variants
(need cutouts; the transparent renders were sufficient), `lamelo_ball_illawarra2019.jpg`
(carries a photographer watermark and jersey sponsors — rejected for the sticker),
`sse_capture_curl_raw.txt`.

All on-screen text authored for this episode is PG-13 (`SYBAU`, `ONE WAY ONLY`, `NPC`,
`TOUCH GRASS`, `AURA`, `6 7`, `MODEL`, `ONE PIPE`, `OPEN`, `FIRST WORD 0.5s`,
`WHOLE THING 1:07`, `SERVER-SENT EVENTS`, `SSE`, `CHAT`); the crude spoken lines
("raw dogging", "backshots", "Psy bow") are never printed.
