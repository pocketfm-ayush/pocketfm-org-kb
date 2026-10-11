# Backend Direct Export Path

Aliases: path 2 backend Kafka → exporter

Product context: `go-radioly-service/pfm-kb/modules/backend-direct-path.md`

## What it is
Backends may publish directly onto exporter Kafka topics, bypassing gateway allowlist and router handlers.

## Graph anchors
| `CLAUDE dual path` | `CLAUDE.md` |
| `exporter consumer` | `internal/exporter/kconsumer.go` |

## Risks
- Expecting router GTM handlers to run on backend-direct messages.
- Skipping gateway validation assumptions for backend-published payloads.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "CLAUDE dual path" --graph $GRAPH
```
