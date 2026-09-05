# EP25 asset attributions

## ep25_gha_run_viewport.png / ep25_gha_jobs_graph.png

- **What:** two browser captures (1554x873 PNG each, verified via ffprobe) of one real,
  public GitHub Actions run: repository `actions/runner` (GitHub's own public runner
  repo), workflow "Runner CI" / `build.yml`, run **#7570** — "Prepare 2.337.0 release
  (#4658)", triggered via push to `main`, Status **Success**, total duration 5m 3s,
  9 artifacts. `_run_viewport` shows the run header + success banner + all-jobs list;
  `_jobs_graph` shows the `Matrix: build` graph with **7 green completed jobs**
  (linux-arm/arm64/x64, osx-arm64/x64, win-arm64/x64) plus 2 green docker jobs.
- **Source:** `https://github.com/actions/runner` → Actions tab → run #7570
  (logged-out public view — "Sign in to view logs" visible in the viewport capture).
- **Why this is compliant with the spec's image rules:** this is a *deliberate product
  screenshot* — the CD beat's conveyor overlay recreates exactly this machine, and the
  brief calls for the real all-green pipeline inset in the monitor above the belt.
  Wanted branding (GitHub Actions UI) is the subject, not incidental. No private
  individuals: the only avatar/username visible ("rentziass") is a public GitHub
  maintainer acting in public on a public repo.
- **Used in:** `animations/slot_cd/` — `ep25_gha_jobs_graph.png` (copied to
  `animations/slot_cd/assets/gha_jobs_graph.png`) is inset inside the monitor card
  (designed browser chrome, 720x405 at canvas x 120-840, y 284-689) above the conveyor.
  The success-header capture (`_run_viewport`) is kept as the alternate/backup crop and
  is not currently composited.
