# Platform Export

## What It Is
Delivers enriched S2S events to growth/analytics platforms for attribution and CRM.

## Actors
Exporter workers; IAM/Nexus/Payments/IPAPI for enrichment; platform APIs.

## Journey
Consume tenant topic → whitelist/dedup/enrich → batch send → DLQ/drop on failure reasons.

## Security / PII / Compliance
Exports may hash or send PII-derived fields to Meta/AppsFlyer — treat as sensitive.

## Gaps
Allowlist ownership is DB/config; confirm before changing rules.
