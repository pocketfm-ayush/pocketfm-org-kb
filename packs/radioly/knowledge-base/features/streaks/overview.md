# Streaks

Aliases: listen streak, daily streak, streak config, keep the streak

Product context: `radioly/pfm-kb/modules/streaks.md`

## What it is

Launch chooses listen streak **or** daily check-in — not both.
Opening Home does not claim the day.

## Graph anchors

| Symbol | Source |
|---|---|
| streak | `v3/experience/streak/` |


## Key product notes

Launch tells the app whether to track a **listen streak** or **daily
check-in**. Those two are alternatives for one launch, not a stack.

The listen streak is a day-count the listener keeps by coming back
(listen / claim). This slice only owns that launch choice and the
countdown. Claim rules and coin amounts live with the older streak
product.

## Risks

- Tracking streak and check-in on the same launch.
- Client-deciding “this user is on check-in.”

## Related
- `daily-checkin`
- `loyalty`
- `rewarded-ads`

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "streaks" --graph $GRAPH
```
