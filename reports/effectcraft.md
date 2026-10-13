# effectcraft — changes per release

10 releases, 2026-10-02 → 2026-10-12. Each release is counted as the changes that landed between the previous release tag and its own; the first one is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised. The charts cover released changes; the commentary under them is generated from the same numbers.

## Changes by type

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/effectcraft-changes-line.png">
  <img alt="effectcraft: changes per release, stacked by type, as lines" src="../charts/light/effectcraft-changes-line.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/effectcraft-changes-bar.png">
  <img alt="effectcraft: changes per release, stacked by type, as bars" src="../charts/light/effectcraft-changes-bar.png">
</picture>

**What this shows**

- effectcraft has had 10 releases with 779 changes in total, over 10 days.
- The biggest release was v0.9.2 (12 Oct) with 140 changes, which is 18% of everything released so far.
- Release size has stayed fairly steady: the first 5 releases averaged 75 changes each and the last 5 releases averaged 81.
- Overall, fixes make up 35% of changes and features 34%.
- The work has shifted from building new things to fixing: features went from 53% of changes in the first 5 releases to 17% in the last 5 releases, and fixes from 13% to 56%.
- Performance work is 6% of changes (48), most of it in v0.2.0 (5 Oct), which had 21.
- After features and fixes, the next biggest group is documentation at 8%.

