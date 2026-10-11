# Default feed cache

Aliases: default feed, shared rails, default home cache

Product context: `radioly/pfm-kb/modules/default-feed-freshness.md` · flow `radioly/pfm-kb/flows/open-home.md`

## What it is

Shared editorial / default home rails freshness. Not a per-user private snapshot.

## Graph anchors

| Symbol | Source |
|---|---|
| `DefaultHomeFeedData.get_full_details` | feed services (see `home-feed` overview) |
| Home entry | `v3/feed_api/views.py` → `get_feed_data` |

## Key edges

- Feature slug `default-feed-cache` ↔ product module `default-feed-freshness` (`slug-map.yaml`).
- Personalized rails and shared rails differ — logout must not keep another person's rails.


## Key product notes

Popular / Top Picks / genre rails are built for a **cohort** (language,
locale, app vintage, replica generation) and reused. They are not a
per-user Home blob.

## Risks

- Claiming per-uid cache keys for shared editorial rails without evidence.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "default feed cache" --graph $GRAPH
```
