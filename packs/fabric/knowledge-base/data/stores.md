# Fabric stores

| Store | Role |
|---|---|
| Scylla | Impression time-bucket counts; playtime / AI-PGC / exclusion state |
| MySQL | Opt-in for AI-PGC sync mode |
| Kafka | Impression and playtime event ingest |
| Temporal | Namespace config only in this repo (not business workflows) |

No invented table names — verify in service READMEs / CQL before SQL.
Playtime mode dependencies are opt-in (`ConfigForMode`).
