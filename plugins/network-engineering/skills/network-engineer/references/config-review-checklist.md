# Config review checklist

Walk every section that matches the paste. Record a finding only where the config shows the problem or the absence is material. Quote the stanza. Severity guide: High = can cause an outage, route leak or security exposure; Medium = degrades redundancy, visibility or operability; Low = hygiene.

## 1. General and syntax

| Check | Finding if | Severity |
|---|---|---|
| Syntax matches the stated vendor and release | Mixed syntax, unterminated stanzas, unknown keywords | High |
| Every interface has a description (far end, circuit ID) | Missing | Low |
| Hostname, domain, NTP, timezone, syslog present | Any missing on a new device | Medium |
| Config references an object that is not defined (policy, prefix-list, VLAN, class) | Undefined reference | High |
| Deprecated or platform-unsupported command | Present | Medium |

## 2. Layer 2 and VLAN

| Check | Finding if | Severity |
|---|---|---|
| VLAN defined on both ends of the trunk and in the allow list | One side only | High |
| QinQ: S-VLAN per RSP, C-VLAN mapping consistent OLT to aggregation to NNI | Mapping differs between hops | High |
| MTU consistent along the path, allowing for QinQ (+8) and MPLS labels (+4 each) | Lower MTU on an intermediate hop | High |
| LACP on every multi-member bundle, same mode both ends, min-links set | Static LAG, or min-links absent | Medium |
| Storm control / MAC limit on access-facing ports | Absent on customer-facing or OLT uplink ports | Medium |
| Spanning tree not running toward the OLT or NNI unless designed | Unexpected STP | Medium |
| No unused VLANs left in trunk allow lists | Present | Low |

## 3. IGP (IS-IS or OSPF)

| Check | Finding if | Severity |
|---|---|---|
| Correct area/level on each interface; level-2-only where the design says so | Mismatch | High |
| Authentication on all adjacencies, same key on both ends | Missing or asymmetric | Medium |
| Loopback advertised with a /32 (/128) and passive | Not passive, or wrong mask | Medium |
| Metrics match the design (primary vs secondary path) | Default metrics on links that need engineered paths | Medium |
| Wide metrics (IS-IS) enabled consistently | Narrow on some nodes | High |
| BFD on IGP adjacencies where sub-second failover is required | Absent on core links | Medium |
| LDP-IGP sync or SR microloop avoidance where MPLS is used | Absent | Medium |
| Customer-facing or NNI interfaces are passive or excluded from the IGP | Active adjacency toward an RSP | High |

## 4. BGP

| Check | Finding if | Severity |
|---|---|---|
| Every neighbour has an explicit import and export policy | Any neighbour without both | High |
| eBGP export limited to the intended prefixes (prefix-list or community) | Export-all, or "accept everything" default | High |
| Import from an RSP or external peer filters bogons, own prefixes, default route (unless intended) and overly specific prefixes (>/24 v4, >/48 v6) | Missing | High |
| max-prefix set on every eBGP session with a sensible warning threshold | Absent | Medium |
| Route reflector clients correctly set; no full mesh gaps on iBGP | Missing client flag or peer | High |
| next-hop-self on iBGP toward the RR where eBGP next hops are not in the IGP | Absent | High |
| Communities tagged on import (origin, peer type) and acted on at export | No community discipline | Medium |
| Local-preference, MED and AS-path prepend used consistently with the design | Conflicting | Medium |
| Peer description, password or TCP-AO, TTL security on eBGP | Missing | Medium |
| Graceful restart or graceful shutdown community in use for planned work | Absent where maintenance is frequent | Low |
| No static routes that duplicate or override BGP learned routes without reason | Present | Medium |

## 5. Route leak and unintended routing impact

Ask these questions of any change that touches policy:

1. Can a route learned from one external peer be re-advertised to another external peer? If the export policy does not stop it, it is a leak. High.
2. Does a new static or aggregate route attract traffic away from a more specific route that is still needed? High.
3. Does a metric or local-preference change move traffic onto a link that cannot carry it? Check the link capacity. High if unknown.
4. Does the change withdraw a prefix the RSP depends on, even briefly? Medium to High depending on the window.
5. Does the change alter the default route anywhere? High until proven intended.

## 6. MPLS and services

| Check | Finding if | Severity |
|---|---|---|
| LDP or SR enabled on every core interface in the path | Gap | High |
| Label range and SRGB consistent across nodes (SR) | Differ | High |
| Transport MTU covers service MTU plus labels | Short | High |
| L2VPN / EVPN: RD and RT consistent, same VLAN or service MTU both ends | Mismatch | High |
| L3VPN: import/export RT correct, no unintended VRF leaking | Leak | High |
| Pseudowire control word and VCCV settings match both ends | Mismatch | Medium |

## 7. QoS

| Check | Finding if | Severity |
|---|---|---|
| Classification on ingress at the OLT uplink and NNI matches the agreed marking | Missing or different per hop | Medium |
| Queue mapping and scheduler match the service tiers; voice and management queues protected | Absent | Medium |
| Policers on NNI match the RSP contract rate (burst sized sensibly) | Absent or burst far too small | Medium |
| Trust boundary explicit (trust DSCP from RSP, remark from customer) | Trust everything | Medium |

## 8. Security hygiene

| Check | Finding if | Severity |
|---|---|---|
| Management access restricted by ACL / loopback / VRF | Open on all interfaces | High |
| SSH only, no telnet, no HTTP | Present | High |
| AAA with TACACS or RADIUS, local fallback, accounting on | Local users only | Medium |
| SNMP v3 or v2c with ACL and non-default community | Default or open community | High |
| Control-plane policing / protection present | Absent | Medium |
| uRPF or anti-spoof on customer-facing and NNI interfaces where feasible | Absent | Medium |
| No secrets, keys or communities pasted into the review output | Present | Always redact |

## 9. Redundancy

| Check | Finding if | Severity |
|---|---|---|
| Every single-homed element is a known, accepted risk | Unstated single point of failure | Medium |
| Two uplinks, two IGP paths, two BGP sessions (or RR pair) for each aggregation node | One | Medium |
| Failover behaviour is deterministic (metric, local-pref, BFD timers) | Equal cost where the design wants primary/secondary | Medium |

## CUSTOMISE: company platform specifics

Fill in so the review can name platform-specific commands and rules:

- Core and aggregation platform: `<e.g. Juniper MX / Nokia 7750 / Arista 7280>` (verify)
- OLT platform: `<e.g. Huawei MA5800 / Nokia 7360 ISAM>` (verify)
- IGP in use and level/area convention: `<IS-IS level 2 only>` (verify)
- iBGP topology: `<two route reflectors per region>` (verify)
- RSP NNI model: `<QinQ, one S-VLAN per RSP per POI>` (verify)
- Standard import/export policy names to look for: `<RSP-IN / RSP-OUT>` (verify)
- Bogon and max-prefix standards: `<fill in>`
