# S2S Mismatch Validation

Aliases: s2s_validation, mismatch detector

Product context: `airflow/pfm-kb/modules/s2s-mismatch-validation.md`

## What it is
Validation jobs that detect mismatches between expected and observed S2S attribution/event delivery.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `mismatch_detector` | `s2s_validation/mismatch_detector.py` |
| `s2s_events helpers` | `s2s_events/` |

## Risks
- Treating mismatch reports as proof a specific exporter is down without checking Relay/kafka workers.
- Inventing mismatch thresholds.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "S2S Mismatch Validation" --graph $GRAPH
```
