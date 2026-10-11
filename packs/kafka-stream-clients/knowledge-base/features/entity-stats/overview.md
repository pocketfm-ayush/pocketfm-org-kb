# Entity Stats Workers

Aliases: update-entity-stats, content-entity-stats

Product context: `kafka-stream-clients/pfm-kb/modules/entity-stats.md`

## What it is
Workers that update aggregated entity statistics used by content/discovery systems.

## Graph anchors
| `update_entity_stats` | `workers/update_entity_stats.py` |
| `update_entity_stats_v2` | `workers/update_entity_stats_v2.py` |

## Risks
- Treating stats workers as source of catalog truth.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Entity Stats Workers" --graph $GRAPH
```
