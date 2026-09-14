# **EP 21 — How a site checks your leaked password without seeing it (BRAINROT EDITION)**

*Security  ·  Intermediate  ·  \~50s  ·  Builds: A password-leak checker  ·  New piece: k-anonymity*

  

**0:00**  **HOOK —** A website can tell you your password got leaked, and you never send it the password. Like, at all. It never sees it. Sounds delulu. It's real, and it works, and it's kinda genius.

  

***ON-SCREEN:*** *"THEY KNOW YOUR PASSWORD LEAKED. THEY NEVER SAW IT."*

  

**0:04**  **PROBLEM —** So there's this site, Have I Been Pwned, and it has hundreds of millions of leaked passwords. But if you send yours over to check, even scrambled up, some random guy on the other end now has a thing he can crack. So you're stuck. Ts pmo fr.

  

**0:10**  **BUILD —** The sneaky move goes like this. Your phone scrambles the password into gibberish right there on the phone, that's called a hash. Then it sends only the first five letters of the gibberish. Five. That's it. Nothing else leaves your phone. Lock in, this is the good part.

  

**0:20**  **NEW COMPONENT —** The server goes 'bet' and sends back every leaked hash that starts with those five letters, like six, seven hundred of them. Then your phone checks that pile by itself. The server has zero clue which of the six seven hundred you actually wanted. You're hiding in a crowd, and that trick has a name, k-anonymity. No cap. Your browser does this exact thing when it pops up that 'your password was in a breach' warning.

  

**0:40**  **PAYOFF + NEXT —** So the secret never leaves your phone, and the only thing that travels is a crowd to hide in. W move. Next one: how your app finds out you got paid without ever asking. It just gets told.

  

***ON-SCREEN:*** *"YOUR SECRET HIDES IN A CROWD OF GIBBERISH."*

  

**OVERLAYS / B-ROLL (timed) — brainrot cast**

  

**0:01**  The REAL Chrome 'This password appeared in a data breach' popup screenshot inset in browser chrome; Trippi Troppi (confused shrimp-cat) staring at it, eyes twitching, 'HOW DID IT KNOW' chip. Turn: Kai Cenat reaction cutout leans into frame with a 'chat, is this real?' chip.

  

**0:06**  TAKEOVER, two acts: an envelope labeled 'password123' hovering over a mailbox marked BREACH CHECKER, and behind the mailbox two Skibidi cameramen with binoculars ready to fanum-tax it. Act 2: a red ✗ slams on the envelope, 'DON'T SEND IT' stamp, the envelope wobbles back and forth between the phone and the mailbox with a 'STUCK' chip while Trippi sweats.

  

**0:12**  Cappuccino Assassino (ninja cappuccino) on the phone screen scrambles 'password123' into its real 40-character SHA-1 string, cbfdac6008f9cab4083784cbd1874f76618d2a97. Turn: Tung Tung Tung Sahur bat-chops after the fifth character; only 'CBFDA' rides up the wire on a Chimpanzini Bananini, while the other 35 characters snap into a padlocked box that stays on the phone.

  

**0:22**  TAKEOVER, two acts: the server (Ballerina Cappuccina spinning at a filing cabinet) slams back a wall of hashes that all start CBFDA, counter reads '677 HASHES', LaMelo 6-7 hands bob on the count. Act 2: split screen, LEFT the phone doing a Where's-Waldo scan down the wall until one row lights up 'PWNED' with a green scan line; RIGHT the server side where Trippi Troppi shrugs with a '?' over all 677 rows, 'K-ANONYMITY' chip. Payoff card at 0:41: the phone with a padlock, the crowd of hashes around it, 'HIDE IN THE CROWD', no tease chip.

  

**EFFECTS (timed)**

  

**0:06**  Riser + tug-of-war wobble on the envelope; wrong buzzer on the red ✗; an 'erm what the sigma' voice meme as the cameramen raise binoculars; bruh on 'stuck'.

  

**0:12**  Ninja shwing on the scramble; tung-tung-tung knock on the chop; whoosh as the five characters leave; padlock click on the rest; sheesh on 'nothing else leaves'.

  

**0:24**  Bass drop as the wall of hashes lands; the "6 7" snippet on '677'; ticking pops during the Where's-Waldo scan, sparkle + ding on the match; a 'huh' pop on the server-side shrug; vine boom on 'hide in the crowd'.

  

**ALT HOOKS (A/B):** *1) "Five letters of gibberish check hundreds of millions of passwords. Sheesh."   2) "How Chrome knows your password leaked without ever seeing it. No cap."*

  

**LEARN MORE:** [Cloudflare: Validating Leaked Passwords with k-Anonymity](https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/)

  

**VISUAL REF:** The Cloudflare post above contains the canonical hash-prefix/range-query diagrams to redraw. For a live demo, screen-record haveibeenpwned.com/Passwords with dev tools open — you can literally show only the 5-char prefix leaving the browser. Brainrot cast + sourcing plan: BRAINROT_STYLE.md in the editing repo.
