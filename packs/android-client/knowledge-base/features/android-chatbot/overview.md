# Chatbot

Aliases: in-app chatbot assistant

Product context: `android-client/pfm-kb/modules/chatbot.md`

## What it is
In-app chatbot experience for support/assistant style conversations.

## Graph anchors
| `chatbot ui` | `aural/chatbot/ui` |
| `chatbot domain` | `aural/chatbot/domain` |

## Risks
- Logging raw chat PII in analytics.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Chatbot" --graph $GRAPH
```
