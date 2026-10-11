# Impression Ingest Consumer

## What It Is
Write path that turns raw impression events into durable count buckets.

## Actors
Kafka producers (apps/Relay); impression consumer workers.

## Event Meaning
GTM/ADS device and user impressions mean a surface was shown; retries re-attempt failed writes.

## Gaps
Exact topic names and tenant routing are config — verify before claiming.
