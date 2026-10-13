# vectorcraft — changes per release

12 releases, 2026-10-02 → 2026-10-12. Each release is counted as the changes that landed between the previous release tag and its own; the first one is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised. The charts cover released changes; the commentary under them is generated from the same numbers.

## Changes by type

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/vectorcraft-changes-line.png">
  <img alt="vectorcraft: changes per release, stacked by type, as lines" src="../charts/light/vectorcraft-changes-line.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/vectorcraft-changes-bar.png">
  <img alt="vectorcraft: changes per release, stacked by type, as bars" src="../charts/light/vectorcraft-changes-bar.png">
</picture>

**What this shows**

- vectorcraft has had 12 releases with 885 changes in total, over 10 days.
- The biggest release was v0.10.0 (12 Oct) with 191 changes, which is 22% of everything released so far.
- Releases are getting bigger: the first 6 releases averaged 49 changes each and the last 6 releases averaged 98.
- Overall, fixes make up 49% of changes and features 33%.
- The work has shifted from building new things to fixing: features went from 49% of changes in the first 6 releases to 25% in the last 6 releases, and fixes from 28% to 59%.
- Performance work is 2% of changes (18), most of it in v0.1.0 (2 Oct), which had 7.
- Since the last release, 139 more changes have landed on main and not been released yet: 29 features and 90 fixes among them.

