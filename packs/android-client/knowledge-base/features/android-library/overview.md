# Library

Aliases: bookmarks, my list, library tab

Product context: `android-client/pfm-kb/modules/library.md`

## What it is
Saved/bookmarked shows and library tab UI for resume and collection management.

## Graph anchors
| `library ui` | `aural/library/ui` |
| `library domain` | `aural/library/domain` |

## Risks
- Assuming downloads ownership lives only here — player/download may own offline packs.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Library" --graph $GRAPH
```
