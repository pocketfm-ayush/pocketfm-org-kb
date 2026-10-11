# In-player ads

Aliases: mid-roll, instream, virtual voice ahead, disclaimer ad, boundary audio

Product context: `radioly/pfm-kb/modules/in-player-ads.md`

## What it is

First-party clip wins over network mid-roll. AI-voice warning and
explicit disclaimer still play for subscribers and ad-free.

## Graph anchors

| Symbol | Source |
|---|---|
| `audio_ad` | `v3/ads/ads_cms/viewsets.py` |
| instream ack | `v3/ads/services/instream_acknowledgement_api/` |

## Risks

- Playing network mid-roll on top of (or instead of) a first-party clip.
- Hiding Virtual Voice Ahead / disclaimer for subscribers.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "audio_ad" --graph $GRAPH
```
