# Jargon translation table

Use the customer phrase in replies. Keep the technical term in internal notes. Where a term sits on the RSP side, the customer phrase hands it back without blame.

| Technical term | Customer wording | Notes / who owns it |
|---|---|---|
| ONT (optical network terminal) | The connection box installed in your home (usually a small white box with lights, with our label) | Network operator |
| NTD | Same as ONT; "the connection box" | Network operator |
| PON / GPON | The fibre network in your street | Network operator |
| OLT | The equipment at our exchange that your fibre connects to | Network operator. Rarely needed in a reply |
| LOS (loss of signal) / red LOS light | The connection box is not receiving a light signal from our network (the red light) | Network operator. Usually a fibre or power issue |
| LOSi / dying gasp | The connection box lost power or signal at <time> | the network operator. Dying gasp = power loss at the home |
| RX level / optical power / dBm | The strength of the light signal reaching your connection box | Network operator. Never quote the number; say "too weak", "within the normal range" |
| Splitter / FDH / cabinet | A shared piece of equipment in the street that serves your home and your neighbours | Network operator |
| Lead-in / drop / drop cable | The fibre cable running from the street into your home | Network operator |
| Pit / pit and pipe / conduit | The underground access point and ducts near your property | Network operator or developer (construction stage) |
| Premises fibre / internal cabling | The fibre cable inside your home between the entry point and the connection box | Network operator up to the connection box |
| UNI / LAN port / ETH port | The network socket on the connection box that your modem plugs into | Network operator port; customer cable |
| CPE / RG / modem / router | Your modem or router (the device your provider gave you or you bought) | RSP or customer |
| PPPoE / PPP session / DHCP | Your provider's login for your service (the part that lets your modem connect to their network) | RSP |
| Authentication / radius / credentials | Your provider's username and password for the service | RSP |
| IP address / default route | The settings your provider gives your modem so it can reach the internet | RSP |
| BNG | Your provider's equipment | RSP. Do not name it |
| NNI / aggregation / uplink | The link between our network and your provider's network | Network operator up to the NNI; rarely needed |
| VLAN / service port / GEM / T-CONT | The settings that connect your service to your provider (internal) | Network operator provisioning. Say "the settings for your service" |
| Provisioning / service order / activation | Setting up your service on our network once your provider places the order | the network operator, after RSP order |
| RFS (ready for service) | The date the fibre network in your estate is live and providers can connect homes | Network operator |
| RSP / retail service provider | Your internet provider (the company you pay) | Use "your provider" |
| Wholesale | We build and run the fibre network; your provider sells the service over it | Explain once, simply, if asked why we cannot change plans or bills |
| Speed tier / 100/20, 250/25 | Your plan speed | RSP |
| Throughput / sync speed / line rate | The speed the connection to your home can deliver | Network operator if port or optical; RSP for plan |
| Latency / jitter / packet loss | Delay or glitches in the connection, noticeable in video calls and gaming | Either; describe the symptom |
| Multicast / IPTV | TV channels delivered over the connection | RSP service; the network operator carries it |
| OTDR / power meter / light test | A test our technician runs on the fibre cable | Network operator field |
| Splice / splice closure / enclosure | A joint in the fibre cable, usually in the street or a pit | Network operator |
| Macrobend / bend radius | The fibre cable is bent too tightly somewhere, which weakens the signal | Network operator or inside the home |
| Dirty connector / APC / UPC | The fibre connector needs cleaning or replacing | Network operator field |
| Flapping / intermittent registration | The connection box is dropping on and off our network | the network operator; describe as "dropping out at our end" only if NOC confirms |
| Adjacent ONTs | Your neighbours' connections | Internal; say "other homes nearby" |
| Planned works / maintenance window | Scheduled maintenance on the network in your area between <times> | Network operator |
| Outage / incident / P1 | A network issue affecting your area | Network operator; give the area and expected update time, not the severity code |
| Truck roll / dispatch / field appointment | A technician visit | Network operator field; give the window |
| No fault found (NFF) | Our technician tested the connection and it was working correctly at the time of the visit | Say what was tested, not the acronym |
| Defect / rectification | Something that needs fixing on the install or in the street, and the work to fix it | Network operator or contractor |
| Easement / lot / stage | The strip of land where services run; your block; the part of the estate being built | Developer or the network operator |
| SLA / service level | The timeframes we work to | Give the timeframe, not the term, and only if confirmed |

## Translation rules

1. Describe what the customer would notice (lights, dropouts, speed), not the mechanism.
2. One fact per sentence. "The light signal reaching your connection box is too weak, so the box cannot connect to our network" is two linked facts; fine. Three or more, split.
3. Keep "appears" and "we are checking" for anything the technical note marks as likely or possible.
4. Numbers: no dBm, no percentages of packet loss, no port numbers. Dates and appointment windows: yes.
5. Where the term is on the RSP side, the customer phrase names "your provider" as the next step without saying the problem is theirs.
6. Internal identifiers (ticket IDs, OLT names, PON ports, serials) stay in the technical column.

## Worked examples

| Technical | Customer wording |
|---|---|
| ONT offline, LOS, RX none, adjacent ONTs online, no DG | The connection box in your home is not receiving the light signal from our network, while nearby homes are connected normally. This points to the cable between the street and your home, so a technician visit is the next step. |
| PPPoE PADI seen, no PADO, MAC learned on correct VLAN | We have checked the connection from our network to your home and it is working. The next step is with your provider, who manages the login that lets your modem connect. We have noted what we found so they can pick it up. |
| RX -27.5 dBm, borderline, intermittent registration | The light signal reaching your connection box is weaker than it should be, which can cause dropouts. We are arranging for a technician to test the cable. |
| Dying gasp 02:14, ONT back 06:40 | Our records show the connection box lost power at about 2:15 am and came back at about 6:40 am. If you had a power outage or the box was unplugged, that would explain it. |
| NFF, UNI up 1G full, RX -18 dBm | Our technician tested the connection to your home and it was working correctly, with a strong signal and the connection box port running at full speed. |

## CUSTOMISE

- the company's preferred name for the ONT in customer material ("connection box" by default; confirm against the install guide).
- Product and plan names residents may use, and the RSP list for the estate.
- Approved outage wording and the public status page, if one exists.
