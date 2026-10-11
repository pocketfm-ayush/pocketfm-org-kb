# Show thumbnail mapping

Aliases: shows_thumbnail_mapping, show_thumbnail_mapping, ShowThumbnailMapping, thumbnail props

Product context: `radioly/pfm-kb/modules/show-thumbnail-mapping.md`

**Repo:** `radioly_client_api`  
**ORM:** `v2/content_api/models_new/show_thumbnail_map.py` → `ShowThumbnailMapping`  
**MySQL table:** `shows_thumbnail_mapping` (`Meta.db_table`, `managed = False`)

## Columns / props

| Field | Type | Notes |
|---|---|---|
| `show_id` | CharField(60), unique | Show key |
| `thumbnail_url` | CharField(255), null | Primary thumbnail |
| `mid_res_image_url` | CharField(255) | Mid-res image |
| `low_res_image_url` | CharField(255) | Low-res / web |
| `props` | JSONField, null | CMS aspect-ratio thumbnails |
| `update_time` | DateTimeField | `auto_now` |
| `create_time` | DateTimeField | `auto_now_add` |

### `props` shape (CMS)

```json
{
  "aspect_ratio_thumbnails": {
    "1:1":  {"upload_id": "...", "media_id": "..."},
    "2:3":  {"upload_id": "...", "media_id": "..."},
    "16:9": {"upload_id": "...", "media_id": "..."},
    "2:1":  {"upload_id": "...", "media_id": "..."}
  }
}
```

Helpers normalize to `{aspect_ratio: media_id}` via
`ShowThumbnailMapping._normalise_aspect_ratio_props` /
`get_aspect_ratio_props_for_shows` (FMF-2437 batch IN-query).

## Call sites

- `get_show_thumbnail(show_id)` — cached `thumbnail_url`
- `get_les_res_show_thumbnail(show_id)` — cached `low_res_image_url`
- Feed / experience thumbnail config services consume normalized props

## Notes

- Not an Argus warehouse-only fact — live definition is the Radioly ORM model.
- Argus `fm_product_analytics` may lack this bronze/RDS table; prefer CODE SEARCH.

## Graph anchors

See overview body + `data/tables.md` for `shows_thumbnail_mapping`.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "show thumbnail mapping" --graph $GRAPH
```
