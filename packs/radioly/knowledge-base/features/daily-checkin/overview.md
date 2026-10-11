# Daily check-in rewards

Aliases: daily check-in, check-in calendar, jackpot day

Product context: `radioly/pfm-kb/modules/daily-checkin.md`

## What it is

Once-a-local-day coin credit. Replaces listen streak for allocated
listeners. Enrollment is at launch, not calendar open.

## Graph anchors

| Symbol | Source |
|---|---|
| daily check-in | `v3/gamification/daily_checkin_rewards/` |


## Key product notes

A once-a-local-day check-in that pays coins and grows a day count.
Some days are jackpots. The calendar is a read; the check-in is the
credit.

For allocated listeners this **replaces** the listen streak. Enrollment
is decided at launch, not when they open the calendar.

## Risks

- Treating the calendar read as a claim.
- Tracking streak and check-in on the same launch.
- Assuming Android (current experiments are iOS IN/US).

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "daily checkin" --graph $GRAPH
```
