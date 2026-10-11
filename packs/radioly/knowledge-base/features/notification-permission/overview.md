# Notification permission prompts

Aliases: enable notifications, notification sheet, push opt-in

Product context: `radioly/pfm-kb/modules/notification-permission.md`

## What it is

In-session Allow sheets. Not an inbox. Not first-run ATT.

## Graph anchors

| Symbol | Source |
|---|---|
| `get_notification_data` | `v2/push_notification/views.py` |


## Key product notes

In-session **Allow notifications** sheets (copy + a few show images).
Not an inbox. Not first-run ATT / notification (that is
onboarding-first-run).

## Risks

- Treating this as a notification feed.
- Blocking listen when they deny.

## Related
- `notification-inbox`

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "notification permission" --graph $GRAPH
```
