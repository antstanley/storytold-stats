"""Who contributed a change: the humans behind it, and any AI agent or bot it discloses.

"Disclosed" means the history itself says so, in one of three places:
  - the git author of a commit is an agent identity (e.g. `Claude <noreply@anthropic.com>`),
  - a `Co-authored-by:` trailer names one (e.g. `Claude Opus 5.5`, `Codex`, `Copilot`),
  - the commit message carries a "Generated with <tool>" line.
Agent use that leaves no such mark cannot be seen from here.
"""
import re, collections

# (family, pattern over "name <email>", lowercased). First match wins.
AGENTS = [
    ("opencode", r"@opencode\.ai>|^opencode\b"),
    ("Claude", r"@anthropic\.com>|^claude\b"),
    ("OpenAI Codex / ChatGPT", r"@openai\.com>|^(?:openai )?codex\b|^chatgpt\b|^gpt-\d"),
    ("GitHub Copilot", r"^copilot\b|copilot-swe-agent"),
    ("Cursor", r"@cursor\.com>|^cursor(?: agent)? <"),
    ("Kimi", r"^kimi\b"),
    ("DeepSeek", r"@deepseek\.com>|^deepseek\b"),
    ("Qwen", r"@qwen\.ai>|^qwen\b"),
    ("GLM (Z.ai)", r"@z\.ai>|^(?:zcode|glm)\b"),
    ("Codebuff", r"@codebuff\.com>|^codebuff\b"),
    ("Devin", r"devin-ai-integration|^devin ai\b"),
    ("Muse Spark (Meta)", r"^muse spark\b"),
    ("Xiaomi MiMo", r"^xiaomi mimo\b"),
    ("Unnamed agent", r"\bagent\b[^<]*<[^>]*@(?:localhost|invalid\.local)>"),
]
AGENTS = [(family, re.compile(pattern)) for family, pattern in AGENTS]
GENERATED = re.compile(r"Generated (?:with|by) \[?(Claude Code|Codex|Kimi Code|Codebuff|Devin|Cursor|opencode|Copilot)\b", re.I)
GENERATED_FAMILY = {"claude code": "Claude", "codex": "OpenAI Codex / ChatGPT", "kimi code": "Kimi", "codebuff": "Codebuff",
                    "devin": "Devin", "cursor": "Cursor", "opencode": "opencode", "copilot": "GitHub Copilot"}
TRAILER = re.compile(r"^\s*Co-authored-by:\s*(.+?)\s*<([^>]*)>", re.I | re.M)
AUTOMATED = re.compile(r"^(?:no-?reply|agent|bot|ai)@(?!users\.noreply\.github\.com)", re.I)
# Identities counted as human whose address looks automated: candidates for the AGENTS table
SUSPECTS = collections.Counter()
NOREPLY = re.compile(r"^(?:\d+\+)?([^@+]+)@users\.noreply\.github\.com$", re.I)

def agent_family(name, email=""):
    ident = f"{name} <{email}>".lower()
    for family, pattern in AGENTS:
        if pattern.search(ident): return family
    return None

def is_bot(name, email=""):
    return name.lower().endswith("[bot]") or "[bot]@" in email.lower()

def bot_name(name):
    """One spelling per bot: the API says `dependabot`, git says `dependabot[bot]`."""
    return re.sub(r"\[bot\]$", "", name, flags=re.I) + "[bot]"

def model_name(name):
    """The agent's name as written, without context-window notes: `Claude Opus 5.5 (1M context)` -> `Claude Opus 5.5`."""
    return re.sub(r"\s*\(\d+[KM] context\)", "", name).strip()

class Identities:
    """Resolve a git identity (name + email) to one contributor id: `@login` where GitHub tells us, else the name.

    Evidence for a login: a GitHub noreply address; a squash-merge commit, whose git author is the
    PR's author; or, more weakly, being the main commit author inside a PR that login opened. A name alone is trusted only when nearly all of its evidence points at one login.
    """
    def __init__(self):
        self.by_email = collections.defaultdict(collections.Counter)
        self.by_name = collections.defaultdict(collections.Counter)
        self.canonical = {}
        self.votes = collections.defaultdict(collections.Counter)

    def learn(self, name, email, login):
        if not login or agent_family(name, email) or is_bot(name, email): return
        login = self.canonical.setdefault(login.lower(), login)
        if email: self.by_email[email.lower()][login] += 1
        if name: self.by_name[name.lower()][login] += 1

    def vote(self, name, email, login):
        """A weaker hint: `name <email>` wrote most of the commits in a PR opened by `login`."""
        if login and not agent_family(name, email) and not is_bot(name, email):
            self.votes[(name, email)][self.canonical.setdefault(login.lower(), login)] += 1

    def settle_votes(self):
        """Accept a PR-commit hint when the identity looks like the login, or several PRs agree."""
        norm = lambda text: re.sub(r"[^a-z0-9]", "", (text or "").lower())
        for (name, email), logins in self.votes.items():
            if (email or "").lower() in self.by_email: continue
            login, n = logins.most_common(1)[0]
            a, b, c = norm(login), norm(name), norm((email or "").split("@")[0])
            alike = len(a) >= 3 and any(len(x) >= 3 and (a in x or x in a) for x in (b, c))
            if alike or (n >= 2 and n >= 0.8 * sum(logins.values())):
                self.learn(name, email, login)

    def login(self, login):
        return "@" + self.canonical.setdefault(login.lower(), login)

    def resolve(self, name, email):
        m = NOREPLY.match(email or "")
        if m: return self.login(m[1])
        known = self.by_email.get((email or "").lower())
        if known: return "@" + known.most_common(1)[0][0]
        named = self.by_name.get((name or "").lower())
        if named:
            # The odd squash commit carries a maintainer's name on someone else's PR, so ask for
            # a clear majority rather than a single login
            top, n = named.most_common(1)[0]
            if n >= 0.9 * sum(named.values()): return "@" + top
        # A git name that is itself a known login, give or take spaces and case
        as_login = self.canonical.get(re.sub(r"\s+", "", (name or "").lower()))
        if as_login: return "@" + as_login
        return name or "(unknown)"

def contributors(change_commits, pr, ids):
    """Humans, agents and bots behind one change, read from its commits and its PR (if any)."""
    humans, agents_author, agents_co, models, bots = [], set(), set(), set(), set()
    def person(name, email, into):
        family = agent_family(name, email)
        if family: into.add(family); models.add(model_name(name)); return
        if is_bot(name, email): bots.add(bot_name(name)); return
        if AUTOMATED.match(email or ""): SUSPECTS[name] += 1
        who = ids.resolve(name, email)
        if who not in humans: humans.append(who)
    author = None
    if pr and pr.get("author"):
        if pr.get("authorType") == "Bot": bots.add(bot_name(pr["author"]))
        elif agent_family(pr["author"]): agents_author.add(agent_family(pr["author"]))
        else: author = ids.login(pr["author"]); humans.append(author)
    for cm in change_commits:
        person(cm["author"], cm["email"], agents_author)
        for name, email in TRAILER.findall(cm["body"]): person(name, email, agents_co)
        for tool in GENERATED.findall(cm["body"]): agents_co.add(GENERATED_FAMILY[tool.lower()])
    if author is None and humans: author = humans[0]
    return dict(human=author, coauthors=[h for h in humans if h != author],
                agents_author=sorted(agents_author), agents_coauthor=sorted(agents_co - agents_author),
                agent_models=sorted(models), bots=sorted(bots))
