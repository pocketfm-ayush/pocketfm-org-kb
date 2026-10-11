# Repo Mind — airflow

Skills + orchestrator must obey this file and `contract.json`. Feature detail lives
in `features/` when present; the code graph lives in `../graphify/graphify-out/`.

**GitHub:** https://github.com/Pocket-Fm/airflow
**Stack:** Python · Apache Airflow DAGs

## Purpose

Load `airflow/pfm-kb/` for product meaning when present.

Pocket FM Airflow DAGs. prod syncs main (airflow.pocketfm.com); dev syncs develop.

## Architecture map

| Layer | Location | Owns |
|---|---|---|
| dags | `dags/` | Classic Airflow schedules |
| Temporal workers | `temporal/<domain>/` | Migrated durable jobs (content/ads/payments/experience/genai/platforms) |
| domain dirs | `ads/, experience/, payments/, feed/, …` | Job code owned per CODEOWNERS |
| common | `common/` | Shared utils including secrets_manager |

Query the graph before inventing structure:

```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "<question>" --graph $GRAPH
graphify explain "<symbol>" --graph $GRAPH
graphify path "<A>" "<B>" --graph $GRAPH
```

## Conventions

- Format with black before commit. PIP changes go in requirements.txt then Jenkins deploy.
- CODEOWNERS: default @Pocket-Fm/leads; ads/ ads-backend; payments/ monetization; several dirs platform.

## Allowed vs protected paths

See `contract.json` → `allowed_edit_paths` / `protected_paths`.
Never write knowledge-base, graphify, env, or secret files.

## External systems & mocking

airflow, mysql, redis, s3.
DAGs must fetch secrets via secret manager helpers, not hard-coded credentials.

## Commands

```bash
python3 -m compileall -q dags ads experience payments feed marketing_campaign experiment
black --check dags ads experience payments feed || true
```

## Rebuild graph

```bash
graphify extract <local-clone> --code-only --out airflow/graphify
graphify cluster-only airflow/graphify --no-label
```

## Product context

Scheduled-job product meaning: `airflow/pfm-kb/` (start at `index.md`).
Code twins: `features/*/overview.md`. Cover both `dags/` and `temporal/`.

## Gaps

- Confirm DAG vs Temporal runtime before editing (`dags/` vs `temporal/<domain>/`).
- Family twins cover product domains; not every DAG file has its own overview.
- Live cron expressions, experiment %, and coin amounts are not packed — read source.
- Ops-only trees (`redis_analysis`, `db_monitor_jobs`, `db_dumps`) have no pfm-kb twins.
- Folder coverage: `knowledge-base/coverage.md`.

