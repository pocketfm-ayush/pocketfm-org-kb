# Search response cache

Aliases: search cache, cache hit, cache miss, redis search

## What It Is

A shared, **unpersonalized** search payload is reused across users. After a
hit, the server still applies this user’s AI/PGC, campaign, exclusions, and
art before returning.

## User-Visible Invariants

- Two users must not see each other’s personalized list from the shared
  payload.
- If the result *shape* changes (new field, different row type), the shared
  payload must be treated as a new thing — stale shape is a user-visible bug.
- If the shared store is down, search should still return usable results.

## Client Behavior

Feels instant on a hit; still needs network. Freshness is server-side.
