# Gap plan — what to add to Pocket FM KB

Prioritized against Org Brain capabilities and current CKB / Cerebro / Groot.

## P0 — control plane (this repo)

| Add | Why | Status |
|---|---|---|
| `org.yaml` source inventory | Single list of repos in the brain | seeded |
| `handbook/catalog.yaml` + SCHEMA | Lane A SoT outside nested CKB path | seeded |
| `memory/{incidents,decisions,lessons}` | Durable ops/product memory Org Brain expects | seeded (templates) |
| Pocket FM golden questions | Measure retrieval quality on real asks | seeded (starter set) |
| `packs/manifest.yaml` | Map org repos → Groot pack folders | seeded |
| Validate script | Block `ready` without evidence bar | seeded |

## P1 — content we should write / migrate

| Add | Where | Notes |
|---|---|---|
| Migrate `org-handbook/repositories/*` here | `handbook/repositories/` | Keep CKB as mirror or deprecate nested path |
| Service entity stubs for every catalog repo | `handbook/repositories/<id>/service/` | Prefer distill at fixed SHA |
| Cross-repo flows (unlock, ads, onboarding) | `handbook/` + cerebro peers | Label multi-repo; never blend symbols |
| Incident library (redacted) | `memory/incidents/` | From past RCA / `#tech-cs-issues` patterns |
| ADR memory | `memory/decisions/` | Infra onboarding, Scylla, KB layout |
| Deploy / ownership map | `handbook/` capabilities | Link Infra overlays without secrets |
| Missing packs from CKB coverage | content-knowledge-base | litefm depth; content↔radioly cutover; fabric playtime |

## P2 — engine wiring

| Add | Depends on |
|---|---|
| Run `org-brain bootstrap` against this instance | org-kb engine maturity |
| Connector `pfm.content_knowledge_base` | Import pack CONTRACT as evidence sources |
| Connector `pfm.cerebro` | Import merged relationships |
| Connector `pfm.sherlock` | Live ops (TTL cache only — not handbook) |
| Groot locate → org-brain query API | When API stable |
| LightRAG projection sync from `handbook/` | Same promote discipline as CKB |

## P3 — quality & ops

| Add | Why |
|---|---|
| Eval CI on golden questions | Catch regressions before merge |
| Freshness SLOs per wave (P0 weekly, P3 monthly) | Stale SHA evidence |
| Mind map UI for onboarding | Org Brain web stack |
| Permission profiles for Slack vs Cursor vs oncall | Already sketched in `policies.yaml` |

## Explicit non-additions (for now)

- Do not duplicate full `pfm-kb` modules here — keep product twins in CKB packs
- Do not store Graphify `graph.json` blobs here — regenerate from source
- Do not commit embeddings / Postgres dumps — `var/` is local only
- Do not invent metrics or ownership when evidence is missing
