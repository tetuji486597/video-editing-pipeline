# EP27-29 (BRAINROT EDITION) — format plan and per-slot briefs

Read first, in order: `LESSONS_EP20-26.md` (margins x70-870 / y200-1280, graphics NEVER block
text, centered stickers, the fromTo/from-only trap, the missing-class collapse trap, the
crop-iw trap), `OVERLAY_SPEC.md`, `SAFE_ZONE.md`, `BRAINROT_STYLE.md` (cast + sourcing),
`WRITING_RULES.md` (for any on-screen text you author). The EDL is authoritative for every
time: `episodes/<ep>/edl.json` + `beats.md`. Real assets live in `episodes/<ep>/assets/` and
`shared_assets/brainrot/` (see `episodes/ATTRIBUTIONS_EP27-29.md`). Brainrot SFX are
`sfx_shared/br_*.mp3` (see `sfx_shared/BRAINROT_SFX_NOTES.md`).

## Batch-wide conventions (differences from EP20-26)

- **ONE cut per episode** (no A/B): `edl.json`, `master.ass`, `final_nosfx.mp4`, `final.mp4`.
- **The presenter drifted from the script; the recorded words win.** Land every visual on
  the words in `beats.md`, not on the script text.
- **Title stickers (TikTok white boxes, centered on x=540, widest box <=660px, top >=210):**
  - EP27 has NO intro — cold open on the hook. Sticker carries the hook line:
    `NETFLIX HAS A ROBOT` / `THAT BREAKS NETFLIX` / `ON PURPOSE`, held over the HOOK beat,
    fading before PROBLEM. It runs simultaneously with the hook overlay — that overlay must
    live in the lower band and be pairwise-collision-checked against the sticker.
  - EP28 intro (new wording, matches the spoken line): `EXPLAINING STREAMING` /
    `TO GEN ALPHA` / `IN 30 SECONDS`, held over INTRO, fading before HOOK.
  - EP29 intro: `EXPLAINING CONTENT` / `MODERATION TO` / `GEN ALPHA IN 30 SECONDS` — four
    boxes if needed to keep each <=660px; hold over INTRO, fade before HOOK.
- **Every spoken "six seven" gets the bit**: a LaMelo Ball cutout doing the 6-7 hand bob
  pops in for ~1.2s (small, corner, inside margins) + the `br_67` snippet in the SFX pass.
  EP27 hook "Six, seven"; EP28 "sixty-seven seconds" (PROBLEM x2, NEW_COMPONENT x1);
  EP29 "sixty or seventy percent".
- **Cast = real sourced brainrot art** (Italian brainrot PNGs, Skibidi Toilet/Cameraman,
  LaMelo, Kai Cenat, Livvy Dunne, MrBeast, Among Us crewmate, the real Chaos Monkey logo),
  inset in designed chrome per EP4's pattern. No emoji anywhere — SVG glyphs only.
