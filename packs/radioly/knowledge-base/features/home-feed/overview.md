# Home feed

Aliases: home feed, get feed, For You, homepage, get_feed_data

Product context: `radioly/pfm-kb/modules/home-feed.md` · flow `radioly/pfm-kb/flows/open-home.md`

## What it is
`/v2/feed_api/get_feed_data` and `/v3/feed_api/get_feed_data` both call
`v3.feed_api.views.get_feed_data`. Leftover `v2.feed_api.views.get_feed_data`
is not routed. Assembles personalized + editorial rails, then visibility filters.

## Graph anchors
| Symbol | Source |
|---|---|
| `get_feed_data` | `v3/feed_api/views.py` |
| `UserContextBuilder` | `v3/feed_api/services/user_context_builder.py` |
| `FeedModuleFetcher` | `v3/feed_api/services/feed_module_fetcher.py` |
| LiveOps inject | `LiveOpsTentpoleCampaignService` via feed experiment wiring |
| Start Writer module | `StartWriterModule` / start_writing home module |

## Key edges
- Genre chip: only already-enrolled testers; do not allocate launch-only exps here.
- Some locales short-circuit to UGC-row stack (tentpole service nulled there).
- After assemble: disabled/hidden filters, AI↔PGC, DS thumbnails.
- LiveOps may append billboard/module/banner; Start Writer CTA → write/Studio.

## Risks
- Treating v2 vs v3 home as two products.
- Enrolling launch-only experiments on the feed path.
- Missing LiveOps vs festive campaign distinction.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "get_feed_data" --graph $GRAPH
```
