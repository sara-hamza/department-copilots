---
description: Build a context bundle (all notes + open actions) for a topic or search term before starting work on it
argument-hint: <topic or words> [days:<n>]
allowed-tools: ["Bash"]
---

Assemble background for a task from sticky notes.

Arguments: $ARGUMENTS

1. Run `python3 "${CLAUDE_PLUGIN_ROOT}/skills/sticky-notes/scripts/notes.py" bundle "<topic or words>"` (add `--days <n>` if given).
2. Print the bundle in a code block.
3. Below it, write a short `WHERE THIS STANDS` section: 3-6 lines synthesising the notes chronologically, then `OPEN ACTIONS` restated, then `SUGGESTED NEXT STEP` (one line). Keep to what the notes say.
4. Keep this bundle in mind for the rest of the session: if the employee then invokes a department copilot on the same topic, use it as context without re-running the script.
