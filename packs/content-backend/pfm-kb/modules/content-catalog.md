# Content Catalog

## What It Is
Catalog read platform for Pocket FM shows and stories, with supporting feed and attribution helpers.

## Actors
Radioly and other internal callers; CMS/experience roles; listeners via BFF.

## Journey
Caller asks for show/story/feed slices → service applies personalization rules → cached catalog response.

## Product Source Of Truth
Catalog rows live in content stores; Radioly may still own many consumer journeys.

## Gaps
Endpoint cutover vs Radioly is incomplete — verify routes before migration claims.
