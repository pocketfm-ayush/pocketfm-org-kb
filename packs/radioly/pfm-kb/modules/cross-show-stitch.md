# Cross-show stitch

Aliases: stitching UX, cross details, cross show, show chain, bridge promo

## What It Is

A **test-only** handoff: a few titles are chained. Testers can see a
next-title block at the end of the episode list, and sometimes hear a
short bridge before the next title’s first episode.

This is not general autoplay and not Home recommendations.

## Actors

Listener already in the test, on a title in the chain. CMS/editorial
does not invent the chain in the app.

## Journey

1. Listener is on a chained title.
2. One test: episode list can be cut at a fixed end; a next-title id
   is set so the app can load the end-of-list block.
3. App asks for that block only when the id is present and they have
   scrolled to the end.
4. Another test: a promo / bridge can play when handing off to the
   next title.

## User-Visible Invariants

- No chain id → no stitch block. Do not pick a “similar” title.
- Autoplay’s next-up is a different path. Do not assume stitch is
  everyone’s next play.
- The end-of-list block is not the bigger-art Home rail, even if the
  same title is promoted there for testers.

## Client Behavior

Needs network. If the block fails, omit it — do not invent a next title.

## Gaps

Which titles are chained and which test is live are not recorded here.
