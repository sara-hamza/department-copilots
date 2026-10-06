---
description: Review a pasted config (Junos, Cisco/Arista, Huawei/Nokia OLT) for syntax, routing policy, redundancy, VLAN, QoS and security hygiene
argument-hint: <paste the config snippet, and say what it is for if known>
---

Run the network-engineer skill in **review-config** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Identify the vendor and syntax style from the paste and state it in the first line.
2. Work through every section of `references/config-review-checklist.md` that applies (BGP, IGP, policy, VLAN/L2, QoS, security hygiene, management). Skip sections with no matching config and say which were skipped.
3. Output the Config review template: CONFIG SUMMARY, FINDINGS (High / Medium / Low, each with the line or stanza quoted, the problem and the fix), MISSING OR AMBIGUOUS, SUGGESTED CORRECTIONS (in the same syntax as the paste), QUESTIONS.
4. Flag every neighbour without an explicit import and export policy, every static route without a stated purpose, and every interface without a description.
5. Do not rewrite the whole config. Quote only the lines that need changing.
6. Input missing: if the paste is not a config (for example a diagram description only), say so and ask for the relevant stanzas by name.
