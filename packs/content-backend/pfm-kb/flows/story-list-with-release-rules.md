# Story list with release rules

## Journey
1. Caller requests stories for a show.
2. Approved stories load from catalog.
3. FastPass, branching, and stitching experiment rules may hide, cut, or renumber.
4. Client receives the listener-visible episode list.

## Modules
- [story-catalog-read](../modules/story-catalog-read.md)
- [fastpass-story-release](../modules/fastpass-story-release.md)
- [branching-stories](../modules/branching-stories.md)
- [stitching-ux](../modules/stitching-ux.md)

## Failure modes
- Listener expects CMS full list but sees compacted FastPass/branching list.
- Experiment variant changes episode count without CMS edit.
