---
name: golang
description: Go service conventions — Gin/GORM patterns, errors, tests.
triggers: [golang, go, gin, gorm]
intent: implement
priority: 70
---

# Golang

## Do
- Follow Pocket FM Go service patterns (handler → service → repo).
- Wrap errors with context; do not lose the cause.
- Table-driven tests; use shared clients (httpclient, mysql wrappers) when present.
- Context propagation on outbound calls.

## Do not
- Panic for routine user errors.
- Bypass repo layers to hit DB from handlers without cause.

## Related
`database-sql`, `performance-review`, `security-review`, `docker`, `kubernetes` as applicable.
