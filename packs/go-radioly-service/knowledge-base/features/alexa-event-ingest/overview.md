# Alexa Event Ingest

Aliases: alexa logging route

Product context: `go-radioly-service/pfm-kb/modules/alexa-event-ingest.md`

## What it is
Authenticated Alexa-specific ingest route under logging_data for voice-surface events.

## Graph anchors
| `LogAlexaEvents` | `internal/gateway/http/routes.go` |

## Risks
- Posting Alexa events to the unauthenticated batch route and expecting identical auth semantics.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "LogAlexaEvents" --graph $GRAPH
```
