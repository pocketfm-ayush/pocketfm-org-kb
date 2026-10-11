# Offline Experiment Allocations

Aliases: offline_experiment_allocations, mux/instream offline allocate

Product context: `airflow/pfm-kb/modules/offline-experiment-allocations.md`

## What it is
Batch allocation jobs that assign offline experiment cohorts (instream ads, caching, offerwall boosters, bigger thumbnails, etc.).

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `offline_experiment_allocation` | `offline_experiment_allocations/offline_experiment_allocation.py` |
| `instream_ads_mux_experiment` | `offline_experiment_allocations/` |

## Risks
- Hard-coding live allocation % in KB or clients.
- Assuming every experiment here is still Temporal- vs DAG-active without checking.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Offline Experiment Allocations" --graph $GRAPH
```
