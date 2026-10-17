# lightcraft — changes per release

9 releases, 2026-10-02 → 2026-10-14. Each release is counted as the changes that landed between the previous release tag and its own; the first one is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised. The charts cover released changes; the commentary under them is generated from the same numbers.

## Changes by type

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/lightcraft-changes-line.png">
  <img alt="lightcraft: changes per release, stacked by type, as lines" src="../charts/light/lightcraft-changes-line.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/lightcraft-changes-bar.png">
  <img alt="lightcraft: changes per release, stacked by type, as bars" src="../charts/light/lightcraft-changes-bar.png">
</picture>

**What this shows**

- lightcraft has had 9 releases with 973 changes in total, over 12 days.
- The biggest release was v0.8.0 (14 Oct) with 185 changes, which is 19% of everything released so far.
- Releases are getting bigger: the first 4 releases averaged 75 changes each and the last 4 releases averaged 151.
- Overall, fixes make up 39% of changes and features 31%.
- The work has shifted from building new things to fixing: features went from 49% of changes in the first 4 releases to 24% in the last 4 releases, and fixes from 24% to 48%.
- Performance work is 6% of changes (54), most of it in v0.1.0 (2 Oct), which had 23.
- After features and fixes, the next biggest group is documentation at 6%.
- Since the last release, 226 more changes have landed on main and not been released yet: 58 features and 79 fixes among them.

