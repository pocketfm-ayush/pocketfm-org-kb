# Discover

Aliases: discover widgets, content discovery

Product context: `android-client/pfm-kb/modules/discover.md`

## What it is
Dedicated Discover surface with its own widgets/domain, distinct from the main home feed modules.

## Graph anchors
| `discover ui` | `aural/discover/ui` |
| `discover domain` | `aural/discover/domain` |

## Risks
- Merging Discover-only fixes into feed without checking both graphs.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Discover" --graph $GRAPH
```
