# Delivery Resilience

## What It Is
Protects accepted client events when the primary bus publish fails, using durable buffer + replay.

## Actors
Gateway publish path; fallback-replay workers; ops.

## Journey
Publish fail → buffer/upload → replay mode re-publishes onto Kafka.

## User-Visible Invariants
App already got success; platform visibility may be delayed until replay catches up.

## Gaps
User-attribution Scylla downtime fallback to Kafka is noted as TODO in source — do not assume it exists.
