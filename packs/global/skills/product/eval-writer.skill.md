<!-- Default skill. Packs may override at <pack>/skills/eval-writer.skill.md -->
# Skill: Eval Writer

**Stage:** approved resolved PRD → `EVALS_READY`  
**Inputs:** final PRD, recorded answers, PRD-analysis JSON, repo mind, knowledge-base,
graph, current tests/source  
**Output:** JSON only; no production code or test files

## Standard

Produce an executable acceptance contract, not a list of optimistic examples. Every MUST
must be covered, and every eval must be deterministic, falsifiable, independently diagnosable,
and traceable to approved product intent.

Use `CONTEXT_BUILDER.md`. If PRD analysis is not `ready_for_evals`, product answers are
missing, or approved text contradicts the mind, return `EVALS_BLOCKED`; do not guess.

## Coverage model

For each requirement, select applicable dimensions:

1. **Positive:** happy path and each distinct approved branch.
2. **Boundary:** empty, zero, one, max, above max, unicode, long query, duplicates.
3. **Negative/validation:** malformed, unsupported, missing, unauthorized.
4. **State:** cache hit/miss, cold/warm user, experiment on/off, eligible/ineligible.
5. **Platform/locale/version:** only explicit supported combinations; pairwise selection is
   allowed when full Cartesian coverage is wasteful, but document it.
6. **Dependencies:** success, empty, timeout/error, partial failure, stale data where defined.
7. **Compatibility:** v2/v3, unchanged fields/defaults/order for existing clients.
8. **Invariants:** exclusions, deduplication, personalization boundary/order, no live IO in
   tests, no per-user data in shared cache.
9. **Observability:** required metric/event/log emitted with stable fields; never assert
   sensitive values.
10. **Quality/performance:** offline relevance metric, latency/query count, or memory target
    only when the PRD defines a measurable threshold and the test environment can measure it.

Do not manufacture expected ranked show IDs without an approved golden dataset. If relevance
is subjective, define a dataset, labels, metric (e.g. nDCG@k), baseline, threshold, slices,
and owner; otherwise mark the eval blocked.

## Eval design procedure

1. Build the context manifest and copy the normalized requirement IDs from PRD analysis.
2. Inspect nearest existing tests found through Graphify. Reuse existing fixture/stub style.
3. Create a requirement coverage matrix before writing eval cases.
4. Convert each acceptance criterion into one or more cases.
5. Define exact fixtures and dependency responses. No “valid user”, “normal response”, or
   “appropriate result” placeholders.
6. Define exact assertions:
   - fields and values
   - ordering and deduplication
   - inclusions/exclusions
   - side effects / emitted event when contractual
   - fields that must remain unchanged
7. Identify the correct level:
   - `bdd`: user-visible/API behavior across layers
   - `unit`: algorithm, branch, formatting, repository contract
   - `offline_quality`: golden dataset / ranking metric
   - `manual`: only when automation is genuinely impossible; include owner and steps
8. Add regression protection for current behavior affected by the blast radius.
9. Add mutation checks: for every MUST, state the smallest intentional defect that would
   make the eval fail. If no defect would fail it, the eval is weak.
10. Validate completeness:
    - every MUST maps to at least one automated eval unless explicitly approved otherwise
    - every P0 product answer maps to an eval or documented non-testable decision
    - no eval relies on unspecified behavior
    - all fixtures are isolated from real external systems

## Confidence self-check (adversarial pass)

Before finalizing, score coverage per requirement and attack your own suite; the cheap moment
to find a thin eval is now, not during repair.

1. Score each requirement `strong | thin | missing` against the coverage model. A requirement
   is `thin` if it has only a happy-path eval, no mutation that fails, or an untested failure
   branch the PRD defines.
2. For the weakest items, run an adversarial lens: "What implementation would pass every eval
   here yet violate approved intent?" If such an implementation exists, the suite has a hole —
   add the eval that closes it.
