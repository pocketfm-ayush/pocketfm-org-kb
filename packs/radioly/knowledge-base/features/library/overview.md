# Library

Aliases: my shows, subscribed, library feed

Product context: `radioly/pfm-kb/modules/library.md`

## What it is
Subscribed / saved shows surface and library feed APIs — not the same as listening history.

## Graph anchors
| Library / subscribed content | `v2/subscribed_content/`, library feed helpers |
| History contrast | `user-show-history` feature |


## Key product notes

The listener’s saved / subscribed titles, not the Home catalog.
Downloads is a different Library tab (downloads), not this list.

## Risks
- Confusing library subscriptions with recent history.
- Inventing offline download rules (see `downloads`).

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "Library" --graph $GRAPH
```
