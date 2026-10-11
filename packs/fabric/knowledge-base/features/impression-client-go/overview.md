# Impression Go Client

Aliases: impression/clientgo, QueryImpressionsByFeatures

Product context: `fabric/pfm-kb/modules/impression-go-client.md`

## What it is
Go library for product services to query impression counts by user/device, asset types, features, scope, and frequency windows.

## Graph anchors
| `NewClient` | `impression/clientgo/` |
| `QueryImpressionsByFeatures` | `impression/clientgo/impression.go` |
| `entitytype / frequency / impressionscope` | `impression/clientgo/enum/` |

## Risks
- Opening raw Scylla sessions in callers instead of this client.
- Mixing entity types (e.g. GTM) incorrectly.

## Query
```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "Impression Go Client" --graph $GRAPH
```
