<!-- Default skill. Packs may override at <pack>/skills/implementation.skill.md -->
# Skill: Implementation

**Stage:** `EVALS_READY` + approved run → `TESTING`  
**Inputs:** resolved PRD, PRD-analysis JSON, eval JSON, repo mind, knowledge-base, graph,
current source/tests  
**Output:** full files through file protocol only

## What you own

Evals and the PRD define **WHAT** must be true when this is done; you decide **HOW** to make
it true with the code in front of you. Do not treat an eval's fixture wiring as a mandated
call sequence, and do not encode choreography the eval did not require. Satisfy the contract
using existing architecture and the smallest change that holds.

## Entry gate

Refuse implementation unless:

- PRD analysis says `ready_for_evals=true`;
- eval writer says `ready_for_implementation=true`;
- every MUST is covered or has explicit product-approved exclusion;
- all proposed paths match `allowed_edit_paths`;
- no required change targets a protected path.

Return a structured blocker instead of improvising around a failed gate.

## Context and evidence

Use `CONTEXT_BUILDER.md`. Start with the feature pack and scoped Graphify queries, then read
only the implicated source and nearest tests. Verify every critical INFERRED edge in source.

Before editing, create an internal change map:

```json
{
  "requirement_to_eval": {"MUST-1": ["E1"]},
  "eval_to_test": {"E1": "v3/search/tests/test_feature_bdd.py"},
  "symbol_changes": ["path.py::Symbol"],
  "callers_checked": ["..."],
  "invariants_at_risk": ["..."],
  "paths_to_write": ["..."]
}
```

Do not output this map; use it to prevent omissions.

## Implementation procedure

1. Encode evals as tests first or in the same output. Tests must represent approved behavior,
   not the current implementation.
2. Reuse existing architecture:
   - HTTP/serialization glue: views and request parser
   - validation/request semantics: `SearchRequestData` / parser
   - business rules: focused service
   - ES query/ranking: ES/search service modules
   - external IO: repository/client layer
   - response shaping: response builder/formatter
3. Preserve compatibility by default:
   - existing fields, types, defaults, ordering, and error behavior
   - v2 behavior when changing shared v2 code used by v3
   - intentional cache-hit/fresh divergences documented in the mind
4. Make cache decisions explicit:
   - response/semantic change: update key version or invalidation strategy
   - never store uid/device-personalized content in shared cache
   - test hit, miss, and Redis failure paths when affected
5. Preserve filtering/personalization order unless approved PRD changes it.
6. Keep external calls injectable/mockable; no real connections in tests.
7. Add focused observability only when specified by PRD/evals; do not log PII or secrets.
8. Run mentally against every eval and mutation statement before emitting files.

## Simplify and self-review before handoff

After the change satisfies the evals and before emitting files, do two passes on your own diff.
Both are scoped to the files you touched; never wander into unrelated code.

**Simplify pass.** Remove dead code, needless indirection, duplicated logic, and leftover
scaffolding. Prefer the existing helper over a new one. The goal is the smallest diff that
still satisfies every eval — a change that is easy to review is easy to keep correct.

**Diff-aware self-review.** Select review lenses by what the diff actually touches and check
each. Skip a lens with a one-line reason when its concern is absent.

- correctness (always): logic, boundaries, nil/empty, error paths
- project-standards (always): layering, conventions, allowed paths
- compatibility: existing fields, types, defaults, ordering, v2↔v3
- cache: key/version, hit/miss parity, no per-user data in shared cache
- personalization: filter/personalization order unchanged unless approved
- dependencies: ES/Redis/Scylla/MySQL/Radioly timeout, partial failure, fallback
- security/abuse: only when auth, PII, or moderation surface is touched

Rate each finding P0–P3. Fix P0/P1 before emitting. Carry any deliberately-unfixed P2/P3 into
the handoff `residual_findings` so it is recorded, never dropped into silence.

## Test rules

- User/API behavior → pytest-bdd where the existing feature uses BDD.
- Pure algorithm/formatter/repository contract → focused pytest.
- **Radioly:** prefer co-located `test_*.py` next to the changed module
  (`…/latam_modules/test_views.py`). Parent `v3/content/tests` is not enough
  for module coverage; CI `get_impacted_tests.py` + diff-cover (≥80%) will fail
  if new lines never run.
- Copy local fixture/stub conventions from the nearest test.
- v3 conftest stubs external infrastructure only; do not stub Search business modules merely
  to make imports pass unless the established file pattern requires it.
- Assert outputs and contractual side effects; avoid private call-count coupling.
- Include regression tests for affected existing behavior.
- Cover null/default fields that downstream `json.loads` / cache readers touch.
- When invalidating caches, use the same locale remapping as readers
  (`LOCALE_CONST_MAPPING` on Radioly LATAM modules).
- A test must fail under the eval’s `mutation_that_must_fail`.
- Groot opens a draft PR only after sandbox pytest passes on discovered targets.

## Hard constraints

- Only write `allowed_edit_paths`; protected paths are immutable in this stage.
- No hidden files, env changes, credentials, generated binaries, or dependency additions
  unless approved and allowed.
- No skips, xfails, assertion weakening, coverage-threshold changes, blanket exception
  catches, fake sleeps, or test-only production branches.
- No unrelated cleanup, renaming, formatting, or architecture migration.
- No invented product defaults.
- Do not suppress errors that the PRD does not define as recoverable.
- If implementation reveals a missing product decision, stop; return `IMPLEMENTATION_BLOCKED`.

## File protocol

Emit complete file contents only:

```text
=== FILE: <path-relative-to-pocket_search-root> ===
<complete contents>
=== END FILE ===
```

Deletion, only when explicitly required:

```text
=== DELETE: <allowed-relative-path> ===
```

No prose between or inside file blocks. After the final file block, you may emit exactly one
handoff block recording the self-review outcome and residuals:

```text
=== HANDOFF ===
{
  "requirement_to_eval": {"MUST-1": ["E1"]},
  "self_review": {"lenses_run": ["correctness", "cache"], "p0_p1_fixed": ["..."]},
  "residual_findings": [
    {"severity": "P3", "file": "path.py", "note": "...", "why_deferred": "..."}
  ]
}
=== END HANDOFF ===
```

## Blocker protocol

If blocked, output JSON instead of files:

```json
{
  "status": "IMPLEMENTATION_BLOCKED",
  "reason": "product_decision|path_violation|eval_conflict|mind_conflict|missing_context",
  "requirement_ids": ["MUST-1"],
  "evidence": ["..."],
  "question": "...",
  "required_next_action": "..."
}
```

After files are applied, the orchestrator must run the scoped tests first, then
`test_command`, `check_command`, and any required coverage/quality command. Failure enters
repair with the original PRD/evals unchanged.
