# Event Enrichment Dependencies

Aliases: IAM Nexus Payments IPAPI enrichment

Product context: `go-radioly-service/pfm-kb/modules/event-enrichment.md`

## What it is
Shared external lookups used mainly by exporters (especially Meta) to attach identity, profile, geo, and purchase value before S2S send.

## Graph anchors
| `ExternalServices` | `internal/externalservices/services.go` |
| `NewClient()` | `internal/externalservices/iam/iam_client.go` |
| `NewClient()` | `internal/externalservices/nexus/nexus.go` |
| `NewClient()` | `internal/externalservices/payments/payments_client.go` |
| `NewClient()` | `internal/externalservices/ipapi/ipapi_client.go` |

## Risks
- Assuming every exporter mode initializes all enrichment clients.
- Writing raw PII into logs during enrichment failures.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "ExternalServices" --graph $GRAPH
```
