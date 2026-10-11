# Content ranking freshness

## Journey
1. Schedule fires for popularity / autoplay / related content jobs.
2. Worker computes ranks or caches.
3. Home/feed/player APIs read fresher rankings.
4. On failure, ops get Slack-style alerts; users see staleness, not usually a crash.

## Modules
- [content-scheduled-jobs](../modules/content-scheduled-jobs.md)
- [scheduled-jobs](../modules/scheduled-jobs.md)
- [temporal-domain-workers](../modules/temporal-domain-workers.md)
