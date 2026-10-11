# Community and profile updates

Aliases: community feed, updates feed, profile feed, community posts

Product context: `radioly/pfm-kb/modules/community-updates.md`

## What it is

`get_community_feed` is this listener’s posts. Profile feed is that
account’s posts. Not Home and not Library.

## Graph anchors

| Symbol | Source |
|---|---|
| `get_community_feed` | `v3/feed_api/views.py` |

## Risks

- Treating Community as For You or “my shows.”
- Leaving a phone number on a people card.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "get_community_feed" --graph $GRAPH
```
