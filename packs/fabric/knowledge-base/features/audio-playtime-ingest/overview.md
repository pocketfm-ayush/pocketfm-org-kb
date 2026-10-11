# Audio Playtime Ingest Mode

Aliases: consumer-playtime, audioplaytime package

Product context: `fabric/pfm-kb/modules/audio-playtime-ingest.md`

## What it is
Playtime mode intended for core audio playtime ingest. Current handler still treats topics as unknown — treat as incomplete until verified.

## Graph anchors
| `ModePlaytime` | `playtime/consumer/registry.go` |
| `audioplaytime.Service` | `playtime/audioplaytime/service.go` |

## Risks
- Shipping product assumptions that Fabric owns continue-listening writes.
- Ignoring kafka-stream-clients / Radioly as the live listening progress path.

## Query
```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "Audio Playtime Ingest Mode" --graph $GRAPH
```
