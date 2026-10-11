# Pocket Pick

Aliases: pocket pick, playables, playable swipe

Product context: `radioly/pfm-kb/modules/pocket-pick.md`

## What it is

Swipe deck of playable title cards. Not Discover, not Home. Empty deck
is allowed. At most one deck per local day.

## Graph anchors

| Symbol | Source |
|---|---|
| pocket pick | `v3/experience/pocket_pick/` |


## Key product notes

A swipe deck of playable title cards (about six), auto-advancing
every 30 seconds. Not Discover, not Home.

## Risks

- Inventing cards when the deck is empty.
- Sending “I am on journey X” from the client.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "pocket pick" --graph $GRAPH
```
