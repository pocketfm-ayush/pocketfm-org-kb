# IAM Identity

Aliases: IAM, iam client, device accounts, profile PII, phone verify

Product context: `radioly/pfm-kb/modules/iam-identity.md` ·
flow `radioly/pfm-kb/flows/users-devices-via-nexus-iam.md`

## What it is
Radioly client to IAM for **identity and PII**: profile updates, device upsert,
phone OTP verify, device↔user account listings, webview/external-device tokens.
Target for migrating direct MySQL `users`/`devices` identity paths (FMF-4712).

## Graph anchors
| Symbol | Source |
|---|---|
| `IAMClient` | `external_services/iam/client.py` |
| Endpoint map | `external_services/iam/constants.py` (`UPDATE_PROFILE`, `UPSERT_DEVICE`, `DEVICE_ACCOUNTS`, …) |

## Risks
- Never log raw email/phone/tokens.
- Preserve existing cache invalidation semantics when swapping MySQL → IAM.
- Distinguish public vs private IAM base URLs by environment.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "IAMClient" --graph $GRAPH
```
