# Player chrome

Aliases: player config, playback speed, sleep timer, player tabs

Product context: `radioly/pfm-kb/modules/player-chrome.md`

## What it is

`/v3/config/player_config` returns speeds, sleep, tabs, and background-play
rules. Not paywall. Not player rails.

## Graph anchors

| Symbol | Source |
|---|---|
| player config | `v3/content_api/` (player_config) |

## Risks

- Inventing tabs or “background play is fine” on the client.
- Treating a reel background-play block as a global player outage.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "get_player_config" --graph $GRAPH
```
