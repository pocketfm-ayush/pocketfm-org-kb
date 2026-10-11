# Budget Booster Worker

Aliases: budget-booster-pack consumer

Product context: `kafka-stream-clients/pfm-kb/modules/budget-booster.md`

## What it is
Worker that applies Budget Booster pack entitlements/eligibility updates from Kafka events.

## Graph anchors
| `budget_booster_pack` | `workers/budget_booster_pack/consumer.py` |

## Risks
- Hard-coding booster multipliers.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Budget Booster Worker" --graph $GRAPH
```
