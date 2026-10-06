---
description: Show open action items across your sticky notes
argument-hint: [topic:<topic>] [all]
allowed-tools: ["Bash"]
---

List open actions from sticky notes.

Arguments: $ARGUMENTS

- Run `python3 "${CLAUDE_PLUGIN_ROOT}/skills/sticky-notes/scripts/notes.py" actions` with `--topic <t>` if a `topic:` token is given and `--all` if the word `all` is given.
- Print the output verbatim in a code block.
- Then, if there are more than five open actions, suggest the three that look most time-sensitive based on their wording (dates, "today", "before", "blocked"). Do not invent priorities beyond what the text supports.
