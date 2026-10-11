# LiveOps Tentpole

Aliases: liveops, tentpole campaign, liveops billboard, episode zero, festive campaign sibling

Product context: `radioly/pfm-kb/modules/liveops-tentpole.md` ·
flow `radioly/pfm-kb/flows/liveops-across-surfaces.md`

## What it is
Timed promotional campaigns that **inject** branded surfaces into home, launch,
Discover, autoplay, ads, and My Store — no dedicated LiveOps URL. Includes genre
tentpole (weekly rotating shows) and direct-campaign (fixed assets). Sibling:
Episode Zero promo assets on show details for eligible low-playtime users.

## Graph anchors
| Symbol | Source |
|---|---|
| `LiveOpsTentpoleCampaignService` | `v3/liveops/campaign.py` |
| `LiveOpsTentpoleService` | `v3/liveops/services/` |
| `TentpoleEligibilityService` | `v3/liveops/` |
| `EpisodeZeroService` | `v3/liveops/services/episode_zero_service.py` |
| `LiveOpsImpressionService` | `v3/liveops/impression/` |

## Key edges
- Feed inject + launch bottom slider / splash / popup; Discover shorts; autoplay subset.
- Impressions via GTM publisher; Fabric must whitelist LiveOps asset types.
- Legacy festive campaigns can coexist on the same feed path — do not conflate.
- UGC ROW home nulls out tentpole service.

## Risks
- Inventing live genre experiment IDs or allocation %.
- Double-firing impressions on failed asset resolution.
- Treating LiveOps as a separate client API.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "LiveOpsTentpoleCampaignService" --graph $GRAPH
graphify explain "EpisodeZeroService" --graph $GRAPH
```
