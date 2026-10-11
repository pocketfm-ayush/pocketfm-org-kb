# Stream Analytics Ingest

Aliases: stream_analytics endpoint, QoE player metrics

Product context: `go-radioly-service/pfm-kb/modules/stream-analytics.md`

## What it is
Dedicated gateway path for player/stream quality analytics payloads (bitrate, startup, buffering style metrics), separate from general event batches.

## Graph anchors
| `LogStreamAnalytics` | `internal/gateway/http/routes.go` |
| `StreamAnalyticsData` | `internal/gateway/eventlog/stream_analytics.go` |

## Risks
- Mixing stream QoE payloads into generic clickstream allowlist rules without reading this path.
- Inventing metric field meanings — read DTO tags.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "LogStreamAnalytics" --graph $GRAPH
```
