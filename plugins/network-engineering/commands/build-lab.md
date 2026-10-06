---
description: Produce a minimal reproducible lab topology and configs (containerlab / EVE-NG style) to test a change offline
argument-hint: <paste the change or describe the scenario, and name the vendor images available if known>
---

Run the network-engineer skill in **build-lab** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Replace any production addressing, AS numbers and hostnames with lab equivalents (RFC 5737 / RFC 3849 documentation ranges, private AS 64512 to 65534) unless the engineer asks to keep them.
2. Identify the smallest topology that reproduces the behaviour under test: usually two to four nodes. State what was deliberately left out and why it does not affect the result.
3. Output the Lab template: LAB PURPOSE, TOPOLOGY (ASCII diagram plus node and link table), TOPOLOGY FILE (containerlab YAML by default; EVE-NG notes if asked), NODE CONFIGS (one block per node, vendor-neutral where possible, otherwise in the syntax of the pasted config), TEST STEPS (numbered, with expected result), WHAT PASS LOOKS LIKE, LIMITS OF THIS LAB.
4. Use `references/verification-commands.md` for the show commands in TEST STEPS. Use `references/change-risk-matrix.md` to decide which failure cases must be tested (for example withdraw the prefix, flap the link, lose the primary path).
5. Input missing: if the change under test is not described, ask for it. If the available images are unknown, default to FRR or Nokia SR Linux containers and note that the vendor syntax will differ from production.
