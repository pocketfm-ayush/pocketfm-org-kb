# Knowledge layers — how Org Brain helps Pocket FM

## What `org-kb` (Org Brain) is

[`ayushgarg2702/org-kb`](https://github.com/ayushgarg2702/org-kb) is a **reusable
engine**, not company knowledge. It gives:

1. **Bootstrap** — scan configured repos → entities, relationships, evidence
2. **Connectors** — git, markdown docs, issues, observability, MCP
3. **Indexes** — lexical (Postgres FTS), symbols, optional vectors
4. **Query API** — intent → evidence → answer or abstain
5. **Mind map UI** — progressive exploration with source links
6. **Evaluation** — golden questions, faithfulness, freshness
7. **ACL** — query-time permissions; secrets never indexed
8. **Org instance split** — private config/memory stay out of the open engine

Pocket FM already has pieces of this story in three places. Org Brain is the
**framework** that makes them coherent end-to-end.

## What we already have

| Asset | Strength | Gap vs Org Brain |
|---|---|---|
| `content-knowledge-base` packs | Strong per-service CONTRACT, skills, pfm-kb, Graphify | Manual; no unified query API; no incremental publish versions |
| `org-handbook/` (inside CKB) | Evidence-pointer entities + LightRAG Lane A | Nested under packs repo; not a full org instance |
| `cerebro-knowledge` | Cross-repo distill + ontology + reconciliation | Separate lifecycle; not wired to Groot locate by default |
| Groot `locate` / Deep Agents | Runtime consumption | Depends on packs + optional LightRAG; no org-brain bootstrap |

## What this instance adds

`pocketfm-org-kb` is the **org control plane**:

- `org.yaml` — which repos are in the brain, waves, scopes
- `handbook/` — Lane A meaning SoT (can absorb / supersede CKB `org-handbook/`)
- `memory/` — incidents, ADRs, lessons (durable human knowledge)
- `evaluation/` — Pocket FM golden questions (not synthetic demo)
- `policies.yaml` + `connectors/` — who can read ops/schema/write
- `packs/manifest.yaml` — explicit link to Groot pack roots

## Helpful patterns to adopt from Org Brain

1. **Evidence-first claims** — already in handbook SCHEMA; enforce everywhere
2. **Knowledge versions** — publish incremental updates after merges/deploys
3. **Abstain when thin** — prefer `insufficient_evidence` over confident guess
4. **Connectors over scrape-everything** — git + docs + issues + Sherlock MCP
5. **Eval as gate** — golden questions before calling a domain “ready”
6. **Mind map** — progressive UI for onboarding / RCA exploration
7. **Instance ≠ engine** — keep secrets and indexes out of the open master

## What we should add to our KB (priority)

See [GAP_PLAN.md](./GAP_PLAN.md).
