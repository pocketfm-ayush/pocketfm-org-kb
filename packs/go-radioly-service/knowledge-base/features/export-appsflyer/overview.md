# AppsFlyer S2S Export

Aliases: exporter-appsflyer, AF S2S

Product context: `go-radioly-service/pfm-kb/modules/export-appsflyer.md`

## What it is
Exporter mode that sends allowed attribution events to AppsFlyer S2S.

## Graph anchors
| `AppsFlyer` | `internal/exporter/enum/providertype/types.go` |
| `NewAppsFlyerProvider()` | `internal/exporter/provider/appsflyer/service.go` |
| `pfmappsflyer` | `internal/externalservices/pfmappsflyer/` |

## Risks
- Duplicating AF sends already owned by kafka-stream-clients without checking event ownership.
- Calling live AF APIs in tests.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "AppsFlyer" --graph $GRAPH
```
