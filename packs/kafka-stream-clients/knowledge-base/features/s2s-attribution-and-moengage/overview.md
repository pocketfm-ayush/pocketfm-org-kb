# S2S Attribution and MoEngage

Aliases: s2s_events_v2 AppsFlyer Facebook Firebase Google, MoEngage consumers

Product context: `kafka-stream-clients/pfm-kb/modules/s2s-attribution-and-moengage.md`

## What it is
Growth S2S workers sending payment/level/misc events to AppsFlyer, Facebook, Firebase, Google (IN/US), plus MoEngage attribution/segment consumers and debuggers.

## Graph anchors
| `s2s_events_v2` | `workers/s2s_events_v2/` |
| `moengage consumer` | `workers/s2s_events_v2/moengage/` |
| `s2s_event_debugger` | `workers/s2s_events_v2/s2s_event_debugger/` |

## Risks
- Fixing Relay exporter when the live path is these Kafka workers (or vice versa).
- Calling live partner APIs in unit tests.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "S2S Attribution and MoEngage" --graph $GRAPH
```
