---
name: swift
description: Swift / iOS service conventions — concurrency, modules, tests.
triggers: [swift, ios, swiftui, uikit, xcode]
intent: implement
priority: 70
---

# Swift / iOS

## Do
- Follow existing module / target layout; reuse shared kits before adding new ones.
- Prefer async/await or existing concurrency helpers already in the repo.
- Keep networking / persistence behind established clients — no ad-hoc URLSession sprawl.
- Unit-test logic layers; avoid UI-test-only coverage for pure business rules.

## Do not
- Force-unwrap without a proven invariant.
- Capture `self` strongly in long-lived closures without cause.
- Bypass app architecture (coordinators / routers) with one-off navigation hacks.

## Related
`code-review`, `security-review`, `agents-coding`, `performance-review` as applicable.
