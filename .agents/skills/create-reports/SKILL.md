---
name: create-reports
description: Generate the per-repo reports in reports/ (charts, plain-English trend commentary and per-release tables) from the compiled storytold stats, and change what they say. Use when asked to regenerate or update the reports, re-export their charts, fix or extend the commentary, or add a chart or table to them. To pull new data from GitHub first, use the compile-stats skill.
---

# Create the reports and their commentary

Each file in `reports/` covers one repo: four charts, a short "What this shows" commentary under them, and per-release tables. All of it is generated. Nothing in `reports/` or `charts/` is edited by hand, because the next run would overwrite it; to change a report you change what generates it.

| Part of a report | Comes from |
|---|---|
| Tables and page structure | `scripts/report.py` |
| "What this shows" bullets | `scripts/commentary.py` |
| Chart images | the web app in `web/`, exported to `charts/light/` and `charts/dark/` by `web/scripts/export-charts.mjs` |
| The numbers behind all three | `data/classified.jsonl` and `data/releases.jsonl`, produced by the [compile-stats](../compile-stats/SKILL.md) skill |

This skill starts from data that is already compiled. If the request is for *newer* numbers, run compile-stats first.

Reports are done when the tables, the commentary and the charts all describe the same data, every embedded image exists, and you have read the commentary for several repos and found it true.

## Regenerate everything

Run from the repo root. You need `python3`, and for the charts `pnpm` and a local Google Chrome.

```sh
python3 scripts/report.py          # README.md, reports/*.md, csv/*.csv
python3 scripts/export_web.py      # the web app's copy of the numbers

cd web
pnpm install
pnpm check && pnpm build
pnpm preview --port 4173 &         # start it after the build
node scripts/export-charts.mjs http://localhost:4173
```

`report.py` stops with an assertion error if the counts do not reconcile, and prints `missing chart: …` for any image a report embeds that is not on disk. Fix the cause of either; do not work around them.

Export the charts whenever the numbers changed, even if the reports' text did not. A chart that is a run behind contradicts the table beside it, and nothing else will tell you.

`export-charts.mjs` opens every repo page in light and dark mode and screenshots each chart card. Stop the preview server when it finishes. Two things trip it up:

- **An unstyled page with no charts** means `vite preview` was started before the last `pnpm build`. Restart it.
- **A different port.** If 4173 is taken, the server picks another and prints it. Pass that URL to the script.

## Check the result

Read at least three reports from top to bottom: the largest repo, the smallest, and one whose releases all fall within a few days. For each:

- **Commentary against tables.** Every figure in a bullet can be checked against the table under it. Check a few.
- **Commentary against charts.** If a bullet says releases are getting bigger, the bars should show it.
- **Charts.** Open a few PNGs and look for overlapping or repeated axis labels, a legend that covers the plot, or an empty plot.
- **Tone.** The bullets should read as plain statements a non-specialist can follow.

Then run `git diff --stat reports/ charts/` and make sure the files that changed are the ones you expected to change.

## Changing the commentary

The commentary is written by rules, not by hand, so that it stays true when the numbers move. `scripts/commentary.py` has one function per report section:

- `types()` — how many releases and changes, the biggest release, whether releases are getting bigger, the mix of change types and whether it has shifted, performance work, unreleased changes.
- `landing()` — pull requests versus direct commits, and how many pull requests came from outside the core team.
- `contributors()` — how many people, new people in the latest release, how concentrated the work is, and how much of it discloses an AI agent.

Each returns a list of sentences. A sentence is only added when the numbers support it, and most trend sentences compare the first half of a repo's releases with the last half.

When you add or change a sentence, hold it to these:

- **Say what happened, not why.** The data shows that fixes went from 26% to 64% of changes. It does not show the reason, so the commentary does not give one.
- **One fact per sentence, with its numbers.** "Releases are getting bigger: the first 4 releases averaged 31 changes each and the last 4 averaged 347." The reader should be able to find both numbers in the table.
- **Plain words.** "Fixing" and "building new things", not "maintenance burden" or "feature velocity". Write "people", "changes", "pull requests". Name a release as `v0.6.0 (10 Oct)`; `name()` does this.
- **Only claim a trend the numbers clear a bar for.** The existing bars: a size change needs the later average to be at least 1.5 times the earlier one (or two thirds of it); a shift in a share needs 10 percentage points; a shift in where pull requests come from needs 20. Below the bar, say it has stayed about the same, or say nothing.
- **Make it right for every repo, not the one in front of you.** The same rule writes all the reports. Before keeping a change, regenerate and read the sentence in every report: `grep -h "<a few words of it>" reports/*.md`. The repos that break rules are the small ones (two contributors, four releases), and the ones whose releases all fall within two days.
- **Mind the small numbers.** Use `count()` so that one release is not "1 releases". Use `pct()` so that 6 of 1,522 is "under 1%" and not "0%". Say "none" and "all" where a percentage would read as 0% or 100%. For a share already worked out as a number, such as the two halves in a trend sentence, use `of(p, "changes")` for the first mention and `bare(p)` after it; both say "none", "all", "under 1%" and "over 99%" for you.
- **Keep a pronoun next to what it refers to.** A sentence that starts "That share…" must directly follow the sentence that gives the share.

If a report needs a remark that no rule could produce (a one-off explanation of an unusual release, say), it does not belong in the generated commentary. Tell the user rather than editing the report.

## Adding or changing a chart

A chart in a report is a screenshot of a chart card on the repo page of the web app.

1. Build the chart in `web/src/routes/[repo]/+page.svelte` (the chart components are in `web/src/lib/components/`, the series and row builders in `web/src/lib/stats.ts`). Give its `<section>` a `data-chart="some-name"` attribute; the export script screenshots every section that has one and names the file after it.
2. If the chart needs numbers the app does not have yet, add them to `scripts/export_web.py`.
3. Embed it in the report with `picture(repo, "some-name", alt)` in `scripts/report.py`. Write alt text that says what the chart shows.
4. Run the export and look at the PNG for at least the smallest and the largest repo, in both themes.

The reports embed images with a `<picture>` element so that GitHub shows the dark export to readers using a dark theme. Paths are relative to `reports/`, so they start with `../charts/`.

One trap when naming a series: do not call a data field `none`. LayerChart treats a style value that matches a field name as that field, so a field called `none` takes over every `stroke="none"` and breaks area charts into fragments.

## Changing a table or the page structure

Tables and section order are in the per-repo loop of `scripts/report.py`. The top-level `README.md` is generated by the same script from the template at the bottom of it. Category definitions, landing types and the contributor rules are explained in that README; keep it in step with any change to what a report shows.

## Finishing

Report which reports changed and why, any commentary rule you added or altered and the repos it now reads differently for, and anything you checked by eye. Commit or push only if you were asked to.
