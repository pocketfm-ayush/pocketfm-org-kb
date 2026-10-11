# UGC (Flutter)

Aliases: PFMUgcOriginal, Flutter UGC bridge

Product context: `ios-client/pfm-kb/modules/ugc-flutter.md`

## What it is
UGC/originals experiences embedded via Flutter modules and native deeplink bridge.

## Graph anchors
| `PFMUgcOriginal` | `Pocket FM/Presentation/Features/PFMUgcOriginal` |
| `FlutterUGCDeeplinkBridge` | `Pocket FM/Flutter/FlutterUGCDeeplinkBridge.swift` |
| `Flutter` | `Pocket FM/Flutter` |

## Risks
- Editing only native Swift when the live UGC UI is Flutter-hosted.
- Breaking Flutter engine lifecycle assumptions.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "UGC (Flutter)" --graph $GRAPH
```
