# Playtime Content Client

Aliases: externalservices/content, exclusion API client

Product context: `fabric/pfm-kb/modules/playtime-content-client.md`

## What it is
Outbound Content service client used by feed-show-exclusion to apply exclusions after thresholds breach.

## Graph anchors
| `content.Client` | `playtime/externalservices/content/` |
| `ExternalServices` | `playtime/externalservices/service.go` |

## Risks
- Calling Content exclusion APIs from the wrong mode (e.g. AI-PGC sync).
- Assuming Content dependency is initialized for every playtime mode.

## Query
```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "Playtime Content Client" --graph $GRAPH
```
