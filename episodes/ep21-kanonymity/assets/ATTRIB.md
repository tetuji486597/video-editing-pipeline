# EP21 assets — sources and usage

All captures made 2026-08-28 with the dummy password `password123` (never a real
password). Full capture notes and cross-checks: `range_stats.txt`.

| asset | source | used in | how |
|---|---|---|---|
| `range_CBFDA.txt` | REAL response of `GET https://api.pwnedpasswords.com/range/CBFDA` (Have I Been Pwned k-anonymity range API, 1,972 suffix lines) | `slot_scan` | 36 verbatim rows (file lines 1499-1534) rendered as the response wall; the scanline lands on the REAL matching row `C6008F9CAB4083784CBD1874F76618D2A97:2266543` (file line 1526). Count chip "1,972 hashes returned" is the real line count. |
| `range_CBFDA.txt` (same) | — | `slot_payoff` | 4 verbatim non-matching rows as the ghosted "crowd" behind the held card (`C4659…:168`, `C5BA6…:375`, `C5ED3…:59`, `C6336…:52`). |
| SHA-1 digest `CBFDAC6008F9CAB4083784CBD1874F76618D2A97` | computed locally, = SHA-1("password123"); recorded in `range_stats.txt` | `slot_build` | the full 40-char digest as the two-line hero string; `CBFDA` prefix snipped. Also truncated (`CBFDAC6008F9CAB4…76618D2A97`) as the hash chip in `slot_problem`. |
| `ep21_hibp_pwned_result_tight.png` | screenshot of haveibeenpwned.com/Passwords result UI ("Oh no - pwned! … seen 2,266,543 times") — deliberate product screenshot, the product IS the subject of the episode | `slot_payoff` | inset as the held photo card inside browser chrome (copied to `animations/slot_payoff/assets/hibp_tight.png`). No incidental third-party branding in the crop; the HIBP UI itself is the deliberate subject. |
| `ep21_hibp_pwned_fullpage.png`, `ep21_hibp_search_and_result.png` | same capture session | (not used in overlays) | kept as capture provenance / alternates. |
| `redraw_ref/cf_*.png` | Cloudflare blog diagrams of the k-anonymity range protocol | style reference ONLY | never pasted into any frame, per the batch plan. |

The header chip `GET api.pwnedpasswords.com/range/CBFDA` in `slot_scan` and the
`HAVE I BEEN PWNED` server-card label in `slot_problem` are deliberate references to the
real service being explained (OVERLAY_SPEC: deliberate product screenshots/UI ARE wanted;
the brand is the subject here).
