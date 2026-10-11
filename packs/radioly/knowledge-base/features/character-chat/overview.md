# Character chat

Aliases: talk to character, character chatbot, show character chat

Product context: `radioly/pfm-kb/modules/character-chat.md` · flow `radioly/pfm-kb/flows/talk-to-character.md`

## What it is

Logged-in chat with one in-world character. Not player character icons.
Crisis replies break character.

## Graph anchors

| Symbol | Source |
|---|---|
| character chat | `v3/experience/character_chat/` |


## Key product notes

A logged-in chat with one in-world character from a configured title.
The character only knows episodes the listener has reached.

## Risks

- Opening chat for guests.
- Spoiling past the listener’s furthest episode.
- Falling back to static bubble copy after the impression cap.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "character chat" --graph $GRAPH
```
