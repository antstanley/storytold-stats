# storytold — changes per release

Generated 2026-10-13 from the public repos at https://github.com/storytold.

The org has 59 repos; 15 of them publish GitHub releases, and those are the ones covered here. Their 128 GitHub releases make 122 distinct release points (ArtCraft tags macOS and Windows builds of one version separately, and one PhotoCraft release candidate shares a commit with v0.1.0).
Every change that landed in a release is put in one category (feature, fix, perf, …) and one landing type (PR merge, squash merge, direct commit, batch commit).

## Headline numbers (released changes only)

| Repo | Releases | Latest | Changes | Feature | Fix | Perf | Everything else | Feature % | Fix % | Perf % |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [cadcraft](reports/cadcraft.md) | 5 | v0.6.2 | 371 | 113 | 215 | 6 | 37 | 30% | 58% | 1.6% |
| [soundcraft](reports/soundcraft.md) | 4 | v0.6.1 | 141 | 51 | 51 | 3 | 36 | 36% | 36% | 2.1% |
| [craft-launcher](reports/craft-launcher.md) | 7 | v0.3.2 | 66 | 22 | 24 | · | 20 | 33% | 36% | 0.0% |
| [deckcraft](reports/deckcraft.md) | 5 | v0.6.1 | 64 | 19 | 14 | · | 31 | 30% | 22% | 0.0% |
| [gridcraft](reports/gridcraft.md) | 5 | v0.6.1 | 256 | 55 | 143 | 1 | 57 | 21% | 56% | 0.4% |
| [vectorcraft](reports/vectorcraft.md) | 12 | v0.10.0 | 885 | 293 | 431 | 18 | 143 | 33% | 49% | 2.0% |
| [photocraft](reports/photocraft.md) | 9 | v0.8.2 | 1699 | 360 | 1045 | 84 | 210 | 21% | 62% | 4.9% |
| [pdfcraft](reports/pdfcraft.md) | 8 | v0.7.1 | 827 | 231 | 388 | 26 | 182 | 28% | 47% | 3.1% |
| [designcraft](reports/designcraft.md) | 8 | v0.7.1 | 408 | 228 | 94 | 5 | 81 | 56% | 23% | 1.2% |
| [filmcraft](reports/filmcraft.md) | 8 | v0.7.2 | 803 | 217 | 380 | 46 | 160 | 27% | 47% | 5.7% |
| [figcraft](reports/figcraft.md) | 5 | v0.5.1 | 214 | 140 | 28 | 5 | 41 | 65% | 13% | 2.3% |
| [lightcraft](reports/lightcraft.md) | 8 | v0.7.1 | 788 | 278 | 269 | 42 | 199 | 35% | 34% | 5.3% |
| [effectcraft](reports/effectcraft.md) | 10 | v0.9.2 | 779 | 268 | 275 | 48 | 188 | 34% | 35% | 6.2% |
| [wordcraft](reports/wordcraft.md) | 5 | v0.6.1 | 405 | 145 | 194 | 3 | 63 | 36% | 48% | 0.7% |
| [artcraft](reports/artcraft.md) | 23 | v0.41.0 | 1522 | 709 | 310 | 14 | 489 | 47% | 20% | 0.9% |
| **All** | **122** |  | **9228** | **3129** | **3861** | **301** | **1937** | 34% | 42% | 3.3% |

"Everything else" is i18n, docs, tests, build/CI, release housekeeping, refactors, dependency bumps, security hardening, reverts and changes that could not be categorised. Per-release tables for every repo are in [`reports/`](reports/).

A further 1153 changes are on `main` but not yet in a release (209 features, 783 fixes, 38 perf); they appear as the "unreleased" row in each repo report and are not in the table above.

### All categories

| Category | Changes | Share |
|---|--:|--:|
| Feature | 3129 | 33.9% |
| Fix | 3861 | 41.8% |
| Perf | 301 | 3.3% |
| i18n | 223 | 2.4% |
| Docs | 433 | 4.7% |
| Test | 208 | 2.3% |
| Build/CI | 263 | 2.9% |
| Release | 244 | 2.6% |
| Refactor | 294 | 3.2% |
| Deps | 27 | 0.3% |
| Security | 44 | 0.5% |
| Revert | 18 | 0.2% |
| Other | 183 | 2.0% |

## How the numbers are produced

**Release ranges.** For each repo the release tags are ordered by version. A release's changes are the commits reachable from its tag but not from any earlier release tag; the first release gets everything before it.

**What counts as one change.** Counting raw commits would overstate repos that merge multi-commit PR branches, and counting only first-parent commits would hide the PRs that land through integration branches. So each release range is split into:

| Landing type | Changes | What it is |
|---|--:|---|
| PR merge | 2977 | a `Merge pull request #N` / `Merge PR #N` merge commit, at any depth of the history (PRs merged into an integration branch count too). The PR's own commits are folded into it. |
| Squash merge | 4854 | a single commit that is the squash of PR #N. |
| Direct commit | 2428 | a non-merge commit pushed straight to the mainline (or brought in by a plain branch merge) with no PR behind it. |
| Batch commit | 122 | a commit made directly on an integration-batch PR branch (follow-up fixes, formatting, conflict clean-up after merging a batch of contributor PRs). |

