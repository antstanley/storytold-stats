# storytold — changes per release

Generated 2026-10-17 from the public repos at https://github.com/storytold.

The org has 66 repos; 15 of them publish GitHub releases, and those are the ones covered here. Their 144 GitHub releases make 138 distinct release points (ArtCraft tags macOS and Windows builds of one version separately, and one PhotoCraft release candidate shares a commit with v0.1.0).
Every change that landed in a release is put in one category (feature, fix, perf, …) and one landing type (PR merge, squash merge, direct commit, batch commit).

## Headline numbers (released changes only)

| Repo | Releases | Latest | Changes | Feature | Fix | Perf | Everything else | Feature % | Fix % | Perf % |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [cadcraft](reports/cadcraft.md) | 6 | v0.7.0 | 481 | 138 | 279 | 9 | 55 | 29% | 58% | 1.9% |
| [soundcraft](reports/soundcraft.md) | 5 | v0.7.0 | 243 | 84 | 110 | 6 | 43 | 35% | 45% | 2.5% |
| [craft-launcher](reports/craft-launcher.md) | 9 | v0.4.1 | 101 | 29 | 39 | · | 33 | 29% | 39% | 0.0% |
| [deckcraft](reports/deckcraft.md) | 6 | v0.7.0 | 177 | 37 | 99 | · | 41 | 21% | 56% | 0.0% |
| [gridcraft](reports/gridcraft.md) | 6 | v0.7.0 | 419 | 68 | 272 | 2 | 77 | 16% | 65% | 0.5% |
| [vectorcraft](reports/vectorcraft.md) | 14 | v0.12.0 | 1382 | 453 | 712 | 22 | 195 | 33% | 52% | 1.6% |
| [photocraft](reports/photocraft.md) | 10 | v0.9.0 | 2093 | 425 | 1317 | 114 | 237 | 20% | 63% | 5.4% |
| [pdfcraft](reports/pdfcraft.md) | 9 | v0.8.0 | 900 | 240 | 444 | 27 | 189 | 27% | 49% | 3.0% |
| [designcraft](reports/designcraft.md) | 9 | v0.8.0 | 477 | 245 | 142 | 6 | 84 | 51% | 30% | 1.3% |
| [filmcraft](reports/filmcraft.md) | 9 | v0.8.0 | 880 | 222 | 441 | 46 | 171 | 25% | 50% | 5.2% |
| [figcraft](reports/figcraft.md) | 6 | v0.6.0 | 268 | 163 | 51 | 5 | 49 | 61% | 19% | 1.9% |
| [lightcraft](reports/lightcraft.md) | 9 | v0.8.0 | 973 | 305 | 381 | 54 | 233 | 31% | 39% | 5.5% |
| [effectcraft](reports/effectcraft.md) | 11 | v0.10.0 | 893 | 290 | 345 | 52 | 206 | 32% | 39% | 5.8% |
| [wordcraft](reports/wordcraft.md) | 6 | v0.7.0 | 454 | 152 | 227 | 6 | 69 | 33% | 50% | 1.3% |
| [artcraft](reports/artcraft.md) | 23 | v0.41.0 | 1522 | 709 | 310 | 14 | 489 | 47% | 20% | 0.9% |
| **All** | **138** |  | **11263** | **3560** | **5169** | **363** | **2171** | 32% | 46% | 3.2% |

"Everything else" is i18n, docs, tests, build/CI, release housekeeping, refactors, dependency bumps, security hardening, reverts and changes that could not be categorised. Per-release tables for every repo are in [`reports/`](reports/).

A further 2737 changes are on `main` but not yet in a release (621 features, 1427 fixes, 64 perf); they appear as the "unreleased" row in each repo report and are not in the table above.

### All categories

