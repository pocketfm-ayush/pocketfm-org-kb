# Firebase / GA4 S2S Export

Aliases: exporter-firebase, GA4

Product context: `go-radioly-service/pfm-kb/modules/export-firebase.md`

## What it is
Exporter mode that forwards allowed events to Firebase / GA4 measurement for analytics.

## Graph anchors
| `Firebase` | `internal/exporter/enum/providertype/types.go` |
| `service.go` | `internal/exporter/provider/firebase/service.go` |

## Risks
- Confusing client SDK Firebase logs with this S2S path.
- Assuming identical payload shape to Meta.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "Firebase" --graph $GRAPH
```
