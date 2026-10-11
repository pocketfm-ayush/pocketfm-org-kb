# Story evolution

Aliases: story cards, collectible cards, card vault, card archive

Product context: `radioly/pfm-kb/modules/story-evolution.md`

## What it is

Collectible cards earned by finishing episodes of an enabled title.
Guest: no vault. Not interactive-story branches.

## Graph anchors

| Symbol | Source |
|---|---|
| story evolution | `v3/experience/story_evolution/` |


## Key product notes

Collectible cards earned by finishing episodes of an **enabled** title.
Home, show, player, profile, and library can surface a banner or vault
entry. The vault is the collection.

## Risks

- Treating cards as a global sticker book.
- Opening a vault for a guest.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "story evolution" --graph $GRAPH
```
