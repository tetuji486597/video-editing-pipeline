# Packed transcripts

Phrase-level, grouped on silences ≥ 0.5s or speaker change.
Use `[start-end]` ranges to address cuts in the EDL.

## ep5  (duration: 2m 28.7s, 20 phrases)
  [003.84-005.52] S0 You've definitely double-tapped.
  [014.28-019.48] S0 You've definitely double-tapped a pay button, so why weren't you charged twice?
  [028.41-029.04] S0 Here's the problem:
  [029.64-036.60] S0 networks are unreliable. Your phone sends "charge me" and the network drops the response, your app retries.
  [046.60-055.40] S0 Here's the problem: networks are unreliable. Your phone sends "charge me" and the network drops the response, your app retries, and a naï...
  [061.16-061.80] S0 Here's the problem:
  [062.32-065.96] S0 networks are unreliable. Your phone sends "charge me"
  [066.46-070.92] S0 and the network drops the response, your app retries, and a naïve server...
  [071.82-072.73] S0 And a naïve?
  [076.54-088.74] S0 Here's the problem: networks are unreliable. Your phone sends "charge me" and the network drops the response, your app retries, and a naïve server happily charges you a second time.
  [089.98-092.62] S0 The fix is an idempotency key,
  [093.20-099.08] S0 a unique ID your app generates for that one payment and attaches to every retry.
  [100.37-104.00] S0 The server records that key the first time it processes the charge.
  [104.52-109.98] S0 If it sees the same key again, it returns the original result instead of charging again.
  [110.78-114.68] S0 The same request sent any number of times has exactly...
  [121.40-126.36] S0 The same request sent any number of times has the effect exactly once.
  [127.98-128.68] S0 Press it twice,
  [129.26-136.80] S0 pay once. That's idempotency. Next episode, we'll talk about how WhatsApp delivers a message in one second.
  [143.98-147.32] S0 Press it twice, pay once. That's idempotency.
  [147.90-152.50] S0 Next episode, we'll talk about how WhatsApp delivers a message in one second.
