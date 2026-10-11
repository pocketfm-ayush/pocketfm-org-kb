# Multi-profile

Aliases: family profile, extra profile, add profile

Product context: `radioly/pfm-kb/modules/multi-profile.md` · flow `radioly/pfm-kb/flows/switch-profile.md`

## What it is

Extra slots on one login. Cap five. 48-hour invite is not login OTP.
Age 13+. Shared coins and unlocks.

## Graph anchors

| Symbol | Source |
|---|---|
| profiles | `v2/profiles/` |


## Key product notes

Extra **slots on one login** so family or friends can listen with
shared unlocks and coins. Not a second account, not account-transfer,
not the public profile page (listener-profile / community-updates).

## Risks

- Treating a slot switch as a new login or account-transfer.
- Using the invite code as the account-login code.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "multi profile" --graph $GRAPH
```
