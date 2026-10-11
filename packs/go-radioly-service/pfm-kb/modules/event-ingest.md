# Event Ingest

## What It Is
Accepts event batches from clients, allowlists them, and places them on the relay bus.

## Actors
Apps posting batches; Relay gateway workers.

## Client Behavior
Clients post batches and move on. Retries are for transport failures, not for reading per-event DLQ from HTTP status alone.

## User-Visible Invariants
Batch success does not guarantee every event exported to ad platforms.

## Event Meaning
Ingest marks the moment Relay accepted an event for routing/export — not that CRM/attribution already updated.

## Gaps
Exact allowlisted event catalog is DB-driven; do not invent names here.
