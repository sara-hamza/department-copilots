# Verification commands (multi-vendor)

Use the column that matches the vendor in the paste. If the vendor is unknown, give the two most likely and ask. Commands are the common forms; check release-specific syntax on the device. "Nokia SR" covers 7750 SR OS; "Huawei OLT" covers MA5800 style VRP; "Nokia OLT" covers 7360 ISAM.

## Interface and physical

| What | Junos | Cisco IOS-XR / IOS-XE | Arista EOS | Nokia SR OS | Huawei VRP / OLT |
|---|---|---|---|---|---|
| Interface state and errors | `show interfaces <if> extensive` | `show interfaces <if>` | `show interfaces <if>` | `show port <port> detail` | `display interface <if>` |
| Optics levels | `show interfaces diagnostics optics <if>` | `show controllers <if> phy` (XR) / `show interfaces <if> transceiver` (XE) | `show interfaces <if> transceiver` | `show port <port> optical` | `display transceiver interface <if>` / OLT: `display port state <f/s/p>` |
| LAG / LACP | `show lacp interfaces` | `show lacp` / `show bundle` (XR) | `show port-channel summary` / `show lacp neighbor` | `show lag <id> detail` | `display eth-trunk <id>` / `display lacp` |
| Error counters only | `show interfaces <if> statistics` | `show interfaces <if> counters errors` | `show interfaces counters errors` | `show port <port> statistics` | `display interface <if> counters` |

## Layer 2 and VLAN

| What | Junos | Cisco | Arista | Nokia SR OS | Huawei VRP / OLT |
|---|---|---|---|---|---|
| VLANs on a trunk | `show vlans <name>` / `show interfaces <if> brief` | `show interfaces trunk` / `show vlan` | `show vlan` / `show interfaces trunk` | `show service sap-using` | `display vlan <id>` / `display port vlan <if>` |
| MAC table | `show ethernet-switching table` / `show bridge mac-table` | `show mac address-table` (XE) / `show l2vpn forwarding bridge-domain mac-address` (XR) | `show mac address-table` | `show service id <id> fdb-mac` | `display mac-address` / OLT: `display mac-address port <f/s/p>` |
| MTU on path | `show interfaces <if>` (MTU line) | `show interfaces <if>` | `show interfaces <if>` | `show port <port>` | `display interface <if>` |
| OLT service port mapping | n/a | n/a | n/a | n/a | `display service-port port <f/s/p>` / `display ont info <f/s/p> <ont-id>` |
| Nokia OLT ONT and service | n/a | n/a | n/a | n/a | `show equipment ont status pon <pon>` / `show vlan bridge-port-fdb` |

## IGP

| What | Junos | Cisco | Arista | Nokia SR OS | Huawei VRP |
|---|---|---|---|---|---|
| IS-IS adjacency | `show isis adjacency` | `show isis adjacency` / `show isis neighbors` (XE) | `show isis neighbors` | `show router isis adjacency` | `display isis peer` |
| OSPF neighbour | `show ospf neighbor` | `show ospf neighbor` | `show ip ospf neighbor` | `show router ospf neighbor` | `display ospf peer` |
| IGP route to a loopback | `show route <prefix> protocol isis` | `show route <prefix>` / `show isis route` | `show ip route <prefix>` | `show router route-table <prefix>` | `display ip routing-table <prefix>` |
| LSDB / topology sanity | `show isis database detail` | `show isis database` | `show isis database` | `show router isis database` | `display isis lsdb` |
| BFD sessions | `show bfd session` | `show bfd session` | `show bfd peers` | `show router bfd session` | `display bfd session all` |

## BGP

| What | Junos | Cisco | Arista | Nokia SR OS | Huawei VRP |
|---|---|---|---|---|---|
| Session summary | `show bgp summary` | `show bgp summary` / `show bgp ipv4 unicast summary` | `show ip bgp summary` | `show router bgp summary` | `display bgp peer` |
| Neighbour detail and policies | `show bgp neighbor <ip>` | `show bgp neighbor <ip>` | `show ip bgp neighbors <ip>` | `show router bgp neighbor <ip>` | `display bgp peer <ip> verbose` |
| Prefixes received from a peer | `show route receive-protocol bgp <ip>` | `show bgp neighbor <ip> routes` / `received-routes` | `show ip bgp neighbors <ip> received-routes` | `show router bgp neighbor <ip> received-routes` | `display bgp routing-table peer <ip> received-routes` |
| Prefixes advertised to a peer | `show route advertising-protocol bgp <ip>` | `show bgp neighbor <ip> advertised-routes` | `show ip bgp neighbors <ip> advertised-routes` | `show router bgp neighbor <ip> advertised-routes` | `display bgp routing-table peer <ip> advertised-routes` |
| Why a path was chosen | `show route <prefix> detail` | `show bgp <prefix>` | `show ip bgp <prefix>` | `show router bgp routes <prefix> detail` | `display bgp routing-table <prefix>` |
| Test a policy offline | `test policy <policy> <prefix>` | `show bgp policy ...` (XR, limited) | n/a | `show router policy <name>` | n/a |
| Max-prefix state | in neighbour detail | in neighbour detail | in neighbour detail | in neighbour detail | in peer verbose |