| Release | Published | Changes | Feature | Fix | Perf | i18n | Docs | Test | Build/CI | Release | Refactor | Deps | Security | Revert | Other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/lightcraft/releases/tag/v0.1.0) | 2026-10-02 | 170 | 99 | 10 | 23 | · | 26 | 3 | 4 | 1 | 3 | · | · | · | 1 |
| [v0.1.1](https://github.com/storytold/lightcraft/releases/tag/v0.1.1) | 2026-10-03 | 48 | 40 | 1 | 4 | · | 2 | · | · | 1 | · | · | · | · | · |
| [v0.2.0](https://github.com/storytold/lightcraft/releases/tag/v0.2.0) | 2026-10-05 | 49 | 7 | 37 | · | · | 1 | · | 2 | 1 | 1 | · | · | · | · |
| [v0.2.1](https://github.com/storytold/lightcraft/releases/tag/v0.2.1) | 2026-10-06 | 33 | 2 | 23 | · | 1 | 2 | · | 3 | 1 | 1 | · | · | · | · |
| [v0.4.0](https://github.com/storytold/lightcraft/releases/tag/v0.4.0) | 2026-10-08 | 68 | 13 | 19 | 4 | 4 | 3 | 9 | 7 | 5 | 3 | · | 1 | · | · |
| [v0.5.0](https://github.com/storytold/lightcraft/releases/tag/v0.5.0) | 2026-10-10 | 171 | 39 | 73 | 5 | 10 | 7 | 5 | 3 | 1 | 7 | · | 1 | · | 20 |
| [v0.6.0](https://github.com/storytold/lightcraft/releases/tag/v0.6.0) | 2026-10-11 | 89 | 29 | 40 | 1 | 3 | 5 | 2 | 2 | 1 | 2 | · | · | · | 4 |
| [v0.7.1](https://github.com/storytold/lightcraft/releases/tag/v0.7.1) | 2026-10-12 | 160 | 49 | 66 | 5 | 5 | 11 | 8 | 1 | 2 | 8 | 1 | · | · | 4 |
| [v0.8.0](https://github.com/storytold/lightcraft/releases/tag/v0.8.0) | 2026-10-14 | 185 | 27 | 112 | 12 | 3 | 4 | 8 | 2 | 1 | 5 | 1 | 6 | 1 | 3 |
| _unreleased (main)_ | 2026-10-15 | 226 | 58 | 79 | 9 | 14 | 9 | 10 | 7 | · | 6 | · | 1 | · | 33 |
| **Released total** |  | **973** | **305** | **381** | **54** | **26** | **61** | **35** | **24** | **14** | **30** | **2** | **8** | **1** | **32** |

Share of released changes: feature 31%, fix 39%, perf 6%, i18n 3%, docs 6%, test 4%, build/ci 2%, release 1%, refactor 3%, security 1%, other 3%.

## How changes landed

**What this shows**

- 65% of changes came in through pull requests; the rest were committed directly.
- That has grown: pull requests were 27% of changes in the first 4 releases and 83% in the last 4 releases.
- Of the 630 pull requests, 81% came from people outside the core team.
- Outside contributions have gone up: 23% of pull requests in the first 4 releases, 91% in the last 4 releases.

| Release | Commits | PR merges | Squash merges | Direct commits | Batch commits | Commits inside PRs | Sync merges | Community PRs | Team PRs |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/lightcraft/releases/tag/v0.1.0) | 206 | · | · | 170 | · | · | 36 | · | · |
| [v0.1.1](https://github.com/storytold/lightcraft/releases/tag/v0.1.1) | 48 | · | · | 48 | · | · | · | · | · |
| [v0.2.0](https://github.com/storytold/lightcraft/releases/tag/v0.2.0) | 121 | 48 | · | 1 | · | 63 | 9 | 15 | 33 |
| [v0.2.1](https://github.com/storytold/lightcraft/releases/tag/v0.2.1) | 113 | 32 | 1 | · | · | 41 | 39 | 4 | 29 |
| [v0.4.0](https://github.com/storytold/lightcraft/releases/tag/v0.4.0) | 169 | 40 | 5 | 23 | · | 79 | 22 | 33 | 12 |
| [v0.5.0](https://github.com/storytold/lightcraft/releases/tag/v0.5.0) | 461 | 132 | · | 1 | 38 | 260 | 30 | 98 | 34 |
| [v0.6.0](https://github.com/storytold/lightcraft/releases/tag/v0.6.0) | 436 | 77 | 3 | 1 | 8 | 326 | 21 | 75 | 5 |
| [v0.7.1](https://github.com/storytold/lightcraft/releases/tag/v0.7.1) | 386 | 121 | · | 2 | 37 | 184 | 42 | 118 | 3 |
| [v0.8.0](https://github.com/storytold/lightcraft/releases/tag/v0.8.0) | 397 | 170 | 1 | 3 | 11 | 200 | 12 | 168 | 3 |
| _unreleased (main)_ | 561 | 193 | 2 | 1 | 30 | 224 | 111 | 190 | 5 |
| **Released total** | **2337** | **620** | **10** | **249** | **94** | **1153** | **211** | **511** | **119** |

Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.

## Contributors

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/lightcraft-contributors.png">
  <img alt="lightcraft: unique contributors per release (returning humans, new humans, disclosed agents, bots)" src="../charts/light/lightcraft-contributors.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/lightcraft-agent-disclosure.png">
  <img alt="lightcraft: changes per release by agent disclosure" src="../charts/light/lightcraft-agent-disclosure.png">
</picture>

**What this shows**

- 142 people have contributed to released changes.
- The first release had 1 person and the latest had 51.
- In the latest release, 29 of the 51 people were contributing for the first time.
- The most active person, @echelon, authored 34% of all changes, and the three most active authored 45% between them.
- 83% of changes say an AI agent was involved (805 of 973).
- That share has gone down: 99% in the first 4 releases and 74% in the last 4 releases.
- Claude accounts for nearly all of the changes that name an agent; 5 other agents are named on 46 changes between them.
- In 264 changes the agent is the commit author itself, not only a co-author.
- These figures only count changes that say so, so the real share may be higher.

| Release | Humans | New | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|--:|---|--:|
| [v0.1.0](https://github.com/storytold/lightcraft/releases/tag/v0.1.0) | 1 | 1 | 168 | 99% | · | Claude | · |
| [v0.1.1](https://github.com/storytold/lightcraft/releases/tag/v0.1.1) | 1 | · | 48 | 100% | · | Claude | · |
| [v0.2.0](https://github.com/storytold/lightcraft/releases/tag/v0.2.0) | 4 | 3 | 49 | 100% | · | Claude | · |
| [v0.2.1](https://github.com/storytold/lightcraft/releases/tag/v0.2.1) | 4 | 2 | 33 | 100% | · | Claude, OpenAI Codex / ChatGPT | · |
| [v0.4.0](https://github.com/storytold/lightcraft/releases/tag/v0.4.0) | 27 | 25 | 59 | 87% | 1 | Claude, OpenAI Codex / ChatGPT, opencode, GitHub Copilot, DeepSeek | · |
| [v0.5.0](https://github.com/storytold/lightcraft/releases/tag/v0.5.0) | 42 | 32 | 140 | 82% | 109 | Claude, OpenAI Codex / ChatGPT, opencode | · |
| [v0.6.0](https://github.com/storytold/lightcraft/releases/tag/v0.6.0) | 30 | 18 | 70 | 79% | 1 | Claude, OpenAI Codex / ChatGPT | · |
| [v0.7.1](https://github.com/storytold/lightcraft/releases/tag/v0.7.1) | 48 | 32 | 154 | 96% | 152 | Claude, OpenAI Codex / ChatGPT, DeepSeek | · |
| [v0.8.0](https://github.com/storytold/lightcraft/releases/tag/v0.8.0) | 51 | 29 | 84 | 45% | 1 | Claude, OpenAI Codex / ChatGPT, GLM (Z.ai), DeepSeek | · |
| _unreleased (main)_ | 59 | 29 | 119 | 53% | 5 | Claude, OpenAI Codex / ChatGPT, Cursor, GitHub Copilot | · |
| **Released total** | **142** |  | **805** | 83% | **264** | Claude, OpenAI Codex / ChatGPT, DeepSeek, opencode, GitHub Copilot, GLM (Z.ai) | · |

Humans are unique people per release, authors and co-authors together; New is how many of them had not appeared in an earlier release of this repo. The total row counts each person once. An agent is disclosed when it is a commit's git author, is named in a `Co-authored-by` trailer, or the message says it was generated with one.

Most active humans in released changes: @echelon (578), @bflatastic (125), @radialmonster (71), @emmertex (26), @bitshiftza (23), @nledford (23), @AlexChambers (21), @MarekSpodBiedry (21), @endthestart (20), @marcoarnulfo (19).
