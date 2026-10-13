# deckcraft — changes per release

5 releases, 2026-10-08 → 2026-10-12. Each row counts the changes that landed between the previous release tag and this one; the first row is everything up to the first tag. See [../README.md](../README.md) for how changes are counted and categorised.

## By category

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

## By how it landed

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
