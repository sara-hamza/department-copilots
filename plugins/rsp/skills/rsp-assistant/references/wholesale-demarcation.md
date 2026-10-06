# Wholesale demarcation: who owns what, and what each side can see

We are the wholesale access network operator. The RSP sells the retail service and owns the customer relationship. Every reply and every question must respect this line.

## Service path and ownership

```
Customer LAN -- CPE -- [UNI] ONT -- drop -- splitter/FDH -- PON -- OLT -- aggregation -- [NNI] -- RSP BNG -- RSP core -- Internet
   RSP/customer   RSP     ^-------------------- the network operator ---------------------^            RSP
```

| Segment | Owner | Fault signals the network operator sees | Fault signals only the RSP sees |
|---|---|---|---|
| Customer LAN, Wi-Fi | Customer (RSP supports) | None | Device connectivity, Wi-Fi, LAN IP |
| CPE (router) | RSP (or customer-supplied, RSP supports) | UNI negotiated speed/duplex, MAC seen on UNI, whether PADI or DHCP discover arrives | CPE logs, WAN status, PPP credentials, firmware |
| UNI (ONT Ethernet port) | Network operator | Port state, speed, errors | n/a |
| ONT | Network operator | Registration, RX/TX, alarms, profile, firmware, uptime, last-down reason | n/a |
| Drop, splitter, FDH, distribution, feeder | Network operator | Optical levels, LOS, adjacent ONT status | n/a |
| OLT and PON | Network operator | Port state, OLT RX, service-port, GEM/T-CONT, VLAN mapping, MAC learned, counters | n/a |
| Aggregation to NNI | Network operator | S-VLAN mapping, NNI LAG state, counters per S-VLAN, PPPoE discovery counters where instrumented | n/a |
| NNI port, RSP side | RSP | NNI LAG state (our side), traffic in and out | Their LAG state, S-VLAN config, traffic |
| BNG, RADIUS, authentication | RSP | Nothing | Session state, auth accept/reject and reason, session start/stop times, VLAN tags seen |
| IP assignment, pools, CGNAT, routing | RSP | Nothing | Assigned IP, pool, NAT state, routes, policies, quotas, filters |
| Retail SLA, billing, customer contact | RSP | Nothing | Everything |

## What "working" means at each demarcation

| Statement | Means, and requires in evidence |
|---|---|
| Access path operating to the UNI | ONT online, ONT RX within range, no active alarms, UNI up, ONT provisioned with the correct profile and VLAN for the RSP |
| Layer 2 path to the NNI | MAC learned on the service port in the correct C-VLAN, S-VLAN mapped to the RSP's NNI, NNI LAG up, counters incrementing both ways on the S-VLAN |
| Session discovery seen | PADI from the customer MAC seen at the OLT or aggregation; PADO returned from the NNI side (if instrumented). PADO seen means the BNG answered; PADI with no PADO means the request did not reach, or was not answered by, the BNG |
| Service active | RSP confirms session established with IP assigned; traffic counters incrementing both directions on the service port |

## Symptom to likely segment (starting point only)

| RSP reports | First access checks | If access is clean, the question is about |
|---|---|---|
| No sync / ONT offline / LOS | ONT state, RX, last-down reason, adjacent ONTs | Nothing; this is the company's |
| ONT online, no PPPoE session | UNI state, MAC learned, VLAN mapping, PADI seen, PADO seen | BNG availability for that S-VLAN, RADIUS result, CPE credentials |
| PPP session but no internet | All of the above plus traffic counters on the service port | IP assigned, default route, policy or quota, CGNAT, DNS |
| DHCP (IPoE) no lease | MAC learned, option 82 insertion if used, discover seen | DHCP server, relay, pool exhaustion |
| Slow speed | Bandwidth profile vs sold tier, PON utilisation, UNI speed, errors and discards | BNG shaping, upstream capacity, CPE, Wi-Fi |
| Intermittent drops | ONT uptime history, RX history, alarms, errors | Session keepalive, BNG reloads, CPE reboots |
| Voice one-way or no registration | ONT voice port state if ONT-hosted, VLAN for voice | SIP registrar, NAT, codec |
| IPTV / multicast | IGMP snooping state, multicast VLAN, joins | Middleware, channel source |
| Many services, one RSP, many OLTs | NNI state, S-VLAN counters, any incident on our side | RSP BNG or core event |
| Many services, one OLT or area | OLT, uplink, power, planned works | Nothing; the network operator incident |

## Wording that respects the demarcation

| Avoid | Use |
|---|---|
| "The fault is on your side" | "The access path to the UNI is operating within specification. To locate where the session stops we need the items below." |
| "Your BNG is not responding" | "PADI frames from the customer MAC are seen at the OLT at 10:12 ACDT; no PADO has been observed. Please confirm whether the BNG received a discovery from this MAC." |
| "The customer's router is faulty" | "The UNI negotiated 1000/full and a MAC is learned, but no PPPoE discovery has been seen from it. Please confirm CPE WAN configuration and whether the CPE logs show PADI being sent." |
| "No issues found" | "Checked: ONT online since 08:02, RX -18.4 dBm, UNI up, MAC learned on VLAN 100, S-VLAN mapped to NNI 2, NNI up with traffic. No fault identified on the access path." |
| "Will be fixed by tomorrow" | "A field visit is the next step on our side; confirmation of the appointment will follow." (only if the employee has confirmed a visit) |

## CUSTOMISE: company wholesale specifics

- Service identifier format used with RSPs: `<e.g. OPT-XXXXXXX / UNI id>` (verify)
- NNI and S-VLAN naming per RSP: `<fill in>`
- Whether PPPoE discovery counters are available and where (OLT, aggregation, probe): `<fill in>`
- Wholesale agreement name and the SLA clause reference for fault restoration: `<fill in>`
- Wholesale operations contacts by role (not personal): `<fill in>`
- Standard optical acceptance range quoted to RSPs: `-8 to -27 dBm ONT RX` (verify)
