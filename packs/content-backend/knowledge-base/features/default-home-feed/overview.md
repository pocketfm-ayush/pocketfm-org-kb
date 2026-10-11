# Default Home Feed Shows

Aliases: default-home/shows, onb_feed_v2

Product context: `content-backend/pfm-kb/modules/default-home-feed.md`

## What it is
Internal API returning ranked default/onboarding home show lists keyed by platform, locale, language, and gender.

## Graph anchors
| `NewService()` | `internal/app/feed/defaulthome/service.go` |
| `GetDefaultHomeShows` | `internal/app/feed/defaulthome/controller.go` |

## Risks
- Omitting required audience headers and inventing defaults.
- Confusing this with full personalized home feed in Radioly.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "NewService()" --graph $GRAPH
```
