# UGC Backend Writer Bridge

Aliases: ugc backend, writer achievements, profile state, creator sync on delete

Product context: `radioly/pfm-kb/modules/ugc-backend-writer.md`

## What it is
HTTP bridge from Radioly to UGC/creator backend for **writer profile-state**
(achievements, is_writer) and **account-delete sync** so creator identity stays
aligned when an FM account is deleted. Not the Stage/Studio UI itself.

## Graph anchors
| Symbol | Source |
|---|---|
| `UGCBackendClient` | `external_services/ugc_backend/client.py` |
| `get_profile_state` | same client |
| delete-user sync callers | account-delete path (CODE SEARCH `_sync_ugc_delete`) |

## Key edges
- Writer profile / profile revamp may fetch achievements via this client.
- Account delete notifies UGC (`DELETE_USER_*` constants).
- Pair with `stage`, `writer-profile`, `account-delete`.

## Risks
- Embedding Studio product rules here — Studio rename lives under Stage.
- Logging Basic-auth credentials from secrets.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "UGCBackendClient" --graph $GRAPH
```
