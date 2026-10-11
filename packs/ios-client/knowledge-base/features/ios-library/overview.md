# Library

Aliases: PFMLibraryView, saved episodes, library detail

Product context: `ios-client/pfm-kb/modules/library.md`

## What it is
Library tab for saved/bookmarked content and library detail collections; overlaps with saved-episode helpers.

## Graph anchors
| `PFMLibraryView` | `Pocket FM/Presentation/Features/PFMLibraryView` |
| `PFMSavedEpView` | `Pocket FM/Presentation/Features/PFMSavedEpView` |
| `libraryDetail route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Confusing library saves with offline download packs.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Library" --graph $GRAPH
```
