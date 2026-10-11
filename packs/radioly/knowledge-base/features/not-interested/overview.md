# Not interested

Aliases: not interested, hide show, remove from feed

Product context: `radioly/pfm-kb/modules/not-interested.md`

## What it is

Listener signal to suppress a show from future rails.

## Graph anchors

| Symbol related | Source area |
|---|---|
| autoplay / continue removed shows | `audio_playtime.*_removed_show*` (`data/scylla-catalog.md`) |
| feed removal helpers | `v2/feed_api/services/removed_show/` |


## Key product notes

The listener dismisses a **title** (show / book / novel) or a
**community post** so it should stop being offered. Not unsubscribe
from Library, and not autoplay “not this next” (autoplay-playlist).

## Risks

- Assuming not-interested is permanent account-wide without checking device vs user keys.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "not interested" --graph $GRAPH
```
