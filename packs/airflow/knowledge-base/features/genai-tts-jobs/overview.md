# GenAI TTS Jobs

Aliases: genai dags, tts crons

Product context: `airflow/pfm-kb/modules/genai-tts-jobs.md`

## What it is
Umbrella for GenAI/TTS scheduled work including auto-genre and comment analysis siblings.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `genai/` | domain |
| `temporal/genai/` | |

## Risks
- Assuming DAG vs Temporal without checking.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "GenAI TTS Jobs" --graph $GRAPH
```
