# Repo Mind — kafka-stream-clients

Skills + orchestrator must obey this file and `contract.json`. Feature detail lives
in `features/` when present; the code graph lives in `../graphify/graphify-out/`.

**GitHub:** https://github.com/Pocket-Fm/kafka-stream-clients
**Stack:** Python · Kafka consumers

## Purpose

Load `kafka-stream-clients/pfm-kb/` for product meaning (start at `index.md`).

Kafka consumer workers: playtime, unlocks, wallet/recon, ads streaks/offerwall,
S2S attribution, experience, feeds packaging, account actions, comms, and more.

## Architecture map

| Layer | Location | Owns |
|---|---|---|
| workers | `workers/` | One module family per consumer domain |
| k8s entry | `workers-kafka-*.sh` | Replica lists — no underscore in worker names |
| utils | `utils/` | Shared helpers |

Query the graph before inventing structure:

```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "<question>" --graph $GRAPH
graphify explain "<symbol>" --graph $GRAPH
graphify path "<A>" "<B>" --graph $GRAPH
```

## Conventions

- New worker: add to the correct `workers-kafka-*.sh` as `worker-name,module.path,replica_count`.
- New packages go in docker-requirements.txt / requirements-docker.txt.
- CODEOWNERS: @Pocket-Fm/leads.

## Allowed vs protected paths

See `contract.json` → `allowed_edit_paths` / `protected_paths`.
Never write knowledge-base, graphify, env, or secret files.

## External systems & mocking

kafka (classic + MSK), mysql, redis, scylla/cassandra, s3, AppsFlyer/Meta/Firebase/Google/MoEngage, Tapjoy/Digital Turbine.
Workers must not open live Kafka/MySQL/Redis in unit tests.

## Commands

```bash
python3 -m unittest discover -s tests
python3 -c 'import yaml,sys; yaml.safe_load(open("config.yaml"))'
```

## Rebuild graph

```bash
graphify extract <local-clone> --code-only --out kafka-stream-clients/graphify
graphify cluster-only kafka-stream-clients/graphify --no-label
```

## Product context

Worker product meaning: `kafka-stream-clients/pfm-kb/` (start at `index.md`).
Code twins: `features/*/overview.md`.

## Coverage

Inventory: `knowledge-base/coverage.md` · folder map: `architecture/source-folder-map.md`.
~29 feature/`pfm-kb` twins (family coverage across worker domains).

## Gaps

- Family twins — not one overview per replica line in workers-kafka-*.sh.
- Verify worker ownership vs Relay exporters before changing S2S paths.
- Verify vs Fabric for playtime and vs Airflow for recon/account/referral batches.
