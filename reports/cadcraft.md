# cadcraft — changes per release

5 releases, 2026-10-08 → 2026-10-12. Each release is counted as the changes that landed between the previous release tag and its own; the first one is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised. The charts cover released changes; the commentary under them is generated from the same numbers.

## Changes by type

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/cadcraft-changes-line.png">
  <img alt="cadcraft: changes per release, stacked by type, as lines" src="../charts/light/cadcraft-changes-line.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/cadcraft-changes-bar.png">
  <img alt="cadcraft: changes per release, stacked by type, as bars" src="../charts/light/cadcraft-changes-bar.png">
</picture>

**What this shows**

- cadcraft has had 5 releases with 371 changes in total, over 4 days.
- The biggest release was v0.5.0 (11 Oct) with 188 changes, which is 51% of everything released so far.
- Releases are getting bigger: the first 2 releases averaged 12 changes each and the last 2 releases averaged 172.
- Overall, fixes make up 58% of changes and features 30%.
- The work has shifted from building new things to fixing: features went from 48% of changes in the first 2 releases to 29% in the last 2 releases, and fixes from 0% to 62%.
- Performance work is rare: 6 changes.
- Since the last release, 109 more changes have landed on main and not been released yet: 25 features and 64 fixes among them.

| Release | Published | Changes | Feature | Fix | Perf | i18n | Docs | Test | Build/CI | Release | Refactor | Deps | Security | Revert | Other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/cadcraft/releases/tag/v0.1.0) | 2026-10-08 | 21 | 12 | · | 1 | · | 1 | · | · | 4 | 1 | · | · | · | 2 |
| [v0.3.0](https://github.com/storytold/cadcraft/releases/tag/v0.3.0) | 2026-10-08 | 4 | · | · | · | · | 1 | · | · | 3 | · | · | · | · | · |
| [v0.4.0](https://github.com/storytold/cadcraft/releases/tag/v0.4.0) | 2026-10-10 | 2 | · | · | · | · | · | · | 1 | 1 | · | · | · | · | · |
| [v0.5.0](https://github.com/storytold/cadcraft/releases/tag/v0.5.0) | 2026-10-11 | 188 | 18 | 160 | · | 1 | 2 | 3 | · | 1 | 3 | · | · | · | · |
| [v0.6.2](https://github.com/storytold/cadcraft/releases/tag/v0.6.2) | 2026-10-12 | 156 | 83 | 55 | 5 | 7 | 1 | · | 1 | 4 | · | · | · | · | · |
| _unreleased (main)_ | 2026-10-13 | 109 | 25 | 64 | 3 | 5 | 6 | 3 | · | · | 3 | · | · | · | · |
| **Released total** |  | **371** | **113** | **215** | **6** | **8** | **5** | **3** | **2** | **13** | **4** | · | · | · | **2** |

Share of released changes: feature 30%, fix 58%, perf 2%, i18n 2%, docs 1%, test 1%, build/ci 1%, release 4%, refactor 1%, other 1%.

## How changes landed

**What this shows**

- 91% of changes came in through pull requests; the rest were committed directly.
- That has grown: pull requests were 16% of changes in the first 2 releases and 97% in the last 2 releases.
- Of the 338 pull requests, 98% came from people outside the core team.
- Outside contributions have gone up: 0% of pull requests in the first 2 releases, 99% in the last 2 releases.

| Release | Commits | PR merges | Squash merges | Direct commits | Batch commits | Commits inside PRs | Sync merges | Community PRs | Team PRs |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/cadcraft/releases/tag/v0.1.0) | 23 | · | 2 | 19 | · | · | 2 | · | 2 |
| [v0.3.0](https://github.com/storytold/cadcraft/releases/tag/v0.3.0) | 4 | · | 2 | 2 | · | · | · | · | 2 |
| [v0.4.0](https://github.com/storytold/cadcraft/releases/tag/v0.4.0) | 3 | 1 | · | 1 | · | 1 | · | 1 | · |
| [v0.5.0](https://github.com/storytold/cadcraft/releases/tag/v0.5.0) | 188 | · | 180 | 8 | · | · | · | 178 | 2 |
| [v0.6.2](https://github.com/storytold/cadcraft/releases/tag/v0.6.2) | 160 | 1 | 152 | 3 | · | 3 | 1 | 151 | 2 |
| _unreleased (main)_ | 109 | · | 102 | 7 | · | · | · | 102 | · |
| **Released total** | **378** | **2** | **336** | **33** | **0** | **4** | **3** | **330** | **8** |

Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.

## Contributors

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/cadcraft-contributors.png">
  <img alt="cadcraft: unique contributors per release (returning humans, new humans, disclosed agents, bots)" src="../charts/light/cadcraft-contributors.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/cadcraft-agent-disclosure.png">
  <img alt="cadcraft: changes per release by agent disclosure" src="../charts/light/cadcraft-agent-disclosure.png">
</picture>

**What this shows**

- 35 people have contributed to released changes.
- The first release had 1 person and the latest had 27.
- In the latest release, 19 of the 27 people were contributing for the first time.
- The most active person, @vangel76, authored 51% of all changes, and the three most active authored 78% between them.
- 86% of changes say an AI agent was involved (319 of 371).
- That share has gone down: 96% in the first 2 releases and 85% in the last 2 releases.
- Claude accounts for all of the changes that name an agent.
- These figures only count changes that say so, so the real share may be higher.

| Release | Humans | New | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|--:|---|--:|
| [v0.1.0](https://github.com/storytold/cadcraft/releases/tag/v0.1.0) | 1 | 1 | 20 | 95% | · | Claude | · |
| [v0.3.0](https://github.com/storytold/cadcraft/releases/tag/v0.3.0) | 2 | 1 | 4 | 100% | · | Claude | · |
| [v0.4.0](https://github.com/storytold/cadcraft/releases/tag/v0.4.0) | 2 | 1 | 2 | 100% | · | Claude | · |
| [v0.5.0](https://github.com/storytold/cadcraft/releases/tag/v0.5.0) | 14 | 13 | 139 | 74% | · | Claude | · |
| [v0.6.2](https://github.com/storytold/cadcraft/releases/tag/v0.6.2) | 27 | 19 | 154 | 99% | · | Claude | · |
| _unreleased (main)_ | 32 | 22 | 83 | 76% | · | Claude | · |
| **Released total** | **35** |  | **319** | 86% | **0** | Claude | · |

Humans are unique people per release, authors and co-authors together; New is how many of them had not appeared in an earlier release of this repo. The total row counts each person once. An agent is disclosed when it is a commit's git author, is named in a `Co-authored-by` trailer, or the message says it was generated with one.

Most active humans in released changes: @vangel76 (193), @MarekSpodBiedry (65), @echelon (50), @SBaksa (11), @Tru10 (10), @aldozar (9), @Ni-zav (8), @switch87 (8), @DWAA1660 (7), @LloydNicholson (7).
