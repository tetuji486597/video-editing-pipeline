# TikTok SFX set (`tt_*`) — what each one is and when to use it

Sourced from myinstants.com (TikTok soundboard) for the EP14-19 batch, after the note that
the previous selection was too limited. Same licensing caveat as the rest of `sfx_shared/`:
**myinstants licensing is unclear and these files are deliberately not committed** — re-download
if rebuilding. See STYLE.md.

One deliberate exclusion:

- **`suspense_riser`** — downloaded, then dropped. Its energy peaks **5.7s** into the file,
  so landing it on a beat means starting it 5.7s earlier, which on these 4-9s beats means
  starting it inside the *previous* beat. No runway.

## The set

| file | dur | impact | what it is | use it when |
|---|---|---|---|---|
| `tt_vine_boom` | 1.25s | 0.10 | **The** TikTok emphasis hit — a deep bass boom from a 2012 Bluezone sample pack, now universal shorthand for "wait, hold up" | a dramatic reveal or a big number landing. The single most valuable sound here — and the easiest to overuse. Max ~2 per episode |
| `tt_metal_pipe` | 3.17s | 0.00 | The falling-pipe clang meme | something structurally FAILS — a system collapsing, a bottleneck seizing |
| `tt_record_scratch` | 0.65s | 0.05 | Abrupt turntable stop | the "actually, that's wrong" turn — pivoting from a naive approach to why it breaks |
| `tt_wrong_buzzer` | 1.06s | 0.05 | Game-show incorrect buzzer | rejected / blocked / collision / denied |
| `tt_error_glitch` | 1.33s | 0.05 | Digital glitch stutter | a corrupted or degraded state, distinct from a hard rejection |
| `tt_notif_trim` | 2.20s | 0.05 | iPhone notification tone (trimmed) | a notification literally arrives on screen |
| `tt_cash_register` | 1.04s | 0.30 | Ka-ching | money, a payment, a transaction |
| `tt_keyboard_trim` | 1.40s | 0.55 | Mechanical typing burst (trimmed from a 10s loop) | text typing itself on screen — a terminal, a URL bar |
| `tt_camera_shutter` | 0.46s | 0.00 | DSLR shutter | a shutter-flash phase boundary inside an overlay (EP4's transition technique) |
| `tt_whoosh` | 2.16s | 0.70 | Long airy transition | a heavier scene/format change |
| `tt_swoosh` | 0.45s | 0.05 | Short swipe | something travels across frame — a packet, a request, a sweep |
| `tt_bubble_pop` | 0.10s | 0.00 | Tiny pop | a single small element appears. Very short; good for ticks |
| `tt_click_trim` | 0.50s | 0.00 | Mouse click (silence stripped) | a UI press, a toggle, a counter increment |
| `tt_sparkle_trim` | 1.60s | 0.10 | Shimmer (trimmed from 6s) | a success/resolve — something arrives correct |
| `tt_correct_ding` | 2.95s | 0.15 | Game-show correct ding | an answer resolves; brighter and more "answer!" than sparkle |
| `tt_bass_drop` | 3.46s | 0.00 | Bass drop | a scale reveal — the moment a number gets very large |

`build_sfx.py` anchors every cue on **when the sound lands**, not on file start, and it
already compensates for each file's measured impact offset (that is why `tt_cash_register`
at 0.30 and `tt_keyboard_trim` at 0.55 can be cued at the exact frame they should be heard).

## Voice memes — one per episode, on the line the meme actually says

I initially left these out (spoken SFX collide with narration and date fast) and was
overruled — correctly, as it turned out, because at least one is a better fit than the
non-verbal hit it replaced. Rules that keep them working:

- **One per episode, maximum.** They are the loudest editorial gesture available.
- **Place them where the meme's words match the narration**, not just where a hit belongs.
  EP19's is the model: the line is "nobody cares if it briefly says a million instead of a
  million three", so `we_do_not_care` lands *on the words*.
- **Trim hard.** Several of these download as 12-18s full clips, and two (`hold_up`,
  `we_do_not_care`) peak a full second in, which would start them inside the previous beat.
  Cut so the phrase begins immediately.
- **Volume gets a x1.25 bump** over the formula: speech competing with speech needs more
  level than a transient to stay legible.

| meme | dur | use it when | placed |
|---|---|---|---|
| `tt_bruh` | 0.79s | something dumb just broke | EP14, the duplicate row flags red |
| `tt_oh_no_no_no` | 2.60s | a slow-motion disaster starting | EP15, the password handed to every app |
| `tt_sheesh` | 1.90s | an impressively large number | EP16, six chars cover fifty billion links |
| `tt_emotional_damage` | 1.60s | a brutal rejection | EP17, the BLOCKED stamp |
| `tt_hold_up` | 0.84s | wait-what, the turn | EP18, your computer doesn't know where google.com lives |

