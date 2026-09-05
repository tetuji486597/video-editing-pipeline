# EP14-19 overlay batch — format plan and per-slot briefs

Read `OVERLAY_SPEC.md` in full first. This file only adds what is specific to these six
episodes: which format each beat gets, the two acts and the turn between them, which real
image anchors it, and the output-timeline second on which the key visual must land.

All times below are **output-timeline seconds** (the finished video's clock), already
derived from the real 24fps extract grid via `tool/helpers/fix_windows.py`. Do not
recompute them from the source ranges.

> **The EDL is authoritative for `start_in_output` and `duration`.** These headings are
> synced from `episodes/*/edl*.json`. If they ever disagree, believe the EDL and re-sync
> this file -- a slot built to a stale duration renders the wrong length and its
> enable-window either truncates the fade or exposes bare footage at the tail.

## Format-mix audit (run at planning, per rule 7 — not after building)

| Episode | Formats used, in beat order | Distinct | Takeovers | Adjacent repeat? |
|---|---|---|---|---|
| EP14 | motion-gfx, TAKEOVER, half-panel, TAKEOVER, transparent, motion-gfx, photo-card | 5 | 2 | none |
| EP15 | half-panel, TAKEOVER, transparent, TAKEOVER, motion-gfx, half-panel | 4 | 2 | none |
| EP16 | motion-gfx, TAKEOVER, half-panel, TAKEOVER, motion-gfx, corner, photo-card | 5 | 2 | none |
| EP17 | half-panel, TAKEOVER, transparent, full-bleed-photo, half-panel, motion-gfx, TAKEOVER, photo-card | 6 | 2 | none |
| EP18 | transparent, TAKEOVER, half-panel, motion-gfx, TAKEOVER, full-bleed-photo | 5 | 2 | none |
| EP19 | half-panel, TAKEOVER, motion-gfx, transparent, corner, TAKEOVER, full-bleed-photo | 6 | 2 | none |

Every episode clears the >=3-distinct-formats bar and the <=2-takeovers cap, and no
episode uses the same format on two consecutive beats.

## Real images

**Shared, already vetted — use these, do not re-source:** `shared_assets/feed/*.jpg`
(16 real photos: puppy, pasta, sunset, lakes, mountains, pancakes, dog, fjord,
strawberries, teapot, waterfall — these are the *feed content* in EP14, i.e. literally
the posts being lazy-loaded), `shared_assets/misc/card_chip.jpg`,
`card_terminal.jpg` (real hands using a real card terminal — the swipe EP17 is about),
`ronaldo.png` (real photo of the public figure whose post is EP19's subject; only
424x362, re-source a higher-res one if you can), `stadium_crowd.jpg`,
`tinyurl_ui.jpg` (real shortener UI captured this session).

**Rejected — do NOT reuse these from `_overlay_snapshots/`.** All four are visual puns,
which is the exact failure the spec calls out:
`keys.jpg` (metaphor for OAuth), `directory_page.jpg` (dictionary page as a metaphor for
DNS — named in the user's own feedback), `mask.jpg` ("costume" pun for EP16),
`cables.jpg` (generic filler).

**Real data captured this session, use it verbatim.** A real `nslookup google.com` run on
this machine returned `172.217.72.139` (plus .113/.100/.102/.101/.138 and IPv6
`2607:f8b0:4023:1013::64`). EP18's DNS beat renders this real answer, not an invented one.
Do not include the resolver line — it is a private LAN address.

---

# EP14 — infinite feeds (7 beats, 55.875s total)

`episodes/ep14-infinitescroll/edl.json`

### slot_title — 0.000, 2.766s
House pattern, transparent, top-left `#block { left:70px; top:190px }`. Thin accent bar +
`SYSTEM DESIGN · 14` kicker + headline **Why Feeds Never End**. Nothing else.

### slot_hook — start 0.000, duration 7.600  (beat 0.000-8.042) — MOTION GRAPHIC
Narration: "So you're doom scrolling TikTok, and it seems to never end..."
Runs *simultaneously* with the title, so it must live in the **right half only**
(x >= 560) and stay clear of the title block. This is deliberate: an opaque format here
would have to wait 2.8s for the title and the beat's idea would land late (rule 10).
- **Act 1** — a vertical column of real feed photos scrolls upward at constant velocity
  (`ease:"none"` is correct here — a scroll that decelerates reads as ending). A scrollbar
  track on the far right has a thumb that shrinks as it descends.
- **Turn (~2.2s)** — the thumb collapses to a sliver and the track's bottom end fades out.
- **Act 2** — the column keeps flowing, now with no visible end to the track.
- **Lands on:** "never end" at **1.97-2.44**.
- Real images: 6-8 from `shared_assets/feed/`.
- Text: none beyond an optional 2-word label. The motion is the message.

### slot_problem — start 8.900, duration 5.600  (beat 8.042-15.083) — FULL-SCREEN TAKEOVER
Narration: "Loading all ten thousand posts up front would burn data, memory, and make the
app freeze before showing anything."
- **Act 1** — a phone frame; feed tiles pour in from the top far faster than they can
  render, stacking past the viewport. A memory meter climbs.
- **Turn (~4.6s local)** — a desaturate hit and a hard stutter.
- **Act 2** — everything locks. The spinner stops mid-rotation, the meter pins at max,
  nothing paints.
- **Lands on:** "freeze" at **13.53**.
- Text budget: headline <=6 words; **one** number only (`10,000`); one label (`MEMORY`).

### slot_build — start 15.900, duration 6.600  (beat 15.083-23.333) — HALF-SCREEN PANEL
Narration: "So we lazy load. Only fetch what's about to enter the screen as you scroll
near the bottom. The app quietly requests the next batch."
Panel occupies the **lower** content band (roughly y=660-1270); the presenter's face stays
visible above it. Grid-measure the face on this footage before fixing the top edge.
- **Act 1** — a viewport window slides down a long column. Tiles inside it are real
  photos; tiles outside are grey skeletons.
- **Turn** — the window reaches the bottom edge and a request pulse travels out of frame.
- **Act 2** — three new skeletons appear below and fill in with real photos.
- **Lands on:** "requests the next batch" at **22.03**.

### slot_new_component — start 24.200, duration 9.200  (beat 23.333-33.667) — TAKEOVER
Narration: "...we use cursor pagination. Hey, give me items after this ID instead of page
numbers, which break when new posts arrive mid-scroll."
The episode's densest beat and its second (final) takeover.
Note the act order is driven by the words: the cursor is named *first*, the breakage
*last*, so the overlay resolves on the broken state.
- **Act 1 (cyan)** — a request line assembles: `GET /feed?after=post_8f2c`. A batch
  returns and anchors to that item.
- **Turn (~5.3s local)** — shutter flash + colour phase-shift to amber.
- **Act 2 (amber)** — the page-number alternative: `?page=2`. A new post arrives at the
  top, every row shifts down one, and one item appears **twice** — flagged red.
- **Lands on:** "cursor pagination" at **25.76**; the duplicate flags on "which break when
  new posts arrive mid-scroll" at **31.12-33.52**.
- Text budget: `after=post_8f2c` is the one hero string. `page=2` only exists in act 2 and
  never co-occurs with it — say so in your collision report.

### slot_recycle — start 34.300, duration 6.500  (beat 33.667-41.417) — TRANSPARENT BAND
Narration: "Items above the screen can even be unloaded to save memory. The feed feels
infinite because the work is spread across your scrolling."
Linework and type over live footage. **No opaque fill.** Translucent fills <=0.32 alpha,
border + glow for definition (rule 11 — a solid chip here would have to be pinned to the
frame edge; a lightened one can sit naturally).
- **Act 1** — a slim vertical strip on the LEFT (keep x within roughly 60-320, and
  grid-measure the presenter's face on this footage first): tiles above the fold dissolve
  into particles one at a time; a small memory meter drops.
- **Turn** — the meter settles and a cyan infinity glyph draws itself.
- **Act 2** — the strip extends past both edges of frame with a gentle continuous loop.
- **Lands on:** "unloaded to save memory" at **35.58**; "feels infinite" at **37.90**.

### slot_ai_angle — start 42.100, duration 6.600  (beat 41.417-49.333) — MOTION GRAPHIC
Narration: "Which batch you get isn't random. A recommendation model decides what to lazy
load. So loading and ranking happen together."
- **Act 1** — six real photo tiles fan out as candidates. Score chips tick in **one at a
  time** (>=0.6s apart).
- **Turn** — a ranking sweep line passes across them.
- **Act 2** — the tiles physically reorder by score and the top three slide into the
  "next batch" slot.
- **Lands on:** "isn't random" at **43.71**; "decides what to lazy load" at **45.55**.
- **Hard text limit: at most two score numbers visible at any instant.** Fade each chip
  out as the next arrives — do not end with six numbers on screen.

### slot_payoff — start 49.600, duration 5.400  (beat 49.333-55.875) — STATIC PHOTO CARD
Narration: "Load what they see, not what they might see."
Deliberately still — the quiet contrast beat. One real feed photo as a large, sharp,
well-lit card; behind it, ghosted grey cards representing what was never loaded.
- **Act 1** — the card lands and holds with a slow drift (no push-in beyond ~1.03).
- **Turn** — the ghost cards behind fade out entirely, leaving only the one real card.
- **Lands on:** "Load what they see" at **49.38**; "not what they might see" at **50.86**.
- **NO next-episode tease chip.** Grep your own markup for `class="tease`, `id="tease`,
  `<span>Next` before you report — the words never appear literally (`&mdash;` + CSS
  uppercase) and this has slipped through twice.

---

# EP15 — OAuth (6 beats, 46.333s total)

`episodes/ep15-oauth/edl.json`

### slot_title — 0.000, 2.766s
`SYSTEM DESIGN · 15` + headline **How "Sign In With Google" Works**.

### slot_hook — start 0.000, duration 5.900  (beat 0.000-6.542) — HALF-SCREEN PANEL
Narration: "So you clicked sign in with Google and got into an app you've never given a
password to. That's called OAuth."
Lower-half panel so it can run under the title. **Needs a real image**: WebSearch for and
download a real screenshot of a real app's login screen showing a "Continue with Google" /
"Sign in with Google" button (public login pages only — do not log into anything). Inset
it in designed card chrome.
- **Act 1** — the login card, with the Google button highlighted.
- **Turn** — the button is pressed; a redirect chip flies out of the card.
- **Act 2** — the app door opens with **no password field ever filled** — show the password
  row struck through / never touched.
- **Lands on:** "That's called OAuth" at **4.99-6.15**.

### slot_problem — start 7.400, duration 6.400  (beat 6.542-14.667) — TAKEOVER
Narration: "This is the bad old way. Give every app your Google password. Now they can do
anything forever and a breach exposes everything."
- **Act 1 (blue)** — the same password chip is handed to four different app cards in
  sequence, each one accepting it.
- **Turn (~3.4s local)** — red flash.
- **Act 2 (red)** — one card breaches; the password leaks out of it and every other card
  lights red in a chain.
- **Lands on:** "Give every app your Google password" at **8.35**; "a breach exposes
  everything" at **12.91**.

### slot_build — start 15.400, duration 5.600  (beat 14.667-21.208) — TRANSPARENT BAND
Narration: "OAuth replaces that with a valet key. The app redirects you to Google. You log
in with Google and not the app."
Linework over live footage, no opaque fill.
- **Act 1** — a redirect path draws: APP -> GOOGLE.
- **Turn** — the path reverses direction.
- **Act 2** — GOOGLE -> APP completes the round trip, with the login happening on the
  Google node, visibly not the app node.
- **Lands on:** "You log in with Google and not the app" at **18.90-21.02**.

### slot_new_component — start 22.000, duration 7.300  (beat 21.208-29.583) — TAKEOVER
Narration: "Google asks, 'Allow this app to see your email and name?' You approve and
Google hands the app a limited access token, not your password."
The episode's hero beat. **Needs a real image**: source a real Google OAuth consent-screen
screenshot (Google's own published developer documentation is the safe source — it is a
deliberately-published product screenshot). Inset it inside the designed sheet chrome
rather than using it full-bleed.
- **Act 1** — the consent sheet rises; the scope rows list in staggered (>=0.6s apart):
  email, then name. Only two.
- **Turn** — Allow is pressed; the sheet dismisses with a flash.
- **Act 2** — a token chip is emitted and travels to the app, while a password vault
  beside it stays visibly shut.
- **Lands on:** the consent question at **22.09-24.16**; "limited access token" at
  **27.00**.

### slot_scope — start 30.300, duration 6.800  (beat 29.583-37.708) — MOTION GRAPHIC
Narration: "The app uses that token, which is scoped to only what you allowed and can be
revoked anytime. The app never sees your credentials."
- **Act 1** — the token as an object with a ring of eight permission slots; only two light
  up. The other six stay dark.
- **Turn** — a revoke switch flips.
- **Act 2** — the token dissolves and the app's access goes dark, while the account itself
  is untouched.
- **Lands on:** "scoped to only what you allowed" at **31.25**; "revoked anytime" at
  **33.76**.

### slot_payoff — start 38.100, duration 6.400  (beat 37.708-46.333) — HALF-SCREEN PANEL
Narration: "So OAuth is a valet key, access without the master key."
- **Act 1** — two cards settle side by side: a MASTER KEY card, dark and locked, and a
  TOKEN card, lit.
- **Turn** — the master-key card recedes and dims out of the composition.
- **Act 2** — the token card holds alone, breathing gently.
- **Lands on:** "access without the master key" at **40.18-41.78**.
- **NO tease chip.**

---

# EP16 — URL shortener (7 beats, 48.208s total)

`episodes/ep16-urlshortener/edl.json`

### slot_title — 0.000, 2.766s
`SYSTEM DESIGN · 16` + headline **How A Link Becomes Six Characters**.

### slot_hook — start 0.000, duration 5.200  (beat 0.000-5.667) — MOTION GRAPHIC
Narration: "A two hundred character link becomes six characters. Simple idea, surprisingly
neat system."
Right-half / lower placement so it can run under the title.
- **Act 1** — a genuinely long URL (make it a real ~200-char URL with query params and a
  tracking string) streams in and wraps across three lines.
- **Turn** — a compression sweep passes through it.
- **Act 2** — it collapses into `tinyurl.com/3mK9Qa`, which lands large.
- **Lands on:** "becomes six characters" at **1.57-2.93**.
- The URL string counts as *one* number and it is the subject, so it is within budget.

### slot_problem — start 6.500, duration 6.800  (beat 5.667-14.125) — TAKEOVER
Narration: "So you might think it hashes the URL, but you want the shortest possible code
and no collisions. Random hashing gives you neither cleanly."
- **Act 1** — two different URLs feed into a hash function and produce two long hex
  digests. Correct, but far too long.
- **Turn** — a truncation blade cuts both digests short.
- **Act 2** — the two truncated codes are **identical**: a collision, flagged red.
- **Lands on:** "no collisions" at **10.30**; "gives you neither cleanly" at **11.80**.

### slot_build — start 14.900, duration 6.600  (beat 14.125-22.167) — HALF-SCREEN PANEL
Narration: "Instead, every new link gets a unique number from a counter, one, two, three,
and so on. Then we encode that number in Base62."
- **Act 1** — links arrive and a counter increments 1, 2, 3 in step with the narration.
- **Turn** — the counter's current value detaches and drops into an encoder.
- **Act 2** — the encoder emits a short Base62 string.
- **Lands on:** the "one, two, three" recital at **18.10-18.96** — tick the counter *on*
  those words; "encode that number in Base62" at **20.30**.
- **Counter implementation:** pre-rendered stacked digit spans crossfaded with
  zero-duration `tl.set` swaps. Never tween `innerText` — GSAP interpolates it and renders
  garbage. And only touch the OUTGOING digit per swap; a blanket hide-all plus a show-one
  at the same position renders a blank frame on every increment.

### slot_new_component — start 23.000, duration 6.400  (beat 22.167-29.375) — TAKEOVER
Narration: "Base62 uses zero through nine, lowercase a through z, and capital A through Z,
sixty-two symbols."
- **Act 1** — three banks of glyphs fill in as they are named: `0-9`, then `a-z`, then
  `A-Z`. Stagger the banks, not the individual glyphs.
- **Turn** — at the 660ms pause before "sixty-two" (output **28.22**), a count-up sweep
  runs across all three banks.
- **Act 2** — the numeral **62** lands, >=140px.
- **Lands on:** "sixty-two symbols" at **28.22-29.16**.
- The glyph banks are visual texture, not numbers to read. `62` is the one hero numeral.

### slot_scale — start 30.100, duration 7.000  (beat 29.375-37.542) — MOTION GRAPHIC
Narration: "So big numbers become tiny strings. Just three characters cover almost a
quarter million links. Six cover over fifty billion."
- **Act 1** — three character slots fill; a bar and a count resolve to **238,328**.
- **Turn** — three more slots snap in beside them.
- **Act 2** — the bar rescales hard and the count resolves to **56.8 billion**; the
  three-character bar is now invisibly small by comparison.
- **Lands on:** "quarter million links" at **33.94**; "over fifty billion" at **36.64**.
- **Only one of the two figures may be on screen at a time** — retire 238,328 as 56.8B
  arrives.

### slot_redirect — start 37.900, duration 4.000  (beat 37.542-41.458) — CORNER ACCENT
Narration: "Visiting the short link looks up the number and redirects you to the original."
A short beat gets the lightest format. A single chip in one corner, footage otherwise
untouched. Runs 0.54s past its beat end, which is inside the 1.0s slack.
- **Act 1** — the chip shows `/3mK9Qa` and a lookup spinner.
- **Turn** — the spinner resolves.
- **Act 2** — the chip flips to `301 ->` and the original URL ghosts in behind it.
- **Lands on:** "looks up the number and redirects" at **38.77-40.47**.

### slot_payoff — start 41.900, duration 5.600  (beat 41.458-48.208) — STATIC PHOTO CARD
Narration: "Every short link is just a number wearing a costume."
**Real image:** `shared_assets/misc/tinyurl_ui.jpg` — a real shortener UI, captured
because it is the subject. Crop to the product surface; do not include the cookie banner.
- **Act 1** — the screenshot holds as a card with a slow drift.
- **Turn** — the short code on it lifts off and reveals the plain integer underneath.
- **Lands on:** "just a number wearing a costume" at **42.87-44.25**.
- **NO tease chip.**

---

# EP17 — fraud detection (9 beats, 62.583s total)

`episodes/ep17-fraud/edl.json`

**This episode has a recorded intro.** The HOOK beat does not start until **6.875**. Do
NOT apply the no-intro house pattern of putting the hook overlay at 2.800 — that is the
exact bug `check_overlay_timing.py` was written to catch, and it shipped once already on
this episode.

### slot_title — 0.000, 2.766s
`SYSTEM DESIGN · 17` + headline **How Banks Catch Fraud In Milliseconds**. Sits over the
recorded intro.

### slot_hook — start 7.500, duration 6.000  (beat 6.875-13.792) — HALF-SCREEN PANEL
Narration: "So your card gets declined the second it's used somewhere strange. A model
made that call in about forty milliseconds."
- **Act 1** — a realistic phone lock-screen push notification from a bank slides in:
  transaction declined, an amount, a foreign city.
- **Turn** — the notification dims and a timing readout scrubs backward.
- **Act 2** — **40 ms** lands as the decision time, >=140px.
- **Lands on:** "declined" at **7.83**; "forty milliseconds" at **12.47**.
- Two numbers max at a time: the amount retires before `40 ms` arrives.

### slot_problem — start 14.600, duration 8.600  (beat 13.792-24.292) — TAKEOVER
Narration: "You can't have a human review every swipe. There are thousands per second, and
rigid rules like block foreign purchases annoy real travelers."
- **Act 1** — transaction rows stream past a single human-reviewer icon far faster than
  it can act; a backlog piles up.
- **Turn (~5.0s local)** — a rigid rule bar slams down across the stream.
- **Act 2** — the rule blocks a legitimate traveller's transaction: a row that was clearly
  fine turns red and is rejected.
- **Lands on:** "rigid rules... annoy real travelers" at **21.24-23.86**.

### slot_build — start 25.000, duration 5.200  (beat 24.292-30.333) — TRANSPARENT BAND
Narration: "So banks learn your normal pattern: where, when, how much, how often you
usually spend."
Linework over live footage, no opaque fill, translucent (<=0.32 alpha) so it can sit
naturally rather than being pinned to the frame edge.
- **Act 1** — three hand-drawn SVG glyphs draw themselves in, staggered: a map pin, a
  clock, an amount mark.
- **Turn** — they converge.
- **Act 2** — they merge into a single baseline ring that breathes.
- **Lands on:** "where, when, how much" at **26.44-30.10** — draw each glyph on its word.

### slot_new_component — start 31.100, duration 6.200  (beat 30.333-37.708) — FULL-BLEED PHOTO
Narration: "Anomaly detection scores each transaction against that baseline in real time.
A four dollar coffee near home looks normal."
**Real image:** `shared_assets/misc/card_terminal.jpg` — real hands using a real card
terminal, i.e. literally the transaction being scored. Full-bleed, dimmed enough that the
type stays the hero, with a scrim gradient behind the type and a multi-layer text-shadow.
Verify legibility on a native-resolution crop, not a downscaled frame.
- **Act 1** — the photo settles; a transaction chip lands on it: `$4.00`.
- **Turn** — a scoring arc sweeps.
- **Act 2** — the arc settles deep in the normal band and the chip goes green.
- **Lands on:** "a four dollar coffee near home looks normal" at **35.52-37.56**.
- **Caption-band warning:** a full-bleed photo must not put a bright region behind the
  burned-in captions. Mask the photo off below ~y=1240 into the dark background.

### slot_outlier — start 38.400, duration 5.600  (beat 37.708-44.042) — HALF-SCREEN PANEL
Narration: "A two thousand dollar charge in another country at three AM is a wild outlier
and gets flagged or blocked."
Deliberately the mirror of the previous slot: same scoring arc, opposite outcome.
- **Act 1** — the same readout, now with outlier values: the amount, and a 3 AM clock.
- **Turn** — the arc slams past the threshold; red flash.
- **Act 2** — a BLOCKED stamp lands.
- **Lands on:** the outlier description at **38.0-42.5**; "flagged or blocked" at **42.6**.
- Exactly two numbers co-visible (amount + time). Nothing else numeric.

### slot_feature_store — start 44.700, duration 5.000  (beat 44.042-49.667) — MOTION GRAPHIC
Narration: "Features about you and the merchant are precomputed in a feature store, so
scoring is instant."
- **Act 1** — feature values are written into store slots ahead of time, filling in.
- **Turn** — a request arrives.
- **Act 2** — the lookup returns in a single frame: a latency bar that is already full,
  next to a ghosted "compute it now" bar that is still crawling.
- **Lands on:** "precomputed in a feature store, so scoring is instant" at **47.63-49.64**.

### slot_ai_angle — start 50.400, duration 5.700  (beat 49.667-56.167) — TAKEOVER
Narration: "This is live machine learning. The model scores a streaming feed of
transactions and keeps adapting as your habits change."
- **Act 1** — a live stream of transactions flows through a model and scores against a
  fixed baseline curve.
- **Turn** — the spending pattern shifts; a new cluster appears off the curve.
- **Act 2** — the baseline curve visibly migrates to fit the new cluster, and the
  previously-flagged points go green.
- **Lands on:** "keeps adapting as your habits change" at **53.2-56.1**.

### slot_payoff — start 56.700, duration 5.400  (beat 56.167-62.583) — STATIC PHOTO CARD
Narration: "Fraud detection is pattern matching at the speed of a swipe."
**Real image:** `shared_assets/misc/card_chip.jpg` — a real card chip macro, held.
- **Act 1** — the card holds, slow drift.
- **Turn** — the chip's contact pads light up briefly in a scan pattern, then settle.
- **Lands on:** "at the speed of a swipe" at **58.5** approx.
- **NO tease chip.** EP17 shipped one before.

---

# EP18 — the full web request (6 content beats + title)

Two variants, identical except the intro. **Everything after INTRO is 0.417s later in B
than in A.** Build each composition ONCE; only the EDL `start_in_output` differs.

- `edl.A.json` — "prepping you for your system design interview", INTRO 0.000-7.000, total 54.667s
- `edl.B.json` — "exploring really cool tech", INTRO 0.000-7.417, total 55.083s

Start times below are given as **A / B**.

### slot_title — 0.000, 2.766s (both variants)
The existing `animations/slot_title/` composition ("What Happens When You Type a URL") is
correct and already rendered — leave it alone.

### slot_hook — start 7.400 / 7.817, duration 5.600  (beat 7.000-13.375 / 7.417-13.792) — TRANSPARENT BAND
Narration: "So you type a URL and hit Enter. Before the page paints, a whole relay race
happens. Let's run it."
Deliberately transparent, not opaque: linework over live footage.
- **Act 1** — a horizontal relay track draws itself with five hand-off nodes.
- **Turn** — a baton starts moving and accelerates.
- **Act 2** — all five nodes light in sequence and the track completes.
- **Lands on:** "a whole relay race happens" at **10.60 / 11.02**.
- Keep this composition — the PAYOFF slot calls back to it.

### slot_problem — start 14.100 / 14.517, duration 6.400  (beats PROBLEM+PROBLEM_B, 13.375-21.000 / 13.792-21.417) — TAKEOVER
One overlay spanning both PROBLEM ranges — they are one idea.
Narration: "Your computer doesn't actually know where google.com lives. Websites are found
by IP addresses, not name."
- **Act 1** — a browser URL field with `google.com` typed; the destination field beside it
  is a blinking `?`. A lookup attempt fails.
- **Turn** — colour phase-shift.
- **Act 2** — the name resolves to the **real** address `172.217.72.139`.
- **Lands on:** "found by IP addresses, not name" at **18.72 / 19.14**.

### slot_dns — start 21.700 / 22.117, duration 7.800  (beat 21.000-30.250 / 21.417-30.667) — HALF-SCREEN PANEL
Narration: "So first comes the DNS, the internet's phone book. Your browser asks a DNS
resolver what's the IP address for google.com and gets back an address."
**This replaces the rejected dictionary-page photo.** The hero is a realistic terminal
recreation printing the **real** `nslookup google.com` output captured this session.
- **Act 1** — the command types itself: `nslookup google.com`. A resolver spinner runs.
- **Turn** — the response arrives.
- **Act 2** — the real answer block prints; one address is highlighted:
  `Name: google.com` / `Address: 172.217.72.139`.
- **Lands on:** "gets back an address" at **28.67 / 29.09**.
- Print at most 3 answer lines, not the full ten-address dump. Omit the resolver line.
- Monospace stack must read `"JetBrains Mono", Menlo, monospace` — leading with
  `ui-monospace` silently falls through to proportional Inter and a terminal that renders
  proportional is the one thing that would give this away.

### slot_tcp_tls — start 30.900 / 31.317, duration 5.900  (beat 30.250-36.833 / 30.667-37.250) — MOTION GRAPHIC
Narration: "Now it opens a TCP connection to that IP, does a quick TLS handshake to
encrypt the link, that's the HTTP lock."
- **Act 1** — a three-way handshake draws as three arcs between client and server: SYN,
  SYN-ACK, ACK, staggered.
- **Turn** — a key-exchange shimmer passes along the channel.
- **Act 2** — a padlock closes and the channel changes from a dotted line to a solid
  shielded one.
- **Lands on:** "that's the HTTP lock" at **35.24 / 35.66** — the padlock must close there.

### slot_response — start 37.500 / 37.917, duration 11.400  (beat 36.833-49.375 / 37.250-49.792) — TAKEOVER
Narration: "and sends the HTTP request. The server, often via CDN and load balancer,
returns HTML, and your browser fetches the CSS, JS, and images it references, then renders
all in a fraction of a second."
The episode's longest and densest beat.
- **Act 1** — the request travels out through a CDN node and a load balancer to the
  server; HTML returns as the first bar of a network waterfall.
- **Turn** — the HTML bar lands and visibly *spawns* child requests.
- **Act 2** — a real-looking waterfall fills in beneath it (css, js, images) and the page
  paints in a mock viewport.
- **Lands on:** "renders all in a fraction of a second" at **47.12 / 47.54** — the paint
  must complete there.
- Waterfall rows are visual bars. Label at most two of them; do not print a timing number
  on every row.

### slot_payoff — start 49.700 / 50.117, duration 4.900  (beat 49.375-54.667 / 49.792-55.083) — FULL-BLEED PHOTO
Narration: "Every page is a relay race you never see."
**Needs a real image**: WebSearch for and download a real photograph of a server rack /
data centre aisle — the actual machine at the far end of the relay, not a metaphor.
- **Act 1** — the photo fills the frame, dimmed, with a slow push-in.
- **Turn** — the five-node relay track from `slot_hook` ghosts in across it as a callback.
- **Lands on:** "a relay race you never see" at **49.9 / 50.3** approx.
- Mask the photo off below ~y=1240 so nothing bright sits behind the captions.
- **NO tease chip.** EP18 shipped one before, and if you remove a tease also remove
  anything that existed only to support it (EP18 previously had a `#tease-scrim` ellipse
  that became a smudge once the pill was gone).

---

# EP19 — approximate counters (7 content beats + title)

Two variants, identical except the intro. **Everything after INTRO is 0.833s EARLIER in B
than in A** (B's intro is shorter).

- `edl.A.json` — "preparing you for your system design interview", INTRO 0.000-8.583, total 59.583s
- `edl.B.json` — "exploring really cool tech", INTRO 0.000-7.750, total 58.750s

Start times below are **A / B**.

### slot_title — 0.000, 2.766s (both variants)
`SYSTEM DESIGN · 19` + headline **Why Like Counts Are Never Exact**.

### slot_hook — start 9.000 / 8.167, duration 5.300  (beat 8.583-14.375 / 7.750-13.542) — HALF-SCREEN PANEL
Narration: "So when you look at a Ronaldo post, that like count isn't exact, and that's
actually the smart design choice."
**Real image:** `shared_assets/misc/ronaldo.png` — a real photo of the public figure whose
post is the subject of the beat. Re-source a higher-resolution version if you can find one
(the shared copy is only 424x362).
Build the post itself as a **realistic social-post UI recreation** with the real photo
inset — that is the EP4 gold-standard pattern, and it is also the only way this beat works:
the like counter has to *move*, which a static screenshot cannot do.
- **Act 1** — the post card lands; the like counter ticks up smoothly.
- **Turn** — the number stutters and forks.
- **Act 2** — two different values sit side by side for a moment, then one settles.
- **Lands on:** "that like count isn't exact" at **10.37 / 9.54**.
- Exactly two numbers co-visible, and only during act 2.

### slot_problem — start 15.100 / 14.267, duration 9.400  (beat 14.375-25.583 / 13.542-24.750) — TAKEOVER
Narration: "If every like had to instantly update one perfectly accurate number, that
single row becomes a bottleneck. Millions of people liking at once would all fight to
write to the same place."
- **Act 1** — a single database row highlighted; one writer updates it cleanly.
- **Turn (on "bottleneck", output 20.47 / 19.64)** — a traffic-jam gridlock effect seizes
  the single counter.
- **Act 2** — write arrows converge on that one row from every direction and jam; a queue
  depth spikes.
- **Lands on:** "bottleneck" at **20.47 / 19.64**; the contention at **21.6-24.8 / 20.8-24.0**.

### slot_build — start 26.300 / 25.467, duration 7.200  (beat 25.583-34.208 / 24.750-33.375) — MOTION GRAPHIC
Narration: "So at massive scale, we relax. Likes are counted across many servers and added
up, with the displayed number trailing slightly behind reality."
- **Act 1** — the single row splits into six shards, each counting independently.
- **Turn** — a summation sweep gathers them.
- **Act 2** — the summed display lands *slightly behind* a faint "true" value that keeps
  climbing.
- **Lands on:** "trailing slightly behind reality" at **32.17 / 31.34**.
- **The six shard counters must be visual pulses/bars, not readable numerals** — only the
  displayed total and the faint true value may be legible numbers (that is the two-number
  cap).

### slot_new_component — start 34.900 / 34.067, duration 5.900  (beat 34.208-41.208 / 33.375-40.375) — TRANSPARENT BAND
Narration: "This is eventual consistency. The count converges to correct in seconds, but
in any instant, it might be approximate."
Linework over live footage, no opaque fill.
- **Act 1** — several traces scatter and diverge.
- **Turn** — a settle pulse.
- **Act 2** — the traces converge onto a single line.
- **Lands on:** "converges to correct in seconds" at **37.24 / 36.41**.

### slot_approx_ok — start 41.600 / 40.767, duration 4.700  (beat 41.208-45.667 / 40.375-44.833) — CORNER ACCENT
Narration: "For likes, nobody cares if it briefly says a million instead of a million
three."
Smallest format for the lightest beat. A single counter chip in one corner.
- **Act 1** — the chip reads `1,000,000`.
- **Turn** — it flips.
- **Act 2** — it reads `1,000,300` and nothing else in the frame reacts — that is the joke.
- **Lands on:** "a million instead of a million three" at **43.3 / 42.5** approx.
- Stacked-digit-span technique for the flip; never tween `innerText`.

### slot_tradeoff — start 46.300 / 45.467, duration 6.900  (beat 45.667-52.875 / 44.833-52.042) — TAKEOVER
Narration: "Speed and availability matter far more than perfect accuracy. Your bank
balance, of course, gets the opposite treatment."
- **Act 1** — a slider labelled LIKES, pushed hard toward SPEED.
- **Turn** — a slider snap plus a hard contrast cut.
- **Act 2** — a second slider, BANK BALANCE, pinned to the opposite end at ACCURACY.
- **Lands on:** "opposite treatment" at **52.13 / 51.30**.
- If you build the slider handle as an SVG `<line>`, do not animate GSAP `rotation` on it
  — a degenerate bounding box warps and vanishes in this renderer. Tween a numeric value
  and write the coordinates in `onUpdate`, or rotate a wrapper with real width and height.

### slot_payoff — start 53.200 / 52.367, duration 5.600  (beat 52.875-59.583 / 52.042-58.750) — FULL-BLEED PHOTO
Narration: "At a billion likes, close enough beats exactly right."
**Real image:** `shared_assets/misc/stadium_crowd.jpg` — a real crowd, which is what a
billion of anything actually looks like.
- **Act 1** — the photo fills the frame, dimmed, slow push-in.
- **Turn** — individual faces in the crowd stop being resolvable as the push-in continues
  — the point being that at that scale the exact count stops mattering.
- **Lands on:** "close enough beats exactly right" at **53.98 / 53.15**.
- Mask off below ~y=1240 so the caption band stays dark.
- **NO tease chip.**
