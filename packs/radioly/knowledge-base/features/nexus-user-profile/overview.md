# Nexus User / Device Profile

Aliases: nexus, fetch_user_fields, user segments, user_created_at, device_created_at

Product context: `radioly/pfm-kb/modules/nexus-user-profile.md` ·
flow `radioly/pfm-kb/flows/users-devices-via-nexus-iam.md`

## What it is
Radioly integration to Nexus for **non-PII** user/device attributes: locale,
language, spending/listening/ad-playtime segments, create timestamps, and related
profile meta. Preferred over direct MySQL `users`/`devices` reads (FMF-4712).

## Graph anchors
| Symbol | Source |
|---|---|
| `NexusClientService` | `external_services/nexus/client.py` |
| `fetch_user_fields` | `external_services/nexus/user_data_fetcher.py` |
| `NEXUS_DEFAULT_USER_FIELDS` | same fetcher |

## Key edges
- Per-request LocalStore field cache warms a default field set for feed/ads/payments.
- Spending-segment defaults coerce `None` → non-spender.
- Rollout gated (e.g. Redis `nexus:iam_rollout_perc`) — verify before assuming 100%.

## Risks
- Do not put PII lookups here — that is IAM.
- Do not invent segment enum values beyond packed constants.
- Unit tests must mock Nexus; no live Scylla/HTTP.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "fetch_user_fields" --graph $GRAPH
graphify explain "NexusClientService" --graph $GRAPH
```
