# Machine Translation Worker

Aliases: translation_worker, GPT/Google translate services

Product context: `kafka-stream-clients/pfm-kb/modules/machine-translation.md`

## What it is
Workers that translate content via configured MT providers for catalog/localization pipelines.

## Graph anchors
| `translation_worker` | `workers/machine_translation/` |

## Risks
- Sending PII through translation vendors unintentionally.
- Hard-coding provider keys.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Machine Translation Worker" --graph $GRAPH
```
