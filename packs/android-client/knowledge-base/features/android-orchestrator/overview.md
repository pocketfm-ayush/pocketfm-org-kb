# Cross-Module Orchestrator

Aliases: DeductCoinOrchestrator, multi use-case sequences

Product context: `android-client/pfm-kb/modules/orchestrator.md`

## What it is
Cross-feature orchestration that sequences multiple use cases (e.g. coin deduct + unlock) without owning a single product screen.

## Graph anchors
| `orchestrator` | `aural/orchestrator/` |

## Risks
- Putting multi-step payment/unlock sequencing only in a UI ViewModel when orchestrator already owns it.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Cross-Module Orchestrator" --graph $GRAPH
```
