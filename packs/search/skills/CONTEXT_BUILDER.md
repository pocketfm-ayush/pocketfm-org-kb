# Shared Context Builder

Every stage must build context in this order. Do not dump the whole repository or graph into
the prompt. Collect only evidence relevant to the PRD, eval, failure, or diff.

## Sources and precedence

When sources disagree:

1. Approved PRD plus recorded product answers define intended behavior.
2. `search/knowledge-base/contract.json` defines enforceable paths, commands, and limits.
3. `search/knowledge-base/CONTRACT.md` defines architecture, conventions, and current public contract.
4. Current source and tests define implemented behavior.
5. `search/knowledge-base/` explains feature intent and prior decisions.
6. `search/knowledge-base/notes/solutions/` is institutional memory: prior root causes,
   what did not work, and reusable patterns. Read it early to avoid re-deriving a known
   answer, but it never overrides current source — a learning can be stale.
7. Graphify supplies discovery and dependency evidence; verify uncertain or INFERRED edges
   against source before using them as facts.

Do not silently resolve a conflict. Record it and stop when it changes product behavior,
public API, data semantics, rollout, compatibility, or safety.

## Grounding rule

Every claim you carry forward must be traceable to evidence, not to a summary of a summary:

- Before asserting how code behaves, read the defining line — do not trust a symbol name,
  a doc sentence, or an earlier turn's paraphrase.
- Cite durable anchors: file + symbol, PR number over a rebase-fragile commit SHA, mind
  section over "somewhere in the mind."
- A learning from the solutions store is a hypothesis until re-verified against current
  source. Mark it `LEARNING_UNVERIFIED` if you have not re-checked it this run.
- If you cannot ground a claim, list it under `unknowns`; never upgrade a guess to a fact.

## Build procedure

1. Read `knowledge-base/contract.json`; capture:
   - repository and graph paths
   - allowed and protected paths
   - source priority and test paths
   - test/check commands and repair limit
   - external systems and mocking rules
2. Read `CONTRACT.md`, especially Current API, layering, invariants, and Definition of Done.
3. Identify the feature slug. Read:
   - `knowledge-base/features/<slug>/overview.md`
   - feature PRD, decisions, evals, and notes if present
   - only relevant shared architecture and PRD documents
   - `knowledge-base/notes/solutions/` entries whose tags, feature, or symbols match the
     task; fold prior root causes and failed approaches into your reasoning
4. Check graph freshness against the Search repository HEAD. If stale, mark graph claims
   provisional; do not rebuild unless the stage is authorized to mutate graph artifacts.
5. Ask one narrow graph question tied to the task:

```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify query "<specific behavior or dependency question>" --graph "$GRAPH" --budget 4000
```

6. Explain each likely changed symbol. Use `path` only for a concrete dependency question:

```bash
graphify explain "<symbol>" --graph "$GRAPH"
graphify path "<changed symbol>" "<suspected caller>" --graph "$GRAPH"
```

7. Verify critical graph claims in current source/tests:
   - INFERRED or AMBIGUOUS edges
   - public API and response shape
   - cache boundaries and personalization order
   - side effects and external calls
8. Produce a compact context manifest before reasoning:

```json
{
  "feature": "feature-slug",
  "mind_version": "current",
  "graph_fresh": true,
  "documents": ["..."],
  "symbols": [
    {
      "name": "Symbol",
      "source": "path.py:L10",
      "evidence": "EXTRACTED|INFERRED_VERIFIED|SOURCE",
      "reason": "why this symbol matters"
    }
  ],
  "invariants": ["..."],
  "constraints": ["..."],
  "prior_learnings": [
    {"path": "knowledge-base/notes/solutions/...", "relevance": "why it applies",
     "status": "LEARNING_VERIFIED|LEARNING_UNVERIFIED"}
  ],
  "unknowns": ["..."]
}
```

The manifest may be embedded in the stage output. Never claim a symbol, path, API field,
default, ordering rule, or dependency without evidence in this context.

## Search invariants to check when relevant

- v3 reuses v2 retrieval and personalization code; inspect both blast radii.
- Shared cache content is unpersonalized. Per-user/device processing happens after cache
  read/write.
- Response-shape or semantic changes require an explicit cache compatibility decision.
- Personalization/filter order is behavior, not an implementation detail.
- External systems are mocked in unit/BDD tests; tests must not make live connections.
- User-visible behavior uses BDD where practical; internal algorithms use focused unit tests.
