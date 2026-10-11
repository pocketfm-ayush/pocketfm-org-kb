# content-backend pack coverage

**As of:** 2026-09-07 · **Ticket:** FMF-4712

## Source reality
- ~170 Go files (~101 non-test)
- App domains: show, stories, continueplaying, feed/defaulthome, feed audiobook,
  showdetailsfallback, appsflyergcd
- Domain features: fastpass, branching, paidnormalization, platformrestriction,
  designrevamp, dsthumbnail, resolutionasset, englishdescdrop
- Experiments: stitchingux, showmeta, androiddesignrevamp, mediareplacement
- Infra helpers: cache, cachewarmup, media apollo resolver, private API auth

## Pack counts
| Layer | Count |
|---|---|
| Feature overviews | 19 |
| pfm-kb modules | 19 |
| pfm-kb flows | 5 |

## Folder map (product twin status)

| Source area | Status | Twin(s) |
|---|---|---|
| `internal/app/show` | covered | show-catalog-read, story-catalog-read, content-catalog |
| `internal/app/showdetailsfallback` | covered | show-details-fallback |
| `internal/app/continueplaying` | covered | home-continue-playing-slices |
| `internal/app/feed` + `defaulthome` | covered | audiobook-feed, default-home-feed |
| `internal/app/appsflyergcd` | covered | attribution-deeplink-storage |
| `internal/domain/features/*` | covered | fastpass, branching, paid, geo, images, english |
| `internal/domain/experiments/*` | covered | stitching-ux, show-meta-experiment, android-design-revamp, show-image-variants |
| `internal/cache` + `cachewarmup` | covered | catalog-cache |
| `internal/bootstrap/apiserver` private routes | covered | private-catalog-api |
| `internal/media` | covered via images | show-image-variants |
| `internal/repository` | covered via features | show/story/fallback repos |
| `internal/mysql|redis|metrics|config|errs` | intentional thin | infra |
| `tests/`, `migrations/`, `infra/` | intentional SKIP | harness/deploy |

## Intentional SKIP
- Per-DTO / mock / sqlmock helpers
- Live experiment allocation % and CMS feed payloads
- Full Radioly↔content-backend cutover matrix (still a gap)

## Honest gaps
- Product family coverage ≠ one overview per `.go` file
- Always verify whether a listener journey still hits Radioly first
