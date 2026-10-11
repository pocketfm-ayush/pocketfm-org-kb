# Key tropes

Aliases: tropes, themes, Discover Stories by Theme, explore themes

## What It Is

A Home rail of story **themes**, plus a theme page of titles. Not
Discover shorts.

## Actors

Listener in the tropes test (India / US; English or Hindi).

## Journey

1. Home may include a themes rail (capped).
2. Tap a theme → theme page (capped titles).
3. English/Hindi: themes the device has seen enough rotate out so the
   rail refreshes.
4. Same one-of-pair and campaign-only hide rules as Home.
5. On the player, a theme card prefers an active Discover short as
   the promo; if none, the usual trailer.

## User-Visible Invariants

- A disabled / hidden / losing-pair title must not stay on a theme.
- Other languages skip rotation (impressions are not counted there).
- Killing personalization must not blank the rail — fall back to the
  editorial order.

## Client Behavior

Needs network. Theme-not-found is a visible miss, not an empty Home.

## Gaps

Which theme test is live, and exact rail placement, are not
recorded here.
