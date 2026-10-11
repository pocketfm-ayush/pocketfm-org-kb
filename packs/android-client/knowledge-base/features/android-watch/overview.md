# Wear / Watch

Aliases: wear OS watch module

Product context: `android-client/pfm-kb/modules/watch.md`

## What it is
Wear/Watch companion surfaces shipped from the `watch/` Gradle module alongside phone app.

## Graph anchors
| `watch module` | `watch/` |

## Risks
- Assuming phone-only Aural fixes automatically cover Wear.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Wear / Watch" --graph $GRAPH
```
