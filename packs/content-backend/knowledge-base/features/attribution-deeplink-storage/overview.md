# AppsFlyer GCD Deeplink Storage

Aliases: appsflyer-gcd-deeplinks, GCD deeplink cache

Product context: `content-backend/pfm-kb/modules/attribution-deeplink-storage.md`

## What it is
Private APIs to upsert/get/patch short-lived AppsFlyer GCD deeplink records keyed by device for later resolution.

## Graph anchors
| `NewService()` | `internal/app/appsflyergcd/service.go` |
| `UpsertDeeplink` | `internal/app/appsflyergcd/controller.go` |

## Risks
- Expecting records to live forever — TTL is short (hours).
- Confusing this with Relay user-attribution cookie store.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "NewService()" --graph $GRAPH
```
