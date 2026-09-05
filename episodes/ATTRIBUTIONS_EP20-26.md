# Asset attributions — EP20-26 batch

Sourced 2026-08-28. User said rights are not a concern for this batch (videos will not
be posted), but sources and licence notes are recorded anyway. Every raster file was
ffprobe-verified (sane dimensions, non-zero size, not an HTML error page). No site was
logged into; all captures are from signed-out public pages.

Use column: **direct** = may appear inside an overlay; **redraw-ref** = reference only,
must be redrawn, never composited into a frame.

## EP20 — tokenization

| File | Source | Licence note | Use |
|---|---|---|---|
| `ep20-tokenization/assets/ep20_tokenizer_strawberries_text.png` | https://platform.openai.com/tokenizer (public, no login; "GPT-5.x & O1/3" setting) | OpenAI product screenshot, captured as the subject of the beat | direct |
| `ep20-tokenization/assets/ep20_tokenizer_strawberries_ids.png` | same | same | direct |
| `ep20-tokenization/assets/ep20_tokenizer_strawberry_question_text.png` | same | same | direct |
| `ep20-tokenization/assets/ep20_tokenizer_strawberry_question_chunks_tight.png` | same (element crop of the chunk widget) | same | direct |
| `ep20-tokenization/assets/token_data.txt` | values read off the page | facts, no licence | data for overlay animation |

Key values: "I love strawberries" = 3 tokens `[40, 3047, 106502]`; the question
`How many R's are in "strawberry"?` = 11 tokens, with "strawberry" split st|raw|berry
(`302, 1618, 19772`). Full breakdown in `token_data.txt`. The primary
platform.openai.com page worked — the tiktokenizer fallback was not needed.

## EP21 — k-anonymity

| File | Source | Licence note | Use |
|---|---|---|---|
| `ep21-kanonymity/assets/ep21_hibp_pwned_fullpage.png` | https://haveibeenpwned.com/Passwords (dummy password `password123`) | HIBP product screenshot, captured as the subject | direct |
| `ep21-kanonymity/assets/ep21_hibp_search_and_result.png` | same (search box + result crop) | same | direct |
| `ep21-kanonymity/assets/ep21_hibp_pwned_result_tight.png` | same (tight "Oh no - pwned!" crop) | same | direct |
| `ep21-kanonymity/assets/range_CBFDA.txt` | https://api.pwnedpasswords.com/range/CBFDA | API response data, no licence concern | data for overlay animation |
| `ep21-kanonymity/assets/range_stats.txt` | derived from the above | — | data |
| `ep21-kanonymity/assets/redraw_ref/cf_hash_bucket.png` | https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/ (`_emdash/api/media/file/01KW48160JCYVRCXT490PY5GR2.png`) | Cloudflare blog illustration — © Cloudflare | **redraw-ref only** |
| `ep21-kanonymity/assets/redraw_ref/cf_hashes_by_prefix.png` | same post (`01KW48RBHQKM122VPS44PKYKYH.png`) | same | **redraw-ref only** |
| `ep21-kanonymity/assets/redraw_ref/cf_range_query_response.png` | same post (`01KW49KG9V4G2VGHNXSTQX55AB.png`) | same | **redraw-ref only** |

Key values: SHA-1("password123") = `CBFDAC6008F9CAB4083784CBD1874F76618D2A97`; range
response for prefix `CBFDA` contains **1972** suffix lines (the "crowd"); matching line
`C6008F9CAB4083784CBD1874F76618D2A97:2266543` — i.e. seen **2,266,543** times, and the
website UI reported the identical number.

## EP22 — webhooks

| File | Source | Licence note | Use |
|---|---|---|---|
| `ep22-webhooks/assets/redraw_ref/ep22_stripe_webhook_handler.png` | https://docs.stripe.com/webhooks ("Create a handler" section) | Stripe published docs — © Stripe | **redraw-ref only** |
| `ep22-webhooks/assets/redraw_ref/ep22_stripe_handler_code.png` | same (handler code with `Stripe-Signature` verification, `payment_intent.succeeded` case) | same | **redraw-ref only** |

**Not obtained:** the modern docs.stripe.com/webhooks page no longer carries a raster
flow diagram (page renders text + code only; the only image assets in the HTML are site
icons), and no published static screenshot of a Dashboard "payment succeeded" event was
found in the docs' static assets. Both were optional; the handler-code captures carry
the real signature-verification flow the overlay needs.

## EP23 — containers

| File | Source | Licence note | Use |
|---|---|---|---|
| `ep23-containers/assets/phippy_full.png` | github.com/cncf/artwork `other/phippy-and-friends/phippy_full.png` (linked from phippy.io) | phippy.io / CNCF, **CC-BY-4.0** | direct (transparent bg, rgba) |
| `ep23-containers/assets/captain_kube_full.png` | same repo | phippy.io / CNCF, CC-BY-4.0 | direct |
| `ep23-containers/assets/zee_full.png` | same repo | phippy.io / CNCF, CC-BY-4.0 | direct |
| `ep23-containers/assets/goldie_full.png` | same repo | phippy.io / CNCF, CC-BY-4.0 | direct |
| `ep23-containers/assets/container_ship.jpg` | https://upload.wikimedia.org/wikipedia/commons/7/7d/Port_Jersey_container_ship_sunset_2018.jpg | **CC BY-SA 2.0**, Eric Kilby (via Flickr) — credit needed if ever published | direct |

Container-ship note: the first candidate (MSC Carmen, Antwerp) was rejected for a huge
legible "MSC" hull logo; a Helsinki container-yard candidate was rejected for legible
HANJIN / MAERSK SEALAND / Hapag-Lloyd branding on the boxes. The Port Jersey sunset shot
(5568x3712) has no legible branding — trade-off: the containers read as silhouette
stacks under port cranes rather than close-up boxes.

## EP24 — kubernetes

| File | Source | Licence note | Use |
|---|---|---|---|
| `ep24-kubernetes/assets/server_rack.jpg` | reused from `ep18-urlrequest/animations/slot_payoff/assets/` — originally `images.unsplash.com/photo-1558494949-ef010cbdcc31` | Unsplash Licence | direct |
| `ep24-kubernetes/assets/phippy_full.png` + `captain_kube_full.png` + `zee_full.png` + `goldie_full.png` | copies of the EP23 CNCF files above | phippy.io / CNCF, CC-BY-4.0 | direct |

## EP25 — CI/CD

| File | Source | Licence note | Use |
|---|---|---|---|
| `ep25-cicd/assets/ep25_gha_run_viewport.png` | https://github.com/actions/runner/actions/runs/32968362960 ("Prepare 2.337.0 release", all green, signed-out) | GitHub product screenshot of a public repo run, captured as the subject | direct |
| `ep25-cicd/assets/ep25_gha_jobs_graph.png` | same run, "Matrix: build" expanded — 7 green build jobs + 2 docker jobs with timings | same | direct |

## EP26 — UDP

| File | Source | Licence note | Use |
|---|---|---|---|
| `ep26-udp/assets/redraw_ref/cf_tcp_vs_udp.svg` | https://www.cloudflare.com/img/learning/ddos/glossary/user-datagram-protocol-udp/tcp-vs-udp.svg (from the "What is UDP?" learning page) | Cloudflare learning-centre illustration — © Cloudflare | **redraw-ref only** |
| `ep26-udp/assets/redraw_ref/cf_tcp_handshake.png` | https://www.cloudflare.com/img/learning/cdn/tls-ssl/tcp-handshake-diagram.png (from the "What is TCP/IP?" page) | same | **redraw-ref only** |
