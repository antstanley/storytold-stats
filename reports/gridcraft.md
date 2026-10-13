# gridcraft — changes per release

5 releases, 2026-10-08 → 2026-10-12. Each release is counted as the changes that landed between the previous release tag and its own; the first one is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised. The charts cover released changes; the commentary under them is generated from the same numbers.

## Changes by type

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/gridcraft-changes-line.png">
  <img alt="gridcraft: changes per release, stacked by type, as lines" src="../charts/light/gridcraft-changes-line.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/gridcraft-changes-bar.png">
  <img alt="gridcraft: changes per release, stacked by type, as bars" src="../charts/light/gridcraft-changes-bar.png">
</picture>

**What this shows**

- gridcraft has had 5 releases with 256 changes in total, over 4 days.
- The biggest release was v0.6.1 (12 Oct) with 145 changes, which is 57% of everything released so far.
- Releases are getting bigger: the first 2 releases averaged 12 changes each and the last 2 releases averaged 116.
- Overall, fixes make up 56% of changes and features 21%.
- The work has shifted from building new things to fixing: features went from 43% of changes in the first 2 releases to 19% in the last 2 releases, and fixes from 4% to 61%.
- Performance work is rare: 1 change.
- Since the last release, 162 more changes have landed on main and not been released yet: 13 features and 129 fixes among them.

| Release | Published | Changes | Feature | Fix | Perf | i18n | Docs | Test | Build/CI | Release | Refactor | Deps | Security | Revert | Other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/gridcraft/releases/tag/v0.1.0) | 2026-10-08 | 16 | 9 | 1 | 1 | · | 1 | · | 1 | · | 2 | · | · | · | 1 |
| [v0.3.0](https://github.com/storytold/gridcraft/releases/tag/v0.3.0) | 2026-10-08 | 7 | 1 | · | · | · | 1 | · | · | 5 | · | · | · | · | · |
| [v0.4.0](https://github.com/storytold/gridcraft/releases/tag/v0.4.0) | 2026-10-10 | 2 | · | · | · | · | · | · | 1 | 1 | · | · | · | · | · |
| [v0.5.0](https://github.com/storytold/gridcraft/releases/tag/v0.5.0) | 2026-10-10 | 86 | 12 | 59 | · | 3 | 1 | 1 | 3 | 2 | 5 | · | · | · | · |
| [v0.6.1](https://github.com/storytold/gridcraft/releases/tag/v0.6.1) | 2026-10-12 | 145 | 33 | 83 | · | 7 | 8 | 3 | 5 | 3 | 2 | · | 1 | · | · |
| _unreleased (main)_ | 2026-10-13 | 162 | 13 | 129 | 1 | 4 | 1 | 8 | 2 | · | 3 | · | 1 | · | · |
| **Released total** |  | **256** | **55** | **143** | **1** | **10** | **11** | **4** | **10** | **11** | **9** | · | **1** | · | **1** |

Share of released changes: feature 21%, fix 56%, i18n 4%, docs 4%, test 2%, build/ci 4%, release 4%, refactor 4%.

## How changes landed

**What this shows**

- 85% of changes came in through pull requests; the rest were committed directly.
- That has grown: pull requests were 17% of changes in the first 2 releases and 92% in the last 2 releases.
- Of the 218 pull requests, 97% came from people outside the core team.
- Outside contributions have gone up: 0% of pull requests in the first 2 releases, 99% in the last 2 releases.

| Release | Commits | PR merges | Squash merges | Direct commits | Batch commits | Commits inside PRs | Sync merges | Community PRs | Team PRs |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/gridcraft/releases/tag/v0.1.0) | 16 | · | 1 | 15 | · | · | · | · | 1 |
| [v0.3.0](https://github.com/storytold/gridcraft/releases/tag/v0.3.0) | 7 | · | 3 | 4 | · | · | · | · | 3 |
| [v0.4.0](https://github.com/storytold/gridcraft/releases/tag/v0.4.0) | 3 | 1 | · | 1 | · | 1 | · | 1 | · |
| [v0.5.0](https://github.com/storytold/gridcraft/releases/tag/v0.5.0) | 222 | 78 | 3 | 5 | · | 116 | 20 | 79 | 2 |
| [v0.6.1](https://github.com/storytold/gridcraft/releases/tag/v0.6.1) | 358 | 126 | 6 | 13 | · | 181 | 32 | 131 | 1 |
| _unreleased (main)_ | 407 | 150 | · | 12 | · | 181 | 64 | 150 | · |
| **Released total** | **606** | **205** | **13** | **38** | **0** | **298** | **52** | **211** | **7** |

Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.

## Contributors

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/gridcraft-contributors.png">
  <img alt="gridcraft: unique contributors per release (returning humans, new humans, disclosed agents, bots)" src="../charts/light/gridcraft-contributors.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../charts/dark/gridcraft-agent-disclosure.png">
  <img alt="gridcraft: changes per release by agent disclosure" src="../charts/light/gridcraft-agent-disclosure.png">
</picture>

**What this shows**

- 44 people have contributed to released changes.
- The first release had 1 person and the latest had 35.
- In the latest release, 28 of the 35 people were contributing for the first time.
- The most active person, @echelon, authored 17% of all changes, and the three most active authored 48% between them.
- 64% of changes say an AI agent was involved (164 of 256).
- That share has gone down: 96% in the first 2 releases and 61% in the last 2 releases.
- Claude accounts for nearly all of the changes that name an agent; 1 other agent is named on 3 changes between them.
- These figures only count changes that say so, so the real share may be higher.

| Release | Humans | New | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|--:|---|--:|
| [v0.1.0](https://github.com/storytold/gridcraft/releases/tag/v0.1.0) | 1 | 1 | 15 | 94% | · | Claude | · |
| [v0.3.0](https://github.com/storytold/gridcraft/releases/tag/v0.3.0) | 2 | 1 | 7 | 100% | · | Claude | · |
| [v0.4.0](https://github.com/storytold/gridcraft/releases/tag/v0.4.0) | 2 | 1 | 2 | 100% | · | Claude | · |
| [v0.5.0](https://github.com/storytold/gridcraft/releases/tag/v0.5.0) | 14 | 13 | 39 | 45% | · | Claude, OpenAI Codex / ChatGPT | · |
| [v0.6.1](https://github.com/storytold/gridcraft/releases/tag/v0.6.1) | 35 | 28 | 101 | 70% | · | Claude | · |
| _unreleased (main)_ | 27 | 15 | 51 | 31% | 1 | Claude | · |
| **Released total** | **44** |  | **164** | 64% | **0** | Claude, OpenAI Codex / ChatGPT | · |

Humans are unique people per release, authors and co-authors together; New is how many of them had not appeared in an earlier release of this repo. The total row counts each person once. An agent is disclosed when it is a commit's git author, is named in a `Co-authored-by` trailer, or the message says it was generated with one.

Most active humans in released changes: @echelon (248), @vangel76 (50), @nihilist-narwhal (29), @harrisonoconnorhover (20), @MarekSpodBiedry (20), @LloydNicholson (15), @neilcawse (10), @justinjohn0306 (8), @GhostMitra (5), @DWAA1660 (4).
