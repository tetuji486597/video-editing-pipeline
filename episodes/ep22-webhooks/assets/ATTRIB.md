# EP22 — real-image usage record

## Direct-use (in a shipped overlay)

- **`animations/slot_sign/assets/stripe_sig_code.png`** — cropped from
  `assets/redraw_ref/ep22_stripe_handler_code.png` (capture of Stripe Docs, "Webhook
  endpoint → Create a handler", docs.stripe.com — the sample webhook-handler code).
  Crop: `1010x344` at `(443, 426)` of the 1554x873 capture — the code surface only
  (lines 26-37: `signature = request.env['HTTP_STRIPE_SIGNATURE']`,
  `Stripe::Webhook.construct_event(...)`, `rescue Stripe::SignatureVerificationError`).
  Used as a DIRECT-USE inset in `slot_sign` (the SIGN beat), dimmed
  (`brightness(0.82) saturate(0.95)`) inside designed card chrome labelled
  "stripe docs · webhook handler". This is a deliberate product screenshot of the real
  thing the beat describes (verifying the `Stripe-Signature` header) — the episode's
  required real image. The crop contains no Stripe nav/branding chrome; the narration
  names Stripe explicitly, so the deliberate-product-screenshot rule applies.

## Redraw-reference only (NOT pasted into any frame)

- `assets/redraw_ref/ep22_stripe_webhook_handler.png` — Stripe Docs "Create a handler"
  prose page. Style reference for the POST/SIGN beat recreations only.
- `assets/redraw_ref/ep22_stripe_handler_code.png` — full capture (the direct-use crop
  above is taken from it; the full frame with Stripe Docs nav/branding is NOT used).

Recreated UI in `slot_post` / `slot_hook` / `slot_build` is Stripe-LIKE, built from
scratch (`POST /webhooks/stripe`, `"type": "payment_intent.succeeded"`, a Stripe-named
notification) — naming Stripe is intentional since the narration names the provider.
