# Show referral

Aliases: gift and earn, invite friends, series gift, referral code

Product context: `radioly/pfm-kb/modules/show-referral.md`

## What it is

Gift a specific series. **New invite codes and new redemptions are
turned off.** Do not build this as a live invite program.

## Graph anchors

| Symbol | Source |
|---|---|
| show referral | `v3/experience/show_referral/` |


## Key product notes

Gift a **specific series** to a friend (Gift & Earn). Referrer shares a
code; referee enters it (Profile → Enter Referral Code). Rewards are
coins for progress on **that** gifted series, not the whole catalog.

**New invite codes and new redemptions are turned off.** Do not build
this as a live invite program unless product turns it back on. Existing
invite tracking may still load.

## Risks

- Shipping new invite/redeem as if the program is live.
- Rewarding catalog-wide listens instead of the gifted series.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "show referral" --graph $GRAPH
```
