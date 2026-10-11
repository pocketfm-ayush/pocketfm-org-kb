# Android Auto / Automotive

Aliases: Android Auto, automotive UI

Product context: `android-client/pfm-kb/modules/automotive.md`

## What it is
Automotive / Android Auto browsing and playback integration layered on the player service.

## Graph anchors
| `automotive ui` | `aural/automotive/ui` |
| `AuralAndroidAutoManager` | `aural/player/service/.../androidauto/` |

## Risks
- Changing Auto browse trees without media-session impact review.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Android Auto / Automotive" --graph $GRAPH
```
