# Feed Show Exclusion

Aliases: consumer-feed-show-exclusion, threshold breach

Product context: `fabric/pfm-kb/modules/feed-show-exclusion.md`

## What it is
Playtime consumer that accumulates listening against thresholds and marks users for Content-side show exclusion from feeds.

## Graph anchors
| `feedshowexclusion.Service` | `playtime/feedshowexclusion/service.go` |
| `ModeFeedShowExclusion` | `playtime/consumer/registry.go` |
| `FeedShowExclusion* repositories` | `playtime/repository/` |

## Risks
- Hard-coding thresholds that Content/config own.
- Assuming exclusion is enforced inside Fabric rather than Content API.

## Query
```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "Feed Show Exclusion" --graph $GRAPH
```
