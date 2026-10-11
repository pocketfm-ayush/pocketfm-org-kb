# Rewards and Ads

Aliases: RewardedVideo, daily login reward, incent, offerwall

Product context: `ios-client/pfm-kb/modules/rewards-and-ads.md`

## What it is
Rewarded video, daily login rewards, incent routes, and offerwall-style reward discovery.

## Graph anchors
| `PFMRewardedVideo` | `Pocket FM/Presentation/Features/PFMRewardedVideo` |
| `PFMDailyLoginReward` | `Pocket FM/Presentation/Features/PFMDailyLoginReward` |
| `incent route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Crediting rewards locally before server acknowledgement.
- Confusing client offerwall with Airflow reward jobs.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Rewards and Ads" --graph $GRAPH
```
