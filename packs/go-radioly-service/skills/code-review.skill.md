---
name: code-review
description: Go Radioly service PR review — Gin handlers, GORM, context, errors.
triggers: [code review, go-radioly, gin]
intent: review
priority: 95
---

# go-radioly-service code review (Go / Gin)

Pack overlay. Use with global `role-reviewer` + `golang`.

## Lenses
1. **Layering** — handler → service → repo; no DB from handlers without cause.
2. **Errors** — wrap with context; preserve cause; map to correct HTTP status.
3. **Context** — propagate `context.Context` on outbound/DB calls; honor cancel.
4. **GORM / MySQL** — query scope, transactions, soft-delete pitfalls.
5. **Shared clients** — use go-common httpclient / mysql wrappers when present.
6. **Tests** — table-driven; mock boundaries; no real prod deps in unit tests.

## Better approach bias
Match nearby packages under `internal/`; prefer small diffs over new packages.
