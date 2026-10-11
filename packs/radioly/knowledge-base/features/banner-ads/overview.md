# Banner ads

Aliases: display ads, image ads, thumbnail ad, player pause ad

Product context: `radioly/pfm-kb/modules/banner-ads.md`

## What it is

Still-image placements. Not mid-roll. Not promo strips (`banners`).

## Graph anchors

| Symbol | Source |
|---|---|
| `get_image_ad` | `v3/ads/views.py` |
| `image_ad` | `v3/ads/ads_cms/viewsets.py` |

## Risks

- Assuming every screen has a banner.
- Treating ad-free as a hard zero-display guarantee.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "get_image_ad" --graph $GRAPH
```
