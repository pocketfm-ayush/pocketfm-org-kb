# Experiment Health Jobs

Aliases: experiment/ long-running reports, dealloc

Product context: `airflow/pfm-kb/modules/experiment-health-jobs.md`

## What it is
Experiment ops jobs that report long-running experiments and support deallocation/cleanup flows.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `report_long_running_exps` | `experiment/report_long_running_exps.py` |
| `dealloc_multi_show_process_experiment` | `experiment/dealloc_multi_show_process_experiment.py` |

## Risks
- Deallocating live experiments without product sign-off.
- Confusing with offline allocation writers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Experiment Health Jobs" --graph $GRAPH
```
