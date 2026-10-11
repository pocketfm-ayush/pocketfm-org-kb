# Language-biased search

Aliases: text search, relevance, fuzzy search, language pool, ES search

## What It Is

Typed-query relevance. Results prefer the listener’s language pools, then
fuzzy/prefix fallbacks if the exact match is thin.

## User-Visible Invariants

- Locale decides which language pool is tried first.
- Weak exact matches can still surface via fuzzy/prefix.
- v3 typed search uses the same relevance brain as v2.

## Client Behavior

Needs network. Ranking is server-side.

## Gaps

Stable “how much” boost per language is not recorded here — do not invent weights.
