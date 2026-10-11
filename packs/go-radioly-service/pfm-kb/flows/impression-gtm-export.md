# Impression to GTM export

## Journey
1. Client sends an impression through gateway ingest.
2. Router matches KT / player-feed sampling / show-promotion handlers.
3. Handler publishes GTM device or user impression events.
4. Downstream exporters/measurement consume those signals.

## Modules
- [event-ingest](../modules/event-ingest.md)
- [gtm-impression-routing](../modules/gtm-impression-routing.md)
- [tenant-routing](../modules/tenant-routing.md)
- [platform-export](../modules/platform-export.md)

## Failure modes
- Match rules miss → no GTM fan-out (silent for the listener).
- Header/identity resolution chooses device vs user incorrectly if ids missing.
