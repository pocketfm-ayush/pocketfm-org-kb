# Key Trope

Aliases: keytrope discovery widgets

Product context: `android-client/pfm-kb/modules/keytrope.md`

## What it is
Key Trope content discovery widgets and related domain/UI for trope-driven browsing.

## Graph anchors
| `keytrope ui` | `aural/keytrope/ui` |
| `keytrope domain` | `aural/keytrope/domain` |

## Risks
- Inventing trope taxonomy in the client — server owns content.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Key Trope" --graph $GRAPH
```
