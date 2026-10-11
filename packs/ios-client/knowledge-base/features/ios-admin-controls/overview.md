# Admin Controls

Aliases: Admin Controls internal tools

Product context: `ios-client/pfm-kb/modules/admin-controls.md`

## What it is
Internal/admin debugging or control surfaces not meant as listener product.

## Graph anchors
| `Admin Controls` | `Pocket FM/Presentation/Features/Admin Controls` |

## Risks
- Exposing admin controls in production builds without gate.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Admin Controls" --graph $GRAPH
```
