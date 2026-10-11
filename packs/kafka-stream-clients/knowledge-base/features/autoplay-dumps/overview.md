# Autoplay Data Dumps

Aliases: autoplay-data-dump workers

Product context: `kafka-stream-clients/pfm-kb/modules/autoplay-dumps.md`

## What it is
Workers that dump autoplay interaction/state data for analytics or recovery pipelines.

## Graph anchors
| `autoplay_data_dump` | `workers/autoplay/` |

## Risks
- Treating dumps as real-time autoplay control plane.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Autoplay Data Dumps" --graph $GRAPH
```
