# Discover tab

Aliases: Discover, shorts, reels, discover feed

Product context: `radioly/pfm-kb/modules/discover-tab.md` · flow `radioly/pfm-kb/flows/open-discover.md`

## What it is

Short-video promo tab. Not Home. English / Hindi / German only.
First-week new or reinstall: tab visible, default-land forced to Home.

## Graph anchors

| Symbol | Source |
|---|---|
| discover tab | `v3/experience/discover_tab/` |

## Risks

- Assembling Discover from Home rails.
- Default-landing a D0–D7 reinstall on Discover.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "discover_tab" --graph $GRAPH
```

## Related
- `stage`
- `pocket-pick`
- `liveops-tentpole`
