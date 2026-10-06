---
description: Tick off an open action item in a sticky note
argument-hint: <note-id> <action-number>   (or describe the action in words)
allowed-tools: ["Bash"]
---

Mark a sticky-note action as done.

Arguments: $ARGUMENTS

- If a note id and number are given: `python3 "${CLAUDE_PLUGIN_ROOT}/skills/sticky-notes/scripts/notes.py" done <note-id> <n>`.
- If the action is described in words instead: run `... actions`, find the single best match, and if exactly one matches, tick it. If several match, list them with their note id and number and ask which one.
- Confirm in one line what was ticked.
