# Show details and unlock

Aliases: show page, show details, unlock, lock price, open episodes

Product context: `radioly/pfm-kb/modules/show-details-and-unlock.md` ·
flow `radioly/pfm-kb/flows/open-show.md` · related `unlocking-byline`, `liveops-tentpole` (Episode Zero)

## What it is
Show page payload plus unlock / lock-price behavior for episodes (and novel
chapters). Computes durable open-episode count; apps do not invent unlock locally.

## Graph anchors
| Symbol | Source |
|---|---|
| Unlock package | `v3/unlocking/` |
| Unlock Scylla stores | `show_unlocks.user_show_unlocks` / `device_show_unlocks` (`data/scylla-catalog.md`) |
| Byline enrichment | `v3/unlocking_byline/` (`ShowDetailBylineService`) |
| Episode Zero promo | `v3/liveops/services/episode_zero_service.py` |

## Key edges
- Feature slug `show-details-unlock` ↔ product `show-details-and-unlock`.
- Coin path: `coins-wallet`; sheet: `paywall`; keep-unlocking: `auto-debit`.
- Byline is copy only — does not change unlock counts.
- Episode Zero may prepend promo assets for eligible low-playtime Android users.

## Risks
- Inventing unlock buffer / free-count rules without source evidence.
- Resetting progress on AI↔PGC migration (must preserve further side).
- Confusing novel chapter unlock with a separate store product.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "show details unlock byline" --graph $GRAPH
```
