---
name: architecture
description: Design or critique system shape — boundaries, data flow, failure modes, and trade-offs.
triggers: [architecture, system design, how should this be structured, boundaries, trade-offs]
intent: plan
priority: 88
---

# 03 · Architecture

**Job:** decide *where* logic lives and *how* pieces talk — not line-by-line code.

## Do
1. Draw current vs proposed flow (services, queues, stores, clients).
2. Name boundaries and ownership (who writes, who reads, who owns schema).
3. Call out failure modes, idempotency, consistency, and backpressure.
4. Prefer existing Pocket FM patterns over greenfield frameworks.
5. Record trade-offs discarded and why.

## Do not
- Jump to framework shopping before clarifying requirements.
- Propose new datastores without ops ownership clarity.
- Conflate with `api-design` (contracts) or `database-sql` (schema/query).

## Output
Context · Options (2–3) · Recommendation · Risks · Follow-on skills
