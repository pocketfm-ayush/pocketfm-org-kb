# AI↔PGC progress sync

## Journey
1. Playtime/progress events for mapped AI/PGC shows arrive.
2. AI-PGC sync consumer (sequential) updates paired progress stores.
3. Radioly selection/playback uses synced progress for handoff.

## Modules
- [ai-pgc-playtime-sync](../modules/ai-pgc-playtime-sync.md)
- [playtime-tracking](../modules/playtime-tracking.md)

## Failure modes
- Concurrent writers corrupt read-modify-write.
- Mapping missing → progress diverges across AI/PGC titles.
