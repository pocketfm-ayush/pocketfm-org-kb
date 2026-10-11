# Share

Aliases: share sheet, share domain

Product context: `android-client/pfm-kb/modules/share.md`

## What it is
Sharing shows/content via system share flows and share-domain helpers.

## Graph anchors
| `share domain` | `aural/share/domain` |
| `share data` | `aural/share/data` |

## Risks
- Hardcoding share URLs that deep-link config should own.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Share" --graph $GRAPH
```
