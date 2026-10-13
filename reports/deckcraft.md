# deckcraft — changes per release

5 releases, 2026-10-08 → 2026-10-12. Each release is counted as the changes that landed between the previous release tag and its own; the first one is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised. The charts cover released changes; the commentary under them is generated from the same numbers.

## Changes by type

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/deckcraft-changes-line.png">
  <img alt="deckcraft: changes per release, stacked by type, as lines" src="../charts/light/deckcraft-changes-line.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/deckcraft-changes-bar.png">
  <img alt="deckcraft: changes per release, stacked by type, as bars" src="../charts/light/deckcraft-changes-bar.png">
</picture>

**What this shows**

- deckcraft has had 5 releases with 64 changes in total, over 4 days.
- The biggest release was v0.1.0 (8 Oct) with 20 changes, which is 31% of everything released so far.
- Release size has stayed fairly steady: the first 2 releases averaged 14 changes each and the last 2 releases averaged 11.
- Overall, features make up 30% of changes and fixes 22%.
- The work has shifted from building new things to fixing: features went from 41% of changes in the first 2 releases to 18% in the last 2 releases, and fixes from 0% to 36%.
- No change was labelled as performance work.
- After features and fixes, the next biggest group is release housekeeping at 20%.
- Since the last release, 53 more changes have landed on main and not been released yet: 16 features and 32 fixes among them.

| Release | Published | Changes | Feature | Fix | Perf | i18n | Docs | Test | Build/CI | Release | Refactor | Deps | Security | Revert | Other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/deckcraft/releases/tag/v0.1.0) | 2026-10-08 | 20 | 11 | · | · | · | 1 | · | 2 | 2 | 2 | 1 | · | · | 1 |
| [v0.3.0](https://github.com/storytold/deckcraft/releases/tag/v0.3.0) | 2026-10-08 | 9 | 1 | · | · | · | 1 | · | · | 6 | 1 | · | · | · | · |
| [v0.4.0](https://github.com/storytold/deckcraft/releases/tag/v0.4.0) | 2026-10-10 | 13 | 3 | 6 | · | · | 1 | · | 2 | 1 | · | · | · | · | · |
| [v0.5.0](https://github.com/storytold/deckcraft/releases/tag/v0.5.0) | 2026-10-11 | 18 | 4 | 8 | · | · | 2 | 1 | 1 | 1 | 1 | · | · | · | · |
| [v0.6.1](https://github.com/storytold/deckcraft/releases/tag/v0.6.1) | 2026-10-12 | 4 | · | · | · | · | · | · | 1 | 3 | · | · | · | · | · |
| _unreleased (main)_ | 2026-10-13 | 53 | 16 | 32 | · | · | 3 | 1 | · | · | 1 | · | · | · | · |
| **Released total** |  | **64** | **19** | **14** | · | · | **5** | **1** | **6** | **13** | **4** | **1** | · | · | **1** |

Share of released changes: feature 30%, fix 22%, docs 8%, test 2%, build/ci 9%, release 20%, refactor 6%, deps 2%, other 2%.

## How changes landed

**What this shows**

- 56% of changes came in through pull requests; the rest were committed directly.
- That has grown: pull requests were 14% of changes in the first 2 releases and 91% in the last 2 releases.
- Of the 36 pull requests, 78% came from people outside the core team.
- Outside contributions have gone up: 0% of pull requests in the first 2 releases, 85% in the last 2 releases.

| Release | Commits | PR merges | Squash merges | Direct commits | Batch commits | Commits inside PRs | Sync merges | Community PRs | Team PRs |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/deckcraft/releases/tag/v0.1.0) | 20 | · | · | 20 | · | · | · | · | · |
| [v0.3.0](https://github.com/storytold/deckcraft/releases/tag/v0.3.0) | 9 | · | 4 | 5 | · | · | · | · | 4 |
| [v0.4.0](https://github.com/storytold/deckcraft/releases/tag/v0.4.0) | 14 | 1 | 11 | 1 | · | 1 | · | 11 | 1 |
| [v0.5.0](https://github.com/storytold/deckcraft/releases/tag/v0.5.0) | 18 | · | 18 | · | · | · | · | 16 | 2 |
| [v0.6.1](https://github.com/storytold/deckcraft/releases/tag/v0.6.1) | 4 | · | 2 | 2 | · | · | · | 1 | 1 |
| _unreleased (main)_ | 53 | · | 47 | 6 | · | · | · | · | 47 |
| **Released total** | **65** | **1** | **35** | **28** | **0** | **1** | **0** | **28** | **8** |

Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.

## Contributors

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/deckcraft-contributors.png">
  <img alt="deckcraft: unique contributors per release (returning humans, new humans, disclosed agents, bots)" src="../charts/light/deckcraft-contributors.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/deckcraft-agent-disclosure.png">
  <img alt="deckcraft: changes per release by agent disclosure" src="../charts/light/deckcraft-agent-disclosure.png">
</picture>

**What this shows**

- 17 people have contributed to released changes.
- The first release had 1 person and the latest had 2; the most in one release was 12, in v0.4.0 (10 Oct).
- Nobody in the latest release was a first-time contributor.
- The most active person, @echelon, authored 53% of all changes, and the three most active authored 70% between them.
- 89% of changes say an AI agent was involved (57 of 64).
- That share has stayed about the same over time (97% in the first 2 releases, 91% in the last 2 releases).
- Claude accounts for all of the changes that name an agent.
- These figures only count changes that say so, so the real share may be higher.

| Release | Humans | New | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|--:|---|--:|
| [v0.1.0](https://github.com/storytold/deckcraft/releases/tag/v0.1.0) | 1 | 1 | 19 | 95% | · | Claude | · |
| [v0.3.0](https://github.com/storytold/deckcraft/releases/tag/v0.3.0) | 2 | 1 | 9 | 100% | · | Claude | · |
| [v0.4.0](https://github.com/storytold/deckcraft/releases/tag/v0.4.0) | 12 | 10 | 9 | 69% | · | Claude | · |
| [v0.5.0](https://github.com/storytold/deckcraft/releases/tag/v0.5.0) | 7 | 5 | 17 | 94% | · | Claude | · |
| [v0.6.1](https://github.com/storytold/deckcraft/releases/tag/v0.6.1) | 2 | · | 3 | 75% | · | Claude | · |
| _unreleased (main)_ | 4 | 2 | 47 | 89% | · | Claude | · |
| **Released total** | **17** |  | **57** | 89% | **0** | Claude | · |

Humans are unique people per release, authors and co-authors together; New is how many of them had not appeared in an earlier release of this repo. The total row counts each person once. An agent is disclosed when it is a commit's git author, is named in a `Co-authored-by` trailer, or the message says it was generated with one.

Most active humans in released changes: @echelon (47), @alexanderalber (9), @h-a-n-a-s-h-i (5), @LloydNicholson (5), @dylanmtaylor (2), @MarekSpodBiedry (2), @switch87 (2), @DimaSmaha (1), @DWAA1660 (1), @hamzaelkachtaf4-star (1).
