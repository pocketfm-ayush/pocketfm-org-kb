# Sponsored ads

Aliases: sponsored, sponsored show, brand ad

Product context: `radioly/pfm-kb/modules/sponsored-ads.md`

## What it is

Brand / sponsored placements. Distinct from RV, banner, and app-open ads.

## Graph anchors

CODE SEARCH `sponsored` under `v3/ads/` / feed widgets.


## Key product notes

A **brand sheet** (“a brand is sponsoring your next episode”):
watch a short message, one episode opens. Not a display still
(banner-ads), not a mid-roll (in-player), not the lock-sheet
watch-to-unlock pack (rewarded-ads). No coins.

## Risks

- Collapsing all ad types into one handler.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "sponsored ads" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

