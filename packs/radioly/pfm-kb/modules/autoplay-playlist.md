# Autoplay playlist

Aliases: playlist, next recommended show, autoplay queue, next up

## What It Is

What plays **after** the current title: an ordered next-up list. This is
not Home and not the player rails.

“Next recommended show” is the same product when the full list is empty.

## Actors

Listener. Some markets inject one audiobook after the current title.

## Journey

1. Current title is playing or just finished.
2. App asks for the next-up list (or a single next title).
3. Some UGC locales get a curated list instead of the usual ranking.
4. Eligible markets may insert one audiobook right after the current
   title. If that title is missing from the list, the audiobook goes first.
5. Old or restricted apps get nothing.

## User-Visible Invariants

- Next-up is not a Home rail and not the player-page stack.
- A stitch / promo title in a test is not the default next-up for everyone.
- Empty next-up on an old app is eligibility, not a catalog outage.

## Client Behavior

Needs network. The app should play the server’s order, not rebuild it
from Home.

## Gaps

Which markets inject an audiobook, and live autoplay ranking, are not
recorded here.
