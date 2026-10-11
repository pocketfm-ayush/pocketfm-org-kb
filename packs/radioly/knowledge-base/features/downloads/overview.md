# Downloads

Aliases: download, offline download, downloaded episodes

Product context: `radioly/pfm-kb/modules/downloads.md`

## What it is

Offline download eligibility and entitlements for episodes.

## Graph anchors

CODE SEARCH `download` under content / user APIs. Confirm before naming handlers.


## Key product notes

Saving an episode **on this device** to play without network. Library
has a Downloads tab; the player has a download control. This is not
unlock, not the saved / subscribed list, and not a mid-roll skip.

## Risks

- Claiming offline rights without unlock / subscription evidence.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "downloads" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

