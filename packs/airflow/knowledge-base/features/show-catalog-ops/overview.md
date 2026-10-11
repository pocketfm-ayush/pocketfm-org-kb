# Show Catalog Ops Jobs

Aliases: shows/ badges, most listened, fast pass history, thumbnails

Product context: `airflow/pfm-kb/modules/show-catalog-ops.md`

## What it is
Show-domain helper jobs: badges, most-listened computations, FastPass history, thumbnail processing support.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `show_badges_service` | `shows/show_badges_service.py` |
| `most_listened_show` | `shows/most_listened_show.py` |
| `fast_pass_history` | `shows/fast_pass_history.py` |
| `thumbnail_processing_service` | `shows/thumbnail_processing_service.py` |

## Risks
- Editing show badges as if they were CMS source of truth.
- Confusing thumbnail processing here with content-backend image variant rules.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Show Catalog Ops Jobs" --graph $GRAPH
```
