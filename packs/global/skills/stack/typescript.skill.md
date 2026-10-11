---
name: typescript
description: TypeScript/Node conventions — types, tests, and API clients.
triggers: [typescript, ts, node, react, vitest]
intent: implement
priority: 70
---

# TypeScript

## Do
- Strict types at boundaries (API DTOs); avoid `any` without reason.
- Match repo test runner (vitest/jest) and lint (eslint).
- Prefer existing design system / shared packages.
- Handle fetch errors and non-JSON responses explicitly.

## Do not
- Disable eslint broadly to land a change.
- Duplicate types that already live in a shared package.

## Related
`database-sql`, `performance-review`, `security-review`, `docker`, `kubernetes` as applicable.
