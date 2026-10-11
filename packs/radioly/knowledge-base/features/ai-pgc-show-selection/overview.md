# AI ↔ PGC show selection

Aliases: AI PGC, AI/PGC, AI<>PGC, AI <-> PGC, PGC show selection, PGC replacement, duplicate show, duplicate pair, keep_ai_default, user_tg pgc, FMF-3783, FMF-3782

Product context: `radioly/pfm-kb/modules/ai-pgc-show-selection.md` · flow `radioly/pfm-kb/flows/ai-pgc-across-surfaces.md`

## What it is

Radioly picks **one** show from an AI↔PGC pair for this user on feed / library /
show-feed surfaces. It does **not** invent pairs. Pairs come from CMS table
`ai_pgc_show_mapping`, cached by `ExclusionConfigService`.

Search has a **parallel** path (`apply_pgc_show_replacement` in pocket_search).
Same pair map and similar rules — different service. Do not name Search
handlers when the ask is Radioly.

`ShowReplicaHelper` is a **different** older device-age replica map. Do not
treat it as AI↔PGC.

## Entry / surfaces

| Surface | Helper | Behavior |
|---|---|---|
| Topic / module entities | `filter_duplicate_shows_from_topic_entities` | keep / skip if alternate already listed / substitute |
| Library | `filter_duplicate_shows_from_library_feed` | same |
| Show feed widgets | `filter_duplicate_shows_from_show_feed` | drop ineligible in place |
| Pre-slice candidate lists | `filter_ineligible_duplicate_show_ids` | drop only (no substitute) so a top-N row can backfill |

All of those call `DuplicateShowService.is_show_eligible`. Files:
`v2/feed_api/helpers.py`,
`v2/content_api/services/duplicate_show_service/duplicate_show_service.py`.

Admin (not the user path): `POST /v3/content/internal/ai_pgc_pair_config`
sets `keep_ai_default` on the pair row, then
`ExclusionConfigService.invalidate_cache`.

## Decision order (`_compute_show_eligibility`)

Show not in any duplicate set (AI↔PGC + legacy CVC/ASURA) → always eligible.

1. **SEM master kill** — AI↔PGC routing off; show the requested ID. CVC/ASURA
   still use the legacy factory.
2. **Manual override** (`OverrideService`) — CS-set preferred ID wins.
3. **Playtime engagement** (`evaluate_pgc_engagement`) — ≥ **180s** on either
   side (Scylla via `ShowPlaytimeService`, 14-day recency for ties). PGC wins
   if only PGC is engaged, or both engaged and PGC is more recent / tied.
   Beats `user_tg` pin. Then availability guard.
4. **Marketing pin** — `user_tg = pgc_<pgc_show_id>` (FMF-3783). Only when
   both sides are cold-start. Forces PGC if that PGC is live.
5. **Cold start** — default **PGC**. If `keep_ai_default` is true on the pair,
   default **AI**. Then availability guard. Lookup failure → PGC.
6. **Legacy factory** — CVC / ASURA playtime pairing.

`duplicate_framework:ai_pgc:kill_switch` plus a per-pair search cache are
applied on the AI↔PGC exits (`_finalize_eligibility`).

## Unlock / player (same pair, later)

When the user is already on a PGC redirect, unlocking can pass `ai_show_id`
and `UnlockMigrationService` copies the AI unlock row to the PGC show before
the Scylla read (`v3/unlocking`). Replica compare uses
`GET /v3/unlocking/internal/...&replica_show_id=`.

## Risks

- Changing order (pin vs playtime vs `keep_ai_default`) desyncs Search.
- Pre-slice drop vs post-slice substitute: filtering after `top_10` leaves gaps.
- Pair map / kill-switch Redis misses fall back to hardcoded
  `ALTERNATE_SHOW_ID` — do not assume CMS is the only source.

## Tests

- `v2/feed_api/tests/test_helpers.py` (duplicate filter)
- `v2/content_api/services/duplicate_show_service/` tests
- `v3/unlocking/tests/api/test_get_view.py` (`replica_show_id`)


## Graph anchors

| Symbol | Source |
|---|---|
| `DuplicateShowService.is_show_eligible` | `v2/content_api/services/duplicate_show_service/` |
| `filter_duplicate_shows_from_*` | `v2/feed_api/helpers.py` |
| `ExclusionConfigService` | pair cache / `ai_pgc_show_mapping` |

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "DuplicateShowService" --graph $GRAPH
graphify query "AI PGC show selection" --graph $GRAPH --budget 4000
```
