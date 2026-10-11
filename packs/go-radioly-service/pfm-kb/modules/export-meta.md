# Meta

## What It Is
Server-side Meta ads events with user/device enrichment for attribution quality.

## Actors
Meta exporter; IAM; Nexus; Payments; IP geo; user-attribution store.

## Security / PII / Compliance
Email/phone/gender/location-derived fields are sensitive; hashing and minimization matter.

## Event Meaning
Purchase and registration style events drive ads optimization; synthetic trial may accompany first purchase success.

## Gaps
Exact event whitelist and hashing rules live in provider + tests.
