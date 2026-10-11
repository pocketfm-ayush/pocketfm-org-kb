# CarPlay

Aliases: CarPlay templates, Siri

Product context: `ios-client/pfm-kb/modules/carplay.md`

## What it is
CarPlay browse/play templates and related automotive integrations under `CarPlay/`.

## Graph anchors
| `PFMCarPlayTemplateManager` | `Pocket FM/CarPlay/PFMCarPlayTemplateManager.swift` |
| `CarPlay` | `Pocket FM/CarPlay` |

## Risks
- Changing CarPlay trees without media-session impact review.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "CarPlay" --graph $GRAPH
```
