---
id: flow.impression-event-consume
type: flow
repository: impression
status: uncertain
evidence:
  - fabric@56264ee2c9fc7d8141e98cf5a3ef0c9fc25178d1:impression/server/consumer/consumer.go#ProcessEvent
---

`ImpressionConsumer.ProcessEvent` handles USER/DEVICE impression events,
updates Scylla counters, DLQs invalid events. Confirm overlap with kafka
`video_impressions` workers per surface.
