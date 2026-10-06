---
description: Save a sticky note (with optional action items) to local personal memory
argument-hint: <text to remember> [topic:<topic>] [tags:<a,b>]
allowed-tools: ["Bash"]
---

Save the following as a sticky note using the sticky-notes skill:

$ARGUMENTS

Rules:
- If the text contains `topic:<x>` or `tags:<a,b>` tokens, strip them and pass as `--topic` / `--tags`. Otherwise infer a topic from the current conversation (ticket number, estate, project, person) and 1-3 tags; if nothing is inferable, omit them.
- Turn anything phrased as a to-do ("ask", "chase", "follow up", "check", "send") into `- [ ] ...` checkbox lines, keeping the employee's words.
- Run: `python3 "${CLAUDE_PLUGIN_ROOT}/skills/sticky-notes/scripts/notes.py" add "<text>" --topic <t> --tags <tags>`
- Reply with one line: the note id, topic, and number of actions captured.
