# Checkout

Aliases: billing, payment options, PG

Product context: `radioly/pfm-kb/modules/checkout.md`

## What it is
Payment options and order placement. Dynamic PG routing (DRS) is infra under the hood — product story stays checkout.

## Graph anchors
| Orders / payments views | `v2/payments/` |
| Journey facade | `v3/payments/payments_journey/` |


## Key product notes

How a listener **pays** for a pack the shop or lock sheet already
offered. Not the shop. Not the lock sheet. Not “am I subscribed?”

## Risks
- Exposing DRS as a listener feature.
- Inventing gateway lists per market.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "Checkout" --graph $GRAPH
```
