# Image attributions — EP14-19 batch

Real images sourced from the web for this batch, with their licences. **Read the
"Action required" line before publishing.**

## Action required

**EP19 `slot_hook` uses a CC BY 2.0 photograph, which carries an attribution
obligation.** CC BY requires crediting the photographer wherever the work is
distributed — in practice a line in the video description is the normal way to satisfy
this for a social upload. Nothing else in this batch requires a credit.

| Episode / slot | Image | Source | Licence | Credit needed |
|---|---|---|---|---|
| EP19 `slot_hook` | Cristiano Ronaldo (post photo + avatar, two crops) | `commons.wikimedia.org/wiki/File:Cristiano_Ronaldo_(cropped).jpg` | **CC BY 2.0** | **YES** |
| EP18 `slot_payoff` | Server rack / data-centre aisle | `images.unsplash.com/photo-1558494949-ef010cbdcc31` | Unsplash Licence | No |
| EP15 `slot_hook` | Real app login screen showing "Continue with Google" | `upload.wikimedia.org/wikipedia/commons/8/87/Screenshot_of_X_%28Twitter%29_login.png` | Public domain | No |
| EP15 `slot_new_component` | Real Google OAuth consent screen | `developers.google.com/static/identity/protocols/oauth2/images/examples/scope-authorization.png` | Google's own published developer documentation | No |
| EP16 `slot_payoff` | Real TinyURL product UI | Captured from `tinyurl.com` this session | Product screenshot, used as the subject | No |
| EP17 `slot_new_component` / `slot_payoff` | Card terminal in use; card chip macro | `shared_assets/misc/` (carried over from the previous batch) | Provenance not recorded — see below | Unknown |
| EP14 (all photo slots) | 16 feed photos used as feed content | `shared_assets/feed/` (carried over from the previous batch) | Provenance not recorded — see below | Unknown |

## Provenance gap on the carried-over assets

`shared_assets/feed/*` and `shared_assets/misc/{card_chip,card_terminal,stadium_crowd,
ronaldo}` were inherited from the previous build of these episodes
(`_overlay_snapshots/2026-08-20_pre-richness-rebuild/`). **That snapshot records no source
URLs or licences** — only the files. They were all inspected this session and carry no
legible branding, watermarks, or identifiable private individuals, but their licences are
unverified.

That is fine for the pre-existing shipped episodes, and it is a risk worth closing before
this batch goes out: if any of them turn out to be licence-restricted, the affected slot
needs its image swapped and re-rendered. The cheapest fix is to re-source the handful that
actually carry a beat (EP17's two card photos, EP19's crowd) from Unsplash/Pexels/Wikimedia
with the URL recorded here, and to treat the EP14 feed tiles as lower risk since they
appear only as small thumbnails.

Note EP19 `slot_hook` no longer uses the carried-over `ronaldo.png` — its agent re-sourced a
higher-resolution Wikimedia original (the row above), so that one is now fully documented.

## Rejected during sourcing, and why

Recorded so nobody re-introduces them:

- `keys.jpg`, `directory_page.jpg`, `mask.jpg`, `cables.jpg` (all in the old snapshot) —
  visual puns, the exact failure the user's feedback named ("the dictionary for the DNS is
  not exactly the image that best applies").
- Two other Google consent-screen images from the same documentation page
  (`authz-multiple-consent.png`, `authz-single-consent.png`) — both show a real account
  address and avatar.
- Four server-rack candidates — legible "SENNHEISER" branding, repeated "Absen" labels, a
  photo captioned as containing white logos, and one that was simply the wrong subject.
- A teapot feed photo — faint "BODUM" branding on the glass.
- Instagram itself was **not** screenshotted: the browser session was logged into the
  user's personal account, so a capture would have pulled their own profile, DM badge and
  "suggested for you" (real private individuals) into a published video. EP19's post is a
  UI recreation with the real photo inset instead — which is also the only way that beat
  works, since its like counter has to move.
