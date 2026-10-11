# Catalog read for show page

## Journey
1. BFF/Radioly (or trusted internal caller) requests show metadata and stories.
2. Private catalog auth accepts the caller role.
3. Show and story services load catalog rows (cache-aside).
4. Domain features reshape stories/images/paid flags as needed.
5. Caller assembles the listener-facing show page.

## Modules
- [private-catalog-api](../modules/private-catalog-api.md)
- [show-catalog-read](../modules/show-catalog-read.md)
- [story-catalog-read](../modules/story-catalog-read.md)
- [catalog-cache](../modules/catalog-cache.md)
- [show-image-variants](../modules/show-image-variants.md)

## Failure modes
- Cache staleness briefly shows old CMS edits.
- Domain rules hide episodes the CMS still lists as approved.
- Fallback route may be used if primary shape is insufficient.
