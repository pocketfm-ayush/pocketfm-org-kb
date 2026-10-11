# Feeds and Packaged Deployment

Aliases: packaged_deployment S3/Scylla, non-PD deps, last active time

Product context: `kafka-stream-clients/pfm-kb/modules/feeds-packaged-deployment.md`

## What it is
Feed/cache workers that dump or refresh packaged deployment data to Redis/S3/Scylla and update last-active timestamps for feeds.

## Graph anchors
| `packaged_deployment` | `workers/packaged_deployment/` |
| `update_last_active_time_msk` | `workers/feeds/update_last_active_time_msk.py` |
| `non_personalised_consumer_msk` | `workers/packaged_deployment/non_pd_deps/` |

## Risks
- Treating S3 dumps as the live personalization API.
- Confusing novels PD workers with FM packaged deployment.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Feeds and Packaged Deployment" --graph $GRAPH
```
