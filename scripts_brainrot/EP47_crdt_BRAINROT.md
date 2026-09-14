# **EP 47 — How Google Docs lets 50 people type at once (BRAINROT EDITION)**

*Distributed Systems / Algorithms  ·  Advanced  ·  \~50s  ·  Builds: A collaborative editor  ·  New piece: Operational Transforms / CRDTs*

  

**0:00**  **HOOK —** Fifty people typing in the same Google Doc at the same time and nobody's letters get eaten. Chat, how? There's an algorithm for it and it's lowkey genius.

  

***ON-SCREEN:*** *"50 CURSORS. ONE DOC. NOTHING GETS EATEN."*

  

**0:03**  **PROBLEM —** The dumb way is two people type in the same sentence at the same second, and whoever's edit reaches the server last just overwrites the other guy. Or the two copies drift apart and now there's two different docs. Gg.

  

**0:08**  **BUILD —** There's two families of fixes. Family one is OT, operational transformation. Every edit that comes in gets redone against the edits that happened at the same time. So you typed a letter at spot six, but somebody else already typed one before yours, so yours slides to spot seven. Six seven. The server fixes the number for you.

  

**0:20**  **NEW COMPONENT —** Family two is CRDTs, conflict-free replicated data types, say it once and never again. Instead of a referee fixing things, the data itself is built so that whatever order the edits show up in, everybody ends up with the exact same doc. No boss needed. Either way, all fifty people's keystrokes land in one doc, live, and nothing gets eaten. Let them cook.

  

**0:38**  **PAYOFF + NEXT —** Everybody types at once and the doc still makes sense. Next one is the finale. A million users on launch day, and we use everything.

  

***ON-SCREEN:*** *"MERGE EVERYONE'S EDITS. LOSE NOTHING."*

  

**OVERLAYS / B-ROLL (timed) — brainrot cast**

  

**0:01**  A Google-Docs-style doc (REAL Docs UI chrome recreated, title blurred) with about fifty coloured cursors, each cursor a tiny Chimpanzini Bananini typing brainrot words ('skibidi', '6 7', 'gyatt'). Turn: the doc fills in perfectly and a 'HOW' Impact caption lands with Trippi Troppi eyes.

  

**0:06**  TAKEOVER: two Skibidi cameramen typing into the same sentence; their edits fly to the server as paper planes and Bombardiro Crocodilo's plane lands last, splatting over the other one, 'EATEN'. Act 2: split-screen, the two copies of the doc drift into different text with Brr Brr Patapim tangled between them, 'GG' stamp, IShowSpeed screaming cutout.

  

**0:16**  OT: a sentence with numbered slots; a letter aimed at slot 6 hovers, somebody inserts a letter earlier and every number shifts live, the target slides to 7, LaMelo 6-7 hands on 'six seven'; Lirilì Larilà's clock reads 'same second'. Turn: a referee-whistle server stamps 'FIXED' on the shifted edit.

  

**0:24**  TAKEOVER: CRDT, two edits with no referee in sight (the server chair is empty, 'NO BOSS'); Cappuccino Assassino tags each letter with a hidden unique ID, and whichever order the two edits arrive in, both docs snap to the identical text with a green checkmark. Act 2: back to the fifty-cursor doc, every monkey typing, nothing lost, Kai Cenat nodding. Payoff card at 0:39: one doc, fifty cursors, 'NOTHING GETS EATEN', no tease chip.

  

**EFFECTS (timed)**

  

**0:06**  Splat + clash flash on the overwrite, bruh on 'eaten'; error glitch as the docs drift; wrong buzzer + an IShowSpeed scream voice meme on the GG stamp. 0:01 fast keyboard clatter under the fifty monkeys, sheesh on 'lowkey genius'.

  

**0:16**  Click per slot-number shift; the "6 7" snippet on 'six seven'; referee whistle on 'FIXED'.

  

**0:24**  Snap-merge pop ×2 as both docs go identical; sparkle on the checkmark; a 'let him cook' voice meme on 'let them cook'; vine boom on 'still makes sense'.

  

**ALT HOOKS (A/B):** *1) "Fifty people in one doc and nobody's letters get eaten."   2) "OT vs CRDT, explained for the brainrotted."*

  

**LEARN MORE:** [crdt.tech](https://crdt.tech/)

  

**VISUAL REF:** Martin Kleppmann's talk "CRDTs: The Hard Parts" (YouTube) has the clearest animations of concurrent edits merging. The classic ot.js live demo (operational-transformation.github.io) lets you drag messages between two editors and watch transforms happen — great to screen-record if it loads for you. Brainrot cast + sourcing plan: BRAINROT_STYLE.md in the editing repo.
