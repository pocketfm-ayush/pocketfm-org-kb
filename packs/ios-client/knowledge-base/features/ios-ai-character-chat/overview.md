# AI Character Chat

Aliases: aiCharacterChat routes

Product context: `ios-client/pfm-kb/modules/ai-character-chat.md`

## What it is
AI character chat intro and conversation routes surfaced from AppRoutes.

## Graph anchors
| `aiCharacterChat` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |
| `aiCharacterChatIntro` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Logging raw chat PII.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "AI Character Chat" --graph $GRAPH
```
