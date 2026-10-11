# Player

Aliases: PFMPlayerView, playback manager, ad player, widgets

Product context: `ios-client/pfm-kb/modules/player.md`

## What it is
Playback UI and managers for audio/video listening, mini/expanded player helpers, and related play widgets.

## Graph anchors
| `PFMPlayerView` | `Pocket FM/Presentation/Features/PFMPlayerView` |
| `PFMPlaybackManager` | `Pocket FM/Presentation/Features/PFMPlayerView/ViewModel/PFMPlaybackManager.swift` |
| `PFMPlayWidgetHelpers` | `Pocket FM/Presentation/Features/PFMPlayWidgetHelpers` |

## Risks
- Putting networking/decoding in player ViewModels.
- Breaking Now Playing / CarPlay session assumptions.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Player" --graph $GRAPH
```
