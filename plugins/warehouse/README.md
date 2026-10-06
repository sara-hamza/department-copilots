# warehouse - Warehouse Assistant

Drop in the stock export, pick lists or usage history and get back which items are running low, what has not moved in six months, which SKUs look like duplicates, and what will probably be needed next month, with the basis stated under every table.

| Command | Use when |
|---|---|
| `/warehouse:stock-analysis <stock export>` | Full picture: LOW STOCK, SLOW MOVERS, DUPLICATE CANDIDATES, REPLENISHMENT RECOMMENDATION, ASSUMPTIONS |
| `/warehouse:shortages <stock export>` | Only what is low, zero or negative against minimum levels or usage |
| `/warehouse:duplicates <stock export or item master>` | Items that appear to be the same thing under different codes or descriptions |
| `/warehouse:forecast <usage history + stock>` | What next month will probably require, from the usage history supplied |

Requires `copilot-common` (its spreadsheet-reader profiler does the file reading).

Reference knowledge lives in `skills/warehouse-assistant/references/`. Minimum levels, slow-mover windows and safety stock rules there are sensible defaults marked `CUSTOMISE`; tune them to the company's inventory policy.

The assistant analyses the export. It does not adjust stock, merge SKUs or raise orders.
