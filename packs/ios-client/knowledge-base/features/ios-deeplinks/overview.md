# Deeplinks

Aliases: AppRoutes deep links, Flutter UGC deeplink bridge

Product context: `ios-client/pfm-kb/modules/deeplinks.md`

## What it is
External URL / campaign / UGC deeplink routing into AppRoutes and Flutter bridges.

## Graph anchors
| `AppRoutes` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |
| `FlutterUGCDeeplinkBridge` | `Pocket FM/Flutter/FlutterUGCDeeplinkBridge.swift` |

## Risks
- Inventing string destinations instead of AppRoutes cases.
- Ignoring deferred attribution handoff owned by other packs.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Deeplinks" --graph $GRAPH
```