## MPLS and services

| What | Junos | Cisco | Arista | Nokia SR OS | Huawei VRP |
|---|---|---|---|---|---|
| LDP neighbours | `show ldp neighbor` | `show mpls ldp neighbor` | `show mpls ldp neighbor` | `show router ldp session` | `display mpls ldp session` |
| Label bindings for a prefix | `show route <prefix> table inet.3` / `show ldp database` | `show mpls ldp bindings <prefix>` | `show mpls ldp bindings` | `show router ldp bindings prefix <prefix>` | `display mpls ldp lsp <prefix>` |
| SR / SRGB | `show isis overview` / `show route table inet.3` | `show isis segment-routing label table` | `show isis segment-routing` | `show router isis sr-database` | `display segment-routing prefix-sid` |
| LSP ping / trace | `ping mpls ldp <prefix>` / `traceroute mpls ldp <prefix>` | `ping mpls ipv4 <prefix>` / `traceroute mpls ipv4 <prefix>` | `ping mpls ldp <prefix>` | `oam lsp-ping prefix <prefix>` / `oam lsp-trace` | `ping lsp ip <prefix>` / `tracert lsp ip <prefix>` |
| L2VPN / pseudowire state | `show l2circuit connections` / `show evpn instance` | `show l2vpn xconnect` / `show l2vpn bridge-domain` | `show bgp evpn` / `show vxlan ...` | `show service id <id> sdp` / `show service id <id> base` | `display mpls l2vc` / `display evpn ...` |
| L3VPN routes | `show route table <vrf>.inet.0` | `show route vrf <vrf>` | `show ip route vrf <vrf>` | `show router <vprn-id> route-table` | `display ip routing-table vpn-instance <vrf>` |

## Aggregation to RSP NNI

| What | Junos | Cisco | Arista | Nokia SR OS | Note |
|---|---|---|---|---|---|
| NNI LAG state and members | `show lacp interfaces ae<N>` | `show bundle Bundle-Ether<N>` | `show port-channel <N> detailed` | `show lag <id> detail` | All members must be collecting/distributing |
| VLANs mapped on the NNI | `show interfaces ae<N>.<unit>` / `show vlans` | `show interfaces trunk` / `show l2vpn ...` | `show interfaces vlans` | `show service sap-using sap lag-<id>` | Compare with the RSP's expected S-VLAN list |
| Traffic both directions | `monitor interface ae<N>` / `show interfaces ae<N> statistics` | `show interfaces Bundle-Ether<N> accounting` | `show interfaces port-channel<N> counters rates` | `monitor port lag-<id>` | Zero in one direction points at the far end |
| Policer / QoS on the NNI | `show firewall filter <name>` / `show class-of-service interface` | `show policy-map interface <if>` | `show policy-map interface <if>` | `show qos ...` / `show service id <id> sap <sap> stats` | Drops here explain "slow" tickets |

## Pre-change and post-change pairs

Run the same command before and after and diff the result. Minimum pairs for a routing change:

1. IGP adjacency list (count and state).
2. BGP summary (state and prefix counts per neighbour).
3. Route to each affected prefix (next hop, protocol, metric).
4. Label binding for each affected loopback (if MPLS).
5. Interface error counters on touched links.
6. NNI traffic rate both directions.

## Junos commit safety

- `commit confirmed 5` then `commit` once verified; otherwise the device rolls back on its own.
- `show | compare` before commit to review the diff; paste the diff into the change ticket.
- `rollback 1` then `commit` to return to the previous config.

## CUSTOMISE: company exact commands

Record the exact commands used on the company's platforms so pasted output is recognised:

- Core: `<platform>`: `<command used for the daily health check>`
- OLT: `<platform>`: `<command to read service-port / ONT state>`
- NNI: `<platform>`: `<command to read per-RSP VLAN counters>`
