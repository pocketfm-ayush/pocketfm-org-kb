# Device cover art

Aliases: cover art, device art, DS art, thumbnail mapping

Product context: `radioly/pfm-kb/modules/device-cover-art.md`

## What it is

Device / design-revamp artwork selection for shows (often via thumbnail mapping).

## Graph anchors

| Symbol / store | Source |
|---|---|
| `shows_thumbnail_mapping` | MySQL — `features/show-thumbnail-mapping/`, `data/tables.md` |
| `content.ds_show_thumbnail` | Scylla — `data/scylla-catalog.md` |


## Key product notes

A **stamp** that can replace catalog cover art for this device, after
rails are built and visibility filters have run. It is not a Home rail
(that is bigger-thumbnails) and not a hide rule.

## Risks

- Confusing Radioly DS art with Search `ds-thumbnails` personalization step.

## Related
- `show-thumbnail-mapping`
- `bigger-thumbnails`

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "device cover art" --graph $GRAPH
```
