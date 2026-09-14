# **EP 30 — How apps test on you without telling you (you're the NPC) (BRAINROT EDITION)**

*DevOps / Product  ·  Beginner  ·  \~45s  ·  Builds: Controlled rollouts & experiments  ·  New piece: Feature flags + A/B testing*

  

**0:00**  **HOOK —** Right now, you and your friend are running two different versions of the same app. Same icon, different app. Neither of you can tell. You're the NPC, sorry.

  

***ON-SCREEN:*** *"HALF OF YOU ARE SEEING A DIFFERENT APP RIGHT NOW."*

  

**0:03**  **PROBLEM —** Shipping a new feature to a hundred percent of people at once is scary. If it's broken, or everybody hates it, everybody gets hit at the exact same time, and undoing it is a whole crash out.

  

**0:08**  **BUILD —** So the new code gets wrapped in a light switch you can flip without shipping anything again. That switch is called a feature flag. The code goes out 'dark', meaning it's inside the app but the switch is off. Sleeper agent.

  

**0:20**  **NEW COMPONENT —** Then you flip it on for one percent of people and watch the numbers. Numbers good, turn it up. Something breaks, kill it instantly and the other ninety nine percent never saw it. Show version A to half the people and version B to the other half, compare, and that's an A/B test. Like, version B got sixty seven percent more taps. Six seven. Big decisions get made off actual numbers, zero vibes.

  

**0:38**  **AI ANGLE —** New AI models get dropped the exact same way. Flag on for a tiny slice of people, A/B test it, then everybody gets it. You might have the new one right now. Delulu or real, you'll never know.

  

**0:48**  **PAYOFF + NEXT —** Ship it dark, and let one percent of people decide if the rest of you get it. Next one: what happens when a database gets too fat for one machine.

  

***ON-SCREEN:*** *"'SHIPPED' AND 'TURNED ON' ARE TWO DIFFERENT BUTTONS."*

  

**OVERLAYS / B-ROLL (timed) — brainrot cast**

  

**0:01**  Two phones side by side, same app icon; LEFT Trippi Troppi's phone with a blue button, RIGHT Trippi Troppi's twin with a green one, both squinting at each other. Turn: an 'NPC' tag drops on both heads while a Livvy Dunne cutout scrolls past unbothered with a 'main character' chip.

  

**0:05**  TAKEOVER, two acts: a '100%' rollout bar filling in one shot; Bombardiro Crocodilo carpet-bombs the new feature onto a stadium of Trippi Troppis all at once. Act 2: every screen goes red at the same instant, a stadium-wide crash out, Skibidi cameramen filming the wreckage; an 'UNDO' button visibly sweating.

  

**0:16**  A physical light switch labeled FEATURE FLAG, Tung Tung Tung Sahur guarding it with the bat resting; the new code as a Chimpanzini Bananini asleep in a hoodie inside the app, 'DARK' chip, switch OFF. Turn: Sahur flips it, the monkey wakes up, and a 'REDEPLOY' truck drives off with a red X because nobody needed it.

  

**0:24**  Audience bar: 1% lit, Kai Cenat watching a metrics graph, ramp 1% → 10% → 50% as the line climbs; a red spike → Sahur slams the switch OFF, 'KILLED'. Act 2: the bar wipes into A | B halves, Ballerina Cappuccina spinning between them balancing two cups; a REAL screenshot of an A/B results panel (LaunchDarkly or Optimizely style) inset, 'B +67%' with LaMelo 6-7 hands. 0:39 AI-angle band: two model chips 'v1' / 'v2' behind the same flag. Payoff card at 0:49: a dark switch next to a shipped box, 'TWO DIFFERENT BUTTONS', no tease chip.

  

**EFFECTS (timed)**

  

**0:05**  Red error-cascade glitch across every screen; bass drop on the stadium crash out; an IShowSpeed scream voice meme; bruh on 'whole crash out'.

  

**0:16**  Physical toggle-switch clunk + click; tung-tung-tung knock as Sahur guards it; a snore loop on the sleeping monkey, then sheesh when it wakes.

  

**0:24**  Pops as the bar ramps; wrong buzzer + record scratch on the KILL; wipe whoosh on the A/B split; the "6 7" snippet on 'B +67%'; ding on the AI-angle chips; vine boom on 'two different buttons'.

  

**ALT HOOKS (A/B):** *1) "Why you and your friend have two different apps and neither of you knows."   2) "They're running A/B tests on you right now. You're the NPC."*

  

**LEARN MORE:** [Martin Fowler: Feature Toggles](https://martinfowler.com/articles/feature-toggles.html)
