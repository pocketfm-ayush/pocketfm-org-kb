---
name: kotlin
description: Kotlin / Android service conventions — coroutines, modules, tests.
triggers: [kotlin, android, jetpack, compose, gradle]
intent: implement
priority: 70
---

# Kotlin / Android

## Do
- Match module boundaries (`feature` / `domain` / `data` / `common-ui`) already in the repo.
- Prefer existing DI / navigation / player patterns — no new frameworks without cause.
- Coroutines with structured concurrency; cancel on lifecycle where applicable.
- Unit-test ViewModels / use cases; keep Android instrumentation out of unit suites.

## Do not
- Block the main thread on network/DB.
- Leak Activity/Fragment/Context into long-lived objects.
- Duplicate shared components that already exist under `common` / `core`.

## Related
`code-review`, `security-review`, `agents-coding`, `performance-review` as applicable.
