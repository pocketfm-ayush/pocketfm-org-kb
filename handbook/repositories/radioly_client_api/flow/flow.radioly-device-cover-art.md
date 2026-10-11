---
id: flow.radioly-device-cover-art
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/content/ds_show_thumbnail/service.py#get_device_thumbnail_map
---

**Aliases:** device cover art, DS art, device thumbnail, ds_show_thumbnail

**When to use:** A per-device stamp that can replace catalog cover art after rails are built. First stop `get_device_thumbnail_map`. Not CMS `shows_thumbnail_mapping` and not the large Home rail art.

**Required inputs:** device id and show id whose art looks wrong.
