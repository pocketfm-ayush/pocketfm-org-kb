# Loyalty and Spending Tags to MoEngage

Aliases: loyalty-moengage-events, user-spending-tag-moengage

Product context: `kafka-stream-clients/pfm-kb/modules/loyalty-moengage-tags.md`

## What it is
Workers that push loyalty and spending-tag attributes into MoEngage for CRM targeting.

## Graph anchors
| `loyalty_moengage_events` | `workers/loyalty_moengage_events.py` |
| `user_spending_tag_moengage` | `workers/user_spending_tag_moengage.py` |

## Risks
- Sending raw PII beyond needed CRM attributes.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Loyalty and Spending Tags to MoEngage" --graph $GRAPH
```
