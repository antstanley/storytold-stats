# figcraft — changes per release

5 releases, 2026-10-10 → 2026-10-12. Each release is counted as the changes that landed between the previous release tag and its own; the first one is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised. The charts cover released changes; the commentary under them is generated from the same numbers.

## Changes by type

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/figcraft-changes-line.png">
  <img alt="figcraft: changes per release, stacked by type, as lines" src="../charts/light/figcraft-changes-line.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/figcraft-changes-bar.png">
  <img alt="figcraft: changes per release, stacked by type, as bars" src="../charts/light/figcraft-changes-bar.png">
</picture>

**What this shows**

- figcraft has had 5 releases with 214 changes in total, over 2 days.
- The biggest release was v0.2.0 (10 Oct) with 86 changes, which is 40% of everything released so far.
- Releases are getting smaller: the first 2 releases averaged 67 changes each and the last 2 releases averaged 7.
- Overall, features make up 65% of changes and fixes 13%.
- The mix has changed: features went from 73% of changes in the first 2 releases to 36% in the last 2 releases, and fixes from 9% to 14%.
- Performance work is 2% of changes (5), most of it in v0.2.0 (10 Oct), which had 3.
- After features and fixes, the next biggest group is documentation at 7%.
- Since the last release, 53 more changes have landed on main and not been released yet: 23 features and 23 fixes among them.

| Release | Published | Changes | Feature | Fix | Perf | i18n | Docs | Test | Build/CI | Release | Refactor | Deps | Security | Revert | Other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.2.0](https://github.com/storytold/figcraft/releases/tag/v0.2.0) | 2026-10-10 | 86 | 65 | 5 | 3 | · | 7 | · | 2 | 1 | 2 | · | · | · | 1 |
| [v0.3.1](https://github.com/storytold/figcraft/releases/tag/v0.3.1) | 2026-10-11 | 48 | 33 | 7 | 1 | · | 5 | · | 1 | 1 | · | · | · | · | · |
| [v0.4.0](https://github.com/storytold/figcraft/releases/tag/v0.4.0) | 2026-10-12 | 66 | 37 | 14 | 1 | 5 | 3 | 1 | 1 | 1 | · | · | 3 | · | · |
| [v0.5.0](https://github.com/storytold/figcraft/releases/tag/v0.5.0) | 2026-10-12 | 5 | · | · | · | · | 1 | · | 3 | 1 | · | · | · | · | · |
| [v0.5.1](https://github.com/storytold/figcraft/releases/tag/v0.5.1) | 2026-10-12 | 9 | 5 | 2 | · | · | · | · | · | 2 | · | · | · | · | · |
| _unreleased (main)_ | 2026-10-14 | 53 | 23 | 23 | · | · | 6 | · | 1 | · | · | · | · | · | · |
| **Released total** |  | **214** | **140** | **28** | **5** | **5** | **16** | **1** | **7** | **6** | **2** | · | **3** | · | **1** |

Share of released changes: feature 65%, fix 13%, perf 2%, i18n 2%, docs 7%, build/ci 3%, release 3%, refactor 1%, security 1%.

## How changes landed

**What this shows**

- 75% of changes came in through pull requests; the rest were committed directly.
- Of the 160 pull requests, none came from people outside the core team.

| Release | Commits | PR merges | Squash merges | Direct commits | Batch commits | Commits inside PRs | Sync merges | Community PRs | Team PRs |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.2.0](https://github.com/storytold/figcraft/releases/tag/v0.2.0) | 86 | · | 59 | 27 | · | · | · | · | 59 |
| [v0.3.1](https://github.com/storytold/figcraft/releases/tag/v0.3.1) | 48 | · | 48 | · | · | · | · | · | 48 |
| [v0.4.0](https://github.com/storytold/figcraft/releases/tag/v0.4.0) | 66 | · | 44 | 22 | · | · | · | · | 44 |
| [v0.5.0](https://github.com/storytold/figcraft/releases/tag/v0.5.0) | 5 | · | 4 | 1 | · | · | · | · | 4 |
| [v0.5.1](https://github.com/storytold/figcraft/releases/tag/v0.5.1) | 9 | · | 5 | 4 | · | · | · | · | 5 |
| _unreleased (main)_ | 53 | · | 36 | 17 | · | · | · | 25 | 11 |
| **Released total** | **214** | **0** | **160** | **54** | **0** | **0** | **0** | **0** | **160** |

Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.

## Contributors

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/figcraft-contributors.png">
  <img alt="figcraft: unique contributors per release (returning humans, new humans, disclosed agents, bots)" src="../charts/light/figcraft-contributors.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/figcraft-agent-disclosure.png">
  <img alt="figcraft: changes per release by agent disclosure" src="../charts/light/figcraft-agent-disclosure.png">
</picture>

**What this shows**

- 2 people have contributed to released changes.
- The first release had 2 people and the latest had 1; the most in one release was 2, in v0.2.0 (10 Oct).
- Nobody in the latest release was a first-time contributor.
- The most active person, @bflatastic, authored 86% of all changes.
- 64% of changes say an AI agent was involved (136 of 214).
- That share has gone down: 99% in the first 2 releases and 7% in the last 2 releases.
- Claude accounts for all of the changes that name an agent.
- These figures only count changes that say so, so the real share may be higher.

| Release | Humans | New | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|--:|---|--:|
| [v0.2.0](https://github.com/storytold/figcraft/releases/tag/v0.2.0) | 2 | 2 | 85 | 99% | · | Claude | · |
| [v0.3.1](https://github.com/storytold/figcraft/releases/tag/v0.3.1) | 2 | · | 48 | 100% | · | Claude | · |
| [v0.4.0](https://github.com/storytold/figcraft/releases/tag/v0.4.0) | 1 | · | 2 | 3% | · | Claude | · |
| [v0.5.0](https://github.com/storytold/figcraft/releases/tag/v0.5.0) | 2 | · | 1 | 20% | · | Claude | · |
| [v0.5.1](https://github.com/storytold/figcraft/releases/tag/v0.5.1) | 1 | · | · | 0% | · | · | · |
| _unreleased (main)_ | 13 | 11 | 16 | 30% | · | Claude | · |
| **Released total** | **2** |  | **136** | 64% | **0** | Claude | · |

Humans are unique people per release, authors and co-authors together; New is how many of them had not appeared in an earlier release of this repo. The total row counts each person once. An agent is disclosed when it is a commit's git author, is named in a `Co-authored-by` trailer, or the message says it was generated with one.

Most active humans in released changes: @bflatastic (183), @echelon (31).
