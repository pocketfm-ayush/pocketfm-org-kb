# Wallet Coins and Payment Recon

Aliases: coins disbursal, payment recon, super saver, juspay mandate, partnership credit

Product context: `kafka-stream-clients/pfm-kb/modules/wallet-coins-and-recon.md`

## What it is
Payment/wallet workers: coin disbursal, gateway recon queues, Super Saver daily disburse, Juspay mandate pre-debit notices, partnership credit coins, battle-pass-for-writers credits.

## Graph anchors
| `coins_disbursal` | `workers/payments/coins_disbursal.py` |
| `recon_worker` | `workers/payments/recon_worker.py` |
| `super_saver_daily_disburse` | `workers/payments/` |
| `juspay_mandate` | `workers/payments/` |
| `credit_coins_v2` | `workers/partnership_campaign/` |

## Risks
- Double-crediting if recon and disbursal both 'fix' the same order without idempotency.
- Hard-coding coin amounts.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Wallet Coins and Payment Recon" --graph $GRAPH
```
