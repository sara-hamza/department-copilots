---
description: Layered troubleshooting of a routing, MPLS, aggregation or RSP NNI fault from pasted configs, logs and show output
argument-hint: <paste configs, logs, show output, and describe the symptom>
---

Run the network-engineer skill in **troubleshoot** mode on this input:

$ARGUMENTS

Steps:
1. Apply `copilot-common` privacy rules. If a screenshot was provided, transcribe it first (screenshot-reader) into a READ FROM IMAGE block.
2. Walk the layers in order: physical, L2, IGP, BGP, MPLS/services, aggregation to RSP NNI. Stop at the first layer that fails. Use the layer table in SKILL.md and the command table in `references/verification-commands.md` to name the exact commands for the vendor in the paste.
3. Output the Troubleshoot template: LIKELY FAULT LAYER, CONFIDENCE, EVIDENCE (✓ / ✗ / ?), NEXT CHECKS (numbered, each eliminates a layer, with the exact command per vendor), IF THAT SHOWS ... THEN ..., SUGGESTED TICKET NOTE.
4. If the vendor cannot be determined from the paste, give the command for the two most likely platforms and ask which one applies.
5. If the evidence does not reach the layer the engineer suspects, say DO NOT CONCLUDE YET and give the single most discriminating check.
6. Input missing: if no config, log or show output was pasted, list under MISSING INFORMATION exactly what to paste (interface state, IGP adjacency, BGP summary, label bindings, NNI counters) and stop.
