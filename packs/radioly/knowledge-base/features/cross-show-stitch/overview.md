# Cross-show stitch

Aliases: stitching UX, cross details, cross show, show chain, bridge promo

Product context: `radioly/pfm-kb/modules/cross-show-stitch.md` · flow `radioly/pfm-kb/flows/finish-show.md`

## What it is

Test-only chained titles. Not default autoplay. No chain id → no block.

## Graph anchors

| Symbol | Source |
|---|---|
| stitching service | `v3/content/stitching_ux/service.py` |


## Key product notes

A **test-only** handoff: a few titles are chained. Testers can see a
next-title block at the end of the episode list, and sometimes hear a
short bridge before the next title’s first episode.

This is not general autoplay and not Home recommendations.

## Risks

- Picking a “similar” title when the chain id is missing.
- Treating stitch as everyone’s next-up.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "ShowCleanerService" --graph $GRAPH
```
