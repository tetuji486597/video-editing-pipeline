# Trending TikTok/meme SFX — sourcing + usage reference

Source: myinstants.com (soundboard of ripped meme/show/movie audio — **not royalty-free**;
reused here at Gordon's explicit direction after flagging the licensing risk, see
project.md session log). Downloaded via direct `/media/sounds/<file>.mp3` links, browser
User-Agent required (myinstants 403s a bare `curl`/no-UA request).

For future episodes: search `https://www.myinstants.com/en/search/?name=<query>` (URL-encode
spaces as `+`). The generic query `tiktok` mostly surfaces random meme-name audio, not the
classic editing stingers — search for the *stinger by function* instead (see table).

## Catalog — what each one is commonly used for

| File | Sound | Commonly used for | Feel |
|---|---|---|---|
| `vine_boom.mp3` | Vine Boom | The single most common short-form edit stinger — punctuates a hard cut, a punchline, a dramatic reveal, or a "beat drop" moment. Works on almost any hard emphasis beat. | Deep, percussive impact, ~1.2s |
| `wrong_buzzer.mp3` | Wrong Answer Buzzer (game-show style) | Marking something as a mistake/fail/bad-idea — "well that was wrong," a blooper, a naive/incorrect approach being called out. | Harsh buzz, ~1.1s |
| `correct_ding.mp3` | Correct Answer (game-show ding) | The inverse — marking a win/solved/"yes, this is right" moment. Common on "aha" or resolution beats. | Bright upward chime, ~1.3s |
| `record_scratch.mp3` | Record Scratch | The classic "wait, what?" / narrative-freeze stinger — used right as a plot twist or surprising fact lands, often paired with a freeze-frame in meme edits. | Vinyl scratch, ~0.9s |
| `suspense_strike.mp3` | Suspense Strike/Riser | Tension-building before a reveal — used in the second or so *before* a punchline/twist rather than on the punchline itself. | Rising cinematic hit, ~3.1s (trim to taste) |
| `bruh.mp3` | "Bruh" sound effect | Comedic exasperation/facepalm — used when something is relatable-annoying or painfully slow/inconvenient, played for a wry laugh rather than genuine shock. | Deep spoken "bruh," ~0.8s |

## How this episode (EP1 — password hashing) used them

| Beat | Output timestamp | SFX | Why |
|---|---|---|---|
| HOOK — "...RUN." | ~3.05s | Vine Boom | Hard punctuation on the hook's payoff word |
| PROBLEM — "wide open" (jar bursts) | ~14.72s | Wrong Answer Buzzer | Naive plain-text storage = the "wrong answer" |
| BUILD — "impossible to reverse" | ~25.89s | Record Scratch | The "wait, you truly can't undo this?" twist |
| NEW_COMPONENT (rainbow) — build-up into "passwords." | starts ~27.0s, lands ~29.88s | Suspense Strike | Tension into the attacker's-tool reveal |
| NEW_COMPONENT (salt) — "...are useless." | ~39.89s | Correct Answer ding | Callback: the defense "wins" |
| NEW_COMPONENT (bcrypt) — "...painful too." | ~43.98s | Bruh | Wry acknowledgment of deliberate slowness |
| PAYOFF — "...riddle..." | ~47.41s | Correct Answer ding (reused) | Callback to the salt beat's "solved" sound — same motif closing the episode |

Roughly one stinger every ~7-9s — sparse enough not to read as chaotic, landing only on
beats that already have a hard emphasis/twist/payoff in the script.

## Mixing notes

- Levels tuned by estimate (0.55-0.7 relative to narration, panned center, no ducking needed
  since each is <3.5s and lands in natural pause/emphasis points) — **not yet confirmed by ear**,
  same caveat as the music bed.
- Suspense Strike is 3s but only ~1.5-2s of its rise is used before the payoff lands; trimmed
  via `atrim` rather than played in full, so it doesn't run past the beat it's building into.
