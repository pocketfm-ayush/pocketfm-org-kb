# Pocket Pick

Aliases: pocket pick, playables, playable swipe

## What It Is

A swipe deck of playable title cards (about six), auto-advancing
every 30 seconds. Not Discover, not Home.

## Actors

Listener in the Pocket Pick test. Android; India / US; English or
Hindi.

## Journey

1. Client nudges (same family as Discover): pause autoplay, Home
   module, player scroll past next-series, Library “discover more,”
   module expand, search tap.
2. Extra nudge: campaign primary title under a listen threshold,
   mid-age device — once.
3. At most one deck per local day.
4. Server picks titles, drops already-shown and a hard exclude list.
5. A later variant opens the playables player on tap.

## User-Visible Invariants

- Empty deck is allowed; do not invent cards.
- Do not send “I am on journey X” — triggers are server-filtered.

## Client Behavior

Needs network. Daily count resets at local midnight.

## Gaps

Which pick variant is live, and the exclude-list rationale, are not
recorded here.
