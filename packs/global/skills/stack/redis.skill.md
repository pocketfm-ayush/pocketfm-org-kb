---
name: redis
description: Redis caching, locks, TTLs, and failure modes.
triggers: [redis, cache, ttl, redis lock]
intent: implement
priority: 70
---

# Redis

## Do
- Key naming conventions; TTL on every cache key unless justified.
- Treat cache as disposable — DB remains source of truth unless designed otherwise.
- Locks: expiry + safe release; avoid deadlocks.
- Watch payload size and hot-key concentration.

## Do not
- Cache authorized-sensitive data without tenancy in the key.
- Infinite TTL “temporary” keys.

## Related
`database-sql`, `performance-review`, `security-review`, `docker`, `kubernetes` as applicable.
