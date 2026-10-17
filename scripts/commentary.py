"""Plain-English commentary on one repo's trends, written from its per-release numbers.

Every sentence is computed, so the commentary stays true when the stats are refreshed. Each
function returns a list of sentences; a sentence is only included when the numbers support it.
"""
import datetime

PLURAL = {"feature": "features", "fix": "fixes", "perf": "performance work", "i18n": "translations", "docs": "documentation",
          "test": "tests", "build-ci": "build and release tooling", "release": "release housekeeping", "refactor": "clean-up",
          "deps": "dependency updates", "security": "security hardening", "revert": "reverts", "other": "other changes"}
CATS = list(PLURAL)

def pct(part, whole):
    """A whole-number percentage as text; a small non-zero share is 'under 1%', never 0%."""
    return pc(100 * part / whole) if whole else "0%"

def pc(p):
    """A percentage already worked out, as text, by the same rule as pct()."""
    return "under 1%" if 0 < p < 1 else f"{p:.0f}%"

def share(part, whole): return 100 * part / whole if whole else 0.0
def total(releases, key): return sum(r[key] for r in releases)
def count(n, word, plural=None): return f"{n:,} {word if n == 1 else plural or word + 's'}"
def cap(sentence): return sentence[0].upper() + sentence[1:]

def name(release):
    """`v0.6.0 (10 Oct)`"""
    d = datetime.date.fromisoformat(release["published"])
    return f"{release['release_tag'].replace('artcraft-', '')} ({d.day} {d:%b})"

def halves(releases):
    """The first and last halves of the release list, and how to refer to them."""
    k = len(releases) // 2
    if k < 2: return None
    return releases[:k], releases[-k:], f"the first {k} releases", f"the last {k} releases"

def types(repo, releases, unreleased, left_out=()):
    """Size of releases and the mix of change types. `left_out` are releases with no categories."""
    out = []
    changes = total(releases, "changes")
    first = datetime.date.fromisoformat(releases[0]["published"]); last = datetime.date.fromisoformat(releases[-1]["published"])
    days = (last - first).days
    out.append(f"{repo} has had {count(len(releases), 'release')} with {count(changes, 'change')} in total" + (f", over {count(days, 'day')}." if days > 1 else "."))
    for r in left_out:
        out.append(f"The first release, {name(r)}, is left out of everything below: its {r['changes']:,} changes of older history were counted but not sorted into types.")
    if len(releases) > 1:
        big = max(releases, key=lambda r: r["changes"])
        out.append(f"The biggest release was {name(big)} with {count(big['changes'], 'change')}, which is {pct(big['changes'], changes)} of everything released so far.")
    h = halves(releases)
    if h:
        early, late, early_name, late_name = h
        a, b = total(early, "changes") / len(early), total(late, "changes") / len(late)
        sizes = f"{early_name} averaged {a:,.0f} changes each and {late_name} averaged {b:,.0f}"
        if a and b / a >= 1.5: out.append(f"Releases are getting bigger: {sizes}.")
        elif a and b / a <= 0.67: out.append(f"Releases are getting smaller: {sizes}.")
        else: out.append(f"Release size has stayed fairly steady: {sizes}.")

    ranked = sorted(CATS, key=lambda c: -total(releases, c))
    top, second = ranked[0], ranked[1]
    if total(releases, top):
        mix = f"Overall, {PLURAL[top]} make up {pct(total(releases, top), changes)} of changes"
        out.append(mix + (f" and {PLURAL[second]} {pct(total(releases, second), changes)}." if total(releases, second) else "."))
    if h:
        f0, f1 = share(total(early, "feature"), total(early, "changes")), share(total(late, "feature"), total(late, "changes"))
        x0, x1 = share(total(early, "fix"), total(early, "changes")), share(total(late, "fix"), total(late, "changes"))
        detail = f"features went from {pc(f0)} of changes in {early_name} to {pc(f1)} in {late_name}, and fixes from {pc(x0)} to {pc(x1)}"
        if f1 - f0 <= -10 and x1 - x0 >= 10: out.append(f"The work has shifted from building new things to fixing: {detail}.")
        elif f1 - f0 >= 10 and x1 - x0 <= -10: out.append(f"The work has shifted from fixing to building new things: {detail}.")
        elif abs(f1 - f0) < 10 and abs(x1 - x0) < 10: out.append(f"The balance between features and fixes has not changed much: {detail}.")
        else: out.append(f"The mix has changed: {detail}.")
    perf = total(releases, "perf")
    if not perf: out.append("No change was labelled as performance work.")
    elif share(perf, changes) < 2: out.append(f"Performance work is rare: {count(perf, 'change')}.")
    else:
        best = max(releases, key=lambda r: r["perf"])
        out.append(f"Performance work is {pct(perf, changes)} of changes ({perf:,})" + (f", most of it in {name(best)}, which had {best['perf']}." if best["perf"] >= 3 else "."))
    rest = [c for c in ranked if c not in ("feature", "fix", "perf") and share(total(releases, c), changes) >= 5]
    if rest: out.append(f"After features and fixes, the next biggest group is {PLURAL[rest[0]]} at {pct(total(releases, rest[0]), changes)}.")
    if unreleased and unreleased["changes"]:
        out.append(f"Since the last release, {count(unreleased['changes'], 'more change')} {'has' if unreleased['changes'] == 1 else 'have'} landed on main and not been released yet: "
                   f"{count(unreleased['feature'], 'feature')} and {count(unreleased['fix'], 'fix', 'fixes')} among them.")
    return out

