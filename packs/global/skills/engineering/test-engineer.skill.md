---
name: test-engineer
description: Design and add tests that lock behavior — unit, integration, fixtures, and failure cases.
triggers: [add tests, write tests, test plan, coverage, regression test]
intent: implement
priority: 88
---

# 06 · Test engineer

**Job:** prove behavior. Use repo conventions (`agents-testing`, `phantom-pytest` when Phantom). Run `harness-test-recheck` after edits.

## Do
1. List behaviors changed or at risk.
2. Prefer existing test harness / fixtures over new frameworks.
3. Cover happy path, edge, and failure/permission cases that matter.
4. Keep tests deterministic (no flaky sleeps / live network unless marked).
5. Name tests after behavior, not implementation trivia.

## Do not
- Chase coverage % while missing the regression that matters.
- Snapshot huge opaque blobs without asserting meaning.
- Duplicate suite logic already covered at a better layer.

## Output
Risks · Cases · Files to add/update · Commands to run · Gaps left intentional