| Release | Published | Changes | Feature | Fix | Perf | i18n | Docs | Test | Build/CI | Release | Refactor | Deps | Security | Revert | Other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/effectcraft/releases/tag/v0.1.0) | 2026-10-02 | 89 | 65 | 3 | 2 | · | 10 | 1 | 3 | 1 | 2 | 1 | · | · | 1 |
| [v0.1.1](https://github.com/storytold/effectcraft/releases/tag/v0.1.1) | 2026-10-03 | 135 | 87 | 2 | 19 | · | 15 | 4 | 1 | 1 | 6 | · | · | · | · |
| [v0.2.0](https://github.com/storytold/effectcraft/releases/tag/v0.2.0) | 2026-10-05 | 123 | 37 | 32 | 21 | · | 16 | 11 | 2 | 1 | 1 | · | 2 | · | · |
| [v0.3.0](https://github.com/storytold/effectcraft/releases/tag/v0.3.0) | 2026-10-06 | 22 | 7 | 8 | 1 | · | 3 | · | 1 | 2 | · | · | · | · | · |
| [v0.3.1](https://github.com/storytold/effectcraft/releases/tag/v0.3.1) | 2026-10-06 | 6 | 2 | 2 | · | · | · | · | 1 | 1 | · | · | · | · | · |
| [v0.4.0](https://github.com/storytold/effectcraft/releases/tag/v0.4.0) | 2026-10-07 | 38 | 7 | 17 | · | · | 6 | · | 3 | 1 | 2 | · | · | · | 2 |
| [v0.6.0](https://github.com/storytold/effectcraft/releases/tag/v0.6.0) | 2026-10-08 | 36 | 3 | 22 | · | 1 | 4 | · | · | 5 | 1 | · | · | · | · |
| [v0.7.0](https://github.com/storytold/effectcraft/releases/tag/v0.7.0) | 2026-10-10 | 66 | 4 | 42 | · | 9 | 5 | 2 | 2 | 1 | · | · | · | 1 | · |
| [v0.8.0](https://github.com/storytold/effectcraft/releases/tag/v0.8.0) | 2026-10-11 | 124 | 16 | 74 | 4 | 9 | 2 | 5 | 2 | 1 | 4 | 1 | · | · | 6 |
| [v0.9.2](https://github.com/storytold/effectcraft/releases/tag/v0.9.2) | 2026-10-12 | 140 | 40 | 73 | 1 | 6 | 2 | 6 | 2 | 4 | 3 | · | 3 | · | · |
| **Released total** |  | **779** | **268** | **275** | **48** | **25** | **63** | **29** | **17** | **18** | **19** | **2** | **5** | **1** | **9** |

Share of released changes: feature 34%, fix 35%, perf 6%, i18n 3%, docs 8%, test 4%, build/ci 2%, release 2%, refactor 2%, security 1%, other 1%.

## How changes landed

**What this shows**

- 52% of changes came in through pull requests; the rest were committed directly.
- That has grown: pull requests were 19% of changes in the first 5 releases and 82% in the last 5 releases.
- Of the 404 pull requests, 61% came from people outside the core team.
- Outside contributions have gone up: 11% of pull requests in the first 5 releases, 71% in the last 5 releases.

| Release | Commits | PR merges | Squash merges | Direct commits | Batch commits | Commits inside PRs | Sync merges | Community PRs | Team PRs |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/effectcraft/releases/tag/v0.1.0) | 119 | · | · | 89 | · | · | 30 | · | · |
| [v0.1.1](https://github.com/storytold/effectcraft/releases/tag/v0.1.1) | 217 | · | · | 135 | · | · | 82 | · | · |
| [v0.2.0](https://github.com/storytold/effectcraft/releases/tag/v0.2.0) | 250 | 44 | · | 79 | · | 81 | 46 | 5 | 39 |
| [v0.3.0](https://github.com/storytold/effectcraft/releases/tag/v0.3.0) | 45 | 20 | 1 | 1 | · | 22 | 1 | · | 21 |
| [v0.3.1](https://github.com/storytold/effectcraft/releases/tag/v0.3.1) | 13 | 6 | · | · | · | 6 | 1 | 3 | 3 |
| [v0.4.0](https://github.com/storytold/effectcraft/releases/tag/v0.4.0) | 96 | 31 | · | 7 | · | 56 | 2 | 8 | 23 |
| [v0.6.0](https://github.com/storytold/effectcraft/releases/tag/v0.6.0) | 92 | 28 | 4 | 4 | · | 56 | · | 1 | 31 |
| [v0.7.0](https://github.com/storytold/effectcraft/releases/tag/v0.7.0) | 170 | 52 | · | 14 | · | 102 | 2 | 28 | 24 |
| [v0.8.0](https://github.com/storytold/effectcraft/releases/tag/v0.8.0) | 300 | 93 | 2 | · | 29 | 166 | 10 | 82 | 13 |
| [v0.9.2](https://github.com/storytold/effectcraft/releases/tag/v0.9.2) | 284 | 122 | 1 | 17 | · | 141 | 3 | 119 | 4 |
| **Released total** | **1586** | **396** | **8** | **346** | **29** | **630** | **177** | **246** | **158** |

Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.

## Contributors

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/effectcraft-contributors.png">
  <img alt="effectcraft: unique contributors per release (returning humans, new humans, disclosed agents, bots)" src="../charts/light/effectcraft-contributors.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/effectcraft-agent-disclosure.png">
  <img alt="effectcraft: changes per release by agent disclosure" src="../charts/light/effectcraft-agent-disclosure.png">
</picture>

**What this shows**

- 66 people have contributed to released changes.
- The first release had 1 person and the latest had 27; the most in one release was 33, in v0.8.0 (11 Oct).
- In the latest release, 13 of the 27 people were contributing for the first time.
- The most active person, @echelon, authored 49% of all changes, and the three most active authored 70% between them.
- 89% of changes say an AI agent was involved (696 of 779).
- That share has gone down: 98% in the first 5 releases and 81% in the last 5 releases.
- Claude accounts for nearly all of the changes that name an agent; 1 other agent is named on 14 changes between them.
- In 123 changes the agent is the commit author itself, not only a co-author.
- These figures only count changes that say so, so the real share may be higher.

| Release | Humans | New | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|--:|---|--:|
| [v0.1.0](https://github.com/storytold/effectcraft/releases/tag/v0.1.0) | 1 | 1 | 88 | 99% | · | Claude | · |
| [v0.1.1](https://github.com/storytold/effectcraft/releases/tag/v0.1.1) | 1 | · | 135 | 100% | · | Claude | · |
| [v0.2.0](https://github.com/storytold/effectcraft/releases/tag/v0.2.0) | 3 | 2 | 119 | 97% | · | Claude | · |
| [v0.3.0](https://github.com/storytold/effectcraft/releases/tag/v0.3.0) | 2 | · | 22 | 100% | · | Claude | · |
| [v0.3.1](https://github.com/storytold/effectcraft/releases/tag/v0.3.1) | 5 | 3 | 3 | 50% | · | Claude | · |
| [v0.4.0](https://github.com/storytold/effectcraft/releases/tag/v0.4.0) | 9 | 5 | 32 | 84% | 2 | Claude, OpenAI Codex / ChatGPT | · |
| [v0.6.0](https://github.com/storytold/effectcraft/releases/tag/v0.6.0) | 4 | 2 | 35 | 97% | 6 | Claude | · |
| [v0.7.0](https://github.com/storytold/effectcraft/releases/tag/v0.7.0) | 21 | 15 | 52 | 79% | · | Claude, OpenAI Codex / ChatGPT | · |
| [v0.8.0](https://github.com/storytold/effectcraft/releases/tag/v0.8.0) | 33 | 25 | 117 | 94% | 115 | Claude, OpenAI Codex / ChatGPT | · |
| [v0.9.2](https://github.com/storytold/effectcraft/releases/tag/v0.9.2) | 27 | 13 | 93 | 66% | · | Claude | · |
| **Released total** | **66** |  | **696** | 89% | **123** | Claude, OpenAI Codex / ChatGPT | · |

Humans are unique people per release, authors and co-authors together; New is how many of them had not appeared in an earlier release of this repo. The total row counts each person once. An agent is disclosed when it is a commit's git author, is named in a `Co-authored-by` trailer, or the message says it was generated with one.

Most active humans in released changes: @echelon (532), @bflatastic (135), @vangel76 (46), @Ni-zav (25), @MarekSpodBiedry (23), @pravdomil (15), @vbasky (13), @sanyamsingh001 (10), @tylerjenningsw (9), @storybored379 (8).
