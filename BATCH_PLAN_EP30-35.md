# EP30-35 overlay batch — conventions and per-slot briefs

Read first, in this order: `OVERLAY_SPEC.md`, `SAFE_ZONE.md`, `LESSONS_EP20-26.md`,
`LESSONS_EP27-29.md`, the `system-design-overlays` skill, and the EP4 gold references
(`episodes/ep4-captcha/animations/slot_new_component/` and `slot_problem/`, read the source).
This file only adds what is specific to these six episodes. **The EDL is authoritative for
all times**: beat windows in `episodes/<ep>/edl.json` (`_beat_windows_output_timeline`) and
every spoken word in output seconds in `episodes/<ep>/beats.md`. No hard-coded seconds here.

## Batch-wide conventions

- **Single variant per episode.** Not brainrot: house style (EP20-26), plain explainer tone.
- **Recorded intro = "Explaining <topic> in 30 seconds."** (EP35: "Monolith versus
  microservices in 30 seconds."). The presenter never says the episode number, but the user
  wants it on the title anyway. **Title sticker** (TikTok-native white boxes, centred on
  x=540, every box <=660px wide, top of stack y=210, matches
  `episodes/ep29-moderation/animations/slot_tiktok_title/`):
  | ep | boxes |
  |---|---|
  | EP30 | `EPISODE 30` / `EXPLAINING A/B TESTING` / `IN 30 SECONDS` |
  | EP31 | `EPISODE 31` / `EXPLAINING SHARDING` / `IN 30 SECONDS` |
  | EP32 | `EPISODE 32` / `EXPLAINING` / `REPLICATION` / `IN 30 SECONDS` |
  | EP33 | `EPISODE 33` / `EXPLAINING` / `LOAD BALANCERS` / `IN 30 SECONDS` |
  | EP34 | `EPISODE 34` / `EXPLAINING` / `DIFFIE-HELLMAN` / `IN 30 SECONDS` |
  | EP35 | `EPISODE 35` / `MONOLITH VS` / `MICROSERVICES` / `IN 30 SECONDS` |
  The sticker covers the INTRO window only (start 0.0, duration = INTRO end, fade out
  ending exactly on the INTRO end so the HOOK cut is clean). Font 44-50px so the widest
  line fits; the `EPISODE NN` box may be smaller (36px) and sit on top.
- **THE COUNTDOWN GAG (user request).** He promises "in 30 seconds"; the episode takes
  45-62s. A stopwatch chip counts 30 -> 0 over the whole remaining video, i.e. slowly
  (`tool/helpers/make_countdown.py`, composited by the coordinator, NOT by builders). It sits
  in the **top-right corner: x 690-870, y 205-305**, from the INTRO end to the last frame,
  on top of everything. **Every slot except the title sticker must keep the corner
  x >= 670, y <= 330 empty** (takeovers included: no headline, chip, glow or push-in
  reaching it — put takeover headlines at y >= 340 or keep them <= 650px wide and left
  of x=660). `check_margins.py` does not know about this reserve; probe it yourself on the
  render (alpha > 8 in that box on any frame = fail).
- **Face geometry (all six sources, measured at 1080x1920):** hair top ~120, brow ~640,
  eye line ~720, mouth ~1000, chin ~1200, face x 240-840. Non-takeover content lives in
  the upper band y 200-600 (over hair/forehead, clear of the brow) or as a left column
  (x 70-330) beside the face. No chest band exists.
- **Captions:** `--caption-font-size 60 --caption-margin-lr 220 --caption-margin-v 400`,
  band y ~1320-1520. Content floor y <= 1280. Zoom 1.0<->1.08 about (540,720).
- **Rendering:** call `tool/helpers/hf_render.sh <slot_dir>` (machine-wide queue, max 2
  concurrent, retries once). Never call npx directly and never run more than one render
  per builder at a time. Takeover renders take 5-14 min; budget for it.
- **Real images:** at least one per episode (listed per episode). Fetch with `curl -A
  "Mozilla/5.0 ..."` into `episodes/<ep>/assets/`, record source + licence in
  `episodes/<ep>/assets/ATTRIB.md` and append to `episodes/ATTRIBUTIONS_EP30-35.md`.
  Personal use only, per the user. ffprobe every image before use.
- **Format mix per episode:** >= 3 distinct formats, <= 2 takeovers, no adjacent repeat,
  every composition two-act (act 1 -> turn -> act 2), no tease chips, no emoji, PG-13.
- **Audits before reporting:** `check_margins.py` clear on every render, `check_fade.py`,
  `check_overlay_files.py` 0 problems, `check_overlay_timing.py` inside beat,
  `check_safe_zone.py`, `check_caption_band.py`, the corner-reserve probe, and composites
  of act-1/turn/act-2 frames over the REAL source frame (with the EDL zoom) proving no
  overlay covers text or the face on non-takeovers.

## Format-mix plan

| Episode | Formats in beat order | Distinct | Takeovers |
|---|---|---|---|
| EP30 | sticker, half-panel (two phones), TAKEOVER, motion-gfx (switch), TAKEOVER, transparent band, photo-card | 5 | 2 |
| EP31 | sticker, half-panel, motion-gfx (vertical wall), TAKEOVER, transparent band, corner card | 5 | 1 |
| EP32 | sticker, corner accent (fire), TAKEOVER, motion-gfx (replication), TAKEOVER (failover), transparent band | 4 | 2 |
| EP33 | sticker, transparent band (crowd), TAKEOVER (dogpile), motion-gfx (dealer), TAKEOVER (least-conn/flatline), corner card | 4 | 2 |
| EP34 | sticker, half-panel (room), motion-gfx (wire), TAKEOVER (paint), TAKEOVER (final colour + padlock), corner (padlock), transparent band | 5 | 2 |
| EP35 | sticker, VS card (half-panel), motion-gfx (monolith block), TAKEOVER (split), transparent band (gauge), corner stamp | 5 | 1 |

---

# EP30 — How companies test on you without telling you (feature flags + A/B)

`episodes/ep30-abtesting/` · beats: INTRO, HOOK, PROBLEM, BUILD, NEW_COMPONENT, AI_ANGLE, PAYOFF
Real image: a real feature-flag dashboard screenshot (LaunchDarkly or Unleash docs page,
`assets/`), used inside slot_build's switch card as the "flag" UI; plus a real A/B result
table screenshot (Optimizely/VWO docs) if cheap, else redraw.

### slot_hook — HALF-PANEL (upper band)
Narration: "Right now, different people are running slightly different versions of the same app and none of them can tell."
Two phone mock-ups side by side, same app, subtly different: one has a blue button, the
other green; one label reads `Buy now`, the other `Get it`. Act 1: both phones slide in
identical. Turn on "slightly different": the diffs highlight with thin rings. Act 2 on
"none of them can tell": the rings fade, two small `you` / `your friend` labels, a `?`.
Lands: "different versions", "can tell". Widths: phones x 120-480 and 560-860, y 220-590.

### slot_problem — TAKEOVER
Narration: "Here's the problem: shipping a new feature to one hundred percent of users at once is risky. If it's broken or people hate it, everyone gets hit at the same time, and rolling back is painful."
Act 1 (cyan): a `100%` rollout dial slams to full; a 6x8 grid of user avatars all flip to
the new feature at once. Turn on "broken": red error cascade — every avatar flashes a red
`!` in a wave (this is the EFFECTS note "red error cascade across all users"). Act 2
(amber) on "rolling back": a `ROLLBACK` lever that drags painfully slowly, avatars
un-flip one by one, a sweat drop. Numbers on screen: `100%` only. Headline y >= 340.

### slot_build — MOTION GRAPHIC (upper band)
Narration: "A feature flag wraps the new code in a switch you can flip without redeploying. The code ships dark, meaning off by default."
A code card `<NewCheckout/>` wrapped by a bracket labelled `if (flag)`; a physical toggle
switch beside it. Act 1: the bracket draws around the code on "wraps". Turn on "flip":
the toggle flips ON then OFF with a click (SFX pass), `no redeploy` chip. Act 2 on "ships
dark": the card dims to a dark ghost, `OFF by default` chip. Real flag-dashboard capture
inset as a small reference thumbnail if used. Keep x 70-660, y 210-600.

### slot_new_component — TAKEOVER (final)
Narration: "You turn it on for one percent of users and watch the metrics. If they look good, you ramp up, and if something breaks, you kill it instantly. Show version A to half your users and version B to the rest. Compare the numbers, and you've run an A/B test. That's how product decisions get made from actual numbers."
Act 1 (green): the toggle from BUILD at `1%`; a metrics sparkline draws; a ramp meter
1% -> 5% -> 25% on "ramp up"; on "kill it instantly" a red `KILL` button slams and the
meter drops to 0 in one frame. Turn on "version A": phase shift to blue/orange. Act 2:
the audience bar splits A | B with a wipe (EFFECTS note), two phones with A/B variants,
a result table `A 3.1%  B 4.4%`, B lights up; `DECISION` stamp on "actual numbers".
Two numbers max co-visible (retire the ramp % before the A/B results).

### slot_ai_angle — TRANSPARENT BAND (upper band)
Narration: "New AI models get rolled out the exact same way — they're flagged on for a small slice of users and A/B tested before everyone gets them."
A model chip `GPT-next` behind the same toggle; a pie with a thin `small slice` wedge lit.
Act 1: chip + toggle. Turn on "small slice": the wedge highlights. Act 2 on "A/B tested":
two tiny chat bubbles A/B, then the wedge grows to full on "everyone gets them".

### slot_payoff — PHOTO/CARD (upper band)
Narration: "So ship it dark and let one percent of users decide whether the rest get it. Next we'll look at how a database outgrows one machine."
Card: `'SHIPPED' AND 'TURNED ON' ARE SEPARATE STEPS` in two lines, a dark ghost card
becoming lit on "turned on"... keep it to: ship-box icon (dark) -> toggle -> `1%` pie.
Lands on "ship it dark", "one percent". No tease chip.

---

# EP31 — How databases hold a billion rows (sharding)

`episodes/ep31-sharding/` · beats: INTRO, HOOK, PROBLEM, BUILD, NEW_COMPONENT, PAYOFF
Real image: DigitalOcean "Understanding Database Sharding" diagram = redraw-ref only; use a
REAL public logo/photo of a data-centre rack row (Wikimedia Commons, CC) for slot_payoff's
"more boxes" card, and a Facebook user-count figure chip (`3.0B users`) with source noted.

### slot_hook — HALF-PANEL (upper band)
Narration: "So no single database server can hold all of Facebook, so they break the data into pieces. Here's how that works."
One database cylinder labelled `ALL OF FACEBOOK` bulging and cracking (crack lines draw,
a strain meter pegs). Turn on "break the data into pieces": it splits into 4 tidy
cylinders with a clean snap. Act 2: the pieces settle in a row, `pieces` label.

### slot_problem — MOTION GRAPHIC (vertical wall, upper band)
Narration: "So you can scale a database vertically with a bigger CPU and more RAM in the same box, but there's a hard ceiling, and it gets absurdly expensive fast."
A server box grows in three steps (`CPU`, `RAM` chips fatten), an up-arrow `VERTICAL`.
Turn on "hard ceiling": a thick ceiling bar slams down and the box bonks it (thud in the
SFX pass). Act 2 on "absurdly expensive": a `$` price tag that stacks `$` `$$` `$$$$` and
tips over. Keep left of x=660, above y=600.

### slot_build — TAKEOVER
Narration: "So instead we scale horizontally by sharding. The data gets split across many machines, and each one holds a slice."
Act 1 (cyan): one big table of rows; a `HORIZONTAL` arrow. Turn on "split": the table
splits into 4 slices that fly to 4 machines (clean split animation, EFFECTS note). Act 2:
each machine shows its slice with a `1/4` chip; a soft `SHARDS` headline at y >= 340.

### slot_new_component — TRANSPARENT BAND (upper band) — long beat, keep it evolving
Narration: "A shard key, say user ID, decides which machine your data lives on. Simplified, users A through M go on shard one and N to Z on shard two. Each shard handles reads and writes for its own slice, so when you need more capacity you just add more machines. The hard parts are picking a key that spreads load evenly and handling queries that need data from several shards."
Act 1: a `shard key = user_id` chip routes user cards to `A-M -> SHARD 1` / `N-Z -> SHARD 2`
(router arrow flicks per card). Turn on "add more machines": a third machine slides in,
routes rebalance. Act 2 on "hard parts": a lopsided load meter (one shard hot) and a query
card that fans out to all shards with a `?`. Land on "A through M", "N to Z", "add more
machines", "several shards". Text budget: labels only, no sentences.

### slot_payoff — CORNER CARD (upper-left, x 70-500)
Narration: "So when you can't make the box any bigger, you use more boxes. Next, we'll talk about how apps survive a server catching fire."
One box with a `MAX` tag -> three boxes, `SPLIT THE DATA; SCALE BY ADDING MACHINES` as two
short lines. Real rack-row photo inset small if it reads. Lands on "more boxes". No tease.

---

# EP32 — How apps survive a server catching fire (replication + failover)

`episodes/ep32-replication/` · beats: INTRO, HOOK, PROBLEM, BUILD, NEW_COMPONENT, PAYOFF
Real image: a screenshot of thesecretlivesofdata.com/raft log-replication step (`assets/`)
inset in slot_build or slot_new_component; a real "status page: all systems operational"
capture for the hook's calm users.

### slot_hook — CORNER ACCENT (upper-left) + calm users
Narration: "So a server dies and users don't notice a thing. That's replication and failover doing their job."
A small server icon catches fire (SVG flames, licking, translucent) on "dies"; beside it
two tiny phone screens keep scrolling calmly with a green dot. Turn on "don't notice":
a `nobody noticed` chip. Act 2: `REPLICATION` / `FAILOVER` two small chips on the words.

### slot_problem — TAKEOVER
Narration: "If all your data sits on one machine and it fails, you're down, and you may have lost data for good. That's unacceptable for anything important."
Act 1 (amber): one machine with all the data rows inside. Turn on "fails": blackout glitch
(EFFECTS note): the whole frame flickers dark, the machine dies with a red X, rows
dissolve to ash on "lost data for good". Act 2 (red): `DOWN` headline y >= 340 and a
`data: 0 rows` counter (the only number).

### slot_build — MOTION GRAPHIC (upper band)
Narration: "So we replicate: live copies of the data on several machines. One is the leader and takes the writes, and the followers copy every change."
Leader box (crown) on the left, two follower boxes right; a write packet lands on the
leader and copies stream to both followers in real time (continuous). Turn on "leader":
the crown pops. Act 2 on "copy every change": copies pulse. Real raft screenshot inset
as a thumbnail with a `real thing` tag if it fits under x=660.

### slot_new_component — TAKEOVER
Narration: "If the leader dies, the system notices and promotes a follower to be the new leader. That's failover and the traffic reroutes on its own often within seconds. The copies also serve reads day-to-day which spreads the load. The whole point is redundancy so no single machine is irreplaceable."
Act 1: the three nodes from BUILD; leader flames out on "dies"; a heartbeat monitor
flatlines; the crown jumps to a follower with a ding on "promotes" (EFFECTS note). Turn:
`FAILOVER` headline (y >= 340), reroute arrows re-draw smoothly to the new leader on
"reroutes", a `< seconds` chip. Act 2: read arrows fan out to all nodes on "serve reads";
on "redundancy" every node gets a small `spare` badge. Two numbers max.

### slot_payoff — TRANSPARENT BAND
Narration: "So redundancy looks like waste until the day that it saves you. Next, we'll look at the traffic cop that decides which of those servers you talk to."
Two idle copies with `waste?` fading to `saved you` on "saves you"; keep copies + a shield.
No tease chip.

---

# EP33 — The traffic cop in front of every big app (load balancing)

`episodes/ep33-loadbalancing/` · beats: INTRO, HOOK, PROBLEM, BUILD, NEW_COMPONENT, PAYOFF
Real image: samwho.dev/load-balancing screenshot (`assets/`) inset in slot_new_component
as the "real simulation"; Cloudflare learning-centre diagram = redraw-ref only.

### slot_hook — TRANSPARENT BAND (crowd)
Narration: "A million people just opened the same app. No single computer handled that because a traffic cop split them up before they ever arrived."
A dense particle crowd of request dots (hundreds, animated) funnelling toward one app
icon; a `1,000,000` counter (stacked digits). Turn on "traffic cop": a small cop/diamond
glyph appears in the funnel neck and the stream fans into lanes. Act 2 on "before they
ever arrived": lanes reach 5 small servers. Keep y 210-600.

### slot_problem — TAKEOVER
Narration: "One server melts under real traffic, so you run 50 identical copies. But there's a new problem: every incoming request has to pick a server and if you pick badly some servers get buried while others sit idle."
Act 1 (red): one server melts (drips, wobble) under a torrent. Turn on "50 identical
copies": a 5x10 grid of servers slams in with a shutter flash. Act 2 (amber) on "pick
badly": all arrows dogpile onto ONE server (pile-up thud), it buries under a stack,
the others show `idle` zzz. Headline y >= 340. `50` is the only number.

### slot_build — MOTION GRAPHIC (upper band, card dealer)
Narration: "A load balancer stands in front of the whole fleet. Every request hits it first and it deals them out. The simplest version is round robin: one for you, one for you, and back around."
A dealer chip `LB` at the left; request cards fly in and get dealt 1-2-3-1-2-3 to three
servers (snap per deal in the SFX pass). Turn on "round robin": a circular arrow
label `ROUND ROBIN`. Act 2 on "back around": the deal loops visibly. Land each "one for
you" on a dealt card (words in beats.md).

### slot_new_component — TAKEOVER
Narration: "Smarter versions send each request to whichever server has the fewest active connections, so slow requests don't pile up in one place. It also keeps health checking the fleet. If a server stops answering, it gets pulled out of rotation which is exactly how last episode's failover stayed invisible to users."
Act 1 (cyan): three servers each with a `connections` meter (3 / 7 / 1); a new request
routes to the lowest with a highlight; `LEAST CONNECTIONS` headline y >= 340. Turn on
"health checking": heartbeat blips on every server. Act 2 on "stops answering": one
server's heartbeat flatlines, it greys and pops out of the lineup on "pulled out"
(EFFECTS note); a small `EP32 failover` callback chip on "last episode's failover". Real
samwho screenshot inset at the bottom (y <= 1250) with a `real sim` tag.

### slot_payoff — CORNER CARD (upper-left)
Narration: "So scale usually looks like 50 ordinary servers and one smart doorman out front. Next we'll look at how two strangers share a secret while the whole world listens."
`50 ORDINARY SERVERS` grid of tiny boxes + `ONE SMART DOORMAN` (the LB glyph with a
bow-tie) landing on the words. No tease chip.

---

# EP34 — Sharing a secret while the whole world listens (Diffie-Hellman)

`episodes/ep34-diffiehellman/` · beats: INTRO, HOOK, PROBLEM, BUILD, NEW_COMPONENT, DH_NAME, PAYOFF
Real image: the Wikipedia Diffie-Hellman paint-mixing diagram (public domain,
`assets/dh_paint_wikipedia.png`) shown REAL in slot_new_component's act 2 as "the famous
picture"; a real https padlock capture from a browser URL bar for DH_NAME.

### slot_hook — HALF-PANEL (upper band)
Narration: "So two strangers can agree on a secret while everyone in the room listens to every word, and the eavesdropper still can't work it out. It actually happens every time you open a website."
Two figures at the ends of a room shouting (speech bursts), a crowd of eavesdroppers with
notepads between them (scribbling). Turn on "still can't work it out": the notepads show
`???`. Act 2 on "open a website": a tiny browser bar with a padlock slides in.

### slot_problem — MOTION GRAPHIC (wire, upper band)
Narration: "Encrypting a conversation needs a shared key. The trouble is two computers that just met have to agree on one over a line anybody could be tapping, and if you send the key, the tapper has it too."
Two laptops joined by a wire; a `KEY` chip travels the wire. Turn on "tapping": a tap
clamp bites the wire, the key duplicates into the tapper's hand (red). Act 2: `the tapper
has it too` — the copied key glows red. Keep x 70-660.

### slot_build — TAKEOVER (paint, part 1)
Narration: "The classic picture is paint. Both sides agree on a public color that everyone can see. Then each secretly mixes in a private color of their own, and they swap the mixtures again in the open."
Act 1 (yellow): two cups of the same public yellow, `PUBLIC` tag, an eavesdropper eye
watching. Turn on "secretly mixes": each side pours a private colour (red / blue) behind
a hand-shield, paint-swirl mixes with colour pops (EFFECTS note) -> orange / green. Act 2
on "swap": the two mixtures cross in the open, the eye sees them. Headline y >= 340.
Colours are the content; text budget: `PUBLIC`, `PRIVATE`, `SWAP` chips only.

### slot_new_component — TAKEOVER (paint, part 2 + the real diagram)
Narration: "Now each side adds their own private color to the other's mixture. Both end up with the identical final color. The eavesdropper only ever saw the mixtures, and unmixing paint is basically impossible. The real version uses math with that same one-way property, and what comes out is a shared key that never once traveled the wire."
Act 1: each side pours its private colour into the received mixture; on "identical final
color" both cups snap to the same brown with a match-cut + ding (EFFECTS note). Turn on
"unmixing paint": the eavesdropper tries to un-pour, an `impossible` chip, red X. Act 2 on
"real version uses math": the real Wikipedia diagram slides in (inset, tagged `the famous
picture`), a one-way arrow glyph; on "never once traveled the wire" a key chip appears on
BOTH ends with the wire between them empty.

### slot_dh_name — CORNER (upper-left)
Narration: "That's Diffie-Hellman. It runs inside the HTTPS padlock from the URL episode, and it's done in milliseconds."
`DIFFIE-HELLMAN` name chip; a real padlock capture; `ms` stopwatch chip on "milliseconds".
Padlock click in the SFX pass.

### slot_payoff — TRANSPARENT BAND
Narration: "So the secret never crosses the wire because each side builds the same one on its own. Next, we'll look at the monolith versus microservice fight."
Two cups growing the same colour on their own, the wire between them empty. No tease chip.

---

# EP35 — Monolith vs microservices, the real fight

`episodes/ep35-microservices/` · beats: INTRO, HOOK, PROBLEM, BUILD, NEW_COMPONENT, PAYOFF
Real image: Martin Fowler's monolith-vs-microservices sketch = redraw-ref; use a REAL
Amazon logo/photo? No — use a real screenshot of a services dependency graph (e.g. the
famous Amazon/Netflix "death star" microservice graph image, widely reposted) in
slot_new_component's complexity act, sourced and attributed.

### slot_hook — HALF-PANEL (VS card)
Narration: "So Amazon split its app into thousands of services, and most startups who copy that move are making a mistake. Here's the real trade-off."
Fighting-game `VS` card: `MONOLITH` (one block) vs `MICROSERVICES` (a swarm of dots),
VS flash on the card land (EFFECTS note). Turn on "making a mistake": a small `copying`
startup chip with a red X. Act 2 on "real trade-off": a balance scale glyph.

### slot_problem — MOTION GRAPHIC (upper band)
Narration: "A monolith is one big code base that deploys as a single unit. It's simple to start with, but at huge scale, one team's change can break everything, and you have to deploy the whole thing every time."
One big block with `DEPLOY` as a single button. Turn on "one team's change": a tiny
change pixel lights the whole block red in a wave. Act 2 on "deploy the whole thing":
the whole block re-deploys with a heavy progress bar. Keep x 70-660.

### slot_build — TAKEOVER
Narration: "Microservices split the app into small independent services. A team owns each one and deploys it on its own schedule."
Act 1: the monolith block shatters into 8 service tiles (EFFECTS note). Turn: phase
shift. Act 2 on "a team owns each": each tile gets a team avatar and its own tiny deploy
button; buttons press at different times on "own schedule". Headline y >= 340.

### slot_new_component — TRANSPARENT BAND (upper band), long beat
Narration: "That buys independent scaling and faster teams, but it adds real complexity. Every call now crosses a network and can fail in new ways, and debugging gets much harder. Honestly, microservices solve an organizational problem. If you don't have lots of teams stepping on each other, a monolith is usually the smarter choice."
Act 1: a complexity gauge climbs into red as network arrows multiply between tiles; a
call arrow fails with a red X on "fail in new ways"; a magnifier over the tangle on
"debugging". Turn on "organizational problem": a `PEOPLE PROBLEM` stamp. Act 2 on
"monolith is usually the smarter choice": the tiles regroup into one calm block with a
check. Real dependency-graph screenshot inset small during act 1 if it fits under x=660.

### slot_payoff — CORNER STAMP (upper-left)
Narration: "So microservices fix a people problem, so check that you actually have one. Next, we'll look at how to update an app with zero downtime."
`SPLIT WHEN YOUR TEAMS NEED IT` in two lines + a checklist tick on "check". No tease chip.
