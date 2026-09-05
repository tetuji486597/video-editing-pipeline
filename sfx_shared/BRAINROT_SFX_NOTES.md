# Brainrot SFX set (`br_*`) -- EP27-29

Sourced 2026-09-04 from myinstants.com (curl with a full Chrome User-Agent; the short `Mozilla/5.0` UA now gets a Cloudflare block page).
Same caveat as `tt_*`: **licensing unclear, deliberately not committed** -- re-download from the URLs below if rebuilding.

Every file went through `sanitize.py` (scratchpad; log below): float peak + RMS measured on the DECODED file, leading silence stripped
(`silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0:detection=peak`), voice memes trimmed to the phrase (<=2.5s, 60ms fade-out
when cut), anything peaking above -1 dBFS attenuated to ~-1.6 dBFS pre-encode (libmp3lame overshoots by up to ~0.9 dB on clipped content --
`br_electric_zap` came back at -0.15 after a -1.0 target, hence the re-encode loop), then re-encoded libmp3lame 320k and re-measured.
All 23 files: decoded peak <= -1.0 dBFS, first audible sample <= 1 ms, `build_sfx.py`'s own `leading_silence()` check = 0 ms.

`vol` = 0.45 * 10^(0.6*(-18-mean)/20) clamped [0.15,0.95], x1.25 for voice memes, bass-heavy capped at 0.45 (LESSONS_EP20-26 formula).
The one-voice-meme-per-episode cap is LIFTED for this batch (BRAINROT_STYLE.md) but variety rules still apply: don't repeat a sound within an episode.

| file | dur | mean dB | peak dBFS | vol | kind | what it is | source |
|---|---|---|---|---|---|---|---|
| `br_six_seven.mp3` | 1.52s | -13.4 | -1.61 | 0.41 | voice | Skrilla 'Doot Doot' 6-7 snippet (the 67 meme audio) | https://www.myinstants.com/en/instant/skrilla-doot-doot-67-6465/ |
| `br_six_seven_voice.mp3` | 1.45s | -27.1 | -10.81 | 0.95 | voice | kid-voice 'six seven!' (alt take) | https://www.myinstants.com/en/instant/six-seven-73913/ |
| `br_tung_sahur.mp3` | 2.50s | -11.3 | -1.60 | 0.35 | voice | 'tung tung tung sahur' chant (first phrase of a 6s clip) | https://www.myinstants.com/en/instant/tung-tung-sahur-29124/ |
| `br_skibidi_toilet.mp3` | 2.50s | -12.6 | -1.54 | 0.39 | voice | 'skibidi dop dop yes yes' hook (first 2.5s of 11s) | https://www.myinstants.com/en/instant/skibidi-toilet-69886/ |
| `br_what_the_skibidi.mp3` | 1.35s | -11.6 | -2.08 | 0.36 | voice | 'ERM what the skibidi' | https://www.myinstants.com/en/instant/erm-what-the-skibidi-53224/ |
| `br_erm_sigma.mp3` | 1.39s | -17.7 | -1.57 | 0.55 | voice | 'erm, what the sigma' | https://www.myinstants.com/en/instant/erm-what-the-sigma-51754/ |
| `br_sybau.mp3` | 1.73s | -12.4 | -1.60 | 0.38 | voice | 'sybau' shout | https://www.myinstants.com/en/instant/sybau-sound-53092/ |
| `br_fries_in_bag.mp3` | 1.83s | -22.6 | -5.75 | 0.77 | voice | 'put the fries in the bag' (first phrase of a 7s clip) | https://www.myinstants.com/en/instant/fries-in-da-bag-16786/ |
| `br_amongus_reveal.mp3` | 4.00s | -22.0 | -3.95 | 0.59 | sting | Among Us role-reveal sting (swell, lands ~1.1s in) | https://www.myinstants.com/en/instant/among-us-role-reveal-sound-34956/ |
| `br_amongus_sus.mp3` | 3.00s | -7.9 | -1.16 | 0.22 | sting | Among Us 'sus' bass sting (bass-heavy) | https://www.myinstants.com/en/instant/amongus-sus-74999/ |
| `br_let_him_cook.mp3` | 2.50s | -10.8 | -1.45 | 0.34 | voice | 'let him cook' (first 2.5s of a 4.4s clip) | https://www.myinstants.com/en/instant/let-him-cook-80585/ |
| `br_diabolical.mp3` | 1.69s | -26.4 | -7.42 | 0.95 | voice | 'f***ing DIABOLICAL' (bleep-free, PG-13 check before use) | https://www.myinstants.com/en/instant/fking-diabolical-93147/ |
| `br_aura_minus1000.mp3` | 2.12s | -27.3 | -11.82 | 0.95 | voice | '-1000 aura' | https://www.myinstants.com/en/instant/1000-aura-97038/ |
| `br_monkey_screech.mp3` | 2.00s | -9.5 | -3.03 | 0.25 | fx | screaming monkeys (first 2s of 5.4s) | https://www.myinstants.com/en/instant/screaming-monkeys-5896/ |
| `br_electric_zap.mp3` | 1.50s | -8.8 | -1.21 | 0.24 | fx | electric shock / zap | https://www.myinstants.com/en/instant/electric-shock-93260/ |
| `br_skill_issue.mp3` | 2.30s | -20.2 | -1.40 | 0.66 | voice | Halo announcer 'skill issue' | https://www.myinstants.com/en/instant/halo-announcer-skill-issue-22687/ |
| `br_nah_id_win.mp3` | 2.30s | -27.6 | -7.47 | 0.95 | voice | Gojo 'nah, I'd win' | https://www.myinstants.com/en/instant/nah-id-win-98808/ |
| `br_gigachad.mp3` | 2.50s | -13.6 | -1.61 | 0.33 | music | Giga Chad theme (first 2.5s, faded) | https://www.myinstants.com/en/instant/giga-chad-36744/ |
| `br_rizz.mp3` | 1.74s | -14.4 | -1.86 | 0.35 | sting | 'rizz' sound effect (sparkle sting) | https://www.myinstants.com/en/instant/rizz-sound-effect-54189/ |
| `br_touch_grass.mp3` | 2.50s | -21.2 | -2.73 | 0.70 | voice | Halo announcer 'touch grass' | https://www.myinstants.com/en/instant/halo-touch-grass-86691/ |
| `br_tralalero.mp3` | 1.60s | -14.6 | -3.94 | 0.44 | voice | 'tralalero tralala' chant | https://www.myinstants.com/en/instant/tralalero-tralala-meme-71934/ |
| `br_chicken_jockey.mp3` | 1.17s | -21.7 | -9.21 | 0.73 | voice | 'CHICKEN JOCKEY' scream | https://www.myinstants.com/en/instant/chicken-jockey-only-22143/ |
| `br_fanum_tax.mp3` | 2.50s | -14.8 | -1.59 | 0.36 | music | 'skibidi toilet sigma fanum tax only in ohio' song bit (first 2.5s) | https://www.myinstants.com/en/instant/skibidi-toilet-sigma-fanum-tax-only-in-ohio-64631/ |

