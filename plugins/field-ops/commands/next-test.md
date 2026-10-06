---
description: Only the next cheapest field test, given what has been tested so far
argument-hint: <what you have tested, the results, and where you are standing>
---

Run the field-assistant skill in **next-test** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules.
2. Place the technician on the decision tree in `references/field-test-sequence.md` using only the tests they say they have done. Do not assume any test was done.
3. Output only:
```
NEXT FIELD TEST
<one test: where to connect, which wavelength or setting, what to record>

IF IT SHOWS ... THEN ...
<two or three branches, each naming the following test or the escalation>

WHY THIS ONE
<one line: it is the cheapest test that separates the top two remaining causes>
```
4. Prefer tests in this order of cost: visual and LED checks, clean and reseat, power meter, VFL, OTDR, splice or re-termination, closure or pit entry. Use the thresholds in `references/optical-interpretation.md`.
5. Input missing: if no tests or readings were given, make the first test "ONT LEDs and RX at the ONT port" and say why.
