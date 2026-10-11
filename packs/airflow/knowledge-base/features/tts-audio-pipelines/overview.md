# TTS Audio Pipelines

Aliases: pgc tts, ugc tts, failed chapters retrigger

Product context: `airflow/pfm-kb/modules/tts-audio-pipelines.md`

## What it is
TTS generation/stitching and failed-chapter retrigger so chapter audio becomes ready.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `genai/tts/` | domain |
| `TtsFailedChaptersRetriggerWorkflow` | temporal/genai |

## Risks
- Inventing which chapters failed without logs.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "TTS Audio Pipelines" --graph $GRAPH
```
