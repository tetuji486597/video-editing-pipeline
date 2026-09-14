# **EP 31 — How databases hold a billion rows (BRAINROT EDITION)**

*Databases & Data  ·  Intermediate  ·  \~50s  ·  Builds: A user database at scale  ·  New piece: Sharding / partitioning*

  

**0:00**  **HOOK —** No single database server can hold all of Facebook. Like, it physically does not fit. So they chopped Facebook into pieces. Lock in.

  

***ON-SCREEN:*** *"ONE DATABASE CAN'T HOLD FACEBOOK. SO THEY CHOPPED IT UP."*

  

**0:03**  **PROBLEM —** You can make the one box bigger. More RAM, bigger CPU, same box. That's called vertical scaling. But there's a hard ceiling, and past a point the price goes full Ohio. One box costing more than a house. Cooked.

  

**0:08**  **BUILD —** So instead you go sideways and split the data across a bunch of normal boxes, and each box holds a slice. That's called sharding, and every slice is a shard.

  

**0:20**  **NEW COMPONENT —** Something has to decide which box you live on, and that's the shard key. Say it's your user ID. Super simplified, everybody A to M goes on shard one, N to Z on shard two. At Facebook size there are way more, so your ID gets crunched and boom, you live on shard sixty seven. Six seven. Each shard handles reads and writes for its own slice, so when you need more room you add more boxes. The annoying parts are picking a key that spreads people out evenly so one shard doesn't get fanum taxed with all the traffic, and questions that need stuff from a bunch of shards at once. Brr Brr Patapim moment.

  

**0:38**  **PAYOFF + NEXT —** When you can't make the box any bigger, you get more boxes. Next one: what happens when one of those boxes literally catches on fire.

  

***ON-SCREEN:*** *"CHOP THE DATA. ADD MORE BOXES."*

  

**OVERLAYS / B-ROLL (timed) — brainrot cast**

  

**0:01**  One database cylinder labeled 'ALL OF FACEBOOK' bulging and cracking, Trippi Troppi trying to hold the lid down; the REAL Facebook 'f' logo on the lid, rows spilling out the seams. Turn: a 'LOCK IN' chip and a Kai Cenat stare cutout as the crack spreads.

  

**0:06**  TAKEOVER, two acts: the vertical-scale ladder, the box gets a bigger CPU, then more RAM, growing taller each step with a price-tag counter spinning up beside it. Act 2: the box smacks into a '$$$ / CEILING' wall, the tag reads more than a house, 'OHIO' stamp, Lirilì Larilà sighing in sandals.

  

**0:16**  Clean split: the cylinder shatters into slices that fly out onto a row of normal boxes; Bombardiro Crocodilo drops one slice per box; A–M / N–Z labels on the first two; Tung Tung Tung Sahur at the front as the shard-key router, reading each user's ID and knocking it toward its box. Turn: one ID gets crunched and routed to a box labeled '67', LaMelo 6-7 hands.

  

**0:24**  Each shard serving its own slice, tiny read/write arrows per box, a new box sliding in on the end ('MORE ROOM'). Act 2: a bad key sends every user to one box and it gets fanum taxed, buried under cards; then a cross-shard question as Brr Brr Patapim with vines tangled across four boxes, 'THE ANNOYING PART'. Payoff card at 0:39: a wall of small boxes vs one giant box crossed out, 'MORE BOXES', no tease chip.

  

**EFFECTS (timed)**

  

**0:06**  Crack/strain creak on the bulging cylinder; cash-register ka-ching per size step; a hard ceiling thud + wrong buzzer; bruh on 'Ohio'.

  

**0:16**  Glass-shatter split into slices; bomber drone as the slices drop; tung-tung-tung knock as the router sends IDs; the "6 7" snippet on 'shard sixty seven'.

  

**0:24**  Highlight-sweep swoosh across the shards; pop as the new box slides in; a Kai Cenat 'AYO' voice meme + error glitch on the fanum-taxed box; rubber stretch + bruh on the Patapim tangle; vine boom on 'more boxes'.

  

**ALT HOOKS (A/B):** *1) "Facebook doesn't fit in one database, so they chopped it up."   2) "What a 'shard key' decides, and why it's your user ID."*

  

**LEARN MORE:** [Wikipedia: Database sharding](https://en.wikipedia.org/wiki/Shard_\(database_architecture\))

  

**VISUAL REF:** DigitalOcean's "Understanding Database Sharding" tutorial has the cleanest redraw-able diagrams of vertical vs horizontal partitioning and shard-key routing. Brainrot cast + sourcing plan: BRAINROT_STYLE.md in the editing repo.
