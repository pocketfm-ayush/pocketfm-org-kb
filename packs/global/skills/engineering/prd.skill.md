---
name: prd
description: Author or normalize product requirements — problem, scope, scenarios, acceptance.
triggers: [prd, requirements, product spec, acceptance criteria, user stories]
intent: plan
priority: 85
---

# 15 · PRD

**Job:** make requirements implementable. Prefer existing `prd-writer`, `prd-format`, `prd-normalize`, `prd-analysis`.

## Do
1. Problem, goals, non-goals, users.
2. Scenarios (Gherkin-friendly) and acceptance checks.
3. Dependencies, risks, analytics/events if relevant.
4. Explicit out-of-scope to prevent gold-plating.
5. Hand off to `planner` / `architecture` for build plan.

## Do not
- Spec UI pixel-perfect without product intent.
- Leave success unmeasurable.

## Output
Problem · Scope · Scenarios · Acceptance · Open questions · Linked skills
