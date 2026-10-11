# Referral Rewards Workers

Aliases: referral state updates, show referral reward

Product context: `kafka-stream-clients/pfm-kb/modules/referral-rewards.md`

## What it is
Workers that update referral program states and disburse show-referral rewards.

## Graph anchors
| `update_referral_states` | `workers/referral/` |
| `show_referral_reward_worker` | `workers/show_referral_reward_worker.py` |

## Risks
- Crediting referral rewards twice across MSK/non-MSK paths.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Referral Rewards Workers" --graph $GRAPH
```
