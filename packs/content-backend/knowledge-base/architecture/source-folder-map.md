# content-backend source folder map

| Folder | Product meaning |
|---|---|
| `internal/app/show` | Show + story catalog HTTP/application services |
| `internal/app/showdetailsfallback` | Legacy-compatible show details |
| `internal/app/continueplaying` | Continue Playing candidate ranking |
| `internal/app/feed` | Audiobook feed modules + default home |
| `internal/app/appsflyergcd` | AppsFlyer GCD deeplink cache APIs |
| `internal/domain/shows|stories` | Core catalog domain models/services |
| `internal/domain/features` | Response-shaping product rules |
| `internal/domain/experiments` | Experiment gates on catalog presentation |
| `internal/cache` + `cachewarmup` | Catalog performance cache |
| `internal/bootstrap/apiserver` | Routes, auth middleware, health |
| `internal/repository` | MySQL/Scylla access adapters |
| `internal/media` | Apollo/media URL resolution |

Query graph before inventing new packages.
