# Content scheduled jobs

Aliases: content dags, feed popularity jobs, content temporal

## What It Is
Umbrella for content/feed freshness: rankings, autoplay caches, daily-show,
catalogs, tropes, throttling, search-adjacent indices, and related Temporal
content schedules.

## Prefer specific twins when debugging
- [daily-show-rotation](daily-show-rotation.md)
- [catalog-sync-jobs](catalog-sync-jobs.md)
- [key-tropes-jobs](key-tropes-jobs.md)
- [content-throttling-jobs](content-throttling-jobs.md)
- [search-index-jobs](search-index-jobs.md)
- [ppv-validation-pipeline](ppv-validation-pipeline.md)
- [temporal-content-worker](temporal-content-worker.md)

## User-Visible Invariants
- Failure → stale discovery/rank more often than a hard error screen.
