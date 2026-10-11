# Listening Streaks

Aliases: daily streaks, streak reclaim

Product context: `android-client/pfm-kb/modules/streaks.md`

## What it is
Daily listening streak tracking, reclaim, and related engage surfaces.

## Graph anchors
| `streaks ui` | `aural/streaks/ui` |
| `streaks domain` | `aural/streaks/domain` |
| `engage data` | `aural/engage/data` |

## Risks
- Hard-coding streak thresholds that backend/config owns.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Listening Streaks" --graph $GRAPH
```
