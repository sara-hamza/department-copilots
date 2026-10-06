---
description: Explain a config, protocol behaviour or routing decision plainly, with a worked packet or route path
argument-hint: <paste the config or output, or ask the question>
---

Run the network-engineer skill in **explain** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Identify what is being asked: a config stanza, a protocol behaviour, a routing decision, or an unexpected output.
2. Output the Explain template: WHAT THIS DOES (plain language, three to six lines), WORKED PATH (a single packet or route followed hop by hop through the pasted config, naming each decision point), WHY IT BEHAVES THIS WAY (the protocol rule that applies), WATCH OUT FOR (common misreadings or side effects), WHERE TO READ MORE (the vendor command from `references/verification-commands.md` that shows the behaviour live).
3. Pitch the explanation at a network engineer who knows the basics but not this stanza. Define a term only the first time it appears.
4. Never invent config that was not pasted. If the worked path depends on a stanza not shown (for example a route-map referenced but not included), stop the path there and list it under MISSING INFORMATION.
5. Input missing: if nothing was pasted and no question was asked, ask for the stanza or output to explain.
