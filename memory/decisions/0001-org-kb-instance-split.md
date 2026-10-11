---
id: ADR-0001
date: 2026-10-11
status: accepted
---

# ADR-0001: Split Pocket FM org KB instance from Org Brain engine

## Context

Org Brain (`ayushgarg2702/org-kb`) is a reusable master. Pocket FM already has
`content-knowledge-base` (Groot packs + nested org-handbook) and
`cerebro-knowledge` (cross-repo semantics). Mixing org config, memory, and
indexes into the open engine or nesting Lane A under packs confuses ownership.

## Decision

Create `pocketfm-org-kb` as the organization-owned instance:

- `org.yaml` / policies / connectors
- `handbook/` as Lane A SoT
- `memory/` for incidents / ADRs / lessons
- `evaluation/` for Pocket FM golden questions
- `packs/manifest.yaml` to point at Groot packs without duplicating them

## Consequences

- Engine upgrades do not rewrite org memory
- Handbook can migrate out of CKB `org-handbook/` over time
- Groot continues to load packs from content-knowledge-base until locate is
  wired to the org-brain query API
