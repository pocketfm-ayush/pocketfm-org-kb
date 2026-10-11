# Search Index Jobs

Aliases: hashtag es index, top search results job

Product context: `airflow/pfm-kb/modules/search-index-jobs.md`

## What it is
Keeps search hashtag indices and top-search helpers fresh (alerts may page search quality).

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `EsIndexHashtagWorkflow` | temporal/content or search/ |
| `search/` | domain |

## Risks
- Changing Radioly/pocket_search query logic here.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Search Index Jobs" --graph $GRAPH
```
