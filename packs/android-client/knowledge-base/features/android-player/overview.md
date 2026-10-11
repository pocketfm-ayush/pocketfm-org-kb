# Player

Aliases: ExoPlayer, mini player, MediaSession, downloads

Product context: `android-client/pfm-kb/modules/player.md`

## What it is
Aural playback stack: PlayerManager, media service/session, mini/expanded player UI, player-feed, Android Auto hooks, and download-related playback ownership.

## Graph anchors
| `PlayerView` | `aural/player/ui/.../PlayerView.kt` |
| `player service` | `aural/player/service` |
| `PlayerManager` | `aural/player/data` |

## Risks
- AndroidView player wraps without onRelease (DROID-8013 leak class).
- Putting new player features only in legacy FeedMediaPlayer without confirmation.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Player" --graph $GRAPH
```
