# App Rating

Aliases: PFMAppRatingView

Product context: `ios-client/pfm-kb/modules/app-rating.md`

## What it is
In-app rating prompts that ask satisfied listeners to rate on the App Store.

## Graph anchors
| `PFMAppRatingView` | `Pocket FM/Presentation/Features/PFMAppRatingView` |

## Risks
- Violating Apple rating prompt frequency guidelines.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "App Rating" --graph $GRAPH
```
