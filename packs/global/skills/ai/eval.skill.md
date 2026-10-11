---
name: eval
description: Define and run evaluations for agents/skills — golden cases, regressions, scorers.
triggers: [eval, evaluation, golden set, agent regression, benchmark skill]
intent: review
priority: 83
---

# Eval

**Job:** measure agent/skill quality. Pair with `eval-writer` for authoring cases.

## Do
1. Define task, success rubric, and failure modes.
2. Keep golden inputs stable; version them when product changes.
3. Score faithfulness to evidence, not fluency alone.
4. Track regressions when prompts/skills change.
5. Prefer small, sharp suites over huge noisy ones.

## Do not
- Optimize only for demo queries.
- Claim quality without a failing counterexample set.

## Output
Suite · Cases · Rubric · Results · Gaps
