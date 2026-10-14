# storytold — changes per release

Generated 2026-10-14 from the public repos at https://github.com/storytold.

The org has 61 repos; 15 of them publish GitHub releases, and those are the ones covered here. Their 130 GitHub releases make 124 distinct release points (ArtCraft tags macOS and Windows builds of one version separately, and one PhotoCraft release candidate shares a commit with v0.1.0).
Every change that landed in a release is put in one category (feature, fix, perf, …) and one landing type (PR merge, squash merge, direct commit, batch commit).

## Headline numbers (released changes only)

| Repo | Releases | Latest | Changes | Feature | Fix | Perf | Everything else | Feature % | Fix % | Perf % |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [cadcraft](reports/cadcraft.md) | 5 | v0.6.2 | 371 | 113 | 215 | 6 | 37 | 30% | 58% | 1.6% |
| [soundcraft](reports/soundcraft.md) | 4 | v0.6.1 | 141 | 51 | 51 | 3 | 36 | 36% | 36% | 2.1% |
| [craft-launcher](reports/craft-launcher.md) | 9 | v0.4.1 | 101 | 29 | 39 | · | 33 | 29% | 39% | 0.0% |
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
| **All** | **124** |  | **9263** | **3136** | **3876** | **301** | **1950** | 34% | 42% | 3.2% |

"Everything else" is i18n, docs, tests, build/CI, release housekeeping, refactors, dependency bumps, security hardening, reverts and changes that could not be categorised. Per-release tables for every repo are in [`reports/`](reports/).

A further 1753 changes are on `main` but not yet in a release (333 features, 1172 fixes, 64 perf); they appear as the "unreleased" row in each repo report and are not in the table above.

### All categories

| Category | Changes | Share |
|---|--:|--:|
| Feature | 3136 | 33.9% |
| Fix | 3876 | 41.8% |
| Perf | 301 | 3.2% |
| i18n | 229 | 2.5% |
| Docs | 434 | 4.7% |
| Test | 208 | 2.2% |
| Build/CI | 268 | 2.9% |
| Release | 245 | 2.6% |
| Refactor | 294 | 3.2% |
| Deps | 27 | 0.3% |
| Security | 44 | 0.5% |
| Revert | 18 | 0.2% |
| Other | 183 | 2.0% |

## Contributors: humans, agents and bots

723 humans contributed to the released changes (668 as the author of at least one change, the rest only as co-authors), alongside 14 disclosed AI agents and 1 bot. 6133 of the 9263 changes (66%) disclose an agent, and 535 of the humans authored at least one change that does.

| Repo | Humans | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|---|--:|
| [cadcraft](reports/cadcraft.md) | 35 | 319 | 86% | · | Claude | · |
| [soundcraft](reports/soundcraft.md) | 22 | 110 | 78% | · | Claude | · |
| [craft-launcher](reports/craft-launcher.md) | 36 | 77 | 76% | · | Claude | · |
| [deckcraft](reports/deckcraft.md) | 17 | 57 | 89% | · | Claude | · |
| [gridcraft](reports/gridcraft.md) | 44 | 164 | 64% | · | Claude, OpenAI Codex / ChatGPT | · |
| [vectorcraft](reports/vectorcraft.md) | 101 | 751 | 85% | 1 | Claude, OpenAI Codex / ChatGPT, Cursor | · |
| [photocraft](reports/photocraft.md) | 255 | 1149 | 68% | 20 | Claude, GitHub Copilot, OpenAI Codex / ChatGPT, Unnamed agent, Cursor, Devin, Qwen | · |
| [pdfcraft](reports/pdfcraft.md) | 178 | 616 | 74% | · | Claude, OpenAI Codex / ChatGPT, opencode, GLM (Z.ai), GitHub Copilot, Muse Spark (Meta), Cursor | · |
| [designcraft](reports/designcraft.md) | 34 | 334 | 82% | · | Claude, OpenAI Codex / ChatGPT, Codebuff | · |
| [filmcraft](reports/filmcraft.md) | 96 | 641 | 80% | 2 | Claude, OpenAI Codex / ChatGPT, Kimi, Xiaomi MiMo | · |
| [figcraft](reports/figcraft.md) | 2 | 136 | 64% | · | Claude | · |
| [lightcraft](reports/lightcraft.md) | 113 | 721 | 91% | 263 | Claude, OpenAI Codex / ChatGPT, DeepSeek, opencode, GitHub Copilot | · |
| [effectcraft](reports/effectcraft.md) | 66 | 696 | 89% | 123 | Claude, OpenAI Codex / ChatGPT | · |
| [wordcraft](reports/wordcraft.md) | 75 | 356 | 88% | · | Claude, OpenAI Codex / ChatGPT, Cursor, Devin, GitHub Copilot, Unnamed agent | · |
| [artcraft](reports/artcraft.md) | 8 | 6 | <1% | · | Claude | 1 |
| **All** | **723** | **6133** | 66% | **409** | 14 agents | 1 |

A human is counted once per repo here, and once in the **All** row even if they contributed to several repos.

### Disclosed agents

