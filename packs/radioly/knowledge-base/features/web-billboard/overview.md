# Web billboard

Aliases: billboard, premiere, web billboard, germany billboard, WEB_SHOW_IDS, Billboard/Premiere

Owning repo: `radioly_client_api` only. `litefm-backend` under `/workspace` is another checkout of the same tree. Do not search or edit it when this repo is linked.

## When it runs

`PersonalisedBillboard.get_billboard` in `v2/feed_api/personalised_feed.py`.

Web platform (`platform == web`) and language `english`, `hindi`, or `german` calls `get_web_billboard_data`. Any other language on web returns an empty list. App platforms do not use this list; German app billboards use `GENDER_WISE_DATA` in `genre_bb.py` via `BillBoardService.get_np_lang_bb`.

## Show list

`WebBillboardService.get_web_show_ids(language)` copies `WEB_SHOW_IDS[language]` from `v2/feed_api/billboards/constants/web_constants.py`. Missing language returns `[]`.

German entries today, in list order:

`DAS_VAMPIRSYSTEM`, `VOM_ALPHA_BEGEHRT`, `DIE_MASKIERTE_SCHONHEIT`, `NORAS_GEHEIMMINS`.

A new show id is added there even when a grep for that id finds nothing.

## Order on the feed

`get_web_billboard_data`:

1. Optional festive campaign shows are prepended from `exp_data["festive_campaign_obj"].get_billboards()` when `is_festive_campaign_user` is set. That is LiveOps, not this list.
2. The ids are shuffled (`secrets.SystemRandom`).
3. `prioritise_billboard_ordering` walks `WEB_SHOW_IDS_PRIORITY_ORDER[language]` and moves each id to index 0. The last id in the priority list becomes slot 1. The one before it becomes slot 2.

German priority list, and the comment in the file: first id is processed first and ends last; last id is processed last and ends first. To put a show in slot 2, place it second from the end of `WEB_SHOW_IDS_PRIORITY_ORDER[Language.German.value]` and keep it in `WEB_SHOW_IDS[Language.German.value]`.

## Images and payload

For each show, `get_billboard_layout` runs, then:

- `update_premier_info` sets `value.premier_info.premier_image_url` and `icon_url` from `WEB_IMAGE_URLS[show_id][high]`. No `WEB_IMAGE_URLS` entry leaves the billboard data unchanged.
- `update_image_res_data` writes the same dict into `value.premier_info.image_res`.
- `props.swipe_time` is `5` (not the default billboard swipe time).

## Do not edit for a Germany web slot

- `genre_bb.GENDER_WISE_DATA` — app German gender lists. It already repeats the four web ids plus `30ff1be80fa234b3a04781026239809a571c6701`.
- `PORTUGUESE_BILLBOARD_SHOW_IDS` and `SPANISH_BILLBOARD_*` in the same file.
- `billboard_helper.get_np_lang_bb` — non-personalised app languages (German, Spanish, Portuguese).
- LiveOps tentpole, which runs on non-web platforms before other app billboards.
- The same paths under `litefm-backend` or any other `/workspace` checkout.

## Tests

`v2/feed_api/tests/billboards/test_web_billboard.py` (`test_get_web_show_ids_german` expects `WEB_SHOW_IDS["german"]`).
