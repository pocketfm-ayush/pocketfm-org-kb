<!-- Default skill. Packs may override at <pack>/skills/prd-analysis.skill.md -->
# Skill: PRD Analysis

**Stage:** `analyze` → `WAITING_FOR_PRODUCT` or `READY_FOR_APPROVAL`  
**Inputs:** PRD, product answers, repo mind, knowledge-base, graph, current source/tests  
**Output:** JSON only; never code or eval files

## Standard

Be a skeptical staff engineer and product analyst. Do not praise the PRD, agree with its
premise, or fill gaps with plausible guesses. A PRD is ready only when a different engineer
could implement it without making product decisions.

Use `CONTEXT_BUILDER.md` exactly. Graphify is a discovery aid, not an unquestionable source
of truth. Verify critical INFERRED edges against current code. Read matching entries in
`knowledge-base/notes/solutions/` first — a prior root cause or failed approach often changes
which questions actually matter — but treat each as `LEARNING_UNVERIFIED` until re-checked.

## Session-settled decisions

A decision the user already examined and chose (in this thread or a recorded answer) is
**carried, not re-asked**. Record it verbatim with its rationale and render it as a
`carried_forward` entry, not a question. You may still surface it if new evidence
*invalidates* it (infeasible, unsafe, or contradicts the mind) — that is a conflict, not a
re-litigation. An unexamined assertion is not settled; it earns exactly one challenge.

## Required PRD format

The contract is `prd-format.skill.md`. If the input is free-form, treat it as
raw: extract what exists into that shape (same headings, `MUST-*` IDs), mark
missing sections `unknown`, and ask for the missing decisions. Do not reject a
PRD only because it was a Confluence page.

Prefer a body that already came from `prd-normalize` or `prd-writer`.

## Analysis procedure

1. Build the shared context manifest, including matching prior learnings.
2. Normalize every requirement into an ID (`MUST-1`, `SHOULD-1`). Split compound statements.
   These IDs are the traceability spine: evals cite them, implementation maps them, mind
   update closes on them. Never renumber a requirement once emitted.
3. Build a requirement-to-evidence map:
   - intended behavior: PRD section / product answer
   - current behavior: mind, knowledge doc, graph node, verified source/test
   - likely touch points and callers
4. Check each dimension below. `not_applicable` requires a reason:
   - actors, eligibility, platforms, locales, versions
   - input types, validation, defaults, bounds, malformed values
   - output schema, ordering, deduplication, pagination, empty state, errors
   - ranking, filtering, tie-breaking, exact/fuzzy behavior
   - cache key, TTL/invalidation, hit/miss parity, personalization boundary
   - v2/v3 parity and backward compatibility
   - experiment allocation, exposure, kill switch, rollback
   - Redis/ES/Scylla/MySQL/API timeout, partial failure, retry, fallback
   - observability: metrics, events, logs, dashboards, alerting
   - privacy/security/abuse/content-moderation constraints
   - migration/backfill/data freshness
   - performance and scale limits
   - acceptance metric and guardrails
5. Identify contradictions separately from omissions. Quote both conflicting statements.
6. Ask as many questions as needed. Do not target an arbitrary small count.
7. Rank questions:
   - `P0_BLOCKING`: changes public behavior, data contract, eligibility, ordering, safety,
     compatibility, rollout, or acceptance criteria
   - `P1_REQUIRED`: needed for robust implementation/evals but a reversible default exists
   - `P2_CLARIFICATION`: improves precision without changing implementation materially
8. Every question must include why it matters, evidence, and concrete options when options
   are knowable. Never smuggle a recommendation in as a question.
9. Compute readiness mechanically. Any unresolved P0, mind conflict, missing MUST acceptance
   criterion, or unverifiable current-flow assumption means `WAITING_FOR_PRODUCT`.

## Strict gates

- No implementation design before product semantics are resolved.
- No new endpoint, response field, default, ranking rule, cache behavior, or rollout model
  may be inferred.
- “Maintain existing behavior” is insufficient unless existing behavior is identified.
- “Handle edge cases” is insufficient; enumerate them.
- “Fast” or “relevant” is insufficient; require measurable criteria.
- A limitation is not permission to ignore a requirement.
- If the PRD conflicts with current behavior, do not choose a side.

## Output schema

Return valid JSON matching this shape:

```json
{
  "status": "WAITING_FOR_PRODUCT",
  "prd_format": {
    "complete": false,
    "missing_sections": ["Acceptance metrics"],
    "malformed_or_compound_requirements": ["MUST-2"]
  },
  "context": {
    "feature": "slug",
    "graph_fresh": true,
    "documents": ["..."],
    "symbols": [
      {
        "name": "Symbol",
        "source": "path.py:L10",
        "evidence": "EXTRACTED",
        "reason": "..."
      }
    ],
    "invariants": ["..."],
    "unknowns": ["..."]
  },
  "summary": {
    "problem": "...",
    "requested_outcome": "...",
    "affected_surfaces": ["v3.universal.search"],
    "non_goals": ["..."]
  },
  "requirements": [
    {
      "id": "MUST-1",
      "text": "...",
      "atomic": true,
      "observable": true,
      "status": "clear|ambiguous|conflicting|unsupported",
      "acceptance_criteria": ["..."],
      "current_behavior_evidence": ["REPO_MIND.md#...", "path.py:L10"],
      "likely_touch_points": ["path.py::Symbol"],
      "dependencies": ["Redis"],
      "open_question_ids": ["Q1"]
    }
  ],
  "carried_forward": [
    {
      "id": "S1",
      "decision": "...",
      "rationale": "...",
      "source": "user answer 2026-08-14 | prior thread",
      "still_valid": true
    }
  ],
  "prior_learnings": [
    {"path": "knowledge-base/notes/solutions/...", "relevance": "...",
     "status": "LEARNING_VERIFIED|LEARNING_UNVERIFIED"}
  ],
  "conflicts": [
    {
      "id": "C1",
      "severity": "blocking",
      "prd_statement": "...",
      "repo_statement": "...",
      "evidence": ["..."],
      "decision_required": "..."
    }
  ],
  "questions": [
    {
      "id": "Q1",
      "priority": "P0_BLOCKING",
      "category": "cache|api|eligibility|ranking|failure|rollout|metric|other",
      "question": "...",
      "why_it_matters": "...",
      "evidence": ["..."],
      "options": [
        {"id": "A", "label": "...", "consequence": "..."}
      ],
      "recommended_option": null,
      "blocks_requirement_ids": ["MUST-1"]
    }
  ],
  "blast_radius": {
    "v2": {"affected": true, "evidence": ["..."]},
    "v3": {"affected": true, "evidence": ["..."]},
    "cache": {"affected": "unknown", "evidence": ["..."]},
    "personalization_order": {"affected": false, "evidence": ["..."]},
    "external_systems": ["elasticsearch"]
  },
  "limitations": [
    {"item": "...", "impact": "...", "resolution": "product|engineering|none"}
  ],
  "readiness": {
    "ready_for_approval": false,
    "ready_for_evals": false,
    "blocking_reasons": ["Q1 unresolved"],
    "required_next_action": "ANSWER_QUESTIONS"
  }
}
```

Use `READY_FOR_APPROVAL` only when every MUST is atomic, observable, conflict-free, and has
testable acceptance criteria; all P0 questions are answered; and remaining assumptions are
explicitly approved.
