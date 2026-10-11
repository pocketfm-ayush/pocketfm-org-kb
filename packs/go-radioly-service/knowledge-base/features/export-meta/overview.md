# Meta (Facebook) S2S Export

Aliases: exporter-meta, Facebook CAPI, Meta provider

Product context: `go-radioly-service/pfm-kb/modules/export-meta.md`

## What it is
Exporter mode for Meta Conversions API: enriches with IAM/Nexus/IP/Payments and attribution cookies, hashes sensitive fields, may synthesize trial signals on first purchase.

## Graph anchors
| `NewFacebookProvider()` | `internal/exporter/provider/facebook/service.go` |
| `enrichFromIAM` | `internal/exporter/provider/facebook/service.go` |
| `resolveFBAttribution` | `internal/exporter/provider/facebook/service.go` |

## Risks
- Sending raw PII instead of hashed fields.
- Ignoring Scylla-backed fbp/fbc fallback when payload omits cookies.
- Inventing Start Trial rules — read provider tests.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "NewFacebookProvider()" --graph $GRAPH
```
