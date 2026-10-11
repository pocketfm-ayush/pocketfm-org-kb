# Home visibility filters

Aliases: disabled shows, hidden shows, campaign-only, campaign PGC

Product context: `radioly/pfm-kb/modules/visibility-filters.md` · flow `radioly/pfm-kb/flows/open-home.md`

## What it is

After Home is assembled, strip disabled and campaign-only titles. Not
AI↔PGC pair pick. Not device-art stamp.

## Graph anchors

| Symbol | Source |
|---|---|
| `filter_disabled_shows_from_feed` | `v2/feed_api/helpers.py` |
| `filter_hidden_shows_from_feed` | `v2/feed_api/helpers.py` |

## Risks

- Filtering only the candidate pool, then stitching a hidden title back.
- Treating campaign-only as a ranking tweak.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "filter_disabled_shows_from_feed" --graph $GRAPH
```
