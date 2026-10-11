# Daily listen-task coins

Aliases: gamified rewards, daily challenges, claim rewards

Product context: `radioly/pfm-kb/modules/gamified-rewards.md`

## What it is

Listen-task coins. Claim vs auto-pay is server-owned. Not daily
check-in.

## Graph anchors

| Symbol | Source |
|---|---|
| `GamifiedRewardsView` | `v3/payments/views/gamified_rewards.py` |


## Key product notes

Coins for finishing a **listen task** (unlock N episodes, sometimes
across series). Daily and weekly pots.

Some listeners are paid when the task completes. Others must
**claim**. That split is server-owned.

Not the check-in calendar. Not ops re-engage coins.

## Risks

- Treating task complete as credit for claim listeners.
- Stacking this with the check-in calendar.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "gamified rewards" --graph $GRAPH
```
