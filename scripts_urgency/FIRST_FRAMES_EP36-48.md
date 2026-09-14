# First frames for EP36-48

Rule set (from the hook research, 2026-09-06): frame zero is already moving, the visual is the
premise, at most five words of on-screen text, the presenter is mid-sentence, no sticker and no
series title. The concept name arrives around second eight. Episode number goes in the caption.
Each entry: FRAME (what is on screen at t=0) · TEXT (on-screen, all caps) · LINE (first spoken
sentence) · HOW (how to shoot it).

## EP36 — zero downtime
FRAME: a real checkout screen (phone screen-record, Amazon or Stripe test page) with the "Pay"
button pressed, and a version tag in the corner flipping from v41 to v42 while the spinner keeps
spinning. Presenter is not in frame yet.
TEXT: UPDATED MID-CHECKOUT
LINE: "They swapped the app out from under you while you were paying."
HOW: screen-record a checkout on your phone, overlay a small version chip that flips at t=0.4s,
cut to you at ~2s already talking.

## EP37 — observability
FRAME: a wall of real log lines scrolling fast (Grafana demo or a `kubectl logs` dump), one red
line frozen and circled while the rest keep moving. Presenter in the corner, small.
TEXT: 3 USERS. 400 SERVERS.
LINE: "Three users in Brazil hit a bug and the team found the exact line in five minutes."
HOW: screen-record a busy log tail, freeze one line with a red ring, keep the scroll moving
around it.

## EP38 — circuit breakers
FRAME: a real status page (githubstatus.com works) going red one row at a time, top to bottom,
like dominoes. Sound of a breaker clunk at the last one.
TEXT: ONE SLOW SERVER
LINE: "One slow server, and sixty seconds later the whole app is dead."
HOW: recreate the status page in HyperFrames from the real capture (you already have it from
EP32), animate rows green to red at 0.15s intervals, cut to you on the clunk.

## EP39 — video fingerprinting
FRAME: the same clip playing twice side by side, the right one mirrored, colour-shifted and
letterboxed, with a MATCH 99% badge slamming on at t=0.5s.
TEXT: STILL CAUGHT
LINE: "Flip it, filter it, crop it. YouTube still knows it's the same video."
HOW: use your own EP26 final as the clip, ffmpeg hflip + hue shift for the right side, badge
in HyperFrames. Bonus: the real 8x8 grayscale fingerprint (from the Krawetz walkthrough) in
frame two.

## EP40 — event sourcing
FRAME: a bank app balance ($2,341.07) on a phone, and at t=0.3s the number dissolves into a
scrolling column of transactions behind it.
TEXT: THIS NUMBER DOESN'T EXIST
LINE: "Your bank has never stored your balance. Not once."
HOW: mock the app in HyperFrames with a realistic balance screen; the dissolve is the pattern
interrupt.

## EP41 — transactions
FRAME: a "Send $100" confirmation on one phone and, at t=0.4s, the screen going black mid
animation with a hard cut to silence.
TEXT: $100. GONE.
LINE: "A crash right here deletes a hundred dollars from both accounts."
HOW: film a real phone screen (any payment app in a sandbox), cut to black on a beat, then to
you. The silence is the interrupt; every other video on the feed is loud.

## EP42 — write-ahead log
FRAME: your hand already on a power cable behind a running database terminal (a live
`INSERT` loop printing rows). You pull it at t=0.5s and the terminal dies.
TEXT: MID-WRITE
LINE: "I just killed a database in the middle of a write. Watch it come back with nothing
missing."
HOW: real hardware, real Postgres or SQLite in a loop on a laptop, real cable. This is the
strongest first frame in the batch because it is physically true and nobody else does it.

## EP43 — CAP theorem
FRAME: two server boxes joined by a cable that a pair of scissors is already closing on. The
cut lands at t=0.6s and both boxes flash a question mark.
TEXT: PICK ONE: RIGHT OR ONLINE
LINE: "The moment this cable is cut, your database has to choose between being right and
being online."
HOW: HyperFrames, mirror the illustrated-proof drawings from the visual ref; scissors are a
real prop if you want it physical (a cheap ethernet cable on camera).

## EP44 — consistent hashing
FRAME: a Discord server list (real screenshot) and, behind it, a grid of a thousand dots that
all jump to new cells at once when a single new box slides in.
TEXT: ADD ONE SERVER. EVERYTHING MOVES.
LINE: "Add one server the normal way and every single piece of data has to move house."
HOW: the dot-stampede is the incomplete visual; the payoff later is the same grid where only
one slice moves.

## EP45 — Bloom filters
FRAME: a plain black square that flickers a few bits on, then a huge "PROBABLY" stamp.
TEXT: WRONG ON PURPOSE
LINE: "This data structure is allowed to lie, and Google, Chrome and your bank all run on it."
HOW: screen-record samwho.dev/bloom-filters flipping bits as you add items; stamp in
HyperFrames. The contrarian claim carries it; the visual is the oddity.

## EP46 — consensus
FRAME: five server boxes voting with raised hands, one of them lying (its hand goes up and
down), messages between them dropping off the edge of the screen.
TEXT: 5 SERVERS. NO BOSS.
LINE: "Five computers, no boss, half the messages get lost, and they still agree every time."
HOW: screen-record thesecretlivesofdata.com/raft election segment as the base, add the liar
and the dropped messages on top.

## EP47 — CRDTs
FRAME: one sentence in a Google Doc with three cursors in it, all typing into the same word at
once, and the word coming out clean.
TEXT: 50 PEOPLE. ONE SENTENCE.
LINE: "Fifty people typing into the same sentence, and it never turns to garbage."
HOW: actually do it: open a doc in three browsers, type simultaneously on a loop, screen-record
the real thing. The real cursors beat any mock.

## EP48 — launch day (finale)
FRAME: a view counter spinning past 1,000,000 while a lone server icon under it glows red and
starts to melt. Presenter walks into frame at t=1s.
TEXT: 1,000,000 USERS. ONE SERVER.
LINE: "A million people just opened your app and you have one server. You have about nine
seconds."
HOW: stacked-digit counter in HyperFrames, melt from the EP33 problem takeover, real walk-in
so the frame has motion before you speak.

## Shared notes
- The line is spoken over the visual, not after it. You are mid-sentence when you first appear.
- No "explaining", no "episode", no "system design" in the first three seconds. The concept is
  named when the viewer is already in (second eight to ten).
- Keep the countdown gag if you like it, but start the chip at ~2s, not at frame zero.
- Post two versions of one episode (old open vs new open) before re-cutting the rest, and
  compare "stopped watching at" and average watch time.