3. Re-check the two Search traps explicitly: a change that quietly reorders
   personalization/filtering, and a response/semantic change that keeps a stale shared-cache
   payload. At least one eval must fail under each when the requirement touches them.
4. Record the self-check outcome in `confidence` (below). Do not emit `EVALS_READY` while any
   MUST is `thin` or `missing`.

## Search-specific checks

Apply only when relevant:

- `QueryRouter`: empty, genre/topic, and text routes.
- Language search: locale pool, exact/prefix/fuzzy cascade, fallback, tie/order rules.
- Cache: hit/miss parity, unpersonalized stored payload, per-user processing after read/write,
  key/version behavior, Redis failure fallback.
- Personalization: AI/PGC → campaign-only → ME → override → disabled → DS thumbnail order.
- v2/v3 compatibility and intentional divergences.
- Filtering: moderated, disabled, suppressed, duplicate, unavailable, audiobook behavior.
- External failures: ES, Redis, Scylla, MySQL, Radioly API, AppsFlyer as applicable.

## Hard rules

- No vague expected outcomes.
- No assertions on implementation calls unless the call/side effect is the contract.
- Do not over-mock the subject under test.
- Do not snapshot entire unstable responses when focused assertions are safer.
- Do not make live network/database/cache calls.
- Do not classify missing product semantics as an “assumption”; block instead.
- A manual eval cannot substitute for automatable MUST behavior without explicit approval.

## Output schema

```json
{
  "status": "EVALS_READY",
  "prd_ref": "...",
  "context": {
    "feature": "slug",
    "graph_fresh": true,
    "documents": ["..."],
    "symbols": ["path.py::Symbol"]
  },
  "coverage_matrix": [
    {
      "requirement_id": "MUST-1",
      "criteria": ["AC-1"],
      "eval_ids": ["E1", "E2"],
      "dimensions": ["positive", "cache_hit", "cache_miss", "redis_failure"],
      "coverage": "complete"
    }
  ],
  "evals": [
    {
      "id": "E1",
      "requirement_ids": ["MUST-1"],
      "acceptance_criterion_ids": ["AC-1"],
      "priority": "must",
      "level": "bdd",
      "surface": "v3.universal.search",
      "title": "...",
      "purpose": "...",
      "preconditions": ["..."],
      "fixtures": {
        "request": {"query": "..."}, 
        "user": {"locale": "IN"},
        "dependencies": {
          "redis": {"mode": "miss"},
          "elasticsearch": {"hits": []}
        }
      },
      "action": "...",
      "assertions": [
        {"path": "result.shows", "operator": "equals", "expected": []}
      ],
      "invariants": ["No user-specific data is written to shared cache"],
      "observability_assertions": [],
      "test_target": "v3/search/tests/test_<feature>_bdd.py",
      "existing_pattern": "v3/search/tests/test_v3_universal_search_bdd.py",
      "mutation_that_must_fail": "Move personalization before cache write",
      "tags": ["cache_miss", "regression"]
    }
  ],
  "offline_quality_plan": null,
  "manual_evals": [],
  "uncovered_items": [],
  "blocked_items": [],
  "confidence": {
    "per_requirement": [
      {"requirement_id": "MUST-1", "strength": "strong", "reason": "..."}
    ],
    "adversarial_holes_closed": [
      {"requirement_id": "MUST-1", "passing_but_wrong_impl": "...", "eval_added": "E7"}
    ],
    "weakest_remaining": []
  },
  "quality_gate": {
    "all_must_covered": true,
    "all_p0_answers_covered": true,
    "no_live_dependencies": true,
    "no_unspecified_expectations": true,
    "ready_for_implementation": true
  }
}
```

If blocked, return:

```json
{
  "status": "EVALS_BLOCKED",
  "blocked_items": [
    {
      "requirement_id": "MUST-1",
      "missing_decision": "...",
      "question": "...",
      "why_eval_cannot_be_written": "..."
    }
  ],
  "quality_gate": {"ready_for_implementation": false}
}
```
