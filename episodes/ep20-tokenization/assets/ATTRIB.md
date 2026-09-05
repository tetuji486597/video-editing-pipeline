# EP20 asset usage notes

All four PNGs are deliberate product screenshots of https://platform.openai.com/tokenizer
(captured 2026-08-28, tokenizer setting "GPT-5.x & O1/3"; see `token_data.txt` for the
real values transcribed off the page). A deliberate product screenshot is the wanted
kind of real image for this beat — the tokenizer IS the subject.

## Used in overlays

- `ep20_tokenizer_strawberries_ids.png` → cropped to
  `animations/slot_tokens/assets/tokenizer_tokens_ids_crop.png`
  (ffmpeg `crop=1056:440:80:1064`). The crop keeps only the readout region —
  "Tokens 3 / Characters 19", the real ID array `[40, 3047, 106502]`, and the
  Text/Token IDs toggle. The page's "Platform / Developer Docs / Log in" header bar
  (unrelated chrome/branding) sits at y≈800-880 in the source capture and is fully
  cropped out. Inset in designed browser chrome in `slot_tokens`, with the URL pill
  reading `platform.openai.com/tokenizer` (deliberate product reference).

## Real values animated (not pasted as pixels)

- `slot_build` dramatizes the narration's split ("Rarer ones will split straw and
  berry"): `[I][ love][ straw][berries]`. The REAL capture tokenizes
  "I love strawberries" as 3 tokens `[I][ love][ strawberries]` — the 4-way split is
  the narration's dramatization, noted here so nobody "fixes" it against the capture.
- `slot_new_component` / `slot_payoff` token IDs:
  - `40` ("I") — REAL-VERBATIM from the capture.
  - `3047` (" love") — REAL-VERBATIM from the capture.
  - `1618` — real captured value for the "raw" chunk of `How many R's are in
    "strawberry"?` (st|raw|berry), ADAPTED here to label the dramatized " straw" chunk.
  - `19772` — real captured value for the "berry" chunk, ADAPTED to label
    "berries" in slot_new_component; used for "berry" in slot_payoff where it is
    real-verbatim for that chunk string.
- `slot_tokens` context meter (`128K`) and `$ / 1M TOKENS` chip are designed elements,
  not from the capture; the chip deliberately carries no invented price figure.

## Not used

- `ep20_tokenizer_strawberries_text.png` (page top; input box view) and
  `ep20_tokenizer_strawberry_question_text.png` /
  `ep20_tokenizer_strawberry_question_chunks_tight.png` (the st|raw|berry colored
  chunks) — the chunk colours from the tight crop are recreated as the pastel chip
  palette in slot_build/slot_new_component (style reference only, not pasted).
