# Shared with Search (cross-product)

Participating packs: `radioly`, `search`.

## Ordered journey (product)

1. CMS maintains shared pair / campaign / thumbnail meaning.
2. Radioly applies rules on feed, library, show-feed, and related surfaces
   (`ai-pgc-show-selection`, visibility filters, device cover art).
3. Search applies parallel rules on universal search personalization
   (`ai-pgc-replacement`, `campaign-only-shows`, `ds-thumbnails`).
4. Listener sees one consistent title choice per surface family — but
   handlers differ by service. Never name Search symbols for a Radioly ask.

## Modules

- Radioly: `modules/ai-pgc-show-selection.md`, `modules/visibility-filters.md`,
  `modules/device-cover-art.md`
- Search: `../search/pfm-kb/modules/ai-pgc-replacement.md`,
  `campaign-only-shows.md`, `ds-thumbnails.md`
- Code twins: `radioly/.../ai-pgc-show-selection`, `show-thumbnail-mapping`;
  `search/.../ai-pgc-replacement`, `ds-thumbnails`, `campaign-only-shows`

## User-visible invariants

- Pair map meaning is shared; service code is not.
- Cache in Search stores unpersonalized payloads; Radioly home shared rails
  are not a per-uid Search cache.

## Failure modes

- Answering with the wrong pack's handlers.
- Assuming Argus warehouse tables document app MySQL pair maps.
