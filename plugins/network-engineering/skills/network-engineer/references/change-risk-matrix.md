# Change risk matrix

Score a change on four axes, take the highest axis as the overall rating, then apply the controls for that rating. State the score and the axis that drove it in the review.

## Axis 1: blast radius (who can be affected)

| Score | Scope | Examples |
|---|---|---|
| 1 | One device, no customer-facing effect | Description change, syslog server, SNMP ACL |
| 2 | One device, one service or one PON | Single service port, single ONT profile, single VLAN add |
| 3 | One site or OLT | OLT uplink, aggregation switch config, IGP metric on one link |
| 4 | Region or RSP | Policy change on an RSP NNI, route reflector change, IGP area change |
| 5 | Whole network | Core routing policy, default route, SRGB, AAA server change |

## Axis 2: reversibility

| Score | Reversibility | Examples |
|---|---|---|
| 1 | Instant, automatic | Junos `commit confirmed`, Nokia rollback checkpoint |
| 2 | Instant, manual | Reverse command known and tested |
| 3 | Minutes, with convergence | Routing policy revert, IGP metric revert |
| 4 | Requires a second window or vendor | Software upgrade, hardware swap |
| 5 | Not cleanly reversible | Renumbering, data migration, licence change |

## Axis 3: protocol impact

| Score | Impact | Examples |
|---|---|---|
| 1 | None | Cosmetic, logging |
| 2 | Local only, no convergence | Interface description, QoS counter reset |
| 3 | Convergence on one protocol | IGP metric change, BGP policy on one neighbour |
| 4 | Convergence on several protocols or session reset | BGP session bounce, IGP area change, MTU change |
| 5 | Control-plane restart | Software upgrade, RE switchover, AAA change |

## Axis 4: window and timing

| Score | Timing | Notes |
|---|---|---|
| 1 | Business hours, no impact possible | Reads, descriptions |
| 2 | Business hours, impact bounded to one service, customer informed | Single service work |
| 3 | Standard maintenance window | Default for anything touching routing |
| 4 | Extended window with RSP notification | NNI or RSP-affecting work |
| 5 | Outside any window, or emergency change | Requires incident reference and duty manager approval |

## Overall rating and required controls

| Overall (highest axis) | Rating | Required before go |
|---|---|---|
| 1 to 2 | LOW | Peer review; verification command listed; rollback line |
| 3 | MEDIUM | Change ticket; pre-checks recorded; window agreed; rollback tested or rehearsed; verification checklist |
| 4 | HIGH | All MEDIUM controls plus RSP notification (if NNI or RSP-affecting), second engineer on the bridge, lab rehearsal recommended (see build-lab), go/no-go criteria written |
| 5 | CRITICAL | All HIGH controls plus CAB approval, vendor TAC case open if software or hardware, staged rollout (one node first), customer communication plan |

## Standard risk statements

Reuse these in the RISKS section with the reason from the paste:

| Risk | Typical reason | What limits it |
|---|---|---|
| Route leak | Export policy not restricted after adding a peer | Explicit export policy, max-prefix on the receiving side |
| Traffic black-hole | Next hop unreachable after policy or IGP change | Pre-check next-hop reachability, BFD, verify RIB after change |
| Session reset | Changing AS, password, TTL, address family on an established BGP session | Schedule in window, notify RSP, graceful shutdown first |
| MTU mismatch | Adding QinQ or an MPLS label layer | Check path MTU with a sized ping before and after |
| Asymmetric routing | Metric changed on one direction only | Change both ends in the same step |
| Lost management access | ACL, AAA or management VRF change | Console or out-of-band first; `commit confirmed` |
| Convergence storm | IGP area change or many prefixes withdrawn at once | Stage the change, lower timers only if designed |
| Capacity shortfall | Traffic moved to a link without checking load | Pre-check utilisation on the receiving link |

## Pre-check minimum set by rating

| Rating | Record before the change |
|---|---|
| LOW | Interface state of touched interfaces |
| MEDIUM | Plus IGP adjacency count, BGP summary (prefix counts per neighbour), route to the affected prefixes, label bindings if MPLS |
| HIGH | Plus traffic counters on affected links, RSP service counts on the NNI, full config save and diff, lab rehearsal result |
| CRITICAL | Plus vendor TAC reference, communication sent, rollback rehearsed and timed |

## Rollback triggers

Write at least one trigger per risk. Examples:

- BGP prefix count from neighbour X drops by more than 10% of the pre-check value within 5 minutes.
- Any IGP adjacency that was Up in the pre-check is not Up 2 minutes after commit.
- NNI traffic counters stop incrementing in either direction.
- More than N ONT or service alarms raised on the affected OLT within 5 minutes (CUSTOMISE N).

## CUSTOMISE: company change rules

- Standard maintenance window: `<e.g. Tue/Thu 00:00 to 05:00 local>` (verify)
- RSP notification lead time for NNI-affecting work: `<e.g. 5 business days>` (verify)
- CAB cadence and emergency change approver: `<fill in>`
- Alarm-count rollback threshold (N above): `<fill in>`
- Change ticket system name (for the ticket note only; never accessed): `<fill in>`
