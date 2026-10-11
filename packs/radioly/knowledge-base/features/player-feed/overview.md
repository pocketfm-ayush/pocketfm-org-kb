# Player feed

Aliases: player feed, player rails, episode page feed, get_player_feed, next series, new releases, new on pocketfm

Product context: `radioly/pfm-kb/modules/player-feed.md`

## What it is

`get_player_feed`, `get_player_feed_data`, and `get_player_feed_new` are
the same player-page rails product. Not Home.

## Graph anchors

| Symbol | Source |
|---|---|
| `get_player_feed` | `v3/feed_api/views.py` |
| `get_player_feed_new` | `v3/feed_api/views.py` |
| `NEW_REL_MODULE_NAME` | `v2/feed_api/services/player_feed_widgets.py` |

## Risks

- Debugging Home for a wrong player row.
- Treating an empty extra stack for non-testers as a failed feed.
- Looking for the New Releases / Next Series title in `content-backend` or `go-radioly-service`. The constant is `NEW_REL_MODULE_NAME` in this pack. Clients render that server string; they do not own the “Pocket FM” wording.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "get_player_feed" --graph $GRAPH
```
