# Impression Python Client

Aliases: impression/clientpy, impression_client

Product context: `fabric/pfm-kb/modules/impression-python-client.md`

## What it is
Python library mirroring the Go client for Scylla-backed impression queries (Airflow/Django-style callers).

## Graph anchors
| `ImpressionClient` | `impression/clientpy/src/impression_client/client.py` |
| `ImpressionRepository` | `impression/clientpy/src/impression_client/repository.py` |

## Risks
- Assuming PyPI package name without checking install path.
- Diverging query semantics from Go client.

## Query
```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "Impression Python Client" --graph $GRAPH
```
