---
description: Tracked list of open items for a development with owner, due date and status; flags stale and ownerless items
argument-hint: <paste project notes, emails, previous open-items list> [as-of:<date>]
---

Run the developer-assistant skill in **open-items** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules.
2. Take the as-of date from an `as-of:` token, else the input, else today. Extract every item that is waiting on someone using the "open item" test in `references/development-intake-checklist.md` (section "What counts as an open item"). Group by the intake topics.
3. Produce exactly this template:

```
OPEN ITEMS: <development> | as of <date>

# | Topic | Item | Owner | Side (Company / Developer / Third party) | Needed by | Status | Last update | Flags
1 | Comms room | ... | ... | Developer | 14 Nov 2026 | Open | 29 Sep 2026 | STALE

SUMMARY
Open: <n>   Developer-side: <n>   our side: <n>   Overdue: <n>   Ownerless: <n>   Stale: <n>

CHASE THIS WEEK (developer-side, ordered by needed-by)
1. <item> | contact | suggested wording from the question bank

INTERNAL THIS WEEK (our side)
1. <item> | owner | due

CLOSED SINCE LAST LIST (if a previous list was provided)
- <item> | closed <date> | evidence

MISSING INFORMATION
<owners, dates or statuses not in the input>
```

4. Flags: STALE (no update in 14 days, CUSTOMISE), OVERDUE (needed-by passed), OWNERLESS, NO DATE. Preserve item numbers from a previous list; number new items from the next free number.
5. Do not close an item unless the input states it was resolved; quote the evidence.
6. If no input is given, ask for the notes or previous list and output the empty table.