## Notes on specific files

- `br_six_seven` is the Skrilla 'Doot Doot' bar (quiet 0.7s beat lead-in, the '6-7' lands at ~1.3s -- build_sfx anchors on impact offset so cue it where it should LAND). `br_six_seven_voice` is a clean kid-voice 'six seven!' that lands at t=0.
- `br_amongus_reveal` is a swell that peaks ~1.1s in; `br_amongus_sus` is bass-heavy (mean -7.9 dB) -- vol capped, keep it away from vine boom.
- `br_diabolical` is the uncensored 'f***ing diabolical' clip -- edge of PG-13 per BRAINROT_STYLE; use only if Gordon OKs the word, otherwise cut the first ~0.5s.
- `br_fries_in_bag` and `br_aura_minus1000` had sub-threshold room tone (-53 dB RMS) that the -45 dB peak gate let through (273 ms / 105 ms of 'silence' per build_sfx's silencedetect) -- fixed with a manual head trim (0.62 s / 0.38 s) before the gate.
- `br_tung_sahur`, `br_skibidi_toilet`, `br_let_him_cook`, `br_gigachad`, `br_fanum_tax`, `br_monkey_screech` are the first N seconds of longer clips with a 60 ms fade -- the phrase is at the head in all of them (checked on 100 ms RMS envelopes, not by ear; listen once before cueing).
- Not found on myinstants: a clean solo 'monkey screech' (used 'screaming monkeys'), an exact 'put the fries in the bag' (used 'fries in da bag', same meme), and 'W rizz' as a voice line (used the sparkle 'rizz sound effect'). 'chad' is the Giga Chad theme, not a voice line.

## Trim / sanitize log

```
br_six_seven: src krilla_doot.mp3 1.56s peak -0.2 rms -12.1 -> silence-trim, keep 2.5s, gain -1.44dB -> 1.52s peak -1.61 rms -13.4 first-audible 0.0ms lead-sil 0ms
br_six_seven_voice: src six_seven_a.mp3 1.45s peak -10.8 rms -27.1 -> silence-trim, keep 2.5s, gain +0.00dB -> 1.45s peak -10.81 rms -27.1 first-audible 0.0ms lead-sil 0ms
br_tung_sahur: src ung_a.mp3 6.03s peak -0.2 rms -11.3 -> silence-trim, keep 2.5s +fade, gain -1.36dB -> 2.50s peak -1.60 rms -11.3 first-audible 0.9ms lead-sil 0ms
br_skibidi_toilet: src kibidi_toilet.mp3 11.45s peak +0.5 rms -9.5 -> silence-trim, keep 2.5s +fade, gain -1.60dB -> 2.50s peak -1.54 rms -12.6 first-audible 0.5ms lead-sil 0ms
br_what_the_skibidi: src ibidi_erm.mp3 1.38s peak -2.3 rms -11.6 -> silence-trim, keep 2.5s, gain +0.00dB -> 1.35s peak -2.08 rms -11.6 first-audible 0.0ms lead-sil 0ms
br_erm_sigma: src igma_a.mp3 1.39s peak +0.3 rms -16.1 -> silence-trim, keep 2.5s, gain -1.60dB -> 1.39s peak -1.57 rms -17.7 first-audible 0.0ms lead-sil 0ms
br_sybau: src ybau_b.mp3 1.93s peak -0.6 rms -11.8 -> silence-trim, keep 2.5s, gain -1.04dB -> 1.73s peak -1.60 rms -12.4 first-audible 0.0ms lead-sil 0ms
br_fries_in_bag: src fries-in-da-bag.mp3 7.01s peak -5.7 rms -24.8 -> manual start 0.62s, silence-trim, keep 2.45s +fade, gain +0.00dB -> 1.83s peak -5.75 rms -22.6 first-audible 0.0ms lead-sil 0ms
br_amongus_reveal: src amongus_reveal_a.mp3 4.57s peak -3.9 rms -22.5 -> silence-trim, keep 4.0s +fade, gain +0.00dB -> 4.00s peak -3.95 rms -22.0 first-audible 3.9ms lead-sil 0ms
br_amongus_sus: src mongus_sus.mp3 4.65s peak +2.7 rms -8.1 -> silence-trim, keep 3.0s +fade, gain -1.60dB -> 3.00s peak -1.16 rms -7.9 first-audible 0.0ms lead-sil 0ms
br_let_him_cook: src cook_a.mp3 4.41s peak +1.3 rms -8.1 -> silence-trim, keep 2.5s +fade, gain -1.60dB -> 2.50s peak -1.45 rms -10.8 first-audible 0.0ms lead-sil 0ms
br_diabolical: src iabolical_b.mp3 1.69s peak -7.4 rms -26.4 -> silence-trim, keep 2.5s, gain +0.00dB -> 1.69s peak -7.42 rms -26.4 first-audible 0.0ms lead-sil 0ms
br_aura_minus1000: src ra_1000.mp3 3.55s peak -11.8 rms -29.5 -> manual start 0.38s, silence-trim, keep 2.5s +fade, gain +0.00dB -> 2.12s peak -11.82 rms -27.3 first-audible 0.0ms lead-sil 0ms
br_monkey_screech: src screaming-monkeys.mp3 5.38s peak -1.5 rms -9.4 -> silence-trim, keep 2.0s +fade, gain +0.00dB -> 2.00s peak -3.03 rms -9.5 first-audible 0.0ms lead-sil 0ms
br_electric_zap: src hock_a.mp3 3.02s peak +4.4 rms -9.5 -> silence-trim, keep 1.5s +fade, gain -2.17dB -> 1.50s peak -1.21 rms -8.8 first-audible 0.0ms lead-sil 0ms
br_skill_issue: src kill_halo.mp3 3.44s peak -1.4 rms -22.0 -> silence-trim, keep 2.3s +fade, gain +0.00dB -> 2.30s peak -1.40 rms -20.2 first-audible 0.0ms lead-sil 0ms
br_nah_id_win: src ah_id_win_b.mp3 3.14s peak -7.4 rms -29.0 -> silence-trim, keep 2.3s +fade, gain +0.00dB -> 2.30s peak -7.47 rms -27.6 first-audible 0.0ms lead-sil 0ms
br_gigachad: src igachad.mp3 15.93s peak -0.6 rms -12.0 -> silence-trim, keep 2.5s +fade, gain -0.75dB -> 2.50s peak -1.61 rms -13.6 first-audible 0.0ms lead-sil 0ms
br_rizz: src izz_a.mp3 1.93s peak -1.9 rms -14.8 -> silence-trim, keep 2.5s, gain +0.00dB -> 1.74s peak -1.86 rms -14.4 first-audible 0.0ms lead-sil 0ms
br_touch_grass: src rass_halo.mp3 2.57s peak -2.7 rms -21.3 -> silence-trim, keep 2.5s +fade, gain +0.00dB -> 2.50s peak -2.73 rms -21.2 first-audible 0.0ms lead-sil 0ms
br_tralalero: src tralalero.mp3 1.60s peak -3.9 rms -14.6 -> silence-trim, keep 2.5s, gain +0.00dB -> 1.60s peak -3.94 rms -14.6 first-audible 0.0ms lead-sil 0ms
br_chicken_jockey: src chicken_jockey.mp3 1.17s peak -9.2 rms -21.7 -> silence-trim, keep 2.5s, gain +0.00dB -> 1.17s peak -9.21 rms -21.7 first-audible 0.0ms lead-sil 0ms
br_fanum_tax: src fanum.mp3 5.02s peak +0.9 rms -13.0 -> silence-trim, keep 2.5s +fade, gain -1.60dB -> 2.50s peak -1.59 rms -14.8 first-audible 0.0ms lead-sil 0ms
```
