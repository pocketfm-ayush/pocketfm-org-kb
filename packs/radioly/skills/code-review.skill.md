---
name: code-review
description: Radioly (Django) PR review lenses — ORM, views, caches, experiments.
triggers: [code review, radioly, django]
intent: review
priority: 95
---

# Radioly code review (Django / Python)

Pack overlay for `radioly_client_api`. Use with global `role-reviewer` + `python`.

## Radioly-specific lenses
1. **Views / URLs** — handler matches `urls.py`; no dead v2/v3 drift without intent.
2. **ORM / MySQL** — N+1, missing `select_related`/`prefetch`, wrong `db_table`.
3. **Cache / Redis** — key template from `key_schema` / helpers; invalidate on write paths.
4. **Scylla / ES** — only when the diff touches those clients; check consistency claims.
5. **Experiments** — `EXPERIMENT_ID` / allocation; no hard-coded variant without flag.
6. **Authz / user** — uid/device from request helpers; never trust client-only ids.
7. **Tests** — co-located `test_*.py` + fixtures; no live MySQL/Redis/Scylla in unit tests.
8. **Diff-cover** — new production lines need pytest coverage (CI ~80%).

## Better approach bias
Prefer existing v2/v3 helpers, serializers, and experiment helpers over new abstractions.

## Not for
Infra/Helm (ask `#infra-devops`), warehouse SQL (Argus), mobile clients.
