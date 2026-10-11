# Key Tropes

Aliases: PFMKeyTropes, tropeDetail

Product context: `ios-client/pfm-kb/modules/keytropes.md`

## What it is
Browse-by-trope discovery and trope detail routes.

## Graph anchors
| `PFMKeyTropes` | `Pocket FM/Presentation/Features/PFMKeyTropes` |
| `tropeDetail route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Inventing trope taxonomy in the client.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Key Tropes" --graph $GRAPH
```
