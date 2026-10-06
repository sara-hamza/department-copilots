---
description: What actually needs my attention? Ranked triage of minutes, schedule exports, RAID logs and notes into TODAY, WAITING ON, DECISIONS REQUIRED, SLIPPING and NOTHING NEEDED
argument-hint: <paste minutes, notes, RAID items, or name a schedule/RAID CSV or XLSX file> [as-of:<date>]
allowed-tools: ["Bash"]
---

Run the project-copilot skill in **attention** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. If a spreadsheet (CSV/XLSX schedule or RAID export) is provided, apply the copilot-common spreadsheet-reader skill to profile it before reading rows; state which columns were treated as task, owner, due date, status and % complete. If a PDF is provided, apply document-reader and keep page references.
2. Take the as-of date from an `as-of:` token, else from the input, else today. State the as-of date on the first line.
3. Rank every item using `references/attention-triage-rules.md` (blocked milestone > overdue dependency > unowned decision > stale item > everything else). Use `references/raid-method.md` to recognise risks, issues and dependencies hiding in prose.
4. Produce exactly this template:

```
ATTENTION TRIAGE (as of <date>)

TODAY
1. <item> | why now: <rule that ranked it> | source: <doc/line/row>
2. ...

WAITING ON
<who> | <what> | since <date> | chase by <date> | source

DECISIONS REQUIRED
<decision> | options if known | owner | needed by <date> | source

SLIPPING
<milestone or task> | baseline <date> -> forecast <date> (<n> days) | cause if stated | source

NOTHING NEEDED (explicitly parked)
<item> | why it can wait | revisit <date>

MISSING INFORMATION
<what would change the ranking: owners, due dates, baseline dates, current status>
```

5. Every TODAY item must cite the rule that put it there and its source line or row. Never invent dates or owners; write `owner: TBC` or `due: not stated`.
6. If no input is given, ask for minutes, notes or a schedule/RAID export and list the three inputs that produce the best triage (schedule with baseline and forecast dates, RAID log with owners, latest minutes).
