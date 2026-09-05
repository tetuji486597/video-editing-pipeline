<!-- v2: dumbed down to five-year-old register + de-AI'd (no 'not X, it's Y', no em dashes in narration, no rules of three). Source of truth is the Google Doc; this is the repo mirror. -->

# **EP 27 — Netflix has a robot that breaks Netflix (BRAINROT EDITION)**

*DevOps / Reliability  ·  Intermediate  ·  ~40s  ·  Builds: A failure-proofing practice  ·  New piece: Chaos engineering*

**0:00**  **HOOK —** Okay so Netflix has a robot, and the robot's whole job is to break Netflix. Like, their own servers. On purpose. Six seven. It's real, look it up.

***ON-SCREEN:*** *"NETFLIX HAS A ROBOT THAT BREAKS NETFLIX. ON PURPOSE."*

**0:05**  **PROBLEM —** Every company goes "oh our stuff never goes down," and then it goes down at 3am and some poor guy gets woken up and everybody's mad. Cap. Negative aura.

**0:11**  **BUILD —** So Netflix went, fine, we'll break it ourselves first. The robot's called Chaos Monkey and it just unplugs a server in the middle of the day while everyone's sitting right there watching. Let him cook.

**0:19**  **NEW COMPONENT —** The fancy name for this is chaos engineering. You go "ok if I kill this one box nobody should notice," and then you kill the box and you watch. If nothing happened, cool. If something did break, also cool honestly, because you found it at lunch instead of at 3am. And then you get braver and start killing way more boxes at once, like a whole city of boxes.

**0:34**  **PAYOFF + NEXT —** Break your own stuff in the day so it can't break you at night. Next one's about why ChatGPT types so slow.

***ON-SCREEN:*** *"BREAK IT YOURSELF FIRST."*

**OVERLAYS / B-ROLL (timed) — brainrot cast**

**0:01**  Chimpanzini Bananini (banana-monkey) in a Netflix-red bandana, wrench in hand, sneaking up on a server rack under a neon 'PRODUCTION' sign; the REAL Chaos Monkey logo inset on the rack. Turn: he yanks a cable, one server dies, a LaMelo "6 7" hand-bob cutout pops in the corner on 'six seven'.

**0:06**  TAKEOVER, two acts: a smug 'NEVER GOES DOWN' slide with a Skibidi Toilet presenter → hard cut to 3:00 AM where Tung Tung Tung Sahur IS the pager, knocking on the bedroom door ('PROD DOWN'); an AURA counter plummets to -10,000 while Skibidi cameramen (the customers) film the outage.

**0:12**  Chimpanzini unplugs ONE server (red X); the dashboard beside it stays GREEN; Kai Cenat reaction cutout sipping coffee, totally calm; wall clock reads 2:00 PM. Lands on 'middle of the day'.

**0:21**  TAKEOVER: a Roblox-style QUEST LOG — GUESS ✓ → KILL ONE BOX ✓ → WATCH ✓ (a graph line flinches, red blip, 'FOUND ONE' stamp with an SVG moai). Act 2: the box count grows and Bombardiro Crocodilo carpet-bombs a whole map CITY of boxes, dashboard still green. Payoff card at 0:35: day/night split, 'LET THE MONKEY COOK', no tease chip.

**EFFECTS (timed)**

**0:01**  Monkey screech + zap; vine boom on 'break Netflix'; the "6 7" audio snippet on 'six seven'.

**0:06**  Bruh on 'cap'; tung-tung-tung knock ×3 on the 3am pager; error glitch + bass drop as the aura counter falls. 0:12 record-scratch on the chaos-vs-calm cut; sparkle on the green dashboard.

**0:21**  A different sound per quest checkbox (click / pop_bubble / bubble_pop / ding); wrong buzzer on the flinch; sheesh on 'FOUND ONE'; bass_hit on the city bomb; vine boom on 'let the monkey cook'.

**ALT HOOKS (A/B):** 1) "Netflix breaks Netflix every single day. On purpose."   2) "The monkey that unplugs Netflix servers for a living."

**LEARN MORE:** Netflix Chaos Monkey (official docs)

**VISUAL REF:** The official Chaos Monkey logo/art on the docs site is instantly recognizable and worth showing on screen. Netflix's Tech Blog posts on the Simian Army have the original diagrams. Brainrot cast + sourcing plan: BRAINROT_STYLE.md in the editing repo.
