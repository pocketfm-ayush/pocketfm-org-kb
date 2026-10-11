# DS Thumbnails

Aliases: DS thumbnail, device thumbnail, search artwork

Product context: `search/pfm-kb/modules/ds-thumbnails.md`

## What it is
Device-specific (DS) show thumbnail overrides: one Scylla read → map of show_id → media_id,
then stamp result rows in place. Also covers iOS new-design thumbnail updates.

## Graph anchors
| Symbol | Source | Community | Degree |
|---|---|---|---|
| `ShowThumbnailService` | `v2/search/services/show_thumbnail.py` L38 | 5 | 10 |
| `get_device_thumbnail_map()` | same file L16 | 5 | — |
| `ShowThumbnailMapping` | `v2/search/models_new/show_thumbnail.py` L6 | 5 | — |
| `DSShowThumbnailRepository` | `v2/search/repositories/ds_show_thumbnail_repository.py` L36 | 40 | — |

## Key edges
- Service → repository + mapping model [INFERRED]
- Imported by v2 and v3 views [EXTRACTED]
- `get_media_url()` via `media_service.py` (Community 5)

## Tests
- `v2/search/tests/test_ds_show_thumbnail_service.py`
- `v3/search/tests/test_v3_ds_thumbnail.py`
- UX BDD scenarios around image update/unchanged

## Risks
- Graph notes a TODO: unoptimized one-by-one method calls in `show_thumbnail.py`.
- Must use already-fetched device map when stamping — avoid N+1 Scylla reads in the hot path.

## Query
```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify explain "ShowThumbnailService" --graph $GRAPH
```
