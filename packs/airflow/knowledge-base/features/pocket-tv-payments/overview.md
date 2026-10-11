# Pocket TV Payments Jobs

Aliases: tv juspay recon, tv s2s subscription events, tv shutdown refund

Product context: `airflow/pfm-kb/modules/pocket-tv-payments.md`

## What it is
TV gateway recon, subscription S2S events, and TV shutdown refund batches.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `pocket_tv/payments/` | domain |
| TV recon DAGs / Temporal | `dags/` / temporal/payments |

## Risks
- Applying FM-only payment rules to TV without checking TV paths.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Pocket TV Payments Jobs" --graph $GRAPH
```
