<!-- Search overlay. Merges over global/skills/explain-flow.skill.md -->
# Skill: Explain / debug Pocket Search

Follow `global/skills/explain-flow.skill.md`. This overlay names the Search facts.

## Canonical names (use these, not invented ones)

From `search/knowledge-base/CONTRACT.md` and `features/universal-search/overview.md`:

- v3 entry: `UniversalSearchV3View` → `UniversalSearchV3Handler` + `QueryRouter`
  (`v3/search/views.py`)
- v3 request: `SearchRequestData` (`v3/search/data/request_data.py`)
- v3 `QueryRouter`: empty query → `GenreTropeService`; genre/topic →
  `ShowFilterServiceV3`; else text → `ShowSearchServiceV3` → `ShowSearchService` /
  `lang_biased_results`
- v3 orchestration (`UniversalSearchV3Handler.build_response`):
  1. init services
  2. cache key → read
  3. hit: personalize → DS thumbnails → return
  4. miss: search → filters → **cache unpersonalized** → personalize → DS thumbnails
- Personalize order: AI/PGC → campaign-only → ME exclusion → override → disabled
  shows → DS thumbnails
- Cache key must not include uid/device. Personalization always runs after cache.
- v3 is not standalone. Changing v2 requires a v3 blast-radius check.

## "Reduce universalsearch v3" — cases to walk

Do not assume latency is high. Cover each case and say which are unverified:

1. *What reduce means* — p99 time, payload bytes, ES load, Redis load, or result count?
2. *Live evidence* — quote Sherlock if present. If Sherlock has no signal, write
   `No live latency evidence` and treat the ask as a design review, not an incident.
3. *Cache-hit path* — still personalizes. Reducing retrieval does nothing on a hit.
4. *Cache-miss path* — ES / `ShowSearchService` + filters, then write cache.
5. *Empty vs genre vs text* — `QueryRouter` picks different services.
6. *Key / shape risk* — changing response shape requires a cache-key change (`src_v3:`).
7. *v2 coupling* — `ShowSearchServiceV3` calls `ShowSearchService`.

Candidate levers (only if they appear in the pack): cache TTL/key, skip a personalize
step behind a flag, shrink ES fields, short-circuit empty-query discovery. Each lever
needs a risk line.

## Screenshots / search UI

If the ask is a search-results screenshot or `universal.search` curl:

1. Prefer `architecture/api-to-screen.md` (this pack) and Radioly’s Experience
   map for cross-surface asks.
2. Primary path: `/v2/search/universal.search` (v3: `UniversalSearchV3View`).
3. Never paste JWTs / uids from Confluence example curls.

## Clarify before concluding

If env, path (cache-hit vs miss), or what “reduce” means is still unclear after
Sherlock + pack, ask 1–3 cross-questions. Mark guesses as Assumption. Do not
invent live latency or architecture missing from the pack.

## Slack format

Same as the global skill: `*bold*`, no `**`, no `---`, no markdown tables,
no mermaid/ASCII diagrams. Lead with *Verdict* → *Details* (bullets) →
*Flow* as `A → B → C` or numbered steps if asked → Questions if needed.
Keep it ≤15 short lines. No operator Steps / model / sources unless
`raw_metadata=true`.
