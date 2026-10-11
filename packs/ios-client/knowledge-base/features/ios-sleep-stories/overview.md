# Sleep Stories

Aliases: PFMSleepStories

Product context: `ios-client/pfm-kb/modules/sleep-stories.md`

## What it is
Sleep stories listening experience and related routing.

## Graph anchors
| `PFMSleepStories` | `Pocket FM/Presentation/Features/PFMSleepStories` |
| `sleepStoriesView route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Applying serial-show unlock rules blindly to sleep catalogs.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Sleep Stories" --graph $GRAPH
```
