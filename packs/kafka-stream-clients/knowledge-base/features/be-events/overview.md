# Backend Events Service Worker

Aliases: be-events-service

Product context: `kafka-stream-clients/pfm-kb/modules/be-events.md`

## What it is
Generic backend-events consumer service for internal BE event fan-in processing.

## Graph anchors
| `be_events/service` | `workers/be_events/service.py` |

## Risks
- Assuming all BE events share one schema without reading handlers.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Backend Events Service Worker" --graph $GRAPH
```
