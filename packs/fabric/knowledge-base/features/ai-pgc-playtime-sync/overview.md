# AI↔PGC Playtime Sync

Aliases: consumer-ai-pgc-sync, aipgcsync

Product context: `fabric/pfm-kb/modules/ai-pgc-playtime-sync.md`

## What it is
Sequential playtime consumer that syncs listening progress between AI and PGC show mappings (unlocking-aware), using Scylla+MySQL.

## Graph anchors
| `aipgcsync.Service` | `playtime/aipgcsync/service.go` |
| `ModeAIPGCSync` | `playtime/consumer/registry.go` |
| `AIPGCSync repositories` | `playtime/repository/` |

## Risks
- Running multiple pods that break sequential read-modify-write assumptions.
- Inventing plan/mapping ids.

## Query
```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "AI↔PGC Playtime Sync" --graph $GRAPH
```
