# PPV LDAU and Propagation

Aliases: ppv ldau sync, propagation prioritization, writer payout ranking

Product context: `airflow/pfm-kb/modules/ppv-ldau-propagation.md`

## What it is
LDAU sync and propagation prioritization that affect PPV/writer ranking and payout-related ordering.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| LDAU sync workflows | `temporal/` / `ppv_validation/` |
| Propagation prioritization | `ppv_validation/` |

## Risks
- Inventing payout amounts or live ranking formulas.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "PPV LDAU and Propagation" --graph $GRAPH
```
