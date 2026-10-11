# Knowledge-base coverage inventory

Folder-level audit of packs under this repo. Regenerated from disk +
`global/catalog.yaml`. **Facts never merge across packs.**

**As of:** 2026-09-07 (FMF-4712 fill; FMF-4714 Holmes + pack-isolation skills)  
**Mean pack maturity:** product-pack layer Full for catalog packs (not file/function encyclopedia)

## Isolation (Groot)

- Default Slack ask → one primary pack/`repo_id`.
- Product (`pfm-kb/`) and code (`knowledge-base/`) twins stay **inside** that pack.
- Global skills (`monitoring-deploy`, `agents-repo-rules`, …) apply to all packs but
  must not invent cross-pack architecture.
- Same product words (feed, AI/PGC, playtime, shows) often mean **different modules**
  in radioly vs search vs kafka vs fabric — resolve pack before citing code.
- **Labeled multi-repo:** when the ask names 2+ services, or is client-vs-backend /
  cross-repo feature work, Groot may attach 2–3 packs with `# MULTI-REPO CONTEXT`.
  Claims stay labeled by `repo_id` — never blend symbols across sections.

## Role lens (Radioly ecosystem)

| Role | Pack | Maturity | features/ | pfm-kb | Notes |
|---|---|---|---|---|---|
| **Consumer** | `radioly` | Full | 100 | 100 mod + 23 flows | Domain twins |
| **Worker** | `kafka-stream-clients` | Full | 29 | 29 mod + 5 flows | Worker domain families |
| **Workflow** | `fabric` | Full | 12 | 12 mod + 3 flows | Impression + playtime + Temporal NS |
| **Workflow** | `airflow` | Full | 52 | 52 mod + 8 flows | Family twins |
| **Relay** | `go-radioly-service` | Full | 21 | 21 mod + 5 flows | Modes + providers |
| **Catalog** | `content-backend` | Full | 19 | 19 mod + 5 flows | APIs + domain features |
| **Lite FM** | `litefm-backend` | Bootstrap | 0 | stub index | Separate from radioly |
| **Android** | `android-client` | Full | 28 | 28 mod + 6 flows | Aural app-shell |
| **iOS** | `ios-client` | Full | 35 | 35 mod + 6 flows | Presentation features |

## Pack folder matrix

| Pack | onboarded | features | data/ | pfm-kb modules | pfm-kb flows | slug-map | Rich architecture | Maturity |
|---|---|---|---|---|---|---|---|---|
| search | yes | 12 | yes | 12 | 2 | yes | yes | Full |
| radioly | yes | 100 | yes | 100 | 23 | yes | yes | Full |
| fabric | yes | 12 | yes | 12 | 3 | yes | yes | Full |
| go-radioly-service | yes | 21 | yes | 21 | 5 | yes | yes | Full |
| content-backend | yes | 19 | yes | 19 | 5 | yes | yes | Full |
| litefm-backend | yes | 0 | no | stub | 0 | no | stub | Bootstrap |
| airflow | yes | 52 | yes | 52 | 8 | yes | yes | Full |
| kafka-stream-clients | yes | 29 | yes | 29 | 5 | yes | yes | Full |
| ios-client | yes | 35 | yes | 35 | 6 | yes | yes | Full |
| android-client | yes | 28 | yes | 28 | 6 | yes | yes | Full |

## Remaining gaps (honest)

- Domain depth still expands from source + graph (not every file/symbol/DAG).
- Fabric `consumer-playtime` core ingest may still be incomplete — verify before claiming.
- content-backend ↔ Radioly cutover matrix is still incomplete.
- Client packs are **app-shell** product KB, not a mirror of every Radioly module.
- Relay vs kafka S2S ownership must be confirmed per event in source.
- kafka-stream-clients twins are **worker families**, not one overview per K8s replica line.

## Totals

| Metric | Count |
|---|---|
| Catalog packs | 9 |
| Packs with `pfm-kb` | 9 |
| Feature overviews | ~308 |
| `pfm-kb` modules | ~308 |
| `pfm-kb` flows | ~63 |
