# craft-launcher — changes per release

7 releases, 2026-10-10 → 2026-10-11. Each release is counted as the changes that landed between the previous release tag and its own; the first one is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised. The charts cover released changes; the commentary under them is generated from the same numbers.

## Changes by type

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/craft-launcher-changes-line.png">
  <img alt="craft-launcher: changes per release, stacked by type, as lines" src="../charts/light/craft-launcher-changes-line.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/craft-launcher-changes-bar.png">
  <img alt="craft-launcher: changes per release, stacked by type, as bars" src="../charts/light/craft-launcher-changes-bar.png">
</picture>

**What this shows**

- craft-launcher has had 7 releases with 66 changes in total.
- The biggest release was v0.2.1 (11 Oct) with 24 changes, which is 36% of everything released so far.
- Releases are getting bigger: the first 3 releases averaged 7 changes each and the last 3 releases averaged 13.
- Overall, fixes make up 36% of changes and features 33%.
- The work has shifted from building new things to fixing: features went from 48% of changes in the first 3 releases to 20% in the last 3 releases, and fixes from 14% to 52%.
- No change was labelled as performance work.
- After features and fixes, the next biggest group is release housekeeping at 11%.
- Since the last release, 33 more changes have landed on main and not been released yet: 6 features and 15 fixes among them.