| Category | Changes | Share |
|---|--:|--:|
| Feature | 3560 | 31.6% |
| Fix | 5169 | 45.9% |
| Perf | 363 | 3.2% |
| i18n | 276 | 2.5% |
| Docs | 495 | 4.4% |
| Test | 246 | 2.2% |
| Build/CI | 284 | 2.5% |
| Release | 259 | 2.3% |
| Refactor | 318 | 2.8% |
| Deps | 28 | 0.2% |
| Security | 59 | 0.5% |
| Revert | 19 | 0.2% |
| Other | 187 | 1.7% |

## Contributors: humans, agents and bots

879 humans contributed to the released changes (811 as the author of at least one change, the rest only as co-authors), alongside 14 disclosed AI agents and 1 bot. 7018 of the 11263 changes (62%) disclose an agent, and 629 of the humans authored at least one change that does.

| Repo | Humans | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|---|--:|
| [cadcraft](reports/cadcraft.md) | 57 | 403 | 84% | · | Claude | · |
| [soundcraft](reports/soundcraft.md) | 37 | 139 | 57% | · | Claude | · |
| [craft-launcher](reports/craft-launcher.md) | 36 | 77 | 76% | · | Claude | · |
| [deckcraft](reports/deckcraft.md) | 19 | 162 | 92% | · | Claude | · |
| [gridcraft](reports/gridcraft.md) | 59 | 216 | 52% | 1 | Claude, OpenAI Codex / ChatGPT | · |
| [vectorcraft](reports/vectorcraft.md) | 142 | 832 | 60% | 2 | Claude, OpenAI Codex / ChatGPT, Cursor | · |
| [photocraft](reports/photocraft.md) | 298 | 1368 | 65% | 20 | Claude, GitHub Copilot, OpenAI Codex / ChatGPT, Cursor, Unnamed agent, Devin, Qwen | · |
| [pdfcraft](reports/pdfcraft.md) | 188 | 645 | 72% | · | Claude, OpenAI Codex / ChatGPT, opencode, GLM (Z.ai), GitHub Copilot, Muse Spark (Meta), Cursor | · |
| [designcraft](reports/designcraft.md) | 45 | 376 | 79% | · | Claude, OpenAI Codex / ChatGPT, Codebuff | · |
| [filmcraft](reports/filmcraft.md) | 109 | 689 | 78% | 3 | Claude, OpenAI Codex / ChatGPT, Kimi, GitHub Copilot, Xiaomi MiMo | · |
| [figcraft](reports/figcraft.md) | 13 | 153 | 57% | · | Claude | · |
| [lightcraft](reports/lightcraft.md) | 142 | 805 | 83% | 264 | Claude, OpenAI Codex / ChatGPT, DeepSeek, opencode, GitHub Copilot, GLM (Z.ai) | · |
| [effectcraft](reports/effectcraft.md) | 80 | 763 | 85% | 126 | Claude, OpenAI Codex / ChatGPT | · |
| [wordcraft](reports/wordcraft.md) | 88 | 384 | 85% | · | Claude, OpenAI Codex / ChatGPT, Cursor, Devin, GitHub Copilot, Unnamed agent | · |
| [artcraft](reports/artcraft.md) | 8 | 6 | <1% | · | Claude | 1 |
| **All** | **879** | **7018** | 62% | **416** | 14 agents | 1 |

A human is counted once per repo here, and once in the **All** row even if they contributed to several repos.

### Disclosed agents

| Agent | Changes | As git author | As co-author | Humans authoring those changes | Repos |
|---|--:|--:|--:|--:|--:|
| Claude | 6825 | 416 | 6409 | 608 | 15 |
| OpenAI Codex / ChatGPT | 208 | · | 208 | 51 | 9 |
| GitHub Copilot | 36 | · | 36 | 5 | 5 |
| Cursor | 17 | · | 17 | 6 | 4 |
| opencode | 11 | · | 11 | 4 | 2 |
| GLM (Z.ai) | 4 | · | 4 | 3 | 2 |
| Unnamed agent | 4 | · | 4 | 2 | 2 |
| Codebuff | 3 | · | 3 | 1 | 1 |
| DeepSeek | 3 | · | 3 | 1 | 1 |
| Devin | 2 | · | 2 | 2 | 2 |
| Kimi | 2 | · | 2 | 1 | 1 |
| Muse Spark (Meta) | 2 | · | 2 | 1 | 1 |
| Qwen | 1 | · | 1 | 1 | 1 |
| Xiaomi MiMo | 1 | · | 1 | 1 | 1 |

