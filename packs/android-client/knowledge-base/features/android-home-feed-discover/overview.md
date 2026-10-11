# Home Feed

Aliases: home tabs, feed explore modules

Product context: `android-client/pfm-kb/modules/home-feed-discover.md`

## What it is
Home bottom-nav host plus Explore/content feed modules that render server-driven widgets and CTAs.

## Graph anchors
| `home navigation` | `aural/home/` |
| `feed ui` | `aural/feed/ui` |
| `FeedWidgetTitleAndSubtitle` | `aural/feed/ui/common/...` |

## Risks
- Hardcoding Compose colors instead of AuralColor/AuralTypography tokens.
- Treating feed as the only discovery surface — Discover module is separate.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Home Feed" --graph $GRAPH
```
