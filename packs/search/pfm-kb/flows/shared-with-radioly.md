# Shared with Radioly (cross-product)

Participating packs: `search`, `radioly`.

## Ordered journey (product)

1. Listener searches or opens empty-query discovery.
2. Search retrieves / routes, then personalizes: AI/PGC → campaign-only →
   ME exclusion → override → disabled → DS thumbnails.
3. Parallel Radioly surfaces (Home, library, show feed) apply Radioly's
   AI↔PGC and visibility helpers — same product intent, different code.

## Modules

- Search modules under `modules/` for each personalize step.
- Radioly product: `../../radioly/pfm-kb/modules/ai-pgc-show-selection.md`
  and `visibility-filters.md`.

## User-visible invariants

- Personalization order in Search is pack-defined; do not reorder from memory.
- Radioly feed selection is not `apply_pgc_show_replacement`.

## Failure modes

- Citing `DuplicateShowService` for a Search ask (or the reverse).
