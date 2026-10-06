---
description: Interpret ONT status, 1490/1310 RX levels, OTDR events and power meter readings - ranked causes, evidence, next test, when to escalate
argument-hint: <type the readings and status, or drop a photo of the test set or ONT>
---

Run the field-assistant skill in **interpret** mode on:

$ARGUMENTS

Steps:
1. Apply `copilot-common` privacy rules. If a photo or screenshot of a test set or ONT was supplied, transcribe it first (screenshot-reader) into a READ FROM IMAGE block; keep units and mark unclear digits with (?).
2. Classify every reading against `references/optical-interpretation.md`: ONT RX, OLT RX from ONT, OTDR events (reflective vs non-reflective, end of fibre, macrobend, dirty connector), power meter values at each test point.
3. Use the decision tree in `references/field-test-sequence.md` to rank causes from the premises outward, using adjacent ONT status and OLT port state as the main discriminators.
4. Output the Interpret template: LIKELY CAUSE(S) (ranked, with a confidence word), EVIDENCE (✓ / ✗ / ?), NEXT FIELD TEST (one test only, the cheapest that discriminates the top two causes, with where to connect and what result means what), WHEN TO ESCALATE.
5. Worked pattern to reuse: ONT Offline, 1490 nm RX -30.1 dBm, OLT port operational, adjacent ONTs online points to the drop, lead-in or premises fibre; next test is a power meter at the premises side of the lead-in, then at the pit.
6. Input missing: if no readings were given, list under MISSING INFORMATION the four readings that matter most (ONT state and LOS LED, ONT RX, adjacent ONT status, OLT port state) and stop.
