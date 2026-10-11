# AI ↔ PGC across feed and search

Same product rule, two products.

| Surface | Product module |
|---|---|
| Home feed, library, show rails | [ai-pgc-show-selection](../modules/ai-pgc-show-selection.md) |
| Search results | [Search AI/PGC](../../search/modules/ai-pgc-replacement.md) |
| Player unlock after a PGC redirect | same Radioly module (progress copy) |

## User-Visible Invariants

- Pair membership is shared. Changing a pair in CMS eventually changes
  both feed and search (freshness window is operational, not recorded here).
- Playtime ≥ ~3 minutes and “keep AI for cold users” must stay aligned
  across surfaces or the same listener sees AI on feed and PGC in search
  (or the reverse).
- Device-age “replica shows” are a different, older product. Do not treat
  them as AI/PGC.

## Failure modes

- Routing kill on one surface only → split experience.
- Marketing pin honored on search but ignored on feed after playtime —
  that is intended (playtime wins). Do not “fix” it without product.
