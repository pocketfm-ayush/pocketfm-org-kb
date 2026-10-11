# MoEngage S2S Export

Aliases: exporter-moengage, MoEngage provider

Product context: `go-radioly-service/pfm-kb/modules/export-moengage.md`

## What it is
Exporter mode that delivers allowed events to MoEngage for CRM / engagement orchestration.

## Graph anchors
| `Moengage` | `internal/exporter/enum/providertype/types.go` |
| `service.go` | `internal/exporter/provider/moengage/service.go` |

## Risks
- Confusing Airflow MoEngage jobs with this real-time Relay exporter.
- Assuming all clickstream events go to MoEngage.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "Moengage" --graph $GRAPH
```
