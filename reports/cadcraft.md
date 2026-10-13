# cadcraft — changes per release

5 releases, 2026-10-08 → 2026-10-12. Each row counts the changes that landed between the previous release tag and this one; the first row is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised.

## By category

| Release | Published | Changes | Feature | Fix | Perf | i18n | Docs | Test | Build/CI | Release | Refactor | Deps | Security | Revert | Other |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/cadcraft/releases/tag/v0.1.0) | 2026-10-08 | 21 | 12 | · | 1 | · | 1 | · | · | 4 | 1 | · | · | · | 2 |
| [v0.3.0](https://github.com/storytold/cadcraft/releases/tag/v0.3.0) | 2026-10-08 | 4 | · | · | · | · | 1 | · | · | 3 | · | · | · | · | · |
| [v0.4.0](https://github.com/storytold/cadcraft/releases/tag/v0.4.0) | 2026-10-10 | 2 | · | · | · | · | · | · | 1 | 1 | · | · | · | · | · |
| [v0.5.0](https://github.com/storytold/cadcraft/releases/tag/v0.5.0) | 2026-10-11 | 188 | 18 | 160 | · | 1 | 2 | 3 | · | 1 | 3 | · | · | · | · |
| [v0.6.2](https://github.com/storytold/cadcraft/releases/tag/v0.6.2) | 2026-10-12 | 156 | 83 | 55 | 5 | 7 | 1 | · | 1 | 4 | · | · | · | · | · |
| _unreleased (main)_ | 2026-10-13 | 73 | 9 | 54 | 2 | 2 | 3 | 2 | · | · | 1 | · | · | · | · |
| **Released total** |  | **371** | **113** | **215** | **6** | **8** | **5** | **3** | **2** | **13** | **4** | · | · | · | **2** |

Share of released changes: feature 30%, fix 58%, perf 2%, i18n 2%, docs 1%, test 1%, build/ci 1%, release 4%, refactor 1%, other 1%.

## By how it landed

| Release | Commits | PR merges | Squash merges | Direct commits | Batch commits | Commits inside PRs | Sync merges | Community PRs | Team PRs |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| [v0.1.0](https://github.com/storytold/cadcraft/releases/tag/v0.1.0) | 23 | · | 2 | 19 | · | · | 2 | · | 2 |
| [v0.3.0](https://github.com/storytold/cadcraft/releases/tag/v0.3.0) | 4 | · | 2 | 2 | · | · | · | · | 2 |
| [v0.4.0](https://github.com/storytold/cadcraft/releases/tag/v0.4.0) | 3 | 1 | · | 1 | · | 1 | · | 1 | · |
| [v0.5.0](https://github.com/storytold/cadcraft/releases/tag/v0.5.0) | 188 | · | 180 | 8 | · | · | · | 178 | 2 |
| [v0.6.2](https://github.com/storytold/cadcraft/releases/tag/v0.6.2) | 160 | 1 | 152 | 3 | · | 3 | 1 | 151 | 2 |
| _unreleased (main)_ | 73 | · | 71 | 2 | · | · | · | 71 | · |
| **Released total** | **378** | **2** | **336** | **33** | **0** | **4** | **3** | **330** | **8** |

Changes = PR merges + squash merges + direct commits + batch commits. Commits = changes + commits inside PRs + sync merges.

## Contributors

| Release | Humans | New | Changes disclosing an agent | Share | Agent is git author | Agents disclosed | Bots |
|---|--:|--:|--:|--:|--:|---|--:|
| [v0.1.0](https://github.com/storytold/cadcraft/releases/tag/v0.1.0) | 1 | 1 | 20 | 95% | · | Claude | · |
| [v0.3.0](https://github.com/storytold/cadcraft/releases/tag/v0.3.0) | 2 | 1 | 4 | 100% | · | Claude | · |
| [v0.4.0](https://github.com/storytold/cadcraft/releases/tag/v0.4.0) | 2 | 1 | 2 | 100% | · | Claude | · |
| [v0.5.0](https://github.com/storytold/cadcraft/releases/tag/v0.5.0) | 14 | 13 | 139 | 74% | · | Claude | · |
| [v0.6.2](https://github.com/storytold/cadcraft/releases/tag/v0.6.2) | 27 | 19 | 154 | 99% | · | Claude | · |
| _unreleased (main)_ | 24 | 16 | 47 | 64% | · | Claude | · |
| **Released total** | **35** |  | **319** | 86% | **0** | Claude | · |

Humans are unique people per release, authors and co-authors together; New is how many of them had not appeared in an earlier release of this repo. The total row counts each person once. An agent is disclosed when it is a commit's git author, is named in a `Co-authored-by` trailer, or the message says it was generated with one.

Most active humans in released changes: @vangel76 (193), @MarekSpodBiedry (65), @echelon (50), @SBaksa (11), @Tru10 (10), @aldozar (9), @Ni-zav (8), @switch87 (8), @DWAA1660 (7), @LloydNicholson (7).
