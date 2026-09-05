# Writing rules — how the scripts must NOT sound (de-AI pass, 2026-08-28)

Gordon's feedback on the EP27-29 rewrites: "figure out how to not sound like an AI, you're
using a lot of the language patterns that an LLM usually produces." Applied to every episode
in the script doc (EP 20-48). Apply to ANY script or on-screen text written for this series.
Sources: Wikipedia:Signs_of_AI_writing; blakestockton.com "Don't write like AI: It's not X, it's Y";
futurism.com on ChatGPT tics; the OpenAI community thread on avoiding its structures.

You are rewriting SPOKEN LINES so they read like a person wrote them, not a language model.
The content, facts, numbers, order of ideas, beat timings and length stay the same. The
tone stays what it is: a plain, friendly, second-person explainer. Do NOT make it slangy,
jokey or "brainrot" — that is only for EP 27-29, which you are not touching.

## What you may change
Only the text of these paragraph types:
- the beat lines: `**0:00**  **HOOK —** ...`, `**PROBLEM —**`, `**BUILD —**`, `**NEW COMPONENT —**`,
  `**AI ANGLE —**`, `**PAYOFF + NEXT —**` (rewrite the sentence text AFTER the label; keep the
  label, its timestamp and its em dash EXACTLY as-is — that dash is structural)
- the `***ON-SCREEN:*** *"..."*` quotes
- the `**ALT HOOKS (A/B):**` two alternates

## What you must keep byte-for-byte
The `# **EP NN — title**` heading, the italic meta line, blank paragraphs (`  `), the
OVERLAYS / B-ROLL section, the EFFECTS section, LEARN MORE (including its markdown link),
VISUAL REF. Preserve the exact markdown markers and paragraph structure of the input.

## The tells to remove (all of them, every occurrence)
1. **Negation-reframe**: "it's not X, it's Y" / "isn't just X, it's Y" / "not only X but Y" /
   "the problem isn't X, it's Y" / "X — not Y". Say the true thing directly.
2. **Em dashes inside sentences.** Replace with a comma, a period, or a rewrite. (Label
   dashes and heading dashes stay.) Zero em dashes may remain in narration/on-screen/alt-hook text.
3. **Rule of three / tricolons**: three parallel items or three parallel fragments. Cut to
   two, or write a normal sentence. (Genuinely necessary technical lists of three are OK
   once per episode, written as a plain sentence, not a rhythmic beat.)
4. **Staccato fragment chains** for drama ("On purpose. Every day. In production."). Allow at
   most one two-fragment punch per episode where the original hook needs it.
5. **Rhetorical question answered by the speaker** as a device ("Who does the reading? The
   machines."). Allow at most one per episode, and only if it's the hook's actual premise.
6. **Aphorism payoffs**: tidy, symmetrical, poster-shaped closers ("Break it on your schedule,
   not the universe's"). The PAYOFF should sound like a person summing up, not a slogan.
   The ON-SCREEN line may stay short and punchy but must not be a negation-reframe or a
   symmetrical antithesis.
7. **Stock LLM phrasing**: "the magic is", "here's the thing", "here's the trick", "the beauty
   of", "genuinely", "quietly", "elegant", "seamless(ly)", "unlock", "leverage", "crucially",
   "in short", "simply put", "at its core", "the key insight", "it turns out", "think of it
   as" (max one per episode), "in other words", "essentially", "ultimately", "robust",
   "powerful", "supercharge", "game-changer", "landscape", "delve", "dive into".
8. **Uniform pacing**: every sentence the same length. Mix a long plain sentence with a
   short one. Let a sentence be slightly untidy. Use "and" to join clauses sometimes.
9. **Over-signposting**: "First... Then... Finally..." as rhythm. Fine to sequence, don't drum.

## What good looks like
Before: "That's chaos engineering: run controlled experiments on failure. State a hypothesis
— 'if this server dies, users notice nothing' — limit the blast radius, kill it, measure. If
the system flinches, you found a real weakness on your schedule, not the universe's."
After: "That practice is called chaos engineering. You write down what you expect, something
like 'if this server dies, users won't notice.' You keep the test small so a surprise can't
take everything down, then you kill the server and watch what happens. If something flinches,
you've found a real weakness, and you found it during a workday instead of during an outage."

## Output
Write the full episode block back with the same structure. Nothing else in the file.
Before finishing, grep your own output: zero "—" outside `**HOOK —**`-style labels and the
`# **EP NN — ...**` heading; zero "not just"/"isn't just"/"not only"; no three-item
rhythmic lists in the beat lines.
