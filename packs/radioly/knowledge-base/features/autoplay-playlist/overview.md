# Autoplay playlist

Aliases: playlist, next recommended show, autoplay queue, next up

Product context: `radioly/pfm-kb/modules/autoplay-playlist.md` · flow `radioly/pfm-kb/flows/finish-show.md`

## What it is

`get_playlist_data` is the ordered next-up list. `get_next_recommended_show`
is the same product when the list is empty. Not Home, not player rails,
not stitch.

## Graph anchors

| Symbol | Source |
|---|---|
| `get_playlist_data` | `v3/feed/views.py` |
| `get_next_recommended_show` | `v3/feed_api/views.py` |

## Risks

- Playing a Home card when next-up is empty.
- Treating stitch / bridge promo as default autoplay.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "get_playlist_data" --graph $GRAPH
```
