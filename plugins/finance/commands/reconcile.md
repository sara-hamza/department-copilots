---
description: Reconcile two lists that should agree (ledger vs statement, PO lines vs invoices, bank vs cashbook) into MATCHED / ONLY IN A / ONLY IN B / AMOUNT DIFFERENCES
argument-hint: <drop or paste list A and list B; say which is which and what the matching key is if known>
allowed-tools: ["Bash"]
---

Run the finance-reviewer skill in **reconcile** mode on:

$ARGUMENTS

Steps:
1. If CSV/XLSX files are provided, apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first) on each list to find the key and amount columns, then match with a short Python snippet. Show results, not code.
2. Follow `references/reconciliation-method.md`: pick the matching key (reference, invoice number, date plus amount), normalise it, match exact first, then tolerance matches, then one-to-many combinations only where the method allows.
3. Produce the RECONCILIATION template from SKILL.md: BASIS (what A and B are, key used, tolerance), SUMMARY (count and total for each list, matched, unmatched each side, net difference), MATCHED (count and total only unless asked), ONLY IN A, ONLY IN B, AMOUNT DIFFERENCES (Key, A amount, B amount, Difference), PROBABLE EXPLANATIONS and NEXT STEPS FOR THE REVIEWER.
4. Totals must reconcile: A total minus B total must equal the sum of ONLY IN A minus ONLY IN B plus AMOUNT DIFFERENCES. Show that check line.
5. If the lists share no usable key, say so and offer the best fallback (date plus amount) with its risk of false matches.
