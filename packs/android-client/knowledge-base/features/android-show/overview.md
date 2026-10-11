# Show Details

Aliases: show page, episodes, comments, reviews

Product context: `android-client/pfm-kb/modules/show-details.md`

## What it is
Show details, episode lists, comments/reviews, and related show common UI before playback.

## Graph anchors
| `show ui` | `aural/show/ui` |
| `show domain` | `aural/show/domain` |
| `show common` | `aural/show/common` |

## Risks
- Bypassing content-backend/Radioly catalog contracts when inventing episode fields.
- Editing only legacy show fragments for Aural users.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Show Details" --graph $GRAPH
```
