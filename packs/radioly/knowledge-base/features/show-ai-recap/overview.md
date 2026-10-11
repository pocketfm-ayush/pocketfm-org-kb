# Show AI recap

Aliases: daily recap, saga so far, show recap, AI recap

Product context: `radioly/pfm-kb/modules/show-ai-recap.md`

## What it is

Skippable audio recap before the next episode. Not `get_episode_recap`.

## Graph anchors

| Symbol | Source |
|---|---|
| show AI recap | `v3/experience/show_ai_recap/` |


## Key product notes

A skippable audio recap before the next episode — either yesterday’s
episode or a multi-episode “saga so far.” The listener is in **one**
of those two, not both.

This is not the per-episode recap card (episode-recap).

## Risks

- Mixing this with the per-episode recap card.
- Error-sheeting when recap audio is missing — continue into the episode.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "ShowAIRecapService" --graph $GRAPH
```
