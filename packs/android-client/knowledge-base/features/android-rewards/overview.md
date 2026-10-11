# Rewards

Aliases: rewards center, incentive claims

Product context: `android-client/pfm-kb/modules/rewards.md`

## What it is
Rewards surfaces for claiming and viewing incentive/reward inventory beyond a single ad completion.

## Graph anchors
| `rewards ui` | `aural/rewards/ui` |
| `rewards domain` | `aural/rewards/domain` |

## Risks
- Merging rewards UI changes into ads offerwall without checking module boundaries.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Rewards" --graph $GRAPH
```
