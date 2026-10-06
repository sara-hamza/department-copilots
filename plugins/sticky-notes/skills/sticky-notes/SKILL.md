---
name: sticky-notes
description: This skill should be used when an employee wants to remember something, jot a note, save an action item, "note that", "remind me", "what did I write about X", "what's open on ticket Y", "give me everything I have on project Z", or build a context bundle for a task. It is personal local memory stored as Markdown under ~/.copilots/sticky-notes with no sync and no integrations.
version: 1.0.0
---

# Sticky Notes

Personal, local memory. Every note is a plain Markdown file the employee owns and can open in any editor.

## Storage

- Directory: `~/.copilots/sticky-notes/` (override with `COPILOT_NOTES_DIR`).
- One file per note: `YYYYMMDD-HHMM-<slug>.md` with a small header (`id`, `created`, `topic`, `tags`) and a Markdown body.
- Action items are ordinary checkboxes: `- [ ] text`. Ticking them edits the file in place.
- Nothing else is ever written anywhere. Nothing leaves the machine.

## The script

All operations go through the bundled script:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/sticky-notes/scripts/notes.py" <command> ...
```

| Command | Purpose |
|---|---|
| `add "text" [--topic T] [--tags a,b] [--title TITLE]` | Save a note. Put action items in the text as `- [ ] ...` lines |
| `list [--topic T] [--tag X] [--days N] [--limit N]` | Newest first, one line each |
| `search "words" [--topic T]` | Keyword search with matching lines |
| `actions [--topic T] [--all]` | Open checkbox items across notes |
| `done NOTE_ID N` | Tick the Nth open action in a note |
| `bundle TOPIC-or-words [--days N]` | Full text of every matching note plus consolidated open actions |
| `topics` | Topics with counts |
| `path` | Where the files live |

## How to behave

**Capturing.** When the employee says "note that ...", "remember ...", "add an action ...": save immediately with `add`. Infer a `--topic` from the conversation (ticket number, estate name, project, person) and 1-3 `--tags` (department or theme). Write actions as checkbox lines. Confirm in one line with the note id. Do not rewrite the employee's wording beyond fixing obvious typos.

**Recalling.** "What did I note about X" → `search`. "What's open" → `actions`, optionally scoped by topic. Present results as-is; do not summarise away detail the employee might need.

**Context bundles.** When the employee starts a task ("working on ticket 48812 again", "prep for the Elm Estate meeting"), run `bundle <topic>` and use the result as background for the department skill. Offer to save the outcome of the task back as a new note on the same topic.

**Organising.** On request, propose topic/tag clean-ups, but only rename or edit files when the employee agrees; show what will change first.

## Privacy

Follow `copilot-common` privacy rules. Do not put customer personal data into notes unless the employee dictates it. Never copy notes into outputs shared outside the team without the employee asking.
