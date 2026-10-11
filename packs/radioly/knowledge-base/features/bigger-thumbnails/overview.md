# Bigger thumbnails

Aliases: bigger thumbnails, large home art, editorial BT

Product context: `radioly/pfm-kb/modules/bigger-thumbnails.md` · flow `radioly/pfm-kb/flows/open-home.md`

## What it is

One larger-art Home rail. Not device-art stamp. The ops dashboard is
retired and unrouted.

## Graph anchors

| Symbol | Source |
|---|---|
| `BiggerThumbnailsService` | `v3/experience/bigger_thumbnails/services/bigger_thumbnails_service.py` |

## Risks

- Confusing this rail with per-device cover art.
- Re-enabling the commented `bt-dashboard` route as if it still serves art.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "BiggerThumbnailsService" --graph $GRAPH
```

## Related
- `device-cover-art`
- `show-thumbnail-mapping`
- `home-feed`
