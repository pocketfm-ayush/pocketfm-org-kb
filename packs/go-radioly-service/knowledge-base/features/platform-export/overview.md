# Platform Export (Umbrella)

Aliases: exporter mode, S2S providers

Product context: `go-radioly-service/pfm-kb/modules/platform-export.md`

## What it is
Umbrella for Kafka consumers that enrich events and deliver S2S to TikTok, Firebase/GA4, AppsFlyer, Meta (Facebook), and MoEngage.

## Graph anchors
| `InitProvider()` | `internal/exporter/provider/provider.go` |
| `NewExporterCtrl()` | `internal/exporter/kconsumer.go` |
| `Start()` | `internal/bootstrap/exporter/exporter.go` |

## Risks
- Initializing MySQL+Scylla+Redis for every exporter — deps are opt-in per provider.
- Calling live platform APIs in unit tests.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "InitProvider()" --graph $GRAPH
```
