# Unlocking Byline

Aliases: unlock byline, free tomorrow byline, lock message, how unlocked label

Product context: `radioly/pfm-kb/modules/unlocking-byline.md`

## What it is
Show-page / episode-list **copy and styling** that explains *how* an episode is
unlocked (plan byline, “free tomorrow”, styled lock messages). Not the unlock
mechanic itself — that remains show-details-unlock / auto-debit / wallet.

## Graph anchors
| Symbol | Source |
|---|---|
| `UnlockingBylineExperiment` | `v3/unlocking_byline/experiments/` |
| `ShowDetailBylineService` | `v3/unlocking_byline/services/` |
| `BylineStyleConfig` | `v3/unlocking_byline/byline_style_config.py` |
| `BylineKafkaService` | `v3/unlocking_byline/` (Kafka backfill path) |

## Key edges
- Show details enrichment calls byline helpers for eligible experiment users.
- Some paid plan IDs suppress byline text (`NO_BYLINE_PLAN_IDS`).
- Distinct from auto-debit (keep unlocking while listening).

## Risks
- Changing unlock counts when only byline copy should change.
- Inventing byline strings — they live in style config / locale sources.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "ShowDetailBylineService" --graph $GRAPH
```
