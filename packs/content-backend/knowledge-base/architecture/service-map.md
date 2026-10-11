# content-backend — service map

| Surface | Role | Product twins |
|---|---|---|
| `/internal/show*` + `/internal/stories/query` | Private show/story catalog | show-catalog-read, story-catalog-read, private-catalog-api, catalog-cache |
| `/internal/show_details_fallback/*` | Legacy show details | show-details-fallback |
| `/internal/continue-playing/shows` | CP candidates | home-continue-playing-slices |
| `/internal/feed/default-home/shows` | Onboarding/default home | default-home-feed |
| `/internal/appsflyer-gcd-deeplinks/*` | GCD deeplink CRUD | attribution-deeplink-storage |
| `/v2/feed_api/get_feed_data` | Audiobook feed modules | audiobook-feed |
| Domain features/experiments | Response shaping | fastpass, branching, stitching, images, paid, geo |

Radioly remains the consumer BFF for many journeys — confirm cutover per route.
