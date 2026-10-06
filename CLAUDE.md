# Department Copilots - maintainer notes

This repo is a Claude Code plugin marketplace. Root manifest: `.claude-plugin/marketplace.json`. Plugins live in `plugins/<name>/`.

## Conventions every plugin must follow

1. **Local only.** No MCP servers, no network calls, no hooks that read company systems. The only writes to disk are Sticky Notes under `~/.copilots/sticky-notes/`.
2. **Same loop everywhere:** INPUT → UNDERSTAND → REASON → ASSIST → HUMAN. The employee decides; the plugin never claims to have acted.
3. **Every skill starts by applying `copilot-common` privacy rules** (see `plugins/copilot-common/skills/privacy-rules/SKILL.md`).
4. **Output formats are plain text blocks** with UPPERCASE section headers (`LIKELY FAULT DOMAIN`, `EVIDENCE`, `NEXT CHECKS` ...) so they paste cleanly into tickets, emails and Teams.
5. **Commands are modes.** `commands/<mode>.md` with frontmatter `description`, `argument-hint`. The body says what input to expect, which reference file to read, and which output template to use.
6. **Skills hold the knowledge.** `skills/<skill>/SKILL.md` under 400 lines; detail goes in `references/`.
7. **Australian English** (analyse, prioritise, programme for schedules, colour).
8. **Never fabricate evidence.** If the input lacks something, say so under a MISSING INFORMATION / QUESTIONS heading.

## Adding a department plugin

Copy `plugins/noc/` as the template, rename, rewrite SKILL.md + references + commands, add an entry to `marketplace.json`, run `python3 scripts/validate.py`.
