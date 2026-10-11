# Coins and coin wallet

Aliases: coins, coin wallet, coin store, coin balance, UserCoinWallet

Product context: `radioly/pfm-kb/modules/coins-wallet.md` · flow `radioly/pfm-kb/flows/buy-coins.md`

## What it is

Spendable coin balance and lock price for unlocks. Separate from reward /
cashback cash. Follow-for-coins is gone.

## Graph anchors

| Symbol | Source |
|---|---|
| `UserCoinWallet` | payments models (see `Meta.db_table` `user_coin_wallet`) |
| `get_coin_data_from_cache` / `get_coin_data_cache_key` | `v2/payments/helpers.py` |
| `CoinsHistory` service | `v3/history/services/coins_history.py` |
| `TransactionsService` | `v3/payments/services/transactions_service.py` |

## Key edges

- Balance lives in MySQL `user_coin_wallet` (also listed in `radioly_api/db_router.py`).
- Reward / cashback wallets are different tables — do not mix with spendable coins.
- Show-page lock price must agree with paywall / unlock pricing path.

## Stores

- MySQL: `user_coin_wallet`, `user_coin_wallet_txns`, `transactions` — see `data/mysql-orm-catalog.md`.

## Risks

- Showing reward cash as spendable coins.
- Inventing a coin price that disagrees with the show page.

## Related
- `paywall`
- `checkout`
- `pricing`

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "coins wallet" --graph $GRAPH
```
