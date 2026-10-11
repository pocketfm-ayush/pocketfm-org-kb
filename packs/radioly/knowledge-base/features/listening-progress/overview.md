# Listening progress

Aliases: resume, last listened, playtime progress

Product context: `radioly/pfm-kb/modules/listening-progress.md`

## What it is
Server-side listening progress used for resume, unlock gates, and Episode Zero eligibility (low playtime).

## Graph anchors
| Playtime helpers | `v2/user_api/playtime_helpers.py` |
| Scylla playtime | `data/scylla-catalog.md` |
| Episode Zero gate | `EpisodeZeroService` |


## Key product notes

Where they left off in a title, and the last title they played. Not
Library (saved list) and not Home.

## Risks
- Confusing with fabric playtime consumers or wallet playtime-credits.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "Listening progress" --graph $GRAPH
```
