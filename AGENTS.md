# GSP knowledge base

This repository is the single source of truth for our work with **Global Shipping Partners (GSP)**. Every AI agent (Claude Code or any other) and every teammate reads this file first.

If you are a new session: read this file, then [README.md](README.md), then [project/status.md](project/status.md). That is enough to be up to speed. Go deeper through the [map](#where-to-look) only as the task needs.

**Sync both ways.** Other sessions, agents and teammates edit this repository too. At the start of every session, pull the latest version (`git pull`) before reading or writing. At the end of any session that changed something, commit and push, so the next session sees it. Work that stays in a chat and never reaches this repository is lost.

## Absolute law

Do not break these rules. If anything elsewhere in this repository disagrees with this section, this section wins. If unsure, stop and ask, and do not take the looser reading.

### Confirmation gate

Before changing anything outside this repository (a website, an account, a DNS record, a client-facing message):

1. Restate the request in your own words: outcome, scope, constraints.
2. Say what you believe is out of scope.
3. Ask clarifying questions about anything vague.
4. Wait for explicit approval.

A restatement, silence, or an earlier conversation is not approval for a new change. Read-only work (reading, researching, drafting inside this repo) does not need the gate.

### Chesterton's fence

Do not remove, rename, or "clean up" anything you do not understand: on the client's live site, in their accounts, or in this repository. Check [decisions/](decisions/) and [logs/](logs/) first, then ask.

### Pareto principle

Do the small part of the work that carries most of the result first.

### Client-facing changes

Nothing goes live on a GSP property (the live site, the staging site, DNS, email, Google Business Profile, directory listings, social accounts) without approval for that exact change. Drafts and previews are fine when asked for.

### Approvers

- **Our side:** Krischan.
- **Client sign-off** for anything public-facing (copy, design, launch): Jason Kwon, through the team, never by an agent contacting him directly.

### Credentials

Do not write passwords, API keys, tokens, recovery codes, or card or bank details into this repository in plain text. Record **which** accounts exist and **where** each login is kept in [map/accounts.md](map/accounts.md). The team's choice of where logins are kept is open in [decisions/0002-credentials.md](decisions/0002-credentials.md); until it is decided, ask a teammate.

### Other clients

This repository is about GSP only. Never bring in names, accounts, or details from any other client or from the team's other repositories.

## Keeping this repository true

- **Facts carry a source and date.** Write where a fact came from (client said it, their site, a directory) and when. Mark guesses as guesses.
- **Research** goes in [research/](research/), one dated file per piece of work. Use the `research-note` skill.
- **The client's world** (company, people, brand, competitors) lives in [client/](client/). Update it when research or the client changes what we know.
- **Our work** (scope, status, roadmap) lives in [project/](project/). Keep [project/status.md](project/status.md) current: it is the first thing a new session reads.
- **Decisions** that someone might later want to undo go in [decisions/](decisions/).
- **Logs:** end every session that changed something with a log in [logs/](logs/). Use the `session-log` skill. Never rewrite an old log.
- **Open questions** for the client go in [project/open-questions.md](project/open-questions.md), and come out when answered.
- Keep this file short. Put detail in linked files.

## Where to look

| Looking for | Go to |
| --- | --- |
| Where things stand right now | [project/status.md](project/status.md) |
| Who GSP is: services, offices, history | [client/company.md](client/company.md) |
| Jason Kwon and other client contacts | [client/people.md](client/people.md) |
| Brand, messaging, what the client dislikes | [client/brand.md](client/brand.md) |
| What we are delivering and when | [project/scope.md](project/scope.md) |
| The long-term plan and business vision | [project/roadmap.md](project/roadmap.md) |
| Questions waiting on the client | [project/open-questions.md](project/open-questions.md) |
| Prep for the next client meeting | [project/next-meeting.md](project/next-meeting.md) |
| Competitors and partners | [client/competitors.md](client/competitors.md) |
| Accounts, domains, tools, where logins are kept | [map/accounts.md](map/accounts.md) |
| Audits and research | [research/](research/) |
| Reports and other client deliverables | [deliverables/](deliverables/) |
| Why things are the way they are | [decisions/](decisions/) |
| What already happened | [logs/](logs/) |
