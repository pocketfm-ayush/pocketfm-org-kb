# OTP login

Aliases: phone login, guest login, OTP

Product context: `radioly/pfm-kb/modules/otp-login.md`

## What it is
Phone OTP and guest/auth entry into a server-authenticated session. IAM may own verify endpoints under FMF-4712.

## Graph anchors
| Auth / OTP views | `v2/user_api/` |
| IAM verify | `external_services/iam` `VERIFY_PHONE_OTP` |


## Key product notes

How a listener starts a **session**: phone or email code, or Google /
Apple, or skip (guest). This is **not** “Forgot account?” (that is
account-recovery) and **not** the 48-hour invite code for a family
profile (that is multi-profile).

## Risks
- Logging OTP codes.
- Bypassing IAM when migration requires it.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "OTP login" --graph $GRAPH
```
