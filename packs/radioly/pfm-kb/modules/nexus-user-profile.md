# Nexus user / device profile

Aliases: nexus, spending segment, listening segment, user created at

## What It Is
Source of truth for **non-PII** listener/device attributes used across feed, ads,
payments, and loyalty: segments, locale/language, create times, and related meta.
Radioly should prefer Nexus over direct MySQL `users`/`devices` for these fields.

## Actors
Listener (indirect). Radioly services. Platform Nexus.

## Journey
1. A request needs segment or create-time style fields.
2. Radioly asks Nexus (with per-request caching when available).
3. Downstream logic (feed ranking, ads eligibility, plans) uses those fields.

## User-Visible Invariants
- Wrong segment defaults can change paywall/ads intensity.
- Missing create-time can break age-based eligibility.

## Security / PII / Compliance
Non-PII by design. Do not route email/phone/name through Nexus.

## Gaps
- Rollout percentage and shadow-read status are live ops — verify flags in source.
