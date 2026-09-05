# EP20-26 overlay batch — format plan and per-slot briefs

Read `OVERLAY_SPEC.md` in full first, then `SAFE_ZONE.md`, then the
`system-design-overlays` skill (repo copy: `skills/system-design-overlays/SKILL.md`).
This file only adds what is specific to these seven episodes.

> **The EDL is authoritative for all times.** Every episode's exact beat windows and
> land-on-word times live in `episodes/<ep>/edl.A.json` / `edl.B.json`
> (`_beat_windows_output_timeline`) and `episodes/<ep>/beats.md` (word-level payoff
> times in output seconds, per variant). This file deliberately carries NO hard-coded
> seconds — pull them from those files at build time.

## Batch-wide conventions

- **A/B variants.** Every episode ships two cuts differing only by the intro/hook take:
  A = "prepping you for your system design interview", B = "Exploring Really Cool Tech".
  **EP20 exception:** the source has no cool-tech take; EP20-B is a COLD OPEN starting
  directly on the hook. Build every content composition ONCE and share it across A/B —
  only EDL `start_in_output` values (and title stickers) differ.
- **TikTok title sticker** replaces the house title card (see skill section "TikTok-native
  title box"; reference `episodes/ep19-likecounts/animations/slot_tiktok_title/`).
  Wording fixed: A = `MASTERING SYSTEM` / `DESIGN:` / `EPISODE N` (3 boxes);
  B = `RLLY COOL TECH:` / `EPISODE N` (2 boxes). **Boxes must end by x=860**
  (SAFE_ZONE: the EP19 sticker overhung the rail; narrow it). EP20-B's sticker instead
  carries the hook text: `AI COULDN'T COUNT` / `THE R'S IN` / `"STRAWBERRY"`, held over
  the hook beat.
- **EP26 correction chip (user request):** the presenter says "episode 25" in every EP26
  intro take. Both variants get a small TikTok-style corrective sticker that pops exactly
  on the spoken word "25" (time from beats.md): a compact white box `*EPISODE 26`, plus a
  smaller second line `he can't count` — dry, small, bottom-left of the title stack,
  clear of the face and x<=860. It reads as an intentional gag, not an error.
- **Captions (forward-looking spec, SAFE_ZONE):** `--caption-font-size 60
  --caption-margin-lr 220 --caption-margin-v 400`, separate caption file per variant
  (`--subtitles-out master.A.ass` / `master.B.ass`). Content floor stays y<=1280.
- **Zoom:** every range `zoom:{mode:"slow",from,to,focal 540,960}`, 1.0<->1.045
  alternating (already in the EDLs).
- **Real images:** each episode has at least one (list per episode below), sourced into
  `episodes/<ep>/assets/` — see `episodes/ATTRIBUTIONS_EP20-26.md`. Items marked
  redraw-ref are style references only, do not paste them into frames.
- **SFX pass (after composite):** 8-10 distinct sounds/episode from `sfx_shared/`, one
  voice meme each, volumes from TIKTOK_SFX_NOTES.md calibration; final mix
  `loudnorm=I=-14:TP=-2:LRA=11`; verify peak and audibility at 32kHz.

## Format-mix audit (planning-stage, per skill rule 7)

| Episode | Formats used, in beat order | Distinct | Takeovers | Adjacent repeat? |
|---|---|---|---|---|
| EP20 | half-panel, TAKEOVER, motion-gfx, TAKEOVER, half-panel(real shot), transparent | 4 | 2 | none |
| EP21 | half-panel, TAKEOVER, motion-gfx, TAKEOVER, transparent, photo-card | 5 | 2 | none |
| EP22 | transparent, TAKEOVER, motion-gfx, TAKEOVER, half-panel, corner | 5 | 2 | none |
| EP23 | half-panel, TAKEOVER, motion-gfx, half-panel, TAKEOVER, full-bleed-photo | 4 | 2 | none |
| EP24 | half-panel, motion-gfx, half-panel, TAKEOVER, transparent, photo-card | 5 | 1 | none |
| EP25 | transparent, TAKEOVER, motion-gfx, TAKEOVER, corner, transparent, half-panel | 5 | 2 | none |
| EP26 | corner(intro fix), half-panel, TAKEOVER, motion-gfx, half-panel, TAKEOVER, transparent, half-panel | 5 | 2 | none |

---

# EP20 — Why AI can't spell "strawberry" (tokenization)

`episodes/ep20-tokenization/` · beats: HOOK, PROBLEM, BUILD, NEW_COMPONENT, TOKENS, PAYOFF
Real images: OpenAI tokenizer screenshots (+ real token strings/IDs recorded in assets/).

### slot_hook — HALF-SCREEN PANEL (lower band)
Narration: "So if you asked ChatGPT how many Rs there are in strawberry, for years it
would get it wrong because it hasn't actually seen the word strawberry."
Realistic chat-app UI recreation (rounded card, user bubble, assistant bubble, typing dots).
- **Act 1** — user bubble types: `How many R's are in "strawberry"?`; assistant typing
  indicator pulses; a confident answer starts to assemble.
- **Turn** — the answer lands wrong: `There are 2 R's in "strawberry."` — freeze-frame
  vignette + red ✗ stamp (record-scratch cue in the SFX pass).
- **Act 2** — the ✗ holds, the wrong "2" underlined red; a small red shake on the bubble.
- **Lands on:** "get it wrong" (time from beats.md). In variant B the title sticker holds
  the top of frame simultaneously — panel stays in the lower band; verify no collision.

### slot_problem — TAKEOVER
Narration: "Here's the problem. Models can't eat raw text, and letter by letter is too
slow to learn from. Whole words means a vocabulary of millions, and one typo becomes an
unknown word."
- **Act 1 (cyan)** — path one: a sentence dripping through one letter at a time,
  agonizingly slow (a crawling char-by-char ticker + a progress bar barely moving).
- **Turn** — colour phase-shift + slam.
- **Act 2 (amber)** — path two: a shelf/wall of word-tiles overflowing while a vocabulary
  counter spins to the millions (stacked-digit spans, never tween innerText); then
  `strawbery` (typo) slides in and flags `[UNK]` red.
- **Lands on:** "vocabulary of millions" (counter peak), "unknown word" (`[UNK]` flag).
- Text budget: one headline <=6 words; the counter and `[UNK]` are the two numbers/labels.

### slot_build — MOTION GRAPHIC (upper band, over live footage)
Narration: "So a tokenizer chops text into tokens, chunks somewhere between letters and
words. Common words stay whole. Rarer ones will split straw and berry."
The sentence `I love strawberries` in large type slices into token blocks
`[I][ love][ straw][berries]` with clean slice-cuts (click SFX per slice in the SFX pass),
each block picking up one of the tokenizer's real pastel chunk colours.
- **Act 1** — the sentence types on as plain text.
- **Turn** — a slice blade sweeps; cuts land one at a time (>=0.6s apart).
- **Act 2** — blocks separate with gaps and gentle float; `straw`+`berry` split lands last.
- **Lands on:** "chops text into tokens" (first slice), "straw and berry" (final split).
- Keep everything above the brow line and inside x=60-860; translucent chips (<=0.32 fill).

### slot_new_component — TAKEOVER (final)
Narration: "The model never receives letters at all. It receives token ID numbers, so
asking it to count letters is like asking you to count letters in a word you've only ever
heard spoken."
- **Act 1 (amber)** — the four token blocks from BUILD reappear; card-flip one at a time
  to reveal their REAL IDs (use the values captured in assets/, e.g. 40/3021/15717/20853
  style) — 3D flip per block.
- **Turn** — shutter flash; colour shift to cyan.
- **Act 2 (cyan)** — the ID numbers stream as packets into a model intake glyph while the
  original letters dissolve to particles — the model end only ever sees numbers.
- **Lands on:** "token ID numbers" (flip completes), "only ever heard spoken" (letters gone).
- Two numbers max visible at any instant: fade each ID as the next flips.

### slot_tokens — HALF-SCREEN PANEL with the REAL tokenizer screenshot
Narration: "It's also why AI pricing and context windows are measured in tokens. Tokens
are the only unit the model actually reads."
The real OpenAI tokenizer capture (assets/) inset in designed browser chrome — the
deliberate product screenshot IS the subject.
- **Act 1** — the screenshot card lands; the token-count readout on it gets a highlight ring.
- **Turn** — sweep.
- **Act 2** — a context-window meter beside it fills tick by tick, denominated in tokens;
  a small `$ / 1M tokens` chip.
- **Lands on:** "measured in tokens". Two numbers max co-visible.

### slot_payoff — TRANSPARENT BAND
Narration: "So AI doesn't read your words. It reads chunks with ID numbers."
Linework over live footage, no opaque fill: the word `strawberry` splits into
`[straw][berry]` outline chips, each tagged with a small ID, breathing gently.
- **Act 1** — the word draws itself. **Turn** — one clean split. **Act 2** — chips + IDs hold.
- **Lands on:** "chunks with ID numbers". **NO tease chip.**

---

# EP21 — leaked-password check without seeing it (k-anonymity)

`episodes/ep21-kanonymity/` · beats: BLOOPER, HOOK, PROBLEM, BUILD, SCAN, KANON, PAYOFF
Real images: HIBP result screenshot; REAL range-API response `assets/range_CBFDA.txt`
(the crowd of real hash suffixes); Cloudflare diagrams = redraw-ref only.
BLOOPER (the "Ana-anonymity" stumble) opens both variants — title sticker holds over it;
no other overlay there.

### slot_hook — HALF-SCREEN PANEL
Narration: "So a website can tell you your password leaked in a breach without you ever
sending your password in. That sounds impossible, but it isn't."
Realistic Chrome-style breach-warning dialog recreation ("Change your password — this
password appeared in a data breach").
- **Act 1** — the dialog slides in over a mock settings surface.
- **Turn** — a "how did it know?" scrub: the dialog dims, a password field with dots
  appears below with an outbound arrow.
- **Act 2** — the outbound arrow gets a red ✗ — the password never left the device; a
  checkmark on the local side.
- **Lands on:** "without you ever sending your password in".

### slot_problem — TAKEOVER
Narration: "Have I Been Pwned holds hundreds of millions of breached passwords, but
sending yours to be checked, even hashed, hands a stranger something crackable. It's a
catch-22."
- **Act 1 (blue)** — an envelope with a password chip hovers toward a BREACH CHECKER
  server card holding a huge vault counter (hundreds of millions).
- **Turn** — tug-of-war wobble on the envelope; red flash.
- **Act 2 (red)** — the envelope gets ✗-stamped; a hash chip beside it CRACKS open
  (fracture lines) — "even hashed" is still crackable.
- **Lands on:** "even hashed" (crack), "catch-22" (both sides lit red, stalemate).

### slot_build — MOTION GRAPHIC (upper band)
Narration: "Here's the trick. Your device hashes the password locally, then sends only
the first five characters of the hash, just the prefix."
Monospace hero: `password123` → SHA-1 → the REAL digest
`CBFDAC6008F9CAB4083784CBD1874F76618D2A97` typing out; scissors snip after char 5.
- **Act 1** — hash types on-device (phone outline, local).
- **Turn** — scissor-snip: `CBFDA` detaches (snip SFX cue).
- **Act 2** — ONLY the 5-char prefix travels off-frame; the remaining 35 chars stay
  locked on the phone with a padlock.
- **Lands on:** "first five characters" (snip), "just the prefix" (travel).
- The digest is one hero string (counts as one number). Keep chips translucent.

### slot_scan — TAKEOVER (final)
Narration: "The server returns every breached hash starting with those five characters,
hundreds of them, and your device checks for a match locally."
THE REAL DATA BEAT: render rows from `assets/range_CBFDA.txt` — the actual API response.
- **Act 1 (cyan)** — a response wall pours in: dozens of real suffix rows under a header
  `GET api.pwnedpasswords.com/range/CBFDA`, count chip from the real line count.
- **Turn** — the wall settles; a device-side scanline starts.
- **Act 2** — Where's-Waldo scan: the scanline sweeps rows; the REAL matching suffix row
  (`C6008F9CAB40...`) lights green with its real breach count.
- **Lands on:** "hundreds of them" (wall complete), "checks for a match locally" (green row).
- Rows are visual texture (mono, small, dimmed); only the count chip and the matched row's
  count are readable numbers.

### slot_kanon — TRANSPARENT BAND
Narration: "The server can never tell which of those hundreds you were asking about.
You're hidden in a crowd, and that property has a name: k-anonymity."
Linework: a field of identical outline dots; one is you, indistinguishable.
- **Act 1** — dots draw in; a server-side `?` glyph sweeps and fails to lock onto any dot.
- **Turn** — settle pulse.
- **Act 2** — the label `k-ANONYMITY` lands (the naming moment), dots breathe.
- **Lands on:** "k-anonymity" — the label must land on the word.

### slot_payoff — STATIC PHOTO CARD (real HIBP screenshot)
Narration: "So you don't send the secret. Send a crowd it can hide in."
The real haveibeenpwned result capture as a held card, slow drift.
- **Act 1** — the card lands. **Turn** — ghosted identical hash rows fade in behind it —
  the crowd. **Act 2** — hold.
- **Lands on:** "send a crowd it can hide in". **NO tease chip.**

---

# EP22 — instant payment notifications (webhooks)

`episodes/ep22-webhooks/` · beats: HOOK, PROBLEM, BUILD, POST, SIGN, PAYOFF
Real images: Stripe docs webhook-flow / event-payload screenshots (deliberate product
screenshots — inset in designed chrome; also usable as redraw-ref).

### slot_hook — TRANSPARENT BAND (runs simultaneously with the title sticker)
Narration: "So your app finds out you got paid the instant it happens without ever
checking. That's called a webhook."
- **Act 1** — a phone outline (lower half, clear of the sticker) sits idle, screen dim.
- **Turn** — a push notification card slides in unprompted: `Payment succeeded — $1,250.00`
  (notif SFX cue).
- **Act 2** — a small outbound "did the app ask?" arrow gets crossed out — it never asked.
- **Lands on:** "the instant it happens" (push arrives), "That's called a webhook".

### slot_problem — TAKEOVER
Narration: "You met the clunky alternative back in the chat episode asking, 'Anything
new?' on repeat. For payments, that's thousands of wasted calls a day to catch one event."
- **Act 1** — flashback vignette (one-beat rewind cue): an app card fires `anything new?`
  requests at a server; every reply `204 · nothing`. A wasted-calls counter spins up
  (stacked digit spans).
- **Turn** — desaturate hit + "we don't do this anymore" — the polling loop freezes.
- **Act 2** — the pile of grey wasted calls vs ONE lit event chip — thousands to one.
- **Lands on:** "anything new" (first poll), "thousands of wasted calls" (counter peak).
- Two numbers max: the counter and the `1`.

### slot_build — MOTION GRAPHIC
Narration: "A webhook flips the direction. You hand the payment provider a URL and say,
'Call me when something happens.'"
- **Act 1** — APP and STRIPE nodes with the old request arrow APP→STRIPE pulsing.
- **Turn** — the arrow REVERSES direction with a whoosh (the beat's whole idea in one move).
- **Act 2** — a URL chip `myapp.com/webhooks` is handed across and slots into the
  provider node; a small bell arms on it.
- **Lands on:** "flips the direction" (arrow reversal), "call me when something happens"
  (bell arms).

### slot_post — TAKEOVER (final)
Narration: "The moment a payment succeeds, their server sends an HTTP POST to your URL
with the details. You only do work when there's actually work to do."
- **Act 1 (green)** — a `payment succeeded` event fires on the provider side; a packet
  travels; a realistic terminal/code card prints `POST /webhooks/stripe` + a compact JSON
  payload (`"type": "payment_intent.succeeded"` + one amount) typing on (keyboard SFX cue).
- **Turn** — arrival flash as the payload completes.
- **Act 2** — an idle-vs-active meter: the app's work-lamp is dark the whole time and
  blinks on ONLY when the POST lands — work only when there is work.
- **Lands on:** "HTTP POST" (the request line prints), "actually work to do" (lamp).
- The JSON is the one hero string; at most one amount visible.

### slot_sign — HALF-SCREEN PANEL
Narration: "And because anyone could post to a public URL, they sign each call. You
verify the signature so you know it's really them."
- **Act 1** — a rogue unsigned POST arrives at the public URL — stamped red `UNSIGNED ✗`.
- **Turn** — the genuine call arrives carrying a `Stripe-Signature: t=…,v1=5257a8…`
  header chip; an HMAC check spinner runs.
- **Act 2** — green `VERIFIED` badge pop (badge SFX cue).
- **Lands on:** "sign each call" (header chip), "verify the signature" → badge on
  "really them".

### slot_payoff — CORNER ACCENT
Narration: "So webhooks flip the question. The server calls you."
The reversed arrow from BUILD returns as a small corner glyph — a visual callback.
- **Act 1** — the chip lands: the flipped arrow + a tiny buzzing phone. **Turn** — one
  pulse on "calls you". **Act 2** — quiet hold.
- **Lands on:** "the server calls you". **NO tease chip.**

---

# EP23 — why everyone ships in containers (Docker)

`episodes/ep23-containers/` · beats: HOOK, PROBLEM, BUILD, RUNS, VM, PAYOFF
Real images: phippy.io CNCF art (CC-BY-4.0) — Phippy inset as the container mascot;
real container-ship photo for the payoff.

### slot_hook — HALF-SCREEN PANEL
Narration: "The most annoying phrase in software, 'But it only works on my machine,' got
killed by containers."
- **Act 1** — a code-review comment card: `but it works on MY machine ¯\_..` styled as a
  real thread reply, smug green check beside it.
- **Turn** — a container box drops onto the card (slam).
- **Act 2** — the card lies flat under the box with a small `R.I.P.` headstone chip and a
  red ✗ — the phrase is dead.
- **Lands on:** "got killed by containers" (the drop lands on those words).

### slot_problem — TAKEOVER
Narration: "So code depends on a specific runtime, libraries, and config. If you move it
to another computer with slightly different versions, it will break in mysterious ways."
- **Act 1 (blue)** — machine A: an app block sits on labeled layer stack
  `runtime 18.1 · libs · config` — all green.
- **Turn** — the app block is picked up and dropped onto machine B whose stickers differ
  (`runtime 16.3`); glitch/error overlay hit.
- **Act 2 (red)** — a cascade of mysterious stack-trace lines pours out; the mismatched
  version sticker flashes.
- **Lands on:** "slightly different versions" (sticker mismatch), "break in mysterious
  ways" (cascade).
- Version strings are the two numbers.

### slot_build — MOTION GRAPHIC
Narration: "A container packages your app together with everything it needs, runtime,
libraries, settings, into one standardized unit."
The satisfying pack-into-box: app + `runtime`/`libs`/`config` chips fly one at a time
(>=0.6s apart, click per pack) into an open container box.
- **Act 1** — chips pack in. **Turn** — the lid closes; a label stamps. **Act 2** — the
  sealed box gets its standardized label and a gentle hover.
- **Lands on:** "runtime, libraries, settings" (each chip on its word), "one standardized
  unit" (stamp).

### slot_runs — HALF-SCREEN PANEL (with Phippy)
Narration: "That container runs identically on your laptop, a teammate's machine, and
the cloud because it carries its environment with it."
- **Act 1** — three surfaces draw in: LAPTOP · TEAMMATE · CLOUD; the sealed box (with
  Phippy the CNCF giraffe peeking from it — real sourced art) glides onto the first.
- **Turn** — the box hops surface to surface, identical green check on each, on its word.
- **Act 2** — three identical checks hold; the box breathes.
- **Lands on:** "laptop" / "teammate's machine" / "the cloud" — one hop per word.

### slot_vm — TAKEOVER (final)
Narration: "Unlike a full virtual machine, it shares the host OS kernel, so it's
lightweight, and it boots in seconds. Think shipping container, same box, any ship, any
port."
- **Act 1 (amber)** — the VM tower assembles layer by heavy layer: HOST OS → HYPERVISOR →
  GUEST OS → APP — tall, ponderous; a boot timer crawls.
- **Turn** — sweep cut.
- **Act 2 (cyan)** — beside it the container column: HOST OS → RUNTIME → APP, slim; its
  boot timer snaps done in ~1s while the VM's still crawls. Side-by-side scale contrast
  holds.
- **Lands on:** "shares the host OS kernel" (shared base layer highlights under both),
  "boots in seconds" (timer snap).
- The two boot timers are the two numbers.

### slot_payoff — FULL-BLEED PHOTO
Narration: "So ship the whole kitchen, not just the recipe."
The real container-ship photo fills the frame, dimmed, slow push-in; scrim + strong
text-shadow; mask the photo off below ~y=1240.
- **Act 1** — photo settles. **Turn** — one line lands: `PACKAGE THE ENVIRONMENT, NOT
  JUST THE CODE` (<=6 words is exceeded — use `SHIP THE ENVIRONMENT, NOT THE CODE`).
- **Lands on:** "ship the whole kitchen, not just the recipe". **NO tease chip.**

---

# EP24 — how Google runs a billion containers (Kubernetes)

`episodes/ep24-kubernetes/` · beats: HOOK, PROBLEM, BUILD, CONTROL, AI_ANGLE, PAYOFF
Real images: server-rack photo (hook); phippy.io Captain Kube art (payoff).

### slot_hook — HALF-SCREEN PANEL
Narration: "So a server crashes at three AM and no engineer wakes up because Kubernetes
already handled it. Here's how."
- **Act 1** — a 3:00 AM clock chip + the real server-rack photo inset in a status card;
  one node flips red with a flame/glitch flicker (fire overlay).
- **Turn** — cut to a phone face-down on a nightstand card: notifications `0` — nobody
  paged; a soft `zzz` linework wisp (hand-drawn SVG, no emoji).
- **Act 2** — behind the sleeping phone, the red node quietly flips back green — already
  handled.
- **Lands on:** "three AM" (clock), "no engineer wakes up" (zzz), "already handled it"
  (green flip).

### slot_problem — MOTION GRAPHIC
Narration: "Once you have hundreds of containers across many machines, doing it by hand
is impossible. What restarts crashes? What scales under load? What reroutes around dead
hardware?"
- **Act 1** — container chips multiply across machine outlines until the field is chaos;
  a single human cursor tries to drag one at a time — hopeless.
- **Turn** — the three questions tick in as terse chips, one per spoken question
  (`restarts? · scales? · reroutes?`), each highlighting a matching mini-disaster.
- **Act 2** — the chaos keeps churning, unanswered.
- **Lands on:** each question chip on its words; "by hand is impossible" (cursor gives up).

### slot_build — HALF-SCREEN PANEL
Narration: "Kubernetes is an orchestrator. You declare the desired state, 'I want ten
copies of this app running,' and it makes reality match."
- **Act 1** — a spec card types: `desired: 10 replicas` (mono); below, `actual: 7` in red.
- **Turn** — a control-loop arrow circles between them.
- **Act 2** — actual ticks 8 → 9 → 10 (stacked digit spans, one swap per tick), flips
  green `MATCH`.
- **Lands on:** "ten copies" (desired lands), "makes reality match" (10=10 green).
- The two numbers are desired/actual.

### slot_control — TAKEOVER (the episode's hero beat)
Narration: "A control plane constantly compares actual versus desired. A container dies,
it starts a new one. A machine fails, it reschedules those workloads elsewhere. Traffic
spikes, it auto-scales up, then back down. It's an air traffic controller that never
sleeps."
An air-traffic-tower dashboard over a pod grid — three self-healing micro-events, each on
its words.
- **Act 1 (calm cyan)** — tower glyph + a grid of healthy pods across three node columns;
  an `actual vs desired` ticker breathes.
- **Turn** — a pod blinks out (red) — and a new one pops in beside it (respawn pop cue).
- **Act 2** — a whole node column goes dark; its pods slide to the neighbouring columns;
  then a traffic-spike meter rises and extra pods fade in, then fade back out as it falls.
  The tower sweeps a radar line throughout (trig/onUpdate, never GSAP rotation on a line).
- **Lands on:** "container dies… starts a new one", "machine fails… reschedules",
  "auto-scales up, then back down", tower holds through "air traffic controller".
- Text: the ticker is the only numeric readout; event labels <=2 words.

### slot_ai_angle — TRANSPARENT BAND
Narration: "This is also how AI runs at scale. Kubernetes schedules GPU workloads for
training and inference across huge clusters."
Linework over footage: GPU card glyphs slot into a scheduling grid one by one;
`training` / `inference` are the two labels.
- **Act 1** — grid draws. **Turn** — GPUs slot in (click each). **Act 2** — the grid
  extends past frame edges — huge clusters implied.
- **Lands on:** "GPU workloads" (first slot-in), "huge clusters" (extend).

### slot_payoff — STATIC PHOTO CARD (Captain Kube)
Narration: "So Kubernetes is a robot that babysits your servers."
CNCF's Captain Kube art (real sourced illustration, CC-BY) as a held card, slow drift; a
tiny crib of server glyphs beside it with a `zzz` wisp.
- **Act 1** — card lands. **Turn** — the wheel-logo eye does one calm scan sweep.
  **Act 2** — hold.
- **Lands on:** "robot that babysits your servers". **NO tease chip.**

---

# EP25 — code goes live 100x a day (CI/CD)

`episodes/ep25-cicd/` · beats: HOOK, PROBLEM, CI, CD, ROLLBACK, AI_ANGLE, PAYOFF
Real images: public GitHub Actions run screenshot (inset in CD beat).

### slot_hook — TRANSPARENT BAND (runs under the title sticker)
Narration: "So some companies ship code thousands of times a day and rarely break. The
machine behind that is CI/CD."
- **Act 1** — a deploy ticker chip climbs: `deploys today` with green checks streaming
  past (stacked digits; checks are texture, not counted).
- **Turn** — the counter blurs past 1,000 with a bass cue.
- **Act 2** — the stream keeps flowing, zero red among it.
- **Lands on:** "thousands of times a day" (counter peak), "rarely break" (all-green hold).

### slot_problem — TAKEOVER
Narration: "This is the scary old way. We manually bundle months of changes and deploy on
a tense release day where everyone prays. Big batches, big risk."
- **Act 1 (grey)** — a wall calendar card; an ominous zoom onto one circled date:
  `RELEASE DAY` (riser cue); beside it a bundle of change-chips compresses into one
  giant teetering crate.
- **Turn** — the deploy lever is pulled; hard flash.
- **Act 2 (red)** — the crate wobbles on a tightrope over production; a risk meter pins.
- **Lands on:** "release day" (zoom lands), "big batches, big risk" (meter pins).

### slot_ci — MOTION GRAPHIC
Narration: "Continuous integration means every code change is automatically built and
tested the moment it's merged."
- **Act 1** — a commit chip merges into a main-branch line (merge glyph).
- **Turn** — the merge instantly trips two stations: BUILD then TEST, each flipping green
  on its word.
- **Act 2** — a second commit follows and the same instant loop repeats — continuous.
- **Lands on:** "automatically built and tested", "the moment it's merged" (zero-delay trip).

### slot_cd — TAKEOVER (final)
Narration: "Continuous delivery then carries passing code through an automated pipeline.
Build, test, security scan, deploy, sometimes straight to production with no human hands."
Assembly-line: a conveyor with four stations; the REAL GitHub Actions screenshot inset in
a monitor above the belt (the real machine this recreates).
- **Act 1 (cyan)** — the package rides: BUILD → TEST → SCAN → DEPLOY, a ding + green lamp
  per station on its spoken word.
- **Turn** — at the end of the belt, a barrier labeled with a hand glyph lifts away
  untouched.
- **Act 2** — the package rolls straight through the PRODUCTION door; the belt keeps
  moving behind it.
- **Lands on:** each station on its word; "no human hands" (barrier lifts itself).
- Station names are labels (4 × 1 word — that is the text budget; no other labels).

### slot_rollback — CORNER ACCENT
Narration: "Small frequent changes are easy to test and roll back, so shipping stops
being scary."
One small chip: a red test lamp catches a bad change; it flips back out (`revert ✓`).
- **Act 1** — chip: small change + red lamp (buzzer cue). **Turn** — instant flip-back.
  **Act 2** — green calm; nothing else in frame reacts.
- **Lands on:** "roll back" (the flip).

### slot_ai_angle — TRANSPARENT BAND
Narration: "AI now plugs into the pipeline too, auto-reviewing code and generating tests
before anything reaches production."
Linework: a diff column (added/removed line marks); an AI cursor sweeps it, dropping two
tiny review chips; a generated-test file chip slots into the pipeline ahead of PROD.
- **Lands on:** "auto-reviewing code" (sweep), "generating tests" (test chip).

### slot_payoff — HALF-SCREEN PANEL
Narration: "So we automate the scary parts and shipping stops being scary."
- **Act 1** — the giant crate from PROBLEM ghosts back on the left, grey and cracked.
- **Turn** — it dissolves into a marching row of tiny green step-chips flowing right.
- **Act 2** — the row keeps flowing, calm; headline `SMALL STEPS BEAT BIG LAUNCHES`.
- **Lands on:** "automate the scary parts". **NO tease chip.**

---

# EP26 — video calls glitch on purpose (UDP + jitter buffers)

`episodes/ep26-udp/` · beats: HOOK, PROBLEM, BUILD, JITTER, ROBOT, AI_ANGLE, PAYOFF
Real images: EP26 must carry at least one — preferred: a real Wireshark UDP capture
screenshot (wiki.wireshark.org docs) inset in the BUILD beat, else a real
Wikimedia/Unsplash laptop-video-call photo in the HOOK. Cloudflare diagrams = redraw-ref.
PLUS the intro correction chip (both variants) — see batch-wide conventions.

### slot_fix26 — CORNER ACCENT (intro, both variants)
Pops exactly on the spoken word "25" (time from beats.md): white sticker `*EPISODE 26` +
small second line `he can't count`. Sits bottom-left of the title stack, clear of face,
x<=860. Fades before the hook beat.

### slot_hook — HALF-SCREEN PANEL
Narration: "So YouTube almost never glitches. Your video calls glitch constantly.
Weirdly, the call is doing it on purpose."
Split panel: a video-player card (smooth progress bar, buttery frames implied by a clean
gradient thumbnail) vs a call tile that freezes.
- **Act 1** — both play; the player's bar glides.
- **Turn** — the call tile stutters: pixelation blocks, a spinner, `reconnecting…`.
- **Act 2** — a deliberate-choice stamp on the call side: `ON PURPOSE`.
- **Lands on:** "never glitches" (bar glide), "glitch constantly" (stutter), "on purpose"
  (stamp).

### slot_problem — TAKEOVER
Narration: "Remember the ticks and receipts from the URL episode? Reliable delivery means
waiting for lost data to be resent, which is fine for a video file, but it's useless for a
live call. A word from two seconds ago re-arriving now helps nobody."
- **Act 1 (green)** — the reliable lane: packets with receipt ticks; one drops; a re-send
  loop dutifully replays it — fine for a file (a download bar completes).
- **Turn** — a clock spins +2s; colour shift.
- **Act 2 (red)** — the re-sent word arrives into a live conversation timeline two seconds
  after its slot — the slot is long gone; ✗.
- **Lands on:** "waiting for lost data" (re-send loop), "helps nobody" (late arrival ✗).
- The `+2.0s` chip is the one number.

### slot_build — MOTION GRAPHIC (with the real Wireshark inset if sourced)
Narration: "So live calls use UDP. Fire the packets and never look back. No receipts, no
resends, no waiting."
- **Act 1** — a firing lane: packets stream constantly (`ease:"none"` — constant velocity
  is the point) with speed-lines; a couple tumble off the road.
- **Turn** — nothing happens — that IS the turn: the stream never slows for the lost ones
  (a beat of pointed non-reaction; the receipt column stays empty).
- **Act 2** — three struck-through chips land on their words: `receipts ✗ · resends ✗ ·
  waiting ✗`.
- **Lands on:** "never look back", the three chips on "no receipts, no resends, no waiting".

### slot_jitter — HALF-SCREEN PANEL
Narration: "Your device keeps a tiny jitter buffer, a fraction of a second of audio to
smooth out packets arriving unevenly."
- **Act 1** — packets arrive bunched/uneven into a small holding tank (the buffer), level
  sloshing.
- **Turn** — the outflow valve opens.
- **Act 2** — perfectly even packets exit the bottom; a tiny `~0.2s` capacity chip.
- **Lands on:** "tiny jitter buffer" (tank), "arriving unevenly" (bunched inflow).

### slot_robot — TAKEOVER (final)
Narration: "If a packet is lost, it isn't re-requested. The moment is skipped or papered
over. That's the robot voice. The trade is deliberate. For live conversation, being on
time beats being complete."
- **Act 1 (cyan)** — a live audio waveform scrolls; a packet goes missing; a gap opens in
  the waveform — and NO re-request fires (the return lane stays dark).
- **Turn** — the gap gets papered over: a synthetic patch snaps in, the waveform
  distorts — glitch bands + a robotic serration on the wave (robot-voice audio cue in the
  SFX pass).
- **Act 2 (amber)** — the trade card: `ON TIME` outweighs `COMPLETE` on a tipping balance
  (rotate a wrapper with real bounds, or trig/onUpdate — never GSAP rotation on a bare line).
- **Lands on:** "isn't re-requested" (dark return lane), "robot voice" (distortion),
  "on time beats being complete" (balance settles).

### slot_ai_angle — TRANSPARENT BAND
Narration: "Modern calls soften the damage with AI, models that reconstruct the missing
milliseconds and strip background noise, so small losses become inaudible."
Linework: the gapped waveform returns; an AI shimmer sweeps and the gap regrows
seamlessly; a noise fuzz layer beneath the wave dissolves.
- **Lands on:** "reconstruct the missing milliseconds" (regrow), "strip background noise"
  (fuzz gone).

### slot_payoff — HALF-SCREEN PANEL (visual callback to the hook)
Narration: "Netflix delivers the past perfectly. A call delivers the present imperfectly,
because late is worse than flawed."
The hook's split returns, relabeled: left `THE PAST — PERFECT`, right `THE PRESENT — ON
TIME`; the call tile shows one tiny glitch and keeps going — and that's fine.
- **Act 1** — split returns. **Turn** — labels swap in. **Act 2** — quiet hold.
- **Lands on:** "past perfectly" / "present imperfectly". **NO tease chip.**
