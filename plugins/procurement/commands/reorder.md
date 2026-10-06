---
description: Reorder plan from current stock, usage history and supplier lead times - what to order, how much, by when
argument-hint: <drop the stock export and usage history (CSV/XLSX) or paste them; give lead times and any minimum order quantities>
allowed-tools: ["Bash"]
---

Run the procurement-assistant skill in **reorder** mode on:

$ARGUMENTS

Steps:
1. If a CSV/XLSX is provided, apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first) to identify item, on-hand, on-order, usage and lead-time columns, then compute with a short Python snippet. Show results, not code.
2. Follow `references/reorder-planning-method.md`: average daily usage from the history supplied, reorder point = usage x lead time + safety stock, order quantity to cover the review period or the MOQ, whichever is larger. Use the CUSTOMISE defaults for safety stock and review period unless the employee gives values.
3. Produce the REORDER PLAN template from SKILL.md: BASIS (period of usage history, lead times used, safety stock rule), ORDER NOW table (Item, On hand, On order, Daily usage, Lead time days, Reorder point, Days of cover, Suggested qty, Supplier if known), ORDER SOON (within the review period), NO ACTION (count only), ASSUMPTIONS, QUESTIONS.
4. Days of cover = (on hand + on order) / daily usage. Items with zero usage in the period are excluded from ORDER NOW and listed under ASSUMPTIONS as "no usage in period; not forecast".
5. If lead times are missing, use the CUSTOMISE default and state it per item; never silently assume.
6. The plan is a recommendation for the procurement officer to raise POs against; do not write "ordered" or "PO raised".
