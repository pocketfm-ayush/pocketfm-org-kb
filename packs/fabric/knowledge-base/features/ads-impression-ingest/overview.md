# Ads Impression Ingest

Aliases: ADS_DEVICE_IMPRESSION, ADS_USER_IMPRESSION

Product context: `fabric/pfm-kb/modules/ads-impression-counts.md`

## What it is
Ads-specific impression event handling alongside GTM events in the same impression consumer, feeding ads frequency analytics.

## Graph anchors
| `adsDeviceEvent` | `impression/server/consumer/consumer.go` |
| `adsUserEvent` | `impression/server/consumer/consumer.go` |

## Risks
- Treating ads impressions as identical to GTM asset whitelist rules without reading handlers.
- Confusing with fm-ads-client offerwall in mobile packs.

## Query
```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "Ads Impression Ingest" --graph $GRAPH
```
