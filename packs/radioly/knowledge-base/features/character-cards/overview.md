# Player character cards

Aliases: character sheet, character icons, player characters

Product context: `radioly/pfm-kb/modules/character-cards.md`

## What it is

Player icons from a published sheet. Not character chat. Empty is
normal when CMS has no sheet.

## Graph anchors

| Symbol | Source |
|---|---|
| character cards | `v3/experience/character_cards/` |


## Key product notes

Icons (and a tooltip) on the **player** for a title that has a
published character sheet. Not the chat bubble.

## Risks

- Inventing characters when the sheet is missing.
- Treating this as the chat bubble.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "character cards" --graph $GRAPH
```
