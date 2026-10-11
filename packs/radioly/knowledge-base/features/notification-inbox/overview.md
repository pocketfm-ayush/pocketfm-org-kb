# Notification Inbox

Aliases: in-app notifications, notification center, push notification inbox

Product context: `radioly/pfm-kb/modules/notification-inbox.md`

## What it is
In-app / push notification plumbing in Radioly (`v2/notification`,
`v2/push_notification`, WhatsApp siblings). Distinct from OS permission prompts
(`notification-permission`).

## Graph anchors
| Symbol / area | Source |
|---|---|
| Notification services | `v2/notification/` |
| Push notification | `v2/push_notification/` |
| Rate limiter | `v2/notification/user_wise_rate_limiter.py` |


## Key product notes

Server-backed notification content and dispatch that powers in-app notification
experiences and related push fan-out. Separate from the OS permission prompt.

## Risks
- Inbox UX may be client-owned; confirm API contracts before claiming screens.
- Rate limits and dispatch paths differ by channel.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "notification dispatch inbox" --graph $GRAPH
```
