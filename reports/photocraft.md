# photocraft — changes per release

9 releases, 2026-10-02 → 2026-10-12. Each release is counted as the changes that landed between the previous release tag and its own; the first one is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised. The charts cover released changes; the commentary under them is generated from the same numbers.

## Changes by type

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/photocraft-changes-line.png">
  <img alt="photocraft: changes per release, stacked by type, as lines" src="../charts/light/photocraft-changes-line.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/photocraft-changes-bar.png">
  <img alt="photocraft: changes per release, stacked by type, as bars" src="../charts/light/photocraft-changes-bar.png">
</picture>

**What this shows**

- photocraft has had 9 releases with 1,699 changes in total, over 10 days.
- The biggest release was v0.6.0 (10 Oct) with 521 changes, which is 31% of everything released so far.
- Releases are getting bigger: the first 4 releases averaged 31 changes each and the last 4 releases averaged 347.
- Overall, fixes make up 62% of changes and features 21%.
- The work has shifted from building new things to fixing: features went from 35% of changes in the first 4 releases to 20% in the last 4 releases, and fixes from 26% to 64%.
- Performance work is 5% of changes (84), most of it in v0.8.2 (12 Oct), which had 26.
- Since the last release, 259 more changes have landed on main and not been released yet: 48 features and 178 fixes among them.