| Agent | Changes | As git author | As co-author | Humans authoring those changes | Repos |
|---|--:|--:|--:|--:|--:|
| Claude | 6003 | 409 | 5594 | 518 | 15 |
| OpenAI Codex / ChatGPT | 158 | · | 158 | 47 | 9 |
| GitHub Copilot | 35 | · | 35 | 4 | 4 |
| opencode | 11 | · | 11 | 4 | 2 |
| Cursor | 6 | · | 6 | 5 | 4 |
| Unnamed agent | 4 | · | 4 | 2 | 2 |
| Codebuff | 3 | · | 3 | 1 | 1 |
| GLM (Z.ai) | 3 | · | 3 | 2 | 1 |
| DeepSeek | 2 | · | 2 | 1 | 1 |
| Devin | 2 | · | 2 | 2 | 2 |
| Kimi | 2 | · | 2 | 1 | 1 |
| Muse Spark (Meta) | 2 | · | 2 | 1 | 1 |
| Qwen | 1 | · | 1 | 1 | 1 |
| Xiaomi MiMo | 1 | · | 1 | 1 | 1 |

"As git author" means the commit's author is the agent itself; "as co-author" means a human is the author and the agent is named in a `Co-authored-by` trailer or a "Generated with" line. A change that discloses two agents counts for both. 100 changes have an agent as git author and no human named at all. The model names seen most often: Claude Opus 5.5 (5592), Claude (451), Codex (113), Claude Sonnet 5.5 (112), Claude Fable 5.1 (72), Claude Opus 4.8 (63), Copilot (33), OpenAI Codex (30).

`csv/contributors.csv` lists every human, agent and bot per repo and across the org.

## How the numbers are produced

**Release ranges.** For each repo the release tags are ordered by version. A release's changes are the commits reachable from its tag but not from any earlier release tag; the first release gets everything before it.

**What counts as one change.** Counting raw commits would overstate repos that merge multi-commit PR branches, and counting only first-parent commits would hide the PRs that land through integration branches. So each release range is split into:

| Landing type | Changes | What it is |
|---|--:|---|
| PR merge | 3295 | a `Merge pull request #N` / `Merge PR #N` merge commit, at any depth of the history (PRs merged into an integration branch count too). The PR's own commits are folded into it. |
| Squash merge | 5096 | a single commit that is the squash of PR #N. |
| Direct commit | 2500 | a non-merge commit pushed straight to the mainline (or brought in by a plain branch merge) with no PR behind it. |
| Batch commit | 125 | a commit made directly on an integration-batch PR branch (follow-up fixes, formatting, conflict clean-up after merging a batch of contributor PRs). |

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
| Title read and labelled by an LLM (Claude Haiku), for titles with no prefix, branch or label signal | 5092 | 46.2% |
| PR branch name (`fix/…`, `feat/…`, `perf/…`, `docs/…`) | 4193 | 38.1% |
| Conventional-commit prefix on the title (`fix(...)`, `feat:`, `perf:` …) | 1508 | 13.7% |
| Keyword rules on the title: version bumps, release prep and reverts, plus any title not yet read by the LLM | 182 | 1.7% |
| Integration-batch PR that only bundles other PRs (counted as Other) | 38 | 0.3% |
| `bug` / `enhancement` label on the PR or the issue it closes | 3 | 0.0% |

## Things to know before quoting these

- **The feature/fix split is partly a judgment call.** Roughly half of the changes have no prefix, branch name or label saying what they are; those were labelled from their title alone by an LLM (Claude Haiku, in 8 batches, plus one batch of 217 titles in a later refresh). The labels were spot-checked against the titles and checked for row alignment; one run of 53 shifted labels was found and repaired. The later batch was read against its titles in full and had no shifts. No human has reviewed them one by one. Titles in these repos often just state the new behaviour ("Layers: the active layer falls back to the top layer when it is removed"), which reads as a fix but could be argued either way. Treat the split as indicative, not exact.
- **Agent figures are a floor.** They count what the history discloses. A change written with an agent but committed without a trailer looks human-only, and squash merges keep trailers only if the person merging left them in.
- **"Human" means "not a recognised agent or bot".** An account that is run by an agent but does not say so, or an agent whose name is not in the table yet, is counted as a human.
- **A few people may be counted twice.** 50 of the 723 humans could not be tied to a GitHub login and are identified by git name only; some of them may be the same person as a login.
- **GitHub labels were of no use.** Only a handful of PRs or linked issues carry `bug`/`enhancement` labels.
- **"fixes #123" is not treated as a bug-fix signal.** It is GitHub's issue-closing keyword and is used on feature PRs too.
- **ArtCraft's first release (`artcraft-v0.0.1`) is not categorised.** It sits on about 13,400 commits of earlier monorepo history going back to 2015. It is counted, not labelled, and is left out of every total above.
- **ArtCraft's history was reset before v0.41.0.** `main` was restarted on 2026-09-11, so v0.41.0 covers only the 11 commits on the new history. ArtCraft's macOS and Windows tags for the same version are treated as one release.
- **Not every version number has a release.** Several repos skip versions (e.g. v0.5.0 → v0.6.2); a row covers everything since the previous published release.
- **PhotoCraft `v0.1.0` and `v0.1.1-rc.4` are the same commit** and are shown as one row.
- **Community vs team PRs** uses GitHub's author association at the time of fetching (member/owner/collaborator = team).

## Files

- `reports/<repo>.md` — one repo's charts, a short plain-English commentary on its trends, and per-release tables: by change type, by how changes landed, and by contributor
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
