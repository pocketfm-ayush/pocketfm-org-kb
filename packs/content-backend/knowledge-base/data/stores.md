# content-backend stores

| Store | Role |
|---|---|
| MySQL (primary + optional replica) | Show/story/feed module catalog rows via GORM |
| Scylla | Optional; Continue Playing / related state when configured |
| Valkey Redis (`content`, `content-backend`) | Catalog cache + deeplink TTL records |
| In-process memory cache | Short TTL hot-path show cache |

Redis/cache write failures must not fail the request (best-effort).
Scylla is only initialised when hosts are configured.
