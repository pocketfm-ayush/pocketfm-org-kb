# AI ↔ PGC show selection (feed)

Aliases: AI PGC, AI/PGC, AI<>PGC, PGC show selection, duplicate show, keep AI default

## What It Is

On home feed, library, and show-page rails, Radioly shows **one** title from
an AI / PGC pair. Pairs are CMS-owned. Radioly does not invent pairs.

## Actors

Listener. CS override. Marketing pin (campaign attribution). Ops kill
switch. CMS sets whether a cold user sees AI or PGC.

## Journey

1. A rail contains a show that belongs to a known pair.
2. If routing is killed, the requested ID stays.
3. CS override wins next.
4. About three minutes of play on either side decides the winner; recency
   breaks a tie. Playtime beats a marketing pin.
5. Cold on both sides: campaign can pin live PGC; else default PGC unless
   CMS said keep AI.
6. If the winner is missing from the rail, substitute it (except on
   pre-cut top-N lists, which drop and backfill).

Later, if the listener is sent to the PGC player, unlock progress from the
AI title can be copied so they do not lose episodes.

## User-Visible Invariants

- One pair → one card on a rail.
- Cutting a top-N row *before* this pick leaves holes.
- Search applies the same pair idea on the search list — different surface,
  same product rule.

## Client Behavior

Server decides. The app renders whatever ID comes back.

## Gaps

Which titles are paired is CMS-owned. Do not hardcode show IDs.
