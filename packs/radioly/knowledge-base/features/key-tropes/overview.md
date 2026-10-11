# Key tropes

Aliases: tropes, themes, Discover Stories by Theme, explore themes

Product context: `radioly/pfm-kb/modules/key-tropes.md`

## What it is

Home themes rail plus a theme page. Not Discover shorts. Same hide /
pair rules as Home. Killing personalization must fall back to editorial.

## Graph anchors

| Symbol | Source |
|---|---|
| key tropes | `v3/experience/key_tropes/` |


## Key product notes

A Home rail of story **themes**, plus a theme page of titles. Not
Discover shorts.

## Risks

- Leaving a disabled / losing-pair title on a theme.
- Blanking the rail when personalization is off.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "key tropes" --graph $GRAPH
```
