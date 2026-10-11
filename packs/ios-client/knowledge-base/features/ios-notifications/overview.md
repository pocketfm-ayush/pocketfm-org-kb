# Push Notifications

Aliases: NotificationService, PushTemplateExtension

Product context: `ios-client/pfm-kb/modules/push-notifications.md`

## What it is
Push notification service extensions and rich push templates outside the main feature folders.

## Graph anchors
| `NotificationService` | `NotificationService` |
| `NotificationServiceExtension` | `NotificationServiceExtension` |
| `PushTemplateExtension` | `PushTemplateExtension` |

## Risks
- Assuming main-app feature flags automatically apply inside notification extensions.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Push Notifications" --graph $GRAPH
```
