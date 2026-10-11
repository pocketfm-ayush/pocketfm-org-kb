# Show Details

Aliases: PFMShowDetail, episodes, show page

Product context: `ios-client/pfm-kb/modules/show-details.md`

## What it is
Show details page: metadata, episodes, and CTAs into player, reviews, comments, and unlock.

## Graph anchors
| `PFMShowDetail` | `Pocket FM/Presentation/Features/PFMShowDetail` |
| `showDetail route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Bypassing catalog contracts when inventing episode fields.
- Editing only legacy NewDesign copies without confirming active path.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Show Details" --graph $GRAPH
```