| Release | Published | Changes | Feature | Fix | Perf | i18n | Docs | Test | Build/CI | Release | Refactor | Deps | Security | Revert | Other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/vectorcraft/releases/tag/v0.1.0) | 2026-10-02 | 85 | 47 | 6 | 7 | · | 11 | · | 4 | · | 3 | · | · | · | 7 |
| [v0.1.1](https://github.com/storytold/vectorcraft/releases/tag/v0.1.1) | 2026-10-03 | 1 | · | · | · | · | · | · | · | 1 | · | · | · | · | · |
| [v0.2.0](https://github.com/storytold/vectorcraft/releases/tag/v0.2.0) | 2026-10-05 | 78 | 58 | 7 | · | · | 6 | 4 | · | 1 | 1 | · | 1 | · | · |
| [v0.3.0](https://github.com/storytold/vectorcraft/releases/tag/v0.3.0) | 2026-10-06 | 51 | 19 | 26 | · | · | 2 | 1 | 2 | 1 | · | · | · | · | · |
| [v0.3.1](https://github.com/storytold/vectorcraft/releases/tag/v0.3.1) | 2026-10-06 | 29 | 18 | 8 | · | · | · | 1 | 1 | 1 | · | · | · | · | · |
| [v0.4.0](https://github.com/storytold/vectorcraft/releases/tag/v0.4.0) | 2026-10-07 | 51 | 4 | 35 | · | 4 | 2 | 2 | 3 | 1 | · | · | · | · | · |
| [v0.5.0](https://github.com/storytold/vectorcraft/releases/tag/v0.5.0) | 2026-10-08 | 126 | 24 | 80 | 3 | 6 | 4 | 1 | 1 | 3 | 3 | · | · | 1 | · |
| [v0.6.0](https://github.com/storytold/vectorcraft/releases/tag/v0.6.0) | 2026-10-08 | 12 | 4 | 4 | · | · | 1 | · | 1 | 2 | · | · | · | · | · |
| [v0.7.0](https://github.com/storytold/vectorcraft/releases/tag/v0.7.0) | 2026-10-08 | 15 | 1 | 7 | 1 | 1 | 1 | 1 | · | 1 | · | · | · | · | 2 |
| [v0.8.0](https://github.com/storytold/vectorcraft/releases/tag/v0.8.0) | 2026-10-10 | 131 | 37 | 69 | 2 | 12 | 2 | 5 | 1 | 1 | 2 | · | · | · | · |
| [v0.9.0](https://github.com/storytold/vectorcraft/releases/tag/v0.9.0) | 2026-10-11 | 115 | 25 | 83 | · | 1 | 5 | · | · | 1 | · | · | · | · | · |
| [v0.10.0](https://github.com/storytold/vectorcraft/releases/tag/v0.10.0) | 2026-10-12 | 191 | 56 | 106 | 5 | 6 | 6 | 6 | 2 | 2 | 1 | · | 1 | · | · |
| _unreleased (main)_ | 2026-10-13 | 139 | 29 | 90 | 4 | 5 | 10 | 1 | · | · | · | · | · | · | · |
| **Released total** |  | **885** | **293** | **431** | **18** | **30** | **40** | **21** | **15** | **15** | **10** | · | **2** | **1** | **9** |

Share of released changes: feature 33%, fix 49%, perf 2%, i18n 3%, docs 5%, test 2%, build/ci 2%, release 2%, refactor 1%, other 1%.

## How changes landed

**What this shows**

- 83% of changes came in through pull requests; the rest were committed directly.
- Of the 737 pull requests, 44% came from people outside the core team.
- Outside contributions have gone up: 20% of pull requests in the first 6 releases, 53% in the last 6 releases.

| Release | Commits | PR merges | Squash merges | Direct commits | Batch commits | Commits inside PRs | Sync merges | Community PRs | Team PRs |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/vectorcraft/releases/tag/v0.1.0) | 89 | 1 | · | 84 | · | 4 | · | · | 1 |
| [v0.1.1](https://github.com/storytold/vectorcraft/releases/tag/v0.1.1) | 1 | · | · | 1 | · | · | · | · | · |
| [v0.2.0](https://github.com/storytold/vectorcraft/releases/tag/v0.2.0) | 309 | 77 | · | 1 | · | 213 | 18 | 7 | 70 |
| [v0.3.0](https://github.com/storytold/vectorcraft/releases/tag/v0.3.0) | 117 | 50 | 1 | · | · | 66 | · | 2 | 49 |
| [v0.3.1](https://github.com/storytold/vectorcraft/releases/tag/v0.3.1) | 85 | 29 | · | · | · | 55 | 1 | 4 | 25 |
| [v0.4.0](https://github.com/storytold/vectorcraft/releases/tag/v0.4.0) | 116 | 51 | · | · | · | 60 | 5 | 29 | 22 |
| [v0.5.0](https://github.com/storytold/vectorcraft/releases/tag/v0.5.0) | 301 | 111 | 2 | 13 | · | 173 | 2 | 59 | 54 |
| [v0.6.0](https://github.com/storytold/vectorcraft/releases/tag/v0.6.0) | 24 | 9 | 2 | 1 | · | 12 | · | 4 | 7 |
| [v0.7.0](https://github.com/storytold/vectorcraft/releases/tag/v0.7.0) | 56 | 15 | · | · | · | 31 | 10 | 1 | 14 |
| [v0.8.0](https://github.com/storytold/vectorcraft/releases/tag/v0.8.0) | 355 | 84 | · | 47 | · | 142 | 82 | 35 | 49 |
| [v0.9.0](https://github.com/storytold/vectorcraft/releases/tag/v0.9.0) | 324 | 112 | 3 | · | · | 208 | 1 | 44 | 71 |
| [v0.10.0](https://github.com/storytold/vectorcraft/releases/tag/v0.10.0) | 480 | 190 | · | 1 | · | 287 | 2 | 139 | 51 |
| _unreleased (main)_ | 310 | 139 | · | · | · | 170 | 1 | 74 | 65 |
| **Released total** | **2257** | **729** | **8** | **148** | **0** | **1251** | **121** | **324** | **413** |

Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.

## Contributors

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/vectorcraft-contributors.png">
  <img alt="vectorcraft: unique contributors per release (returning humans, new humans, disclosed agents, bots)" src="../charts/light/vectorcraft-contributors.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/vectorcraft-agent-disclosure.png">
  <img alt="vectorcraft: changes per release by agent disclosure" src="../charts/light/vectorcraft-agent-disclosure.png">
</picture>

**What this shows**

- 102 people have contributed to released changes.
- The first release had 2 people and the latest had 44.
- In the latest release, 29 of the 44 people were contributing for the first time.
- The most active person, @bflatastic, authored 48% of all changes, and the three most active authored 67% between them.
- 85% of changes say an AI agent was involved (751 of 885).
- That share has gone down: 96% in the first 6 releases and 79% in the last 6 releases.
- Claude accounts for nearly all of the changes that name an agent; 2 other agents are named on 7 changes between them.
- In 1 change the agent is the commit author itself, not only a co-author.
- These figures only count changes that say so, so the real share may be higher.

| Release | Humans | New | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|--:|---|--:|
| [v0.1.0](https://github.com/storytold/vectorcraft/releases/tag/v0.1.0) | 2 | 2 | 76 | 89% | · | Claude | · |
| [v0.1.1](https://github.com/storytold/vectorcraft/releases/tag/v0.1.1) | 1 | · | 1 | 100% | · | Claude | · |
| [v0.2.0](https://github.com/storytold/vectorcraft/releases/tag/v0.2.0) | 3 | 1 | 76 | 97% | · | Claude | · |
| [v0.3.0](https://github.com/storytold/vectorcraft/releases/tag/v0.3.0) | 3 | 1 | 51 | 100% | · | Claude | · |
| [v0.3.1](https://github.com/storytold/vectorcraft/releases/tag/v0.3.1) | 4 | 1 | 29 | 100% | · | Claude | · |
| [v0.4.0](https://github.com/storytold/vectorcraft/releases/tag/v0.4.0) | 11 | 8 | 49 | 96% | · | Claude | · |
| [v0.5.0](https://github.com/storytold/vectorcraft/releases/tag/v0.5.0) | 27 | 20 | 121 | 96% | · | Claude | · |
| [v0.6.0](https://github.com/storytold/vectorcraft/releases/tag/v0.6.0) | 5 | 1 | 12 | 100% | · | Claude | · |
| [v0.7.0](https://github.com/storytold/vectorcraft/releases/tag/v0.7.0) | 7 | 4 | 15 | 100% | · | Claude | · |
| [v0.8.0](https://github.com/storytold/vectorcraft/releases/tag/v0.8.0) | 28 | 21 | 109 | 83% | 1 | Claude, OpenAI Codex / ChatGPT, Cursor | · |
| [v0.9.0](https://github.com/storytold/vectorcraft/releases/tag/v0.9.0) | 24 | 14 | 109 | 95% | · | Claude | · |
| [v0.10.0](https://github.com/storytold/vectorcraft/releases/tag/v0.10.0) | 44 | 29 | 103 | 54% | · | Claude, OpenAI Codex / ChatGPT | · |
| _unreleased (main)_ | 26 | 12 | 9 | 6% | · | Claude | · |
| **Released total** | **102** |  | **751** | 85% | **1** | Claude, OpenAI Codex / ChatGPT, Cursor | · |

Humans are unique people per release, authors and co-authors together; New is how many of them had not appeared in an earlier release of this repo. The total row counts each person once. An agent is disclosed when it is a commit's git author, is named in a `Co-authored-by` trailer, or the message says it was generated with one.

Most active humans in released changes: @bflatastic (712), @echelon (153), @dotCooCoo (47), @theironchef (39), @imachus (23), @Ni-zav (21), @haranishi (20), @IHAGI-c (12), @Haven-King (9), @p0lyg0n (8).
