# Comms WhatsApp, Email, Push

Aliases: communication worker, emails, MoEngage push pusher

Product context: `kafka-stream-clients/pfm-kb/modules/comms-whatsapp-email-push.md`

## What it is
Outbound communication workers for WhatsApp/email requests and MoEngage push notification pushing/segmentation helpers.

## Graph anchors
| `communication_worker_msk` | `workers/communication/` |
| `emails` | `workers/emails/` |
| `push_notification_to_moengage` | `workers/push_notification_to_moengage/` |

## Risks
- Sending production messages from local/test without guards.
- Editing templates that live in vendor dashboards.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Comms WhatsApp, Email, Push" --graph $GRAPH
```
