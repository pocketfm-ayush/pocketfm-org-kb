# Promo banners

Aliases: player banner, show-page banner, feed banner, promo strip

Product context: `radioly/pfm-kb/modules/banners.md`

## What it is

Server-picked promo strip for the screen the app named. Not display
ads (`banner-ads`). App must not send journey type.

## Graph anchors

| Symbol | Source |
|---|---|
| `FetchBannerView` | `v3/banner/views/fetch_banner_view.py` |

## Risks

- Client-choosing the strip journey.
- Treating an empty list as an error.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "FetchBannerView" --graph $GRAPH
```
