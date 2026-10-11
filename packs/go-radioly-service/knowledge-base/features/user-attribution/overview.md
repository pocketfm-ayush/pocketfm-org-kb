# User Attribution Capture

Aliases: fbp/fbc store, /v1/user_attribution

Product context: `go-radioly-service/pfm-kb/modules/user-attribution.md`

## What it is
Authenticated API to store and read click attribution metadata (e.g. Meta cookies) used later by exporters when payload omits them.

## Graph anchors
| `UserAttributionService` | `internal/gateway/user_attribution/service.go` |
| `UserAttributionRepository` | `internal/repository/user_attribution.go` |

## Risks
- Assuming Kafka fallback exists when Scylla is down (TODO in source).
- Writing attribution without auth middleware.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "UserAttributionService" --graph $GRAPH
```
