# Search

Aliases: PFMSearchView, search route

Product context: `ios-client/pfm-kb/modules/search.md`

## What it is
In-app search for shows/content, routed via `AppRoutes.search`.

## Graph anchors
| `PFMSearchView` | `Pocket FM/Presentation/Features/PFMSearchView` |
| `case search` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Assuming client-only ranking — search relevance is largely backend (`search` pack).

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Search" --graph $GRAPH
```
