# Discover Shorts

Aliases: PFMDiscoverShortsTab

Product context: `ios-client/pfm-kb/modules/discover-shorts.md`

## What it is
Shorts-style discover tab for short-form content discovery.

## Graph anchors
| `PFMDiscoverShortsTab` | `Pocket FM/Presentation/Features/PFMDiscoverShortsTab` |

## Risks
- Treating shorts player lifecycle as identical to long-form player without checking VMs.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Discover Shorts" --graph $GRAPH
```
