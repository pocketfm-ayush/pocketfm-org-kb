# App open ads

Aliases: app open ad, open ad, launch ad

Product context: `radioly/pfm-kb/modules/app-open-ads.md` · related `launch-overlays`

## What it is

Ads shown on cold/warm app open. Distinct from in-player mid-rolls.

## Graph anchors

CODE SEARCH `app_open` under `v3/ads/`.


## Key product notes

A **full-screen network ad** at cold launch or when the listener
returns from background. One product, two setups the server may attach
on launch config.

This is **not** a launch overlay (popup / nudge / slider), not a
mid-roll, and not watch-to-unlock.

## Risks

- Mixing with launch overlays / rating popup.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "app open ads" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

