<!-- Default skill. Packs may override at <pack>/skills/repair.skill.md -->
# Skill: Repair

**Stage:** failed scoped/full tests, checks, or coverage → retry or `REPAIR_EXHAUSTED`  
**Inputs:** attempt number, exact command/output, changed files, baseline status, resolved
PRD, immutable evals, repo mind, context evidence  
**Output:** full files through file protocol, or terminal JSON

## Entry gate

Read `max_repair_iterations` from `repo-mind.json`; never assume it. Reject attempt numbers
outside `1..max`. The original PRD and evals are immutable during repair.

Use `CONTEXT_BUILDER.md` narrowly: failure trace, changed symbols, direct callers, nearest
tests. Do not reopen broad design or explore unrelated modules.

## Diagnosis before change

Classify every failure:

- `IMPLEMENTATION_DEFECT`: changed logic violates approved behavior.
- `TEST_DEFECT`: test incorrectly encodes an approved eval.
- `REGRESSION`: existing behavior broke.
- `IMPORT_OR_STUB`: isolated test environment is missing valid external stubbing.
- `STATIC_CHECK`: lint/type/style failure.
- `ENVIRONMENT`: dependency/service/tooling issue not caused by patch.
- `FLAKY_OR_ORDER_DEPENDENT`: non-determinism or leaked state.
- `PRODUCT_OR_EVAL_CONFLICT`: approved requirements cannot all hold.
- `PRE_EXISTING`: reproduces on unchanged baseline.

Prove the category with failure output and relevant source/eval evidence. Do not label a
failure “pre-existing” without baseline evidence.

## Causal-chain gate (no fix until the chain is explained)

Do not change code until you can state the full chain from trigger to failing assertion with
no gaps. "Somehow X causes Y" is a gap, not a diagnosis. The chain must reach the point where
valid state first became invalid — the root cause is where bad state *originates*, not where
the test first observes it.

- **Assumption audit.** List the "this must be true" beliefs your diagnosis depends on (the
  stub returns what its name implies, the fixture loads before the call, v2 code behaves this
  way here). Mark each `verified` (you read the line or ran it) or `assumed`. Many wrong
  diagnoses are a correct hypothesis tested against a wrong assumption — verify assumptions
  before trusting the chain.
- **Prediction for uncertain links.** For any link you are not certain of, state something in
  a *different* code path or scenario that must also be true if the link is real, and check it.
  If the prediction is false but a patch makes the test pass, you fixed a symptom — the real
  cause is still active. Reject the patch and keep tracing.
- Obvious links (missing import, clear nil dereference) need no prediction; this is a tool for
  uncertainty, not a ritual.

## Repair procedure

1. Build a failure matrix:
   - failing test/check and first actionable traceback
   - related eval/requirement
   - category
   - root cause
   - smallest corrective change
2. Fix root cause, not the observed symptom.
3. Preserve all unaffected behavior and assertions.
4. For `TEST_DEFECT`, change a test only when it conflicts with the approved eval; cite the
   exact eval field internally.
5. For `IMPORT_OR_STUB`, stub only external infrastructure or follow the established local
   import-isolation pattern. Never replace the subject under test with a mock.
6. For `ENVIRONMENT` or `PRE_EXISTING`, stop and report; do not distort code to compensate.
7. Emit only files needed for this attempt.
8. Orchestrator reruns:
   - originally failing targeted test/check
   - related feature tests
   - full required commands after targeted success

## Immutable safeguards

Never:

- delete, skip, xfail, loosen, or replace a failing acceptance assertion;
- alter eval JSON or approved PRD semantics;
- reduce coverage threshold or exclude changed files;
- catch broad exceptions solely to hide a failure;
- return hard-coded test values or branch on test environment;
- add arbitrary retries/sleeps;
- remove logging/metrics required by evals;
- expand allowed paths or modify protected files;
- perform unrelated refactors;
- claim success without command evidence.

If product/eval intent is contradictory or impossible under the mind, return a blocker. That
is not a failed repair attempt to conceal.

## Attempt discipline

One change at a time. Never alter several things at once "to see what helps" — if the run
goes green you will not know which change was the fix, and a symptom patch can hide.

- Attempt 1: direct root-cause correction.
- Attempt 2: reconsider diagnosis using new evidence; do not repeat the same patch.
- Attempt 3 (or configured maximum): final minimal correction. If still failing, stop.

Each attempt should explain itself through changed files; no prose outside file protocol.

## When stuck, diagnose why — do not try harder

Two failed attempts on the same failure means the diagnosis is likely wrong. Before the final
attempt, name *why* you are stuck and act on it rather than trying another variation:

- hypotheses point at different subsystems → wrong mental model; re-read the chain from the
  origin without your prior assumptions.
- evidence contradicts itself → an assumption in the audit is false; re-verify each.
- fixed but a prediction was wrong → symptom fix; the real cause is still live.
- reproduces only under the full command, not the targeted test → environment/order/leaked
  state, not the patch.
- every candidate fix is a workaround, or the requirements themselves conflict → this is a
  product/design problem; return `REPAIR_BLOCKED` with `PRODUCT_OR_EVAL_CONFLICT`, do not
  contort the code.

## File protocol

```text
=== FILE: <path-relative-to-pocket_search-root> ===
<complete contents>
=== END FILE ===
```

## Terminal outputs

For non-code blockers:

```json
{
  "status": "REPAIR_BLOCKED",
  "attempt": 1,
  "category": "ENVIRONMENT",
  "command": "...",
  "failures": ["..."],
  "evidence": ["..."],
  "required_next_action": "..."
}
```

After the configured maximum:

```json
{
  "status": "REPAIR_EXHAUSTED",
  "attempts": 3,
  "commands_run": ["..."],
  "remaining_failures": [
    {
      "test_or_check": "...",
      "category": "IMPLEMENTATION_DEFECT",
      "first_actionable_error": "...",
      "related_eval_ids": ["E1"],
      "causal_chain": ["trigger -> ... -> failing assertion"],
      "chain_gaps": ["link not yet explained"],
      "assumptions": [
        {"belief": "...", "status": "verified|assumed"}
      ],
      "failed_predictions": ["..."],
      "suspected_root_cause": "...",
      "evidence": ["..."]
    }
  ],
  "changes_attempted": ["..."],
  "ruled_out": ["..."],
  "stuck_reason": "wrong_model|contradictory_evidence|symptom_fix|environment|design_conflict",
  "required_human_decision": "..."
}
```