| Release | Published | Changes | Feature | Fix | Perf | i18n | Docs | Test | Build/CI | Release | Refactor | Deps | Security | Revert | Other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0, v0.1.1-rc.4](https://github.com/storytold/photocraft/releases/tag/v0.1.0) | 2026-10-02 | 14 | · | · | · | · | · | · | 3 | 2 | · | · | · | · | 9 |
| [v0.1.1-rc.5](https://github.com/storytold/photocraft/releases/tag/v0.1.1-rc.5) | 2026-10-02 | 18 | 6 | · | 1 | · | 8 | · | 2 | · | · | · | · | · | 1 |
| [v0.1.1](https://github.com/storytold/photocraft/releases/tag/v0.1.1) | 2026-10-03 | 29 | 17 | 1 | 6 | · | 2 | · | 1 | 1 | 1 | · | · | · | · |
| [v0.2.0](https://github.com/storytold/photocraft/releases/tag/v0.2.0) | 2026-10-05 | 64 | 21 | 31 | 2 | · | 3 | 3 | 1 | 1 | · | · | 2 | · | · |
| [v0.3.0](https://github.com/storytold/photocraft/releases/tag/v0.3.0) | 2026-10-07 | 187 | 35 | 119 | 12 | 4 | 7 | · | 7 | 1 | 1 | · | 1 | · | · |
| [v0.5.0](https://github.com/storytold/photocraft/releases/tag/v0.5.0) | 2026-10-08 | 205 | 53 | 116 | 7 | 8 | 6 | 1 | 4 | 5 | 4 | · | 1 | · | · |
| [v0.6.0](https://github.com/storytold/photocraft/releases/tag/v0.6.0) | 2026-10-10 | 521 | 106 | 322 | 25 | 17 | 17 | 13 | 7 | 1 | 10 | · | 3 | · | · |
| [v0.7.0](https://github.com/storytold/photocraft/releases/tag/v0.7.0) | 2026-10-11 | 244 | 42 | 184 | 5 | 3 | 6 | 3 | · | 1 | · | · | · | · | · |
| [v0.8.2](https://github.com/storytold/photocraft/releases/tag/v0.8.2) | 2026-10-12 | 417 | 80 | 272 | 26 | 9 | 4 | 11 | 5 | 4 | 2 | 1 | 3 | · | · |
| _unreleased (main)_ | 2026-10-13 | 259 | 48 | 178 | 19 | 8 | 2 | 3 | · | · | 1 | · | · | · | · |
| **Released total** |  | **1699** | **360** | **1045** | **84** | **41** | **53** | **31** | **30** | **16** | **18** | **1** | **10** | · | **10** |

Share of released changes: feature 21%, fix 62%, perf 5%, i18n 2%, docs 3%, test 2%, build/ci 2%, release 1%, refactor 1%, security 1%, other 1%.

## How changes landed

**What this shows**

- 94% of changes came in through pull requests; the rest were committed directly.
- That has grown: pull requests were 42% of changes in the first 4 releases and 98% in the last 4 releases.
- Of the 1,592 pull requests, 80% came from people outside the core team.
- Outside contributions have gone up: 33% of pull requests in the first 4 releases, 88% in the last 4 releases.

| Release | Commits | PR merges | Squash merges | Direct commits | Batch commits | Commits inside PRs | Sync merges | Community PRs | Team PRs |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0, v0.1.1-rc.4](https://github.com/storytold/photocraft/releases/tag/v0.1.0) | 14 | · | · | 14 | · | · | · | · | · |
| [v0.1.1-rc.5](https://github.com/storytold/photocraft/releases/tag/v0.1.1-rc.5) | 18 | · | · | 18 | · | · | · | · | · |
| [v0.1.1](https://github.com/storytold/photocraft/releases/tag/v0.1.1) | 29 | · | · | 29 | · | · | · | · | · |
| [v0.2.0](https://github.com/storytold/photocraft/releases/tag/v0.2.0) | 70 | 2 | 50 | 12 | · | 6 | · | 17 | 35 |
| [v0.3.0](https://github.com/storytold/photocraft/releases/tag/v0.3.0) | 187 | · | 187 | · | · | · | · | 77 | 110 |
| [v0.5.0](https://github.com/storytold/photocraft/releases/tag/v0.5.0) | 205 | · | 200 | 5 | · | · | · | 145 | 55 |
| [v0.6.0](https://github.com/storytold/photocraft/releases/tag/v0.6.0) | 566 | 7 | 489 | 25 | · | 30 | 15 | 406 | 90 |
| [v0.7.0](https://github.com/storytold/photocraft/releases/tag/v0.7.0) | 244 | · | 244 | · | · | · | · | 235 | 9 |
| [v0.8.2](https://github.com/storytold/photocraft/releases/tag/v0.8.2) | 422 | 1 | 412 | 4 | · | 2 | 3 | 399 | 14 |
| _unreleased (main)_ | 286 | 1 | 258 | · | · | 22 | 5 | 255 | 4 |
| **Released total** | **1755** | **10** | **1582** | **107** | **0** | **38** | **18** | **1279** | **313** |

Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.

## Contributors

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/photocraft-contributors.png">
  <img alt="photocraft: unique contributors per release (returning humans, new humans, disclosed agents, bots)" src="../charts/light/photocraft-contributors.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/photocraft-agent-disclosure.png">
  <img alt="photocraft: changes per release by agent disclosure" src="../charts/light/photocraft-agent-disclosure.png">
</picture>

**What this shows**

- 255 people have contributed to released changes.
- The first release had 1 person and the latest had 108; the most in one release was 120, in v0.6.0 (10 Oct).
- In the latest release, 55 of the 108 people were contributing for the first time.
- The most active person, @echelon, authored 15% of all changes, and the three most active authored 30% between them.
- 68% of changes say an AI agent was involved (1,149 of 1,699).
- That share has gone down: 85% in the first 4 releases and 70% in the last 4 releases.
- Claude accounts for nearly all of the changes that name an agent; 6 other agents are named on 46 changes between them.
- In 20 changes the agent is the commit author itself, not only a co-author.
- These figures only count changes that say so, so the real share may be higher.

| Release | Humans | New | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|--:|---|--:|
| [v0.1.0, v0.1.1-rc.4](https://github.com/storytold/photocraft/releases/tag/v0.1.0) | 1 | 1 | 4 | 29% | · | Claude | · |
| [v0.1.1-rc.5](https://github.com/storytold/photocraft/releases/tag/v0.1.1-rc.5) | 1 | · | 13 | 72% | · | Claude | · |
| [v0.1.1](https://github.com/storytold/photocraft/releases/tag/v0.1.1) | 1 | · | 29 | 100% | · | Claude | · |
| [v0.2.0](https://github.com/storytold/photocraft/releases/tag/v0.2.0) | 6 | 5 | 60 | 94% | · | Claude | · |
| [v0.3.0](https://github.com/storytold/photocraft/releases/tag/v0.3.0) | 35 | 30 | 72 | 39% | · | Claude, GitHub Copilot, Devin | · |
| [v0.5.0](https://github.com/storytold/photocraft/releases/tag/v0.5.0) | 51 | 36 | 154 | 75% | · | Claude, GitHub Copilot, Qwen | · |
| [v0.6.0](https://github.com/storytold/photocraft/releases/tag/v0.6.0) | 120 | 93 | 371 | 71% | 19 | Claude, OpenAI Codex / ChatGPT, Cursor, GitHub Copilot | · |
| [v0.7.0](https://github.com/storytold/photocraft/releases/tag/v0.7.0) | 75 | 35 | 149 | 61% | · | Claude | · |
| [v0.8.2](https://github.com/storytold/photocraft/releases/tag/v0.8.2) | 108 | 55 | 297 | 71% | 1 | Claude, OpenAI Codex / ChatGPT, Unnamed agent, Cursor | · |
| _unreleased (main)_ | 74 | 30 | 162 | 63% | · | Claude, OpenAI Codex / ChatGPT | · |
| **Released total** | **255** |  | **1149** | 68% | **20** | Claude, GitHub Copilot, OpenAI Codex / ChatGPT, Unnamed agent, Cursor, Devin, Qwen | · |

Humans are unique people per release, authors and co-authors together; New is how many of them had not appeared in an earlier release of this repo. The total row counts each person once. An agent is disclosed when it is a commit's git author, is named in a `Co-authored-by` trailer, or the message says it was generated with one.

Most active humans in released changes: @echelon (680), @vangel76 (131), @bflatastic (118), @Ni-zav (105), @davidmann4 (67), @Elvis33LE (42), @MarekSpodBiedry (40), @kayrockscreenprinting (39), @itrycodinganditsbad (33), @agorevski (32).