| Release | Published | Changes | Feature | Fix | Perf | i18n | Docs | Test | Build/CI | Release | Refactor | Deps | Security | Revert | Other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/craft-launcher/releases/tag/v0.1.0) | 2026-10-10 | 15 | 7 | 1 | · | · | 4 | · | 1 | · | · | · | · | · | 2 |
| [v0.1.1](https://github.com/storytold/craft-launcher/releases/tag/v0.1.1) | 2026-10-10 | 5 | 2 | 2 | · | · | · | · | · | 1 | · | · | · | · | · |
| [v0.1.2](https://github.com/storytold/craft-launcher/releases/tag/v0.1.2) | 2026-10-10 | 1 | 1 | · | · | · | · | · | · | · | · | · | · | · | · |
| [v0.1.3](https://github.com/storytold/craft-launcher/releases/tag/v0.1.3) | 2026-10-10 | 5 | 4 | · | · | · | · | · | · | 1 | · | · | · | · | · |
| [v0.2.0](https://github.com/storytold/craft-launcher/releases/tag/v0.2.0) | 2026-10-10 | 11 | 1 | 7 | · | 1 | · | · | · | 2 | · | · | · | · | · |
| [v0.2.1](https://github.com/storytold/craft-launcher/releases/tag/v0.2.1) | 2026-10-11 | 24 | 7 | 13 | · | 2 | · | 1 | · | · | · | · | 1 | · | · |
| [v0.3.2](https://github.com/storytold/craft-launcher/releases/tag/v0.3.2) | 2026-10-11 | 5 | · | 1 | · | · | · | · | 1 | 3 | · | · | · | · | · |
| _unreleased (main)_ | 2026-10-12 | 33 | 6 | 15 | · | 6 | 1 | · | 5 | · | · | · | · | · | · |
| **Released total** |  | **66** | **22** | **24** | · | **3** | **4** | **1** | **2** | **7** | · | · | **1** | · | **2** |

Share of released changes: feature 33%, fix 36%, i18n 5%, docs 6%, test 2%, build/ci 3%, release 11%, security 2%, other 3%.

## How changes landed

**What this shows**

- 59% of changes came in through pull requests; the rest were committed directly.
- That has grown: pull requests were 14% of changes in the first 3 releases and 88% in the last 3 releases.
- Of the 39 pull requests, 82% came from people outside the core team.
- Outside contributions have gone up: 33% of pull requests in the first 3 releases, 89% in the last 3 releases.

| Release | Commits | PR merges | Squash merges | Direct commits | Batch commits | Commits inside PRs | Sync merges | Community PRs | Team PRs |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/craft-launcher/releases/tag/v0.1.0) | 15 | · | 1 | 14 | · | · | · | 1 | · |
| [v0.1.1](https://github.com/storytold/craft-launcher/releases/tag/v0.1.1) | 5 | · | 1 | 4 | · | · | · | · | 1 |
| [v0.1.2](https://github.com/storytold/craft-launcher/releases/tag/v0.1.2) | 1 | · | 1 | · | · | · | · | · | 1 |
| [v0.1.3](https://github.com/storytold/craft-launcher/releases/tag/v0.1.3) | 5 | · | 1 | 4 | · | · | · | · | 1 |
| [v0.2.0](https://github.com/storytold/craft-launcher/releases/tag/v0.2.0) | 11 | · | 9 | 2 | · | · | · | 9 | · |
| [v0.2.1](https://github.com/storytold/craft-launcher/releases/tag/v0.2.1) | 24 | · | 21 | 3 | · | · | · | 20 | 1 |
| [v0.3.2](https://github.com/storytold/craft-launcher/releases/tag/v0.3.2) | 5 | · | 5 | · | · | · | · | 2 | 3 |
| _unreleased (main)_ | 33 | · | 33 | · | · | · | · | 30 | 3 |
| **Released total** | **66** | **0** | **39** | **27** | **0** | **0** | **0** | **32** | **7** |

Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.

## Contributors

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/craft-launcher-contributors.png">
  <img alt="craft-launcher: unique contributors per release (returning humans, new humans, disclosed agents, bots)" src="../charts/light/craft-launcher-contributors.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/craft-launcher-agent-disclosure.png">
  <img alt="craft-launcher: changes per release by agent disclosure" src="../charts/light/craft-launcher-agent-disclosure.png">
</picture>

**What this shows**

- 18 people have contributed to released changes.
- The first release had 2 people and the latest had 2; the most in one release was 13, in v0.2.1 (11 Oct).
- Nobody in the latest release was a first-time contributor.
- The most active person, @echelon, authored 47% of all changes, and the three most active authored 70% between them.
- 85% of changes say an AI agent was involved (56 of 66).
- That share has stayed about the same over time (86% in the first 3 releases, 82% in the last 3 releases).
- Claude accounts for all of the changes that name an agent.
- These figures only count changes that say so, so the real share may be higher.

| Release | Humans | New | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|--:|---|--:|
| [v0.1.0](https://github.com/storytold/craft-launcher/releases/tag/v0.1.0) | 2 | 2 | 12 | 80% | · | Claude | · |
| [v0.1.1](https://github.com/storytold/craft-launcher/releases/tag/v0.1.1) | 2 | 1 | 5 | 100% | · | Claude | · |
| [v0.1.2](https://github.com/storytold/craft-launcher/releases/tag/v0.1.2) | 1 | · | 1 | 100% | · | Claude | · |
| [v0.1.3](https://github.com/storytold/craft-launcher/releases/tag/v0.1.3) | 1 | · | 5 | 100% | · | Claude | · |
| [v0.2.0](https://github.com/storytold/craft-launcher/releases/tag/v0.2.0) | 6 | 5 | 11 | 100% | · | Claude | · |
| [v0.2.1](https://github.com/storytold/craft-launcher/releases/tag/v0.2.1) | 13 | 10 | 19 | 79% | · | Claude | · |
| [v0.3.2](https://github.com/storytold/craft-launcher/releases/tag/v0.3.2) | 2 | · | 3 | 60% | · | Claude | · |
| _unreleased (main)_ | 24 | 18 | 19 | 58% | · | Claude | · |
| **Released total** | **18** |  | **56** | 85% | **0** | Claude | · |

Humans are unique people per release, authors and co-authors together; New is how many of them had not appeared in an earlier release of this repo. The total row counts each person once. An agent is disclosed when it is a commit's git author, is named in a `Co-authored-by` trailer, or the message says it was generated with one.

Most active humans in released changes: @echelon (41), @itrycodinganditsbad (8), @dylanmtaylor (7), @Nael-Nathanael (5), @bflatastic (3), @AlastorIRL (1), @Benziza (1), @Byxis (1), @Flowershangfromthebranches (1), @JeremyYao (1).
