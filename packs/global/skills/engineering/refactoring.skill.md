---
name: refactoring
description: Improve structure without changing behavior — small steps, tests green, clear diffs.
triggers: [refactor, clean up, simplify, extract, reduce duplication]
intent: implement
priority: 80
---

# 07 · Refactoring

**Job:** make the next change safer. Behavior must stay equivalent unless explicitly scoped otherwise.

## Do
1. Confirm tests (or add characterization tests) before moving code.
2. One concern per PR/commit when possible.
3. Preserve public contracts unless versioned/migrated.
4. Prefer extract/rename/move over clever rewrites.
5. Re-run targeted tests after each meaningful step.

## Do not
- Mix refactors with feature work in the same opaque diff.
- “Improve” by changing semantics silently.
- Large-bang rewrites without a migration plan (`architecture`).

## Output
Goal · Safety net · Steps · Risk of behavior drift · Verification
