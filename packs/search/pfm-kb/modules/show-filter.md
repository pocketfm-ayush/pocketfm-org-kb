# Show filter

Aliases: genre filter, curated search, filter search, search with filter

## What It Is

Search when the request carries a filter/genre context rather than only
free text. Titles still go through query cleanup.

## User-Visible Invariants

- Filter + locale can change which rows appear.
- A filter bug often looks like “search is broken” even when typed search
  is fine.
