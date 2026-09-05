<!-- v2: dumbed down to five-year-old register + de-AI'd (no 'not X, it's Y', no em dashes in narration, no rules of three). Source of truth is the Google Doc; this is the repo mirror. -->

# **EP 28 — Why ChatGPT types so slow (BRAINROT EDITION)**

*Web & Networking / AI  ·  Beginner  ·  ~38s  ·  Builds: A streaming AI response  ·  New piece: Server-Sent Events (streaming)*

**0:00**  **HOOK —** You know how ChatGPT types one word at a time? You think that's for looks. Nope. It literally doesn't know the end of the sentence yet. Bro is making it up as he goes.

***ON-SCREEN:*** *"THE TYPING IS REAL. IT DOESN'T KNOW THE ENDING YET."*

**0:05**  **PROBLEM —** The AI makes one word at a time, and a long answer takes like twenty seconds to finish. If you had to look at a blank screen for twenty seconds you would close the tab. I would close the tab. Sybau.

**0:11**  **BUILD —** So instead of waiting for the whole answer, the server just sends each word to your phone the second it pops out. There's one pipe, it stays open, and words keep falling down it.

**0:18**  **NEW COMPONENT —** That pipe is called Server-Sent Events, SSE, and the thing about it is it only goes one direction, from the server down to you. The chat app episode had a pipe that went both ways, because you talk back in a chat. Here you're just listening, so one way is fine. And the sneaky part is the first word shows up in like half a second, so your brain goes "oh that was fast," even though the whole thing still took twenty. Aura farming, basically.

**0:31**  **PAYOFF + NEXT —** Give people the first word right away instead of making them wait for the last one. Next one: a billion posts a day, and who's actually reading them. Nobody. No human, anyway.

***ON-SCREEN:*** *"SHOW THE FIRST WORD RIGHT AWAY."*

**OVERLAYS / B-ROLL (timed) — brainrot cast**

**0:01**  ChatGPT-style UI typing itself out, except the answer is brainrot ('chat, is this real? 6 7 …'), cursor blinking; Tralalero Tralala (Nike shark) sprinting alongside the cursor. Turn: the cursor pauses mid-word with an 'idk yet' thought bubble, then keeps going.

**0:06**  TAKEOVER: blank screen + spinner, Trippi Troppi (confused shrimp-cat) staring, a stopwatch crawling 0:00 → 0:20. Turn: eyes go dead, 'sybau' chip; the tab's X gets smashed and the browser window flies off-frame — '-1000 AURA'.

**0:12**  Word conveyor: a Chimpanzini Bananini army, each carrying one word chip [The] [answer] [is]…, sprinting down a ONE-WAY pipe from the MODEL to a phone screen; each word appears the instant its monkey arrives; the pipe glows 'OPEN' and never closes.

**0:19**  TAKEOVER: side-by-side — LEFT 'SSE' one-way ↓ pipe; RIGHT the 'chat socket' two-way ⇅ with a Skibidi Toilet and a Cameraman yapping at each other. Turn: right side dims, 'ONE WAY ONLY' slams left. Act 2: a REAL browser DevTools capture of an event-stream response (chunks arriving one by one) inset in chrome; stopwatch split 'FIRST WORD 0.5s' vs 'WHOLE THING 20s' with LaMelo doing 6-7 hands. Payoff at 0:32: the cursor with the first word already on screen, rest ghosted — no tease chip.

**EFFECTS (timed)**

**0:01**  Soft keyboard-typing loop; bruh on 'nope'; sheesh on 'making it up as he goes'.

**0:06**  Riser under the spinner; wrong buzzer + error glitch on the tab close; the "6 7" snippet on '-1000 aura'. 0:12 swoosh_elec per word launch (varied with pops), sparkle when the first word lands.

**0:19**  Shutter on the split; whoosh on the 'ONE WAY ONLY' slam; ding on '0.5s', bass drop on '20s'; click on the payoff cursor blink; vine boom on 'the first word'.

**ALT HOOKS (A/B):** 1) "ChatGPT types slow because it's making it up as it goes."   2) "Why the first word matters more than the last one."

**LEARN MORE:** MDN: Server-Sent Events

**VISUAL REF:** Open any AI chat with browser dev tools → Network tab → click the streaming request → watch the event-stream chunks arrive one by one in real time. Screen-record that: it's the actual words hitting the wire, and it's mesmerizing.
