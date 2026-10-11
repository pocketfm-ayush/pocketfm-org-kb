# Experience Re-engage and Discover

Aliases: user reengage reward, discover tab viewed, key tropes, experience shared events

Product context: `kafka-stream-clients/pfm-kb/modules/experience-reengage-and-discover.md`

## What it is
Experience-domain workers: re-engage rewards, Discover tab view tracking, key tropes events, converted media upload, and shared experience event handlers.

## Graph anchors
| `user_reengage_reward_worker` | `workers/experience/user_reengage_reward_worker.py` |
| `discover_tab_viewed_tracking_worker` | `workers/experience/discover_tab/` |
| `key_tropes_worker` | `workers/experience/key_tropes/` |
| `experience_events_worker` | `workers/experience/shared_events/` |

## Risks
- Hard-coding reengage coin amounts.
- Assuming Discover tracking alone drives ranking.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Experience Re-engage and Discover" --graph $GRAPH
```
