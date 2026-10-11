# Listening Streaks

Aliases: PFMStreaks, streak detail, live activity

Product context: `ios-client/pfm-kb/modules/streaks.md`

## What it is
Daily listening streaks UI plus Live Activity widget extension for streak presence.

## Graph anchors
| `PFMStreaks` | `Pocket FM/Presentation/Features/PFMStreaks` |
| `streakDetail route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |
| `PFMStreakLiveActivityWidget` | `PFMStreakLiveActivityWidget` |

## Risks
- Hardcoding streak thresholds owned by backend.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Listening Streaks" --graph $GRAPH
```
