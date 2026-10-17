# soundcraft — changes per release

5 releases, 2026-10-08 → 2026-10-14. Each release is counted as the changes that landed between the previous release tag and its own; the first one is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised. The charts cover released changes; the commentary under them is generated from the same numbers.

## Changes by type

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/soundcraft-changes-line.png">
  <img alt="soundcraft: changes per release, stacked by type, as lines" src="../charts/light/soundcraft-changes-line.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/soundcraft-changes-bar.png">
  <img alt="soundcraft: changes per release, stacked by type, as bars" src="../charts/light/soundcraft-changes-bar.png">
</picture>

**What this shows**

- soundcraft has had 5 releases with 243 changes in total, over 6 days.
- The biggest release was v0.7.0 (14 Oct) with 102 changes, which is 42% of everything released so far.
- Releases are getting bigger: the first 2 releases averaged 42 changes each and the last 2 releases averaged 73.
- Overall, fixes make up 45% of changes and features 35%.
- The work has shifted from building new things to fixing: features went from 50% of changes in the first 2 releases to 28% in the last 2 releases, and fixes from 20% to 57%.
- Performance work is 2% of changes (6), most of it in v0.6.1 (12 Oct), which had 3.
- Since the last release, 2 more changes have landed on main and not been released yet: 0 features and 1 fix among them.

| Release | Published | Changes | Feature | Fix | Perf | i18n | Docs | Test | Build/CI | Release | Refactor | Deps | Security | Revert | Other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.3.0](https://github.com/storytold/soundcraft/releases/tag/v0.3.0) | 2026-10-08 | 57 | 33 | 2 | · | · | 7 | 3 | 1 | 6 | 4 | · | · | · | 1 |
| [v0.4.0](https://github.com/storytold/soundcraft/releases/tag/v0.4.0) | 2026-10-10 | 27 | 9 | 15 | · | · | · | · | 2 | 1 | · | · | · | · | · |
| [v0.5.0](https://github.com/storytold/soundcraft/releases/tag/v0.5.0) | 2026-10-11 | 13 | 1 | 10 | · | · | 1 | · | · | 1 | · | · | · | · | · |
| [v0.6.1](https://github.com/storytold/soundcraft/releases/tag/v0.6.1) | 2026-10-12 | 44 | 8 | 24 | 3 | · | 1 | · | 4 | 3 | 1 | · | · | · | · |
| [v0.7.0](https://github.com/storytold/soundcraft/releases/tag/v0.7.0) | 2026-10-14 | 102 | 33 | 59 | 3 | · | 3 | · | · | 1 | · | · | 3 | · | · |
| _unreleased (main)_ | 2026-10-15 | 2 | · | 1 | · | · | · | · | 1 | · | · | · | · | · | · |
| **Released total** |  | **243** | **84** | **110** | **6** | · | **12** | **3** | **7** | **12** | **5** | · | **3** | · | **1** |

Share of released changes: feature 35%, fix 45%, perf 2%, docs 5%, test 1%, build/ci 3%, release 5%, refactor 2%, security 1%.

## How changes landed

**What this shows**

- 76% of changes came in through pull requests; the rest were committed directly.
- That has grown: pull requests were 36% of changes in the first 2 releases and 97% in the last 2 releases.
- Of the 185 pull requests, 94% came from people outside the core team.

| Release | Commits | PR merges | Squash merges | Direct commits | Batch commits | Commits inside PRs | Sync merges | Community PRs | Team PRs |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.3.0](https://github.com/storytold/soundcraft/releases/tag/v0.3.0) | 57 | · | 4 | 53 | · | · | · | · | 4 |
| [v0.4.0](https://github.com/storytold/soundcraft/releases/tag/v0.4.0) | 80 | 25 | 1 | 1 | · | 40 | 13 | 25 | 1 |
| [v0.5.0](https://github.com/storytold/soundcraft/releases/tag/v0.5.0) | 31 | 11 | 2 | · | · | 11 | 7 | 11 | 2 |
| [v0.6.1](https://github.com/storytold/soundcraft/releases/tag/v0.6.1) | 139 | 41 | 1 | 2 | · | 67 | 28 | 39 | 3 |
| [v0.7.0](https://github.com/storytold/soundcraft/releases/tag/v0.7.0) | 375 | 98 | 2 | 2 | · | 189 | 84 | 99 | 1 |
| _unreleased (main)_ | 3 | 1 | 1 | · | · | 1 | · | 2 | · |
| **Released total** | **682** | **175** | **10** | **58** | **0** | **307** | **132** | **174** | **11** |

Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.

## Contributors

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/soundcraft-contributors.png">
  <img alt="soundcraft: unique contributors per release (returning humans, new humans, disclosed agents, bots)" src="../charts/light/soundcraft-contributors.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/soundcraft-agent-disclosure.png">
  <img alt="soundcraft: changes per release by agent disclosure" src="../charts/light/soundcraft-agent-disclosure.png">
</picture>

**What this shows**

- 37 people have contributed to released changes.
- The first release had 2 people and the latest had 23.
- In the latest release, 15 of the 23 people were contributing for the first time.
- The most active person, @echelon, authored 27% of all changes, and the three most active authored 60% between them.
- 57% of changes say an AI agent was involved (139 of 243).
- That share has gone down: 94% in the first 2 releases and 38% in the last 2 releases.
- Claude accounts for all of the changes that name an agent.
- These figures only count changes that say so, so the real share may be higher.

| Release | Humans | New | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|--:|---|--:|
| [v0.3.0](https://github.com/storytold/soundcraft/releases/tag/v0.3.0) | 2 | 2 | 55 | 96% | · | Claude | · |
| [v0.4.0](https://github.com/storytold/soundcraft/releases/tag/v0.4.0) | 13 | 12 | 24 | 89% | · | Claude | · |
| [v0.5.0](https://github.com/storytold/soundcraft/releases/tag/v0.5.0) | 5 | 1 | 4 | 31% | · | Claude | · |
| [v0.6.1](https://github.com/storytold/soundcraft/releases/tag/v0.6.1) | 12 | 7 | 27 | 61% | · | Claude | · |
| [v0.7.0](https://github.com/storytold/soundcraft/releases/tag/v0.7.0) | 23 | 15 | 29 | 28% | · | Claude | · |
| _unreleased (main)_ | 3 | 1 | 1 | 50% | · | Claude | · |
| **Released total** | **37** |  | **139** | 57% | **0** | Claude | · |

Humans are unique people per release, authors and co-authors together; New is how many of them had not appeared in an earlier release of this repo. The total row counts each person once. An agent is disclosed when it is a commit's git author, is named in a `Co-authored-by` trailer, or the message says it was generated with one.

Most active humans in released changes: @echelon (236), @grovebit (53), @marcoarnulfo (26), @vbasky (24), @MarekSpodBiedry (7), t (7), @reoniazx (6), @Silvertree2010 (6), @h-a-n-a-s-h-i (5), @itrycodinganditsbad (5).
