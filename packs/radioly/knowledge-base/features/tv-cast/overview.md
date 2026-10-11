# TV and device pair

Aliases: TV cast, App Code, pair TV, pair watch

Product context: `radioly/pfm-kb/modules/tv-cast.md`

## What it is

Sign the same login onto a TV or watch. Not AirPlay / Chromecast.
Phone must already be logged in.

## Graph anchors

| Symbol | Source |
|---|---|
| `TvCastViewSet` | `v2/campaigns/tvcast/viewsets.py` |


## Key product notes

Sign the **same login** onto a TV or watch. Not AirPlay / Chromecast
of the player.

## Risks

- Letting the TV invent an account.
- Reusing a spent or expired code.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "tv cast" --graph $GRAPH
```
