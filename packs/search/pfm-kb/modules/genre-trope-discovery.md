# Genre and trope discovery

Aliases: empty search, empty query, genre discovery, trope, browse search

## What It Is

What the user sees when search is opened with no text (or with a genre/topic
context): curated genres and tropes, not a blank relevance list.

## User-Visible Invariants

- Empty query must not look like a failed search.
- Genre artwork can differ by platform.
- If the genre source is down, the empty-search experience degrades — do not
  invent a fallback catalog.

## Client Behavior

Fetched from the server. Maps of genre/trope → shows are product/CMS-owned
and can drift; treat mismatches as a content gap.
