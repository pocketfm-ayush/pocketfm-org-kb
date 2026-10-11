---
name: python
description: Python service conventions — packaging, typing, tests, async care.
triggers: [python, pytest, django, fastapi, typing]
intent: implement
priority: 70
---

# Python

## Do
- Match repo formatter/linter (ruff/black/mypy as configured).
- Pytest for behavior; fixtures over global mutable state.
- Explicit deps in lockfiles; no drive-by framework adds.
- Careful with async + blocking I/O.

## Do not
- Swallow exceptions without logging context.
- Add `sys.path` hacks when packaging already works.

## Related
`database-sql`, `performance-review`, `security-review`, `docker`, `kubernetes` as applicable.
