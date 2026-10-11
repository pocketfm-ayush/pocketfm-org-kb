---
name: code-review
description: Aural Android PR review — modules, DI, player, coroutines.
triggers: [code review, android, aural, kotlin]
intent: review
priority: 95
---

# android-client / Aural code review (Kotlin)

Pack overlay. Use with global `role-reviewer` + `kotlin`.

## Lenses
1. **Module placement** — feature vs domain vs data vs common-ui; no wrong-layer leaks.
2. **DI / navigation** — existing graphs and deeplink patterns only.
3. **Player / media** — ownership rules; do not fork player state casually.
4. **Coroutines** — structured concurrency; Main-safe UI updates.
5. **Tests** — ViewModel/use-case unit tests; avoid instrumentation for pure logic.

## Better approach bias
Reuse `common` / `core` components; prefer patterns already in `aural/`.
