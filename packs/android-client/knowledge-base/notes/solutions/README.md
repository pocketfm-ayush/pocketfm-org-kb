# Solutions — compounding learnings

Durable, reusable learnings captured after a non-trivial problem is solved and verified.
This store is the "return arrow" of the flow: `mind-update` writes here, and every later
stage reads it through `CONTEXT_BUILDER.md` so the same investigation never happens twice.

## What belongs here

Capture a learning only when it is **non-trivial and reusable**:

- a root cause that took real investigation (not a typo or one-line fix)
- a wrong assumption about a shared dependency (cache, ES, Scylla, Radioly, experiments)
- a convention or pattern that future work should follow
- an approach that looked right and failed, and why

Skip trivial fixes, mechanical changes, and one-off incidents with no generalizable insight.

## Two tracks

Each entry is one of two shapes. Pick by the nature of the learning.

**Bug track** — an incident: something broke, here is why and how it was fixed.
Sections: `Symptoms` → `What Didn't Work` → `Root Cause` → `Solution` → `Why This Works`
→ `Prevention`.

**Knowledge track** — durable guidance: this is how we do X here, and why.
Sections: `Context` → `Guidance` → `Why This Matters` → `When to Apply` → `Examples`.

## File shape

Path: `knowledge-base/notes/solutions/<category>/<slug>.md`

Bug-track categories: `runtime-errors/`, `test-failures/`, `performance-issues/`,
`cache-issues/`, `personalization-issues/`, `integration-issues/`, `data-issues/`.
Knowledge-track categories: `architecture-patterns/`, `conventions/`, `tooling-decisions/`,
`best-practices/`.

Frontmatter (every entry):

```yaml
---
title: "..."
track: bug | knowledge
problem_type: performance_issue | cache | personalization | ...
feature: <feature-slug>
symbols: ["path.py::Symbol"]
tags: ["cache_miss", "v3"]
pr: "#1234"           # prefer a PR link over a rebase-fragile SHA
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
verified_against: "path.py:L10 (source line read this run)"
---
```

## Overlap rule (update, don't duplicate)

Before creating a new entry, search this store. If an existing entry describes the same
root cause or the same guidance (matching feature, symbols, and problem statement), **update
it** with fresher context and bump `last_updated` rather than creating a near-duplicate that
will drift.

## Grounding rule

Every claim in an entry must be grounded per `CONTEXT_BUILDER.md`: read the defining source
line before asserting behavior, cite PR over SHA, and record `verified_against`. An entry is
a hypothesis until re-verified; readers treat it as `LEARNING_UNVERIFIED` until they re-check.
