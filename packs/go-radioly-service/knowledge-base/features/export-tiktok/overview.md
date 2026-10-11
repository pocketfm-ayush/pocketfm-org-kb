# TikTok S2S Export

Aliases: exporter-tiktok, TikTok provider

Product context: `go-radioly-service/pfm-kb/modules/export-tiktok.md`

## What it is
Exporter mode that consumes Relay topics and sends allowed events to TikTok Events API for attribution.

## Graph anchors
| `TikTok` | `internal/exporter/enum/providertype/types.go` |
| `service.go` | `internal/exporter/provider/tiktok/service.go` |

## Risks
- Sharing Facebook enrichment assumptions with TikTok without reading provider deps.
- Inventing TikTok event name mappings.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "TikTok" --graph $GRAPH
```
