# Event Enrichment Dependencies

## What It Is
Server-side enrichment so ads/CRM events carry higher-quality user and purchase context.

## Actors
IAM identity, Nexus profile, Payments value, IP geo services; exporters.

## Security / PII / Compliance
Enrichment touches identity and profile fields — minimize and hash as provider requires.

## Gaps
Per-provider dependency matrix is bootstrap config — verify mode before assuming a client exists.
