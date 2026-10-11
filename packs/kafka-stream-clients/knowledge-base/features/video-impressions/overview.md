# Video Impressions Worker

Aliases: video-impressions-worker, streaming video impressions

Product context: `kafka-stream-clients/pfm-kb/modules/video-impressions.md`

## What it is
Async worker that records video impression/play signals from streaming surfaces.

## Graph anchors
| `video_impressions` | `workers/streaming/video_impressions.py` |

## Risks
- Treating as Fabric GTM impression counts — different pipeline.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Video Impressions Worker" --graph $GRAPH
```
