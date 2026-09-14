# EP32 (replication + failover) — real image sources

Personal use only, per the user. Every file ffprobe'd before use.

| file | used in | source | licence / author | notes |
|---|---|---|---|---|
| `gh_status_full_capture.png` (1265x5822, png) | source capture only (not rendered) | https://www.githubstatus.com/ — Playwright full-page screenshot, 2026-09-05, page zoomed 2.6x so the type is legible when inset | GitHub, Inc. (Statuspage); personal use | the real "All Systems Operational" status page — the actual thing the HOOK beat is about ("users don't notice a thing") |
| `gh_status_banner.png` (1208x160, png) | `animations/slot_hook/assets/` (the calm users' screen, act 1) and `animations/slot_payoff/assets/` (act 2, "saves you": the page stays green) | crop of the capture above (the green "All Systems Operational" bar) | as above | deliberate product screenshot; the only mark is the site's own check + wording |
| `gh_status_cards.png` (1208x410, png) | `animations/slot_hook/assets/` (the uptime card row under the banner, scrolls calmly) | crop of the capture above (Git Operations / Webhooks uptime cards) | as above | 90-day uptime bars, all green |

Tried and abandoned: thesecretlivesofdata.com/raft (the Raft log-replication step). The
visualisation is D3 driven and rendered an empty SVG in headless Playwright (one console
error, no nodes drawn), so no usable frame could be captured; the leader/follower diagram in
slot_build / slot_new_component is hand-built instead.
