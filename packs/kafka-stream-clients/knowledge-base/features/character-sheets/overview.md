# Character Sheet User Actions

Aliases: show-character-user-actions consumer

Product context: `kafka-stream-clients/pfm-kb/modules/character-sheets.md`

## What it is
Worker that persists user actions against show character sheets / character surfaces.

## Graph anchors
| `show_character_user_actions_consumer` | `workers/character_sheets/` |

## Risks
- Mixing with AI character chat client features without checking event types.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Character Sheet User Actions" --graph $GRAPH
```
