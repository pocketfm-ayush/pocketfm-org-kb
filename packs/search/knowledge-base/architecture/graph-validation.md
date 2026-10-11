# Validating the Search graph and knowledge base

The graph plus `knowledge-base/` are the shared source of truth for every skill. Treat them
like production data: verify before trusting, re-verify when the Search repo moves.

## What "correct" means

| Artifact | Correct means |
|---|---|
| Graph (`graph.json`) | Covers the Search code that matters, known flows resolve, and INFERRED edges that skills will act on are human-checked |
| Knowledge (`knowledge-base/`) | Feature folders, PRDs, architecture notes, and KT notes match owners; no stale or contradictory docs |

AST `EXTRACTED` edges are mostly trustworthy. `INFERRED` edges are the risk — they are
resolved by graphify, not read literally from the source.

## Level 1 — Mechanical (do every rebuild)

```bash
# From content-knowledge-base
GRAPH=search/graphify/graphify-out/graph.json

# 1. Freshness: graph commit must match pocket_search HEAD
grep "Built from commit" search/graphify/graphify-out/GRAPH_REPORT.md
git -C /Users/ayushgarg/Desktop/Work/Repo/pocket_search rev-parse --short HEAD

# 2. Scale sanity (expect ~3k nodes, ~6k edges for full pocket_search code-only)
#    Check Summary in GRAPH_REPORT.md

# 3. No import cycles (should stay "None detected")
grep -A2 "## Import Cycles" search/graphify/graphify-out/GRAPH_REPORT.md
```

If HEAD ≠ graph commit → rebuild before any skill work:

```bash
graphify extract /Users/ayushgarg/Desktop/Work/Repo/pocket_search --code-only --out search/graphify
graphify cluster-only search/graphify --no-label
```

## Level 2 — Golden paths (architecture quiz)

These must always resolve. If a path fails or looks wrong, the graph is not ready.

```bash
GRAPH=search/graphify/graphify-out/graph.json

# Request path
graphify path "UniversalSearchV3Handler" "ShowSearchServiceV3" --graph $GRAPH
graphify path "ShowSearchServiceV3" "ShowSearchService" --graph $GRAPH

# Cross-cutting hubs
graphify explain "RedisUtils" --graph $GRAPH
graphify explain "APIUserData" --graph $GRAPH
graphify explain "ShowSearchService" --graph $GRAPH
graphify explain "UniversalSearchV3Handler" --graph $GRAPH

# One product-shaped question
graphify query "how does empty query genre discovery work?" --graph $GRAPH --budget 4000
```

**Pass criteria:** each path exists; explain returns the expected source file; query surfaces
`GenreTropeService` / empty-query related nodes (not unrelated hubs only).

Open `search/graphify/graphify-out/graph.html` and visually confirm the same hubs cluster
near search views/services.

## Level 3 — INFERRED edge audit (highest value)

`GRAPH_REPORT.md` Suggested Questions already lists the edges to verify. For each:

1. Open the cited source file at the cited line.
2. Confirm the use is real (import, call, attribute access) or false.
3. Record the verdict below.

| Edge | Type | Verdict | Checked by | Date |
|---|---|---|---|---|
| `ShowSearchServiceV3` → `ShowSearchService` | INFERRED | | | |
| `ShowSearchServiceV3` → `APIUserData` | INFERRED | | | |
| `UniversalSearchV3Handler` → `APIUserData` | INFERRED | | | |
| `UniversalSearchV3Handler` → `ShowSearchServiceV3` | INFERRED | | | |
| Top 5 `RedisUtils` INFERRED edges | INFERRED | | | |
| Top INFERRED edges on `ShowSearchService` | INFERRED | | | |

Also review **Knowledge Gaps** (isolated nodes). Either document them under
`knowledge-base/architecture/` or note why they are out of scope (admin apps, dead code, etc.).

## Level 4 — Knowledge base review

| Location | Check |
|---|---|
| `knowledge-base/features/<feature>/` | One folder per feature; docs match current behavior |
| `knowledge-base/prds/` | Active cross-cutting PRDs only; superseded docs marked or removed |
| `knowledge-base/architecture/` | Flows and decisions match current code (spot-check via graph) |
| `knowledge-base/notes/` | KT / edge cases still true; dated where useful |

**Rule:** if `knowledge-base/` and the graph disagree, believe the code, fix the doc, then
rebuild the graph if the code was wrong in the graph.

## Level 5 — Skill smoke test (end-to-end)

Pick one small, already-shipped Search ticket (or a fake PRD for an existing feature) and run
`search/skills/prd-analysis.skill.md` only.

**Pass criteria:**
- Every "touch point" cites a real graph node + source location
- Blast radius includes at least one INFERRED caller a grep would miss
- No invented modules
- Open questions are real gaps, not hallucinations

If the analysis invents symbols or misses the v2/v3 coupling, fix `knowledge-base/`, skills,
or graph and rebuild — do not proceed to `implementation.skill.md`.

## Ownership and cadence

| When | Who | What |
|---|---|---|
| After every `pocket_search` merge that touches search | Eng | Level 1 + update graph |
| Weekly while standing up the pack | Eng + 1 Search owner | Level 2 + sample of Level 3 |
| Before declaring the pack production-ready | Eng + product | Levels 3–5; product reviews `knowledge-base/` |
| When a skill produces a wrong claim | Anyone | File a note under `knowledge-base/notes/` or the feature folder, fix graph or docs |

## Sign-off

- [ ] Level 1 pass (fresh vs HEAD)
- [ ] Level 2 golden paths pass
- [ ] Level 3 audit table filled for critical INFERRED edges
- [ ] Level 4 knowledge base reviewed
- [ ] Level 5 prd-analysis smoke test pass

Signed: ________________  Date: ________
