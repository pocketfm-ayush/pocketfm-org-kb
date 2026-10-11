# Episode recap

Aliases: episode recap, recap audio, story recap, get_episode_recap

Product context: `radioly/pfm-kb/modules/episode-recap.md`

## What it is

`get_episode_recap` is one episode’s audio recap. Show-level AI recap
is a different product (`show_ai_recap`).

## Graph anchors

| Symbol | Source |
|---|---|
| `get_episode_recap` | `v3/content/episode_recap/views.py` |

## Risks

- Inventing a recap on miss.
- Mixing this with show-level AI recap.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "get_episode_recap" --graph $GRAPH
```
