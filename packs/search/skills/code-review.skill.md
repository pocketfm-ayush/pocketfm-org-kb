---
name: code-review
description: Pocket Search PR review — query paths, ranking, ES/Redis, Python.
triggers: [code review, pocket_search, search]
intent: review
priority: 95
---

# pocket_search code review (Python)

Pack overlay for search. Use with global `role-reviewer` + `python`.

## Lenses
1. **Query path** — request → service → ES/Redis; no radioly feed symbols pasted here.
2. **Ranking / filters** — empty/null queries, pagination bounds, language/locale.
3. **Cache keys** — exact template; TTL; stampede on miss.
4. **Contracts** — response shape backwards compatible for clients.
5. **Tests** — co-located pytest; mock ES/Redis; assert empty-result behavior.

## Better approach bias
Reuse existing search helpers; do not invent radioly ORM patterns in this pack.
