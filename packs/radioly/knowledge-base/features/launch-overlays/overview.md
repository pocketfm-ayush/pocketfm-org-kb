# Launch overlays

Aliases: launch overlay, launch popup, open overlay

Product context: `radioly/pfm-kb/modules/launch-overlays.md` · flow `radioly/pfm-kb/flows/launch-app.md`

## What it is

Non-ad overlays on launch (promo / permission / education). Distinct from app-open ads.

## Graph anchors

CODE SEARCH launch overlay / foreground config under `v3/experience/`.


## Key product notes

At launch (and on player open / minimise) the server may attach **one
overlay per surface**. Surfaces: home popup, Home top nudge, profile
tooltip, bottom slider, player-open popup, player-minimise popup.

This is **not** the impression-ack. Ack only records that the listener
saw one. Serving happens on launch / player config.

Distinct from first-run permission screens, the Unwind **Home banner**
(a feed module), and the paywall sheet.

## Risks

- Mixing with app-open ads or rating popup.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "launch overlays" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

