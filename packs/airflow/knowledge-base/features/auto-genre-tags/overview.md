# Auto Genre Tags

Aliases: auto genre tag automation

Product context: `airflow/pfm-kb/modules/auto-genre-tags.md`

## What it is
Auto-tags show genres for discovery/catalog freshness.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `genai/auto_genre_tags/` | domain |
| DAG | `dags/genai/auto_genre_tag_automation_dag.py` |

## Risks
- Overwriting CMS genres without product intent.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Auto Genre Tags" --graph $GRAPH
```