> **`tt_hold_up` was SANITIZED 2026-08-28 (EP20-26 batch).** The original download decoded
> to **+14.3 dBFS float peak / +1.8 dB mean RMS** — samples 5x over full scale — and its
> square-wave content made the native AAC encoder overshoot ~3.5 dB *past any limiter
> ceiling*, which is how EP21-B first shipped a +1.4 dB clipped peak from a mix whose
> pre-encode WAV measured a clean -2.0 dBTP. The file now sits at ~-18 dB mean / -5.5 dB
> peak (gain -19.8 dB), in line with the rest of the set; the original is kept as
> `tt_hold_up.orig.bak`. If you re-download any myinstants meme, CHECK ITS FLOAT PEAK
> (`ffmpeg -i f.mp3 -af astats -f null -`) before cueing it — a decoded peak above ~+1 dB
> means the source is broken-hot and will fight every limiter downstream. Related trap
> found the same session: ffmpeg's `alimiter` defaults to `level=true`, which silently
> re-normalizes its OUTPUT back toward full scale — always pass `level=false` when using
> it as a ceiling.
| `tt_we_do_not_care` | 1.46s | genuine indifference | EP19, "nobody cares…" |

Not included: `hawk tuah` and similar crude clips — recognisable, but not for a channel
teaching system design. Say so if you want them.

## Volume calibration — do not hand-pick these

The set spans **-2.8 dB mean (`tt_bass_drop`) to -34.5 dB (`tt_keyboard_trim`)** — a 32 dB
spread. A flat per-cue volume therefore does NOT give flat presence: the first pass used
0.34-0.48 across the board and a difference-energy check found `tt_sparkle_trim` sitting at
1.1x the mix baseline, i.e. inaudible, while the bass hits dominated.

Volumes are now derived from each file's measured mean level, partially normalised
(k=0.6) toward a -18 dB target, clamped to [0.15, 0.95]:

| sound | mean dB | vol | | sound | mean dB | vol |
|---|---|---|---|---|---|---|
| `tt_keyboard_trim` | -34.5 | 0.95 | | `tt_swoosh` | -20.6 | 0.50 |
| `tt_click_trim` | -32.1 | 0.95 | | `tt_metal_pipe` | -18.9 | 0.42* |
| `tt_cash_register` | -29.1 | 0.90 | | `tt_bubble_pop` | -18.9 | 0.45 |
| `tt_correct_ding` | -26.4 | 0.75 | | `tt_sparkle_trim` | -18.3 | 0.72* |
| `tt_notif_trim` | -24.4 | 0.65 | | `tt_wrong_buzzer` | -12.8 | 0.29 |
| `tt_camera_shutter` | -22.6 | 0.58 | | `tt_vine_boom` | -8.5 | 0.30* |
| `tt_error_glitch` | -21.6 | 0.54 | | `tt_bass_drop` | -2.8 | 0.22* |
| `tt_record_scratch` | -21.0 | 0.52 | | `tt_whoosh` | -20.6 | 0.50 |

\* manual override. `sparkle_trim` is boosted past its computed value because it is a soft
broadband shimmer that narration masks; `vine_boom` and `bass_drop` are pulled down because
bass-heavy hits read far louder against a -14 LUFS voice than their mean suggests.

Correction is partial, not full — full normalisation would flatten the set into sameness,
and a vine boom should hit harder than a bubble pop.

## Leading silence — every file here was trimmed

`build_sfx.py` **refuses** any file with more than 20ms of leading silence (it is the guard
added after EP13 shipped a cue 1.25s late). Every `tt_*` file in this directory was passed
through `silenceremove` so its first audible sample is at t=0. **If you add a sound to this
set, trim it the same way or the build will refuse it.** That is separate from, and in
addition to, `impact_offset`, which handles sounds whose peak arrives later than their onset.

## Mixing notes

- Volumes here run **0.30-0.55**. `tt_vine_boom`, `tt_metal_pipe` and `tt_bass_drop` are
  bass-heavy and read much louder than their peak suggests against a -14 LUFS narration —
  keep them at or below 0.45.
- The final mix uses `loudnorm=I=-14:TP=-2:LRA=11`, not `alimiter`, per STYLE.md — a
  sample-peak limiter cannot account for AAC encode overshoot.
- Do not stack two bass hits within ~1s; they sum and the limiter pumps.
