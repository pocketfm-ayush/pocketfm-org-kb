# Ads Playtime, Streaks, Offerwall

Aliases: ad playtime scylla, ad streak retain, reset RV keys, PAM, offerwall webhooks

Product context: `kafka-stream-clients/pfm-kb/modules/ads-playtime-streaks-and-offerwall.md`

## What it is
Ads engagement workers: ad playtime to Scylla, streak retain progress, RV streak key resets, PAM revenue, Tapjoy/Digital Turbine webhook credits.

## Graph anchors
| `playtime_consumer_scylla_ads` | `workers/advertisement/playtime_v2/` |
| `streak_retain_feature` | `workers/streak_retain_feature/` |
| `reset_rv_keys` | `workers/reset_rv_keys/` |
| `pam_v2` | `workers/advertisement/pam_v2/` |
| `tapjoy_webhook_worker` | `workers/tapjoy_webhook_worker_new.py` |
| `digital_turbine_webhook_worker` | `workers/digital_turbine_webhook_worker_new.py` |

## Risks
- Crediting offerwall rewards before server idempotent ack.
- Confusing with Airflow offerwall reward ops or mobile fm-ads-client UI.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Ads Playtime, Streaks, Offerwall" --graph $GRAPH
```
