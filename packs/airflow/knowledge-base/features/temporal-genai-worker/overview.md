# Temporal GenAI Worker

Aliases: genai temporal worker, tts temporal

Product context: `airflow/pfm-kb/modules/temporal-genai-worker.md`

## What it is
Temporal worker for GenAI schedules (e.g. TTS failed-chapter retrigger); many TTS crons may still be DAGs.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `temporal/genai/worker.py` | |

## Risks
- Assuming all TTS moved to Temporal.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Temporal GenAI Worker" --graph $GRAPH
```
