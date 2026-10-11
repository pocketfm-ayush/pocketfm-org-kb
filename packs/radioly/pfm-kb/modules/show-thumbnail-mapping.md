# Show thumbnail mapping

Aliases: thumbnail mapping, DS art map, aspect ratio thumbnails

## What It Is
Catalog of alternate show art (including aspect-ratio variants) so feeds and
experience surfaces can pick the right thumbnail shape for a layout — not a
listener settings screen.

## Actors
CMS/ops uploading art. Feed/experience surfaces. Listener (sees the art).

## Journey
1. Show art variants are stored for a show.
2. A surface requests the appropriate ratio / resolution.
3. Listener sees layout-correct artwork (home large tiles, topic rows, etc.).

## User-Visible Invariants
- Missing mapping falls back to default show art — layouts should not crash.
- Related: [device-cover-art](device-cover-art.md), [bigger-thumbnails](bigger-thumbnails.md).

## Gaps
- Which surface prefers which ratio is layout-specific — confirm in the calling feature.
