# Launch Config

Aliases: launch_config, fetch_config, refresh-config, app launch config, cold start config

Product context: `radioly/pfm-kb/modules/launch-config.md` ·
flow `radioly/pfm-kb/flows/open-app-with-launch-config.md`

## What it is
HTTP surface that returns Android/iOS launch configuration on cold start /
refresh: feature flags, experiment hooks, GTM/slider inputs, player sampling,
LiveOps bottom sheet / splash hooks, Episode Zero allocation hooks, and related
bootstrap payloads before home fully renders.

## Graph anchors
| Symbol | Source |
|---|---|
| `LaunchConfigView` | `v2/feed_api/viewsets.py` |
| Launch config tests | `v2/feed_api/tests/integration/test_launch_config_api.py` |
| LiveOps bottom slider | `BOTTOM_SLIDER_LIVEOPS` wiring in launch path |
| Episode Zero allocate | `EpisodeZeroService` (launch_config path) |

URL evidence: `/v2/feed_api/launch_config`.

## Key edges
- Experiments often allocate here, not on home feed.
- Nexus/IAM fields may be read during config build (FMF-4712).
- Budget Booster / GTM promos may attach via launch surfaces.

## Risks
- Huge blast radius — many features hang off launch payload shape.
- Do not invent flag defaults; read builders in source.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "LaunchConfigView" --graph $GRAPH
```
