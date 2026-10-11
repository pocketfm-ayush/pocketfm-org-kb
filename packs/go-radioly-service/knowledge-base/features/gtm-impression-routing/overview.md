# GTM Impression Routing

Aliases: KT impression, player feed sampling, show promotion login/splash

Product context: `go-radioly-service/pfm-kb/modules/gtm-impression-routing.md`

## What it is
Router handlers that match selected impression surfaces and republish as GTM device/user impression events for downstream measurement.

## Graph anchors
| `KTImpressionHandler` | `internal/eventrouter/handlers/kt_impression.go` |
| `PlayerFeedSamplingImpressionHandler` | `internal/eventrouter/handlers/player_feed_sampling_impression.go` |
| `ShowPromotionLoginImpressionHandler` | `internal/eventrouter/handlers/show_promotion_login_impression.go` |
| `ShowPromotionSplashImpressionHandler` | `internal/eventrouter/handlers/show_promotion_splash_impression.go` |

## Risks
- Mutating caller headers unexpectedly — Build must not corrupt original event headers.
- Expanding Match rules without product sign-off (English/home tile/vertical list eligibility).

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "KTImpressionHandler" --graph $GRAPH
```
