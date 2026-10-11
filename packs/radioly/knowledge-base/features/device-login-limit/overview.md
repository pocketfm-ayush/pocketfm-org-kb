# Device login limit

Aliases: device limit, login limit, too many devices

Product context: `radioly/pfm-kb/modules/device-login-limit.md`

## What it is

Caps concurrent / registered devices per account.

## Graph anchors

| Symbol area | Source |
|---|---|
| `user_login_device` | `audio_playtime.user_login_device` (`data/scylla-catalog.md`) |
| device login helpers | `v2/user_api/` (CODE SEARCH) |


## Key product notes

A **weekly cap on distinct devices** that may request a login
code for one login. Distinct from multi-profile’s “five devices
at once” listen/download benefit, and from OTP rate limits.

## Risks

- Inventing the numeric cap without packed config/evidence.

## Related
- `iam-identity`
- `otp-login`

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "device login limit" --graph $GRAPH
```
