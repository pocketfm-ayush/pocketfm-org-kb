# IAM identity

Aliases: IAM, device accounts, profile PII, phone OTP verify

## What It Is
Source of truth for **identity and PII**: profile fields, device upserts,
device↔user account mappings, phone verification, and related auth tokens.
Radioly should prefer IAM over direct MySQL `users`/`devices` for these paths.

## Actors
Listener. Auth flows. Radioly user/device APIs. IAM service.

## Journey
1. Login, profile edit, device bind, or account lookup needs identity data.
2. Radioly calls IAM endpoints (profile, devices, device accounts, OTP verify).
3. App continues with server-authenticated identity.

## User-Visible Invariants
- Device list / login limits depend on accurate device↔user mappings.
- Profile edits must round-trip through identity, not a stale MySQL-only path.

## Security / PII / Compliance
Email, phone, name, tokens — treat as sensitive; never log raw values.
Mutations (delete/deactivate/OTP) are high-risk account lifecycle paths.

## Gaps
- Full endpoint cutover matrix from MySQL is tracked in FMF-4712 — do not claim zero MySQL without metrics.
