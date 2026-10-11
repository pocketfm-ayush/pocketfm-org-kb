# Search request

Cross-module path for one search tap. Participating modules: universal-search,
query-processing, language-biased-search, genre-trope-discovery, show-filter,
response-caching, then personalization in this **fixed** order.

## Journey

1. Clean the query (query-processing).
2. Reuse a shared unpersonalized payload when one exists (response-caching).
3. If no reusable payload:
   - empty → genre/trope discovery
   - genre/topic filter → show-filter
   - typed text → language-biased search
4. Personalize, in order:
   1. AI / PGC replacement
   2. Campaign-only
   3. Mutual exclusion
   4. Override (hide the non-preferred pair member)
   5. Disabled-show removal
   6. Device-specific art
5. Return the list.

## User-Visible Invariants

- Shared payload must not already be personalized.
- A later step can drop a show a earlier step just swapped in.
- Changing this order changes what two users see for the same query.

## Failure modes

- Shared-store down → still search, skip reuse.
- Genre source down → empty search degrades; do not invent a catalog.
- Attribution down → hide campaign-only titles rather than leak them.
