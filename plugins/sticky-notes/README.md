# sticky-notes

Personal local memory. Plain Markdown files under `~/.copilots/sticky-notes/` (override with `COPILOT_NOTES_DIR`). No sync, no integrations.

| Command | Use |
|---|---|
| `/sticky-notes:note <text>` | Save a note; to-dos become `- [ ]` checkboxes. Optional `topic:<t>` `tags:<a,b>` |
| `/sticky-notes:notes [words]` | List or search |
| `/sticky-notes:actions [topic:<t>]` | Open actions across notes |
| `/sticky-notes:done <id> <n>` | Tick an action |
| `/sticky-notes:bundle <topic>` | Everything on a topic plus open actions, as context before a task |

The script `skills/sticky-notes/scripts/notes.py` is stdlib-only and can be run by hand:

```bash
python3 ~/.claude/plugins/cache/department-copilots/sticky-notes/*/skills/sticky-notes/scripts/notes.py list
```
