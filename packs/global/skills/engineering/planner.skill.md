---
name: planner
description: Turn a goal into an ordered implementation plan with risks, checkpoints, and stop conditions.
triggers: [plan, implementation plan, how should we build, break down, roadmap for task]
intent: plan
priority: 90
---

# 02 · Planner

**Job:** produce an actionable plan before coding. Pair with `role-planner` for role framing; this skill owns the engineering plan shape.

## Do
1. Restate goal + success criteria in one sentence each.
2. List assumptions and open questions (blockers first).
3. Ordered steps — smallest shippable increments.
4. For each step: files likely touched, tests, and rollback/stop condition.
5. Call `harness-plan-critique` before execution when risk is high.

## Do not
- Skip exploration (`repo-explorer`) on unfamiliar code.
- Plan irreversible prod steps without a QA/staging gate.
- Hide uncertainty — mark unknowns explicitly.

## Output
Goal · Success · Assumptions · Steps · Risks · Recheck skills to run
