# Campaign-only Shows

Aliases: campaign show, restricted show, hidden campaign

Product context: `search/pfm-kb/modules/campaign-only-shows.md`

## What it is
Some shows are visible only to users in specific campaigns. Filter removes restricted shows
for non-campaign users; includes kill-switch and AppsFlyer attribution paths.

## Graph anchors
| Symbol | Source | Community | Degree |
|---|---|---|---|
| `apply_campaign_only_show_filter()` | `v2/search/services/campaign_only_show_service.py` L192 | 15 | 13 |
| `is_user_in_any_campaign()` | same file | 15 | — |
| `_present_restricted()` | same file | 15 | — |

## Key edges
- Called from v2 finalize + v3 `._apply_personalization_core()` [EXTRACTED]
- Community 26 — AppsFlyer error / connection BDD coverage

## Tests
- `v2/search/tests/test_campaign_only_show_filter_bdd.py`
- `v2/search/tests/test_appsflyer_attribution.py`

## Risks
- Campaign membership cache (`_is_campaign_user_cached`) — stale membership = wrong visibility.
- Kill switch disables filtering — confirm intended for incidents only.
- Attribution API failures must degrade safely (Community 26).

## Query
```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify explain "apply_campaign_only_show_filter" --graph $GRAPH
```
