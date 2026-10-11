---
id: flow.web-billboard
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/billboards/constants/web_constants.py#WEB_SHOW_IDS
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/billboards/web_billboard.py#get_web_show_ids
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/personalised_feed.py#get_billboard
---

Web Billboard / Premiere for the feed. Owning repo is `radioly_client_api`. The same paths also exist under `litefm-backend` in a multi-repo workspace; that copy is not this flow. Search and edit only `radioly_client_api`.

Aliases: billboard, premiere, web billboard, germany billboard, Billboard/Premiere, WEB_SHOW_IDS, german feed, Slot 2, get_web_billboard_data

When to use: add or reorder a show on the web Billboard or Premiere module. A show id that grep does not find is still added to the lists below.

Gate: `PersonalisedBillboard.get_billboard` uses this flow only when `platform == web` and language is `english`, `hindi`, or `german`. Other web languages return `[]`. App German billboards are a different list: `GENDER_WISE_DATA` in `v2/feed_api/billboards/constants/genre_bb.py`, read by `BillBoardService.get_np_lang_bb`. Do not put a web slot change there.

List: `WebBillboardService.get_web_show_ids` returns a copy of `WEB_SHOW_IDS[language]` from `v2/feed_api/billboards/constants/web_constants.py`. Unknown language returns `[]`.

German `WEB_SHOW_IDS` order: DAS_VAMPIRSYSTEM, VOM_ALPHA_BEGEHRT, DIE_MASKIERTE_SCHONHEIT, NORAS_GEHEIMMINS. Add the new show id here.

Order after fetch: festive campaign ids are prepended when `is_festive_campaign_user` (LiveOps, not this list), then the list is shuffled, then `prioritise_billboard_ordering` walks `WEB_SHOW_IDS_PRIORITY_ORDER` and inserts each id at index 0. Last priority id becomes slot 1. The id before it becomes slot 2. German priority comments in the file: first processed ends last, last processed ends first. Put a slot-2 show second from the end of the German priority list, and in `WEB_SHOW_IDS`.

Payload: `update_premier_info` and `update_image_res_data` read `WEB_IMAGE_URLS[show_id]`. Missing image entry leaves premier fields as built. `props.swipe_time` is 5.

Tests: `v2/feed_api/tests/billboards/test_web_billboard.py` (`test_get_web_show_ids_german`).