"As git author" means the commit's author is the agent itself; "as co-author" means a human is the author and the agent is named in a `Co-authored-by` trailer or a "Generated with" line. A change that discloses two agents counts for both. 100 changes have an agent as git author and no human named at all. The model names seen most often: Claude Opus 5.5 (6304), Claude (484), Claude Sonnet 5.5 (185), Codex (152), Claude Fable 5.1 (79), Claude Opus 4.8 (63), Claude Haiku 5.5 (43), OpenAI Codex (36).

`csv/contributors.csv` lists every human, agent and bot per repo and across the org.

## How the numbers are produced

**Release ranges.** For each repo the release tags are ordered by version. A release's changes are the commits reachable from its tag but not from any earlier release tag; the first release gets everything before it.

**What counts as one change.** Counting raw commits would overstate repos that merge multi-commit PR branches, and counting only first-parent commits would hide the PRs that land through integration branches. So each release range is split into:

| Landing type | Changes | What it is |
|---|--:|---|
| PR merge | 4535 | a `Merge pull request #N` / `Merge PR #N` merge commit, at any depth of the history (PRs merged into an integration branch count too). The PR's own commits are folded into it. |
| Squash merge | 5861 | a single commit that is the squash of PR #N. |
| Direct commit | 2738 | a non-merge commit pushed straight to the mainline (or brought in by a plain branch merge) with no PR behind it. |
| Batch commit | 866 | a commit made directly on an integration-batch PR branch (follow-up fixes, formatting, conflict clean-up after merging a batch of contributor PRs). |

Commits inside an ordinary PR branch and plain sync merges (`Merge branch 'main' into …`) are not changes; they are reported separately in each repo's "By how it landed" table. Counts are counts of changes, not of lines or effort: a one-line fix and a whole new subsystem each count once.

**Contributors.** The contributors of a change are read from its commits (for a PR merge, every commit in the PR branch) and its PR:

