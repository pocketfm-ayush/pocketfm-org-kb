# Listening progress persist

## Journey
1. Player emits playtime events.
2. Critical audio-playtime worker persists progress.
3. Continue Playing / progress gates read durable state.
4. Related cleanup workers may remove stale CP rows.

## Modules
- [listening-playtime](../modules/listening-playtime.md)
- [continue-playing-cleanup](../modules/continue-playing-cleanup.md)
- [kafka-workers](../modules/kafka-workers.md)

## Failure modes
- Critical pipeline lag → stale CP.
- Confusion with Fabric playtime modes.
