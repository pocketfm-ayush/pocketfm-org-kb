# Loyalty (Reward Club)

Aliases: Reward Club, Premium Club, Plus, Pro, Pro+

Product context: `radioly/pfm-kb/modules/loyalty.md`

## What it is

Logged-in tier from last-year hours and coin spend. Bonus is on
coin packs, not subscriptions. App must not send “I am on tier X.”

## Graph anchors

| Symbol | Source |
|---|---|
| loyalty | `v3/gamification/loyalty/` |


## Key product notes

A logged-in club: last-year listening and coin spend become a named tier,
then extra coins on coin-pack buys. A weekly Plus (also shown as Pro)
layer can raise that bonus for a calendar week.

Germany copy uses Premium-Club. The app does not pick the ladder or the
bonus.

## Risks

- Inventing the ladder, bonus %, or Plus targets.
- Leaving a ghost tier that is not on the current ladder.

## Related
- `rewards`
- `daily-checkin`
- `streaks`

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "loyalty" --graph $GRAPH
```
