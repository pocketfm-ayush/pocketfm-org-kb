# Feed Show Exclusion

## What It Is
Hides over-played shows from feed for experiment/quality reasons after listening thresholds.

## Actors
Playtime consumer; Content exclusion API; feed callers (Radioly).

## Journey
Playtime events → threshold check → user marked → Content excludes show from feed.

## Gaps
Threshold / testing_id ownership is product-sensitive — verify config sources.
