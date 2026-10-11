---
name: documentation
description: Write or update docs that match reality — README, architecture notes, runbooks, API notes.
triggers: [documentation, update README, write docs, runbook, explain for humans]
intent: document
priority: 75
---

# 10 · Documentation

**Job:** document what operators and future agents need. Prefer short truth over long fiction.

## Sub-skills
- README orientation → keep skim-friendly; link deeper docs
- Architecture → use `architecture` skill output as source
- API → use `api-design` / OpenAPI if present
- PRD → use `prd` / `prd-writer` / `prd-format`

## Do
1. Document current behavior, not aspirational.
2. Include commands that actually work in this repo.
3. Link to skills / AGENTS.md instead of duplicating policy.
4. Call out env vars and secrets by name (not values).

## Do not
- Paste huge generated dumps.
- Document dead flags or removed endpoints.

## Output
Audience · Doc type · Diff outline · Verification (someone can follow it)
