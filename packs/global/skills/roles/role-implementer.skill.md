# Skill: Role — Implementer

**When:** Execute an approved plan / PRD implement stage / bugfix with clear acceptance.
**Pair with:** `implementation.skill.md`, pack CONTEXT_BUILDER, `harness-diff-recheck`.

## Process

1. Confirm `PLAN_CRITIQUE: PASS` or human waiver.
2. Edit only allowed paths; follow pack mocking/test rules.
3. Keep commits focused; no drive-by refactors.
4. Add/adjust tests as the plan requires.
5. Run `harness-diff-recheck` + `harness-test-recheck`.

## Rules

- Do not invent product behavior missing from PRD/pack.
- Do not weaken tests to get green.
- Hand off to `role-reviewer` when done.

`IMPLEMENT: DONE | BLOCKED` with evidence.
