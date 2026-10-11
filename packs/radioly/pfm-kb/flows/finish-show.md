# Finish a show

Participating modules: autoplay-playlist, cross-show-stitch, player-feed.

## Journey

1. Listener finishes (or is about to finish) a title.
2. App asks for next-up. UGC locales may get a curated list. Some
   markets inject one audiobook after the current title.
3. If they are in the stitch test and the title is chained, the
   episode list may end early and show a next-title block — that is
   not the default next-up.
4. Player rails on the next title are a separate ask.

## User-Visible Invariants

- Next-up ≠ player rails ≠ stitch block.
- Empty next-up on an old app is eligibility.

## Failure modes

- Playlist miss → try the single next title; if that is empty, stop.
  Do not play a Home card.
- Stitch block miss → omit the block; do not invent a next title.
