# Open Home

Participating modules: home-feed, default-feed-freshness, visibility-filters,
ai-pgc-show-selection, bigger-thumbnails.

## Journey

1. App requests Home / For You.
2. Personalized rails for this listener.
3. Shared editorial rails for the cohort (not a per-user blob).
4. Some locales: UGC-row stack instead, then stop.
5. Strip disabled and campaign-only titles.
6. Apply AI/PGC one-of-pair (substitute or drop-and-backfill).
7. Stamp device-specific art.
8. Eligible listeners may get one larger-art Home rail (editorial or
   campaign). That is not the device-art stamp.
9. Genre-chip testers who tapped a genre get that stack instead of For You.
   Home does not enroll them.

## User-Visible Invariants

- Shared rails + personal rails + filters. Debugging only shared-rail
  freshness misses most “wrong Home” bugs.
- Launch-only tests are read, not allocated, on this path.

## Failure modes

- Shared-rail store down → Home still builds, just slower / thinner
  editorial.
- Genre-chip error → fall through to normal Home, do not invent a genre
  stack.
