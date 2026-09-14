# **EP 20 — Why AI can't spell 'strawberry' (BRAINROT EDITION)**

*AI & ML  ·  Beginner  ·  \~45s  ·  Builds: How an LLM reads text  ·  New piece: Tokenization*

  

**0:00**  **HOOK —** Okay so for years you could ask ChatGPT how many R's are in strawberry and bro got it wrong. Three R's. It said two. And the reason is insane. The AI has never seen the word. Like, ever. Chat, is this real?

  

***ON-SCREEN:*** *"AI COULDN'T COUNT THE R'S IN STRAWBERRY. IT HAS NEVER SEEN THE WORD."*

  

**0:04**  **PROBLEM —** See, the model can't eat raw text. Letter by letter is way too slow. Snail behavior. And whole words means a dictionary with like six, seven million words in it, and the second you typo one, that's a brand new word it has never met. Cooked either way.

  

**0:10**  **BUILD —** So there's a chopper that slices your text into little chunks first. That's called a tokenizer, and the chunks are tokens. A normal word like 'love' stays in one piece. A weird word like 'strawberries' gets chopped, 'straw' plus 'berries'. Banana-sized pieces.

  

**0:20**  **NEW COMPONENT —** And the cursed part is the model never even gets the letters. It just gets a list of numbers, one per chunk. So asking it to spell is like asking you to spell a word you've only ever heard out loud. Skill issue, but honestly not its fault. It's also why AI companies bill you in tokens, and why the 'context window' is counted in tokens. Chunks are the only thing the model reads. No cap.

  

**0:36**  **PAYOFF + NEXT —** So the AI reads a pile of chunk numbers and your spelling never even shows up. Next one: how a website knows your password leaked without ever seeing it. Sounds fake, it's real tho.

  

***ON-SCREEN:*** *"THE MODEL ONLY EVER SEES THE NUMBERS."*

  

**OVERLAYS / B-ROLL (timed) — brainrot cast**

  

**0:01**  Chat mockup: "how many R's in strawberry?" and the AI (Trippi Troppi, the confused shrimp-cat, wearing a blindfold) answers "2" with full confidence, red ✗; the REAL viral ChatGPT strawberry-fail screenshot inset in a phone frame. Turn: IShowSpeed screaming cutout slams in on the wrong answer, 'CHAT IS THIS REAL' chip.

  

**0:06**  TAKEOVER, two acts: LEFT Lirilì Larilà (clock elephant) crawling one letter at a time, S… T… R…, clock hands spinning forever; RIGHT Brr Brr Patapim buried under a tipping bookshelf labeled '6,700,000 WORDS', a typo'd 'strawbery' card poking out stamped 'NEVER MET THIS ONE', LaMelo 6-7 hands bobbing on the shelf count. Turn: both sides get a red ✗ and a 'COOKED' stamp.

  

**0:12**  Tung Tung Tung Sahur as the tokenizer, bat-chopping the sentence 'I love strawberries' into blocks \[I\] \[ love\] \[ straw\] \[berries\]; each block lands on the back of a Chimpanzini Bananini who carries it off in a line. Turn: the REAL OpenAI Tokenizer page screenshot with the colored chunk highlighting inset, 'THIS IS THE ACTUAL TOOL' chip.

  

**0:22**  TAKEOVER, two acts: the four blocks flip over to their ID numbers 40, 3021, 15717, 20853; the 15717 card gets LaMelo 6-7 hands because it's got two sevens in it; the Chimpanzini line carries only the numbers into a MODEL box where Cappuccino Assassino sits with the letters locked in a safe behind him. Act 2: Kai Cenat with headphones on, hearing a word, trying to spell it, a '???' bubble; then a pricing meter '$ PER 1M TOKENS' ticking up and a 'CONTEXT WINDOW: 128K TOKENS' bar filling. Payoff card at 0:37: the four number cards with the letters ghosted out behind them, 'IT ONLY SEES THE NUMBERS', no tease chip.

  

**EFFECTS (timed)**

  

**0:01**  Freeze-frame + record scratch on the wrong '2'; IShowSpeed scream voice meme on the red ✗; bruh on 'never seen the word'. 0:06 slow clock tick on the snail side, the "6 7" snippet on 'six, seven million', error glitch on the bookshelf tip, wrong buzzer on 'COOKED'.

  

**0:12**  Tung-tung-tung knock per chop (varied with click / pop_bubble); sheesh when 'straw' + 'berries' land; monkey screech as the Chimpanzini line runs off.

  

**0:22**  Card-flip whoosh per block; the "6 7" snippet again on 15717; safe-door clunk on the locked letters; a confused 'huh' pop on Kai's '???'; ding per price tick; sparkle on the context bar; vine boom on 'only sees the numbers'.

  

**ALT HOOKS (A/B):** *1) "Why the AI can write your whole essay but can't spell strawberry."   2) "The thing AI companies actually charge you for. It's chunks. Six seven."*

  

**LEARN MORE:** [OpenAI Tokenizer (interactive)](https://platform.openai.com/tokenizer)

  

**VISUAL REF:** The tokenizer itself IS the b-roll — type 'strawberry' and screen-record the colored chunk highlighting. Andrej Karpathy's "Let's build the GPT Tokenizer" (YouTube) has clean walkthrough visuals too. Brainrot cast + sourcing plan: BRAINROT_STYLE.md in the editing repo.
