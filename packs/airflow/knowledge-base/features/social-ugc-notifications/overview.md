# Social / UGC Notifications

Aliases: social_notifications, ugc comment reply notifications

Product context: `airflow/pfm-kb/modules/social-ugc-notifications.md`

## What it is
Scheduled/service jobs that send social and UGC comment-reply style notifications to listeners.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `social_notification_service` | `social_notifications/social_notification_service.py` |
| `ugc_comment_reply_notification_service` | `social_notifications/ugc_comment_reply_notification_service.py` |

## Risks
- Spamming notifications without reading eligibility constants.
- Confusing these with MoEngage CRM campaign pushes.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Social / UGC Notifications" --graph $GRAPH
```
