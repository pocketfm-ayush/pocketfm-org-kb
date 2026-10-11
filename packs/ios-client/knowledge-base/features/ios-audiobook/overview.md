# Audiobook

Aliases: PFMAudioBook, audiobook series

Product context: `ios-client/pfm-kb/modules/audiobook.md`

## What it is
Audiobook and audiobook-series browsing/playback entry surfaces distinct from serial show feeds.

## Graph anchors
| `PFMAudioBook` | `Pocket FM/Presentation/Features/PFMAudioBook` |
| `audioBookSeriesView route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Treating audiobook series identically to show episode lists without checking VMs.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Audiobook" --graph $GRAPH
```
