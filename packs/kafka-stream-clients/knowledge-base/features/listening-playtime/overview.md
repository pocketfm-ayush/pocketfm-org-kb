# Listening Playtime

Aliases: audio-playtime-worker, user_show_playtime, critical pipeline

Product context: `kafka-stream-clients/pfm-kb/modules/listening-playtime.md`

## What it is
Critical-path audio listening playtime persistence (date-wise user/device progress) plus related zero-USS unlock helpers on playtime topics.

## Graph anchors
| `audio_playtime` | `workers/streaming/audio_playtime.py` |
| `user_show_playtime` | `workers/user_show_playtime/` |
| `user_show_playtime_msk` | `workers/user_show_playtime_msk/` |

## Risks
- Confusing with Fabric playtime consumers (exclusion/AI-PGC) or Radioly listening-progress APIs.
- Letting critical playtime lag — Continue Playing / progress gates go stale.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Listening Playtime" --graph $GRAPH
```