def landing(releases):
    """Pull requests versus direct commits, and who the pull requests came from."""
    out = []
    changes = total(releases, "changes")
    via_pr = lambda rs: total(rs, "pr-merge") + total(rs, "squash")
    out.append(f"{cap(pct(via_pr(releases), changes))} of changes came in through pull requests; the rest were committed directly.")
    h = halves(releases)
    if h:
        early, late, early_name, late_name = h
        p0, p1 = share(via_pr(early), total(early, "changes")), share(via_pr(late), total(late, "changes"))
        if p1 - p0 >= 20: out.append(f"That has grown: pull requests were {pc(p0)} of changes in {early_name} and {pc(p1)} in {late_name}.")
        elif p0 - p1 >= 20: out.append(f"That has dropped: pull requests were {pc(p0)} of changes in {early_name} and {pc(p1)} in {late_name}.")
    prs = total(releases, "community_prs") + total(releases, "team_prs")
    if prs:
        outside = total(releases, "community_prs")
        some = "none" if not outside else "all" if outside == prs else pct(outside, prs)
        out.append(f"Of the {count(prs, 'pull request')}, {some} came from people outside the core team.")
        if h:
            c = lambda rs: share(total(rs, "community_prs"), total(rs, "community_prs") + total(rs, "team_prs"))
            if abs(c(late) - c(early)) >= 20:
                out.append(f"Outside contributions have gone {'up' if c(late) > c(early) else 'down'}: {pc(c(early))} of pull requests in {early_name}, {pc(c(late))} in {late_name}.")
    return out

def contributors(releases, people, changes_total):
    """How many people take part, how concentrated the work is, and how much of it discloses an AI agent.

    `people` is the repo's contributor rows (see report.py), most active first within each kind.
    """
    out = []
    humans = [p for p in people if p["kind"] == "human"]
    agents = [p for p in people if p["kind"] == "agent"]
    out.append(f"{count(len(humans), 'person has', 'people have')} contributed to released changes.")
    first, last = releases[0], releases[-1]
    peak = max(releases, key=lambda r: r["humans"])
    if len(releases) > 1 and len(humans) > 1:
        line = f"The first release had {count(first['humans'], 'person', 'people')} and the latest had {last['humans']:,}"
        out.append(line + (f"; the most in one release was {peak['humans']:,}, in {name(peak)}." if peak is not last and peak["humans"] > last["humans"] else "."))
        if last["humans"] and last["new_humans"]:
            out.append(f"In the latest release, {last['new_humans']:,} of the {count(last['humans'], 'person', 'people')} were contributing for the first time.")
        elif last["humans"]:
            out.append("Nobody in the latest release was a first-time contributor.")
    authors = [p for p in humans if p["changes_authored"]]
    if len(authors) > 1 and changes_total:
        lead = authors[0]
        out.append(f"The most active person, {lead['contributor']}, authored {pct(lead['changes_authored'], changes_total)} of all changes"
                   + (f", and the three most active authored {pct(sum(p['changes_authored'] for p in authors[:3]), changes_total)} between them." if len(authors) > 3 else "."))
    disclosed = total(releases, "changes_agent_disclosed")
    if not disclosed:
        out.append("No released change says an AI agent was involved.")
        return out
    out.append(f"{cap(pct(disclosed, changes_total))} of changes say an AI agent was involved ({disclosed:,} of {changes_total:,}).")
    h = halves(releases)
    if h:
        early, late, early_name, late_name = h
        d0 = share(total(early, "changes_agent_disclosed"), total(early, "changes")); d1 = share(total(late, "changes_agent_disclosed"), total(late, "changes"))
        if abs(d1 - d0) >= 10:
            out.append(f"That share has gone {'up' if d1 > d0 else 'down'}: {pc(d0)} in {early_name} and {pc(d1)} in {late_name}.")
        else:
            out.append(f"That share has stayed about the same over time ({pc(d0)} in {early_name}, {pc(d1)} in {late_name}).")
    used = lambda a: a["changes_authored"] + a["changes_coauthored"]
    if agents:
        if len(agents) == 1 or used(agents[0]) >= 0.9 * sum(used(a) for a in agents):
            out.append(f"{agents[0]['contributor']} accounts for {'all' if len(agents) == 1 else 'nearly all'} of the changes that name an agent" + (f"; {count(len(agents) - 1, 'other agent')} {'is' if len(agents) == 2 else 'are'} named on {count(sum(used(a) for a in agents[1:]), 'change')} between them." if len(agents) > 1 else "."))
        else:
            out.append(f"The agents named most are {agents[0]['contributor']} ({used(agents[0]):,} changes) and {agents[1]['contributor']} ({used(agents[1]):,}).")
    authored = total(releases, "changes_agent_authored")
    if authored:
        out.append(f"In {count(authored, 'change')} the agent is the commit author itself, not only a co-author.")
    out.append("These figures only count changes that say so, so the real share may be higher.")
    return out