- **Hyper-saturated palette allowed**; deep-fried "turn" transitions on-brand. Meme-style
  Impact-font captions INSIDE overlays are allowed (never covering the burned-in captions
  band y>=1280, never covering the composition's own text).
- **Crude lines stay in the AUDIO only.** On-screen text must stay PG-13: do not print
  "backshots", "raw dogging", "Diddy party", "subhuman". Visualize the idea, not the word.
- **SFX pass**: 14-19 distinct sounds per episode, no repeats; brainrot set first, the
  TikTok set for texture. Voice-meme cap is LIFTED for these three (4-6 per episode is
  right), but never two voice memes within 1.5s of each other or over the presenter's own
  punchline word. Final mix per STYLE.md (loudnorm TP-2, peak check, audibility check with
  clean controls).

## Format-mix audit (planning stage)

| Ep | Formats in beat order | Distinct | Takeovers | Adjacent repeat |
|---|---|---|---|---|
| EP27 | transparent(hook, under sticker), TAKEOVER, motion-gfx, TAKEOVER, photo-card | 4 | 2 | none |
| EP28 | half-panel, TAKEOVER, motion-gfx, TAKEOVER(real capture), corner | 4 | 2 | none |
| EP29 | half-panel, TAKEOVER, motion-gfx, TAKEOVER, transparent, photo-card | 5 | 2 | none |

---

# EP27 — Netflix has a robot that breaks Netflix

`episodes/ep27-chaos/` · beats: HOOK, PROBLEM, BUILD, NEW_COMPONENT, PAYOFF (cold open)

### slot_tiktok_title — hook-text sticker (cold open), over HOOK
`NETFLIX HAS A ROBOT` / `THAT BREAKS NETFLIX` / `ON PURPOSE`. Fade before PROBLEM.

### slot_hook — TRANSPARENT BAND (lower band, under the sticker)
Spoken: "Six, seven. Okay, so Netflix has a robot, and the robot's whole job is to break
Netflix on purpose. What the skibidi?"
- **Act 1** — on "Six, seven": LaMelo 6-7 cutout pops (lower-left, small). Then
  Chimpanzini Bananini (banana-monkey) in a Netflix-red bandana with a wrench creeps toward
  a server-rack glyph; the REAL Chaos Monkey logo inset on the rack; neon `PRODUCTION` tag.
- **Turn** — on "break Netflix on purpose": he yanks a cable, one server goes dark.
- **Act 2** — on "what the skibidi": a Skibidi Toilet head pops up behind the rack.
- Lower band only (y ~ 700-1270 depending on measured chin — grid-measure), sticker owns
  the top. Translucent fills <=0.32; 2 labels max (`PRODUCTION`, one chip).

### slot_problem — TAKEOVER
Spoken: "Every company be glazing themselves like, 'Oh, our stuff never goes down.' And
then it goes down at Among Us three AM, and some poor NPC gets woken up, and everybody's
crashing out. Blud was capping. Holy aura loss."
- **Act 1 (smug blue)** — a conference slide `NEVER GOES DOWN` presented by a Skibidi
  Toilet; glazing sparkles.
- **Turn** — hard cut to `3:00 AM`; Tung Tung Tung Sahur IS the pager, knocking (bat) on a
  bedroom door; an Among Us crewmate as the "poor NPC" bolts upright; `PROD DOWN` in red.
- **Act 2 (red)** — Skibidi cameramen (the customers) filming the outage; an `AURA` counter
  (stacked digit spans) plummets to `-10,000` on "aura loss"; a `CAP` stamp on "capping".
- Lands: "never goes down" (slide), "three AM" (clock), "crashing out" (cameramen),
  "capping" (stamp), "aura loss" (counter). Two numbers max co-visible (3:00, -10,000).

### slot_build — MOTION GRAPHIC (transparent, upper band)
Spoken: "So Netflix went, 'Fine, we'll cook it ourselves.' That robot's called Chaos Monkey,
and it just unplugs a server in the middle of the day while everybody's sitting right there
watching. That's diabolical work, but let him cook."
- **Act 1** — a Netflix-red chip `CHAOS MONKEY` + the real logo lands on "Chaos Monkey".
- **Turn** — Chimpanzini unplugs ONE server on a mini rack (red X) on "unplugs a server"; a
  wall clock reads `2:00 PM` on "middle of the day"; beside it the dashboard stays GREEN.
- **Act 2** — Kai Cenat reaction cutout sipping coffee, calm, on "sitting right there
  watching"; a chef-hat SVG lands on the monkey on "let him cook".

### slot_new_component — TAKEOVER (the hero beat)
Spoken: "The fancy name for this is chaos engineering. You go, 'Okay, if I unalive this box,
nobody should notice.' And then you slime out the box and watch. If nothing happened, W
rizz. If something did break, low-key also Ws because you found out at lunch instead of
your two AM Diddy party. And then you get braver and start yeeting way more boxes at once,
like a whole Ohio of boxes."
- **Act 1 (cyan)** — a Roblox-style QUEST LOG: `GUESS ✓` (a speech chip "nobody should
  notice") → `KILL ONE BOX ✓` (a box glyph gets slimed — green goo SVG — on "slime out")
  → `WATCH ✓`. A dashboard line stays flat → `W RIZZ` chip on "W rizz".
- **Turn** — the line flinches (red blip) on "something did break"; `FOUND ONE` stamp with
  a moai SVG; a `LUNCH 12:30` vs `2:00 AM` clock pair (no party imagery) on "lunch
  instead of".
- **Act 2 (amber)** — Bombardiro Crocodilo carpet-bombs a whole grid of boxes on "yeeting
  way more boxes"; an Ohio-state outline SVG fills with boxes on "Ohio of boxes";
  dashboard still green.
- Headline <=6 words: `CHAOS ENGINEERING` (the one real term).

### slot_payoff — PHOTO CARD (still, quiet)
Spoken: "So break your own stuff in the day so it can't break you at night. Next, we'll talk
about why ChatGPT types like an unk."
- Day/night split card: sun side = Chimpanzini grinning with the wrench, all green; night
  side = everyone asleep (zzz wisps), all green. Headline `BREAK IT YOURSELF FIRST`.
  Optional: a small "unc" chair-and-cane SVG chip on "types like an unk". NO tease chip.

---

# EP28 — Why ChatGPT types so slow

`episodes/ep28-sse/` · beats: INTRO, HOOK, PROBLEM, BUILD, NEW_COMPONENT, PAYOFF

### slot_tiktok_title — `EXPLAINING STREAMING` / `TO GEN ALPHA` / `IN 30 SECONDS`, over INTRO.

### slot_hook — HALF-SCREEN PANEL
Spoken: "You know how ChatGPT yaps one word at a time? Like, chat, is this real or is bro
LARPing? Turns out it legiterally doesn't know the end of the sentence yet. Bro straight
freestyling from the dome."
- **Act 1** — a ChatGPT-style chat UI recreation types a brainrot answer word by word
  ("chat is this real 6 7 ...") with a blinking cursor; Tralalero Tralala (Nike shark)
  sprints alongside the cursor.
- **Turn** — on "doesn't know the end of the sentence yet": the cursor stops mid-word and
  an `idk yet` thought bubble (SVG) appears.
- **Act 2** — on "freestyling from the dome": a tiny mic-drop SVG and the typing resumes.
- Panel in the band clear of the face (grid-measure); ChatGPT chrome is a recreation.

### slot_problem — TAKEOVER
Spoken: "So the AI makes one word at a time, and a long answer takes, like, sixty-seven
seconds to finish. If you had to look at a blank screen for sixty-seven seconds, we would
close the tab and might even touch grass. Like bro, Psy bow."
- **Act 1** — blank screen + spinner; Trippi Troppi (confused shrimp-cat) staring; a
  stopwatch crawls `0:00 → 1:07` (the only number; it IS 67 seconds — LaMelo 6-7 pop on
  the first "sixty-seven").
- **Turn** — on "close the tab": the tab's X gets smashed, the browser window flies off.
- **Act 2** — on "touch grass": a grass strip SVG rises and Trippi walks onto it; on
  "Psy bow" a `SYBAU` chip (that spelling) slams. `-1000 AURA` optional.

### slot_build — MOTION GRAPHIC (transparent)
Spoken: "So instead of raw dogging the whole answer, the server just backshots each word to
your phone the second it pops out. There's one pipe, and it stays open, and words keep
falling down it."
- **Act 1** — MODEL glyph → ONE PIPE → phone screen. A Chimpanzini Bananini army, each
  carrying one word chip, sprints down the pipe; each word appears on the phone the instant
  its monkey arrives (lands on "the second it pops out").
- **Turn** — the pipe glows `OPEN` on "stays open".
- **Act 2** — words keep falling; the phone fills line by line.
- On-screen text: `ONE PIPE` / `OPEN` only (never print the crude words).

### slot_new_component — TAKEOVER (with the REAL capture)
Spoken: "That pipe is called server-sent events, SSE, and the thing about it is it only
goes in one direction, from the server down to you. The chat app episode had a pipe that
went both ways, but you talk back in a chat. Here you're just an NPC listening, so one way
is fine. And the sneaky part is the first word shows up in, like, half a second, so your
brain goes, 'Oh, that was fast,' even though the whole thing still took sixty-seven
seconds. It's basically continuous aura farming."
- **Act 1** — side-by-side: LEFT `SSE` one-way pipe (arrow down only) vs RIGHT `CHAT`
  two-way pipe with a Skibidi Toilet and a Cameraman yapping both directions; an Among Us
  crewmate labelled `NPC` sits at the bottom of the SSE pipe on "NPC listening".
- **Turn** — the right side dims; `ONE WAY ONLY` slams on the left.
- **Act 2** — the REAL DevTools/event-stream capture (assets) inset in browser chrome,
  chunks arriving; a stopwatch split `FIRST WORD 0.5s` vs `WHOLE THING 1:07` (retire one
  before the other lands — two numbers max), LaMelo 6-7 pop on "sixty-seven"; an `AURA`
  meter ticking up on "aura farming".
- Headline: `SERVER-SENT EVENTS` (the one real term).

### slot_payoff — CORNER ACCENT
Spoken: "So give people the first word right away instead of making them bed rot until the
last one. Next, we'll look at who's reading a billion posts a day."
- A chat cursor chip with the first word already shown and the rest ghosted, on "first
  word right away"; a tiny bed-with-phone SVG on "bed rot". NO tease chip.

---

# EP29 — Who reads your skibidi posts

`episodes/ep29-moderation/` · beats: INTRO, HOOK, PROBLEM, BUILD, NEW_COMPONENT, AI_ANGLE, PAYOFF

### slot_tiktok_title — `EXPLAINING CONTENT` / `MODERATION TO` / `GEN ALPHA IN 30 SECONDS` (split to 4 boxes if any exceeds 660px), over INTRO.

### slot_hook — HALF-SCREEN PANEL
Spoken: "A billion posts a day, a billion. MrBeast can't even count to a billion. So who's
reading your skibidi posts?"
- **Act 1** — a counter spins to `1,000,000,000` (stacked digits; the one number) on
  "billion"; a MrBeast cutout beside it with a "counting" finger, giving up on "can't even
  count".
- **Turn** — a pile of post cards pours in.
- **Act 2** — Trippi Troppi buried under the pile with a `help` sign on "who's reading";
  a Skibidi Toilet peeks from the pile on "skibidi posts".

### slot_problem — TAKEOVER
Spoken: "People are too slow, and robots are fast, but lokenuanly dumb. Like a robot will
see some Livvy Dunn post and go, 'Erm, that's a level ten gyat, booted.' Wrong, buddy.
Skill issue."
- **Act 1** — LEFT: a stadium of tiny Trippi Troppis reading phones (too slow); RIGHT: a
  robot judge (Bombardiro Crocodilo with a gavel).
- **Turn** — a social-post card with the REAL Livvy Dunne photo (public figure, the joke is
  the robot misjudging a gymnast photo) slides in; the robot slams `BOOTED` on it with a red
  X; a small `level 10` chip (no other text).
- **Act 2** — `WRONG` flashes; a human hand cursor flips it back with a green check; a
  `SKILL ISSUE` stamp on the robot on "skill issue".

### slot_build — MOTION GRAPHIC (funnel top)
Spoken: "So they use a funnel. First, anything that's an exact copy of something that
already got banned is a mad sus. Tung, tung, tung, gone. Just put the fries in the bag."
- **Act 1** — a funnel; posts pour in; an `EXACT COPY` pair of identical cards lights red
  with a fingerprint glyph; an Among Us `SUS` chip on "mad sus".
- **Turn** — Tung Tung Tung Sahur stamps the copies with the bat, three knocks in sync
  with "Tung, tung, tung"; the cards drop into a trash chute on "gone".
- **Act 2** — on "fries in the bag": a fries-bag SVG chip catches the last card.

### slot_new_component — TAKEOVER
Spoken: "Then the robot looks at everything else and gives each post a score. Is it a Chad?
It stays. Is it subhuman? You're cooked, buddy. In the mid-tier normies where the robot
goes, 'Uh, I don't know, chat. Like a sixty or seventy percent,' those go to an actual
person, and the person decides, and the robot watches what the person picked and gets a
little more based every time."
- **Act 1** — Ballerina Cappuccina spins between four meters `NUDITY / VIOLENCE / SPAM /
  HATE`; each post gets a SCORE dial (trig/onUpdate needle). A gigachad-style silhouette
  card scores high → green `STAYS`; a burnt-toast card scores low → red `COOKED` (never
  print the slur-adjacent word).
- **Turn** — a `normie` card lands at `67%`: the dial wobbles, `idk chat` chip, LaMelo 6-7
  pop on "sixty or seventy".
- **Act 2** — the card slides down a `HUMAN` lane to a Kai Cenat cutout who decides; a
  loop-arrow carries his call back up into the robot as `ROBOT LEARNS`; a `BASED` meter
  ticks +1 on "based".
- Two numbers max co-visible (67% + the based meter).

### slot_ai_angle — TRANSPARENT BAND
Spoken: "There's a name for that too, human in the loop. The robot does the giant pile, and
people do the goofy ahh ones, and the robot keeps learning from the people. Robot mogs on
volume, human mogs on vibes."
- Linework: ROBOT side a torrent of tiny post chips (`GIANT PILE`); HUMAN side one weird
  card (`GOOFY ONES`); a loop arrow between them; on "mogs on volume / vibes" a two-bar
  flex meter (`VOLUME` for the robot, `VIBES` for the human). Headline `HUMAN IN THE LOOP`.

### slot_payoff — PHOTO CARD
Spoken: "So the robot takes the easy ones. Humans take the weird ones. Next, we'll look at
how apps run experiments on you without telling you. You're the NPC. Sorry."
- The un-booted Livvy post with the green check held as a card, the funnel ghosted behind;
  headline `PEOPLE DO THE HARD ONES`; on "You're the NPC" an Among Us crewmate labelled
  `YOU` pops in the corner. NO tease chip.
