# Payment history

Aliases: history, coins history, purchase history, transaction receipt

Product context: `radioly/pfm-kb/modules/payment-history.md`

## What it is

Wallet History: coins, purchases, receipts, free-episode grants.
Ineligible (not IN/US, old app, no login) returns blank 200, not an error.

## Graph anchors

| Symbol | Source |
|---|---|
| `PaymentHistoryEligibilityService` | `v3/history/services/eligibility.py` |
| `CoinsHistoryView` | `v3/history/views/coins_history.py` |
| `PurchaseHistoryView` | `v3/history/views/purchase_history.py` |

## Risks

- Treating empty History outside India/US as an outage.
- Serving another login’s receipt from an order id.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "PaymentHistoryEligibilityService" --graph $GRAPH
```
