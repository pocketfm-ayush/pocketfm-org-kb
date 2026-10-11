# PPV Validation Pipeline

Aliases: ppv validation, ppv recover, ppv batch queue

Product context: `airflow/pfm-kb/modules/ppv-validation-pipeline.md`

## What it is
Daily validation that keeps PPV shows correctly live/paused and refills the validation batch queue.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `PPVValidationWorkflow` | `temporal/` / `ppv_validation/` |
| `PPVValidationExecutor` | `ppv_validation/executor.py` |

## Risks
- Inventing which shows are live without reading validation status.
Confusing catalog PPV test with listener PPV pass.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "PPV Validation Pipeline" --graph $GRAPH
```
