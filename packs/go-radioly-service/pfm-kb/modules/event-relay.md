# Event Relay Pipeline

## What It Is
Central clickstream and backend event pipeline for Pocket apps: ingest, route, enrich, and deliver to growth/analytics platforms.

## Actors
Mobile/web clients, backend publishers, growth/ops, platform APIs (TikTok, Meta, AppsFlyer, Firebase, MoEngage).

## Journey
Events enter via HTTP gateway or backend Kafka → optional router fan-out → exporter enrichment → platform S2S.

## User-Visible Invariants
Listener apps do not wait on platform delivery; growth systems may lag without failing the client ACK.

## Gaps
Which events stay in Relay vs kafka-stream-clients must be confirmed per event name.
