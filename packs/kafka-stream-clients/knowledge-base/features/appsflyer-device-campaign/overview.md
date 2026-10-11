# AppsFlyer Device Campaign Update

Aliases: appsflyer-device-campaign worker

Product context: `kafka-stream-clients/pfm-kb/modules/appsflyer-device-campaign.md`

## What it is
Worker that updates device-level AppsFlyer campaign attribution fields from Kafka events.

## Graph anchors
| `device_campaign_update` | `workers/device_campaign_update.py` |

## Risks
- Overwriting attribution windows incorrectly.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "AppsFlyer Device Campaign Update" --graph $GRAPH
```