Commits inside an ordinary PR branch and plain sync merges (`Merge branch 'main' into …`) are not changes; they are reported separately in each repo's "By how it landed" table. Counts are counts of changes, not of lines or effort: a one-line fix and a whole new subsystem each count once.

**Categories.**

| Category | Meaning |
|---|---|
| Feature | New user-visible capability or a deliberate extension/redesign of one |
| Fix | Corrects wrong behaviour: bugs, crashes, wrong output, regressions, parity corrections |
| Perf | Speed, memory or responsiveness is the point of the change |
| i18n | Translations, locale catalogs, new interface languages |
| Docs | README, AGENTS.md, roadmap/parity trackers, guides, licences |
| Test | Only tests, fixtures, fuzzers, corpora |
| Build/CI | CI workflows, release pipeline, packaging, signing, build tooling |
| Release | Version bumps and release prep |
| Refactor | Internal restructuring, formatting, clean-up, merge fix-ups, with no intended behaviour change |
| Deps | Dependency bumps and pins |
| Security | Hardening against hostile input, sandboxing, signature checks |
| Revert | Reverts an earlier change |
| Other | Integration-batch PRs, and titles that say too little to categorise |

**How each change got its category.** The strongest available signal wins, and the one used is recorded per change in `csv/changes.csv` (`basis` column):

| How the category was decided | Changes | Share |
|---|--:|--:|
| Title read and labelled by an LLM (Claude Haiku), for titles with no prefix, branch or label signal | 4875 | 47.0% |
| PR branch name (`fix/…`, `feat/…`, `perf/…`, `docs/…`) | 3890 | 37.5% |
| Conventional-commit prefix on the title (`fix(...)`, `feat:`, `perf:` …) | 1395 | 13.4% |
| Unambiguous title wording: version bumps / release prep and reverts | 181 | 1.7% |
| Integration-batch PR that only bundles other PRs (counted as Other) | 37 | 0.4% |
| `bug` / `enhancement` label on the PR or the issue it closes | 3 | 0.0% |

## Things to know before quoting these

- **The feature/fix split is partly a judgment call.** Roughly half of the changes have no prefix, branch name or label saying what they are; those were labelled from their title alone by an LLM (Claude Haiku, in 8 batches). The labels were spot-checked against the titles and checked for row alignment; one run of 53 shifted labels was found and repaired. No human has reviewed them one by one. Titles in these repos often just state the new behaviour ("Layers: the active layer falls back to the top layer when it is removed"), which reads as a fix but could be argued either way. Treat the split as indicative, not exact.
- **GitHub labels were of no use.** Only a handful of PRs or linked issues carry `bug`/`enhancement` labels.
- **"fixes #123" is not treated as a bug-fix signal.** It is GitHub's issue-closing keyword and is used on feature PRs too.
- **ArtCraft's first release (`artcraft-v0.0.1`) is not categorised.** It sits on about 13,400 commits of earlier monorepo history going back to 2015. It is counted, not labelled, and is left out of every total above.
- **ArtCraft's history was reset before v0.41.0.** `main` was restarted on 2026-09-11, so v0.41.0 covers only the 11 commits on the new history. ArtCraft's macOS and Windows tags for the same version are treated as one release.
- **Not every version number has a release.** Several repos skip versions (e.g. v0.5.0 → v0.6.2); a row covers everything since the previous published release.
- **PhotoCraft `v0.1.0` and `v0.1.1-rc.4` are the same commit** and are shown as one row.
- **Community vs team PRs** uses GitHub's author association at the time of fetching (member/owner/collaborator = team).

## Files

- `reports/<repo>.md` — per-release tables for one repo: by category, and by how changes landed
- `csv/release_stats.csv` — the same numbers, one row per repo and release
- `csv/changes.csv` — every change with its release, category, basis, landing type, PR number, author and title
- `web/` — SvelteKit + LayerChart app with a stacked line chart and a stacked bar chart per repo, flat or isometric (`cd web && pnpm install && pnpm dev`)
- `charts/dark/` — PNG exports of each repo's stacked line chart
- `data/` — inputs and per-change output: PR metadata (`prs/`), release lists (`releases_api/`), LLM labels (`review/`), and every classified change (`classified.jsonl`)
- `scripts/` — the pipeline, in order:
  1. `clone_repos.sh` — bare clones of the 15 repos into `repos/` (not committed)
  2. `fetch_prs.sh <repo>` — merged-PR metadata for one repo (needs the `gh` CLI)
  3. `build_changes.py` — splits each release range into changes
  4. `classify.py` — assigns categories (`ingest_review.py` merges LLM labels first; a change without a label falls back to keyword rules)
  5. `report.py` — writes this README, `reports/` and `csv/`
  6. `export_web.py` — refreshes the web app's data

## Repos not covered

These have no GitHub releases, so there is nothing to break down per release: artcraft-services (the largest repo by history, ~15,000 commits), craft-libs, craft-repo-status-app, craft-common-actions, craft-launcher-assets, craft-fonts, photocraft-corpus, artcraftx, cloud-worker, github-media, storyteller-ml, storyteller-bevy, fakeyou-recast, and about 30 older, archived or forked repos (Unreal/Unity plugins, ML experiments, forks such as spark and winprint.rs).

## Licence

[MIT](LICENSE).
