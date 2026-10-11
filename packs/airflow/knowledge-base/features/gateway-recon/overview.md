# Payment Gateway Recon

Aliases: apple recon, stripe recon, juspay recon, phonepe recon

Product context: `airflow/pfm-kb/modules/gateway-recon.md`

## What it is
Reconciles gateway transactions so purchases settle and entitlements match the ledger.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| Recon workflows | `temporal/payments/workflows/` |
| payments domain | `payments/` |

## Risks
- Claiming a specific gateway is live without checking schedules.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Payment Gateway Recon" --graph $GRAPH
```
