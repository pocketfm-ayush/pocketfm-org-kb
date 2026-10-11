<!-- Every assistant turn — epistemic recheck. -->
# Skill: Harness response recheck

**When:** Before sending any non-greeting assistant response.
**Goal:** Catch hallucinated certainty, missing evidence, and skipped checks.

## Protocol (mandatory)

1. List discrete **CLAIMS** in the draft.
2. For each claim attach **EVIDENCE**:
   - file path + symbol, or
   - tool name + key fields, or
   - URL, or
   - `INFERRED` (must say why).
3. List **OPEN QUESTIONS** / **ASSUMPTIONS**.
4. Assign **CONFIDENCE** (`high` only if every claim has non-INFERRED evidence).
5. **Adversarial recheck:** “If this is wrong, where?” Re-run or re-read at least
   one critical source when confidence is not high.
6. Only then emit the user-facing answer. Prefer including a short evidence footer
   for deploy/incident/implement work.

## Fail the turn (revise before send) if

- Any metric/latency/5xx number lacks a tool source.
- “Tests pass” / “deploy succeeded” without command or monitoring evidence.
- Pack names / endpoints / tables not in CONTRACT/features (unless INFERRED + asked).
- Review findings fixed in prose but not in the diff.
- Stage gate from `harness-loop` not passed.

## Rubric freeze (Deep Agents style)

On the first verification pass, freeze the checklist. Later passes may only
mark criteria satisfied with **new** evidence — do not silently drop criteria.
