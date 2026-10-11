# Universal search

Aliases: universal search, search v2, search v3, search endpoint, how search works

## What It Is

The single search box on the app. One request: classify empty vs genre vs
typed text, fetch candidates, personalize, return the list.

v2 and v3 both exist. A behavior change usually belongs on both unless the
source says otherwise.

## Actors

Listener (logged-in or guest). App search screen.

## Journey

1. App sends the query and locale.
2. Empty → discovery. Genre/topic filter → curated list. Text → relevance.
3. Shared personalization runs (see [search-request](../flows/search-request.md)).
4. App renders titles, art, and rows.

## User-Visible Invariants

- Empty search is not “no results”; it is genre/trope discovery.
- Personalized swaps must not leak a show the user is not allowed to see.
- v2 and v3 should feel the same unless product has split them.

## Client Behavior

Needs network. A shared unpersonalized payload may be reused, then tailored
per user before display.
