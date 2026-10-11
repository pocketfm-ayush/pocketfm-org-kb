# GTM Impressions (Radioly publish)

Aliases: GTM impression, impression publisher, bottom slider impression

Product context: `radioly/pfm-kb/modules/gtm-impressions.md`

## What it is
Radioly-side publishing and helpers for GTM/ads impression events that later
land in Fabric impression counts for frequency capping. Not the Fabric store itself.

## Graph anchors
| Symbol | Source |
|---|---|
| `GTMImpressionService` | `v3/impression/services/gtm_impression_service.py` |
| `GTMImpressionPublisher` | `v3/gtm/services/impression_publisher_service.py` |
| GTM campaigns | `v2/campaigns/gtms/`, `v3/gtm/` |


## Key product notes

Radioly publishes impression events when promotional/GTM surfaces are shown so
platform impression counts can drive frequency caps later.

## Risks
- Caps are decided by callers using Fabric counts — do not invent cap numbers.
- Pair with fabric `impression-tracking` for the platform store.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "GTMImpressionPublisher" --graph $GRAPH
```

## Related
- `launch-overlays`
- `liveops-tentpole`
- `fabric impression-tracking`