- **Human:** the PR's author, or the commit's git author when there is no PR, plus anyone named in a `Co-authored-by` trailer and anyone else who authored a commit in the PR branch. Each is resolved to a GitHub login where the history gives one (a GitHub noreply address, a squash-merge commit authored by the PR's author, or being the main committer in a PR that login opened) and otherwise kept as the git name.
- **Agent (disclosed):** a known AI agent identity appearing as a commit's git author (for example `Claude <noreply@anthropic.com>`), in a `Co-authored-by` trailer (`Claude Opus 5.5`, `Codex`, `Copilot`, …), or in a "Generated with …" line. Model variants are grouped under one agent: every Claude model is "Claude". The table of recognised agents is in `scripts/contributors.py`.
- **Bot:** a non-AI automation account, such as `dependabot[bot]`.

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
| Title read and labelled by an LLM (Claude Haiku), for titles with no prefix, branch or label signal | 6486 | 46.3% |
| PR branch name (`fix/…`, `feat/…`, `perf/…`, `docs/…`) | 5157 | 36.8% |
| Conventional-commit prefix on the title (`fix(...)`, `feat:`, `perf:` …) | 2075 | 14.8% |
| Keyword rules on the title: version bumps, release prep and reverts, plus any title not yet read by the LLM | 200 | 1.4% |
| Integration-batch PR that only bundles other PRs (counted as Other) | 73 | 0.5% |
| `bug` / `enhancement` label on the PR or the issue it closes | 9 | 0.1% |

## Things to know before quoting these

- **The feature/fix split is partly a judgment call.** Roughly half of the changes have no prefix, branch name or label saying what they are; those were labelled from their title alone by an LLM (Claude Haiku, in 8 batches, plus one batch of 217 titles in a later refresh and three batches of 1,394 titles in the refresh after that). The labels were spot-checked against the titles and checked for row alignment; one run of 53 shifted labels was found and repaired. The 217-title batch was read against its titles in full and had no shifts; the three later batches were sampled against their titles, and the one run the alignment check flagged (40 rows) was read in full and found not to be shifted. No human has reviewed them one by one. Titles in these repos often just state the new behaviour ("Layers: the active layer falls back to the top layer when it is removed"), which reads as a fix but could be argued either way. Treat the split as indicative, not exact.
- **Agent figures are a floor.** They count what the history discloses. A change written with an agent but committed without a trailer looks human-only, and squash merges keep trailers only if the person merging left them in.
- **"Human" means "not a recognised agent or bot".** An account that is run by an agent but does not say so, or an agent whose name is not in the table yet, is counted as a human.
- **A few people may be counted twice.** 61 of the 879 humans could not be tied to a GitHub login and are identified by git name only; some of them may be the same person as a login.
- **GitHub labels were of no use.** Only a handful of PRs or linked issues carry `bug`/`enhancement` labels.
- **"fixes #123" is not treated as a bug-fix signal.** It is GitHub's issue-closing keyword and is used on feature PRs too.
- **ArtCraft's first release (`artcraft-v0.0.1`) is not categorised.** It sits on about 13,400 commits of earlier monorepo history going back to 2015. It is counted, not labelled, and is left out of every total above.
- **ArtCraft's history was reset before v0.41.0.** `main` was restarted on 2026-09-11, so v0.41.0 covers only the 11 commits on the new history. ArtCraft's macOS and Windows tags for the same version are treated as one release.
- **Not every version number has a release.** Several repos skip versions (e.g. v0.5.0 → v0.6.2); a row covers everything since the previous published release.
- **PhotoCraft `v0.1.0` and `v0.1.1-rc.4` are the same commit** and are shown as one row.
- **Community vs team PRs** uses GitHub's author association at the time of fetching (member/owner/collaborator = team).

## Files

- `reports/<repo>.md` — one repo's charts, a short plain-English commentary on its trends, and per-release tables: by change type, by how changes landed, and by contributor. The commentary rounds shares to whole percentages but never shows 0% or 100%: a share of zero is "none", a complete one is "all", and anything rounded to either end is "under 1%" or "over 99%"
- `csv/release_stats.csv` — the same numbers, one row per repo and release
- `csv/changes.csv` — every change with its release, category, basis, landing type, PR number, contributors (human, co-authors, agents, bots) and title
- `csv/contributors.csv` — every human, agent and bot with their change counts, per repo and across the org (`repo` = `(all)`)
- `web/` — SvelteKit + LayerChart app with a stacked line chart and a stacked bar chart per repo, flat or isometric (`cd web && pnpm install && pnpm dev`)
- `charts/light/`, `charts/dark/` — PNG exports of the four charts on each repo's page, embedded in the reports
- `data/` — inputs and per-change output: PR metadata (`prs/`, `prs_extra/`), release lists (`releases_api/`), LLM labels (`review_labels.jsonl`, batches in `review/`), and every classified change (`classified.jsonl`)
- `scripts/` — the pipeline
- `.agents/skills/` — instructions for an AI agent: `compile-stats` refreshes the stats from GitHub, `create-reports` generates the reports, their charts and their commentary

## Repos not covered

These have no GitHub releases, so there is nothing to break down per release: artcraft-services (the largest repo by history, ~15,000 commits), craft-libs, craft-repo-status-app, craft-common-actions, craft-launcher-assets, craft-fonts, photocraft-corpus, artcraftx, cloud-worker, github-media, storyteller-ml, storyteller-bevy, fakeyou-recast, and about 30 older, archived or forked repos (Unreal/Unity plugins, ML experiments, forks such as spark and winprint.rs).

## Licence

[MIT](LICENSE).
