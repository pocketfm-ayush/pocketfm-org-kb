# Temporal Namespace Config

Aliases: temporal-namespaces YAML, namespace-manager

Product context: `fabric/pfm-kb/modules/temporal-namespaces.md`

## What it is
Declarative Temporal namespace configuration (prod FM/comics/media/genai + QA) synced by CI — ops/platform only, not a listener product module.

## Graph anchors
| `prod/*.yaml` | `temporal-namespaces/prod/` |
| `namespace-manager` | `temporal-namespaces/tools/namespace-manager` |
| `README` | `temporal-namespaces/README.md` |

## Risks
- Editing namespaces without owner_email / retention review.
- Treating this YAML as workflow business logic (workflows live in airflow/other services).

## Query
```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "Temporal Namespace Config" --graph $GRAPH
```
