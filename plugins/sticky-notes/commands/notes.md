---
description: List or search your sticky notes
argument-hint: [search words] [topic:<topic>] [tag:<tag>] [days:<n>]
allowed-tools: ["Bash"]
---

Show the employee's sticky notes using the sticky-notes skill.

Arguments: $ARGUMENTS

- No arguments → `python3 "${CLAUDE_PLUGIN_ROOT}/skills/sticky-notes/scripts/notes.py" list --limit 20`
- Words present → `... search "<words>"`, plus `--topic`, `--tag`, `--days` from any `topic:`, `tag:`, `days:` tokens.
- Print the script output verbatim inside a code block. Add at most two lines of observation (for example, which topic has the most open actions). Do not summarise notes away.
