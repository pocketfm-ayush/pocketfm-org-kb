# Query processing

Aliases: query normalize, strip language, clean query, title cleanup

## What It Is

Cleans the typed query and some English titles (unsafe characters, language
tags, parenthesised language suffixes) before ranking and display.

## User-Visible Invariants

- Language tags in the query should not leak into what the user meant.
- English titles may drop a language suffix in the result row. That is
  intentional, not a missing title.

## Client Behavior

Happens on the server. Same cleanup is used for typed search and some
filter/formatted titles.
