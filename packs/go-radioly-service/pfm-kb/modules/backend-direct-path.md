# Backend Direct Export Path

## What It Is
Alternate intake where trusted backends write straight to export buses.

## Actors
Backend services; exporters.

## Journey
Backend → Kafka export topic → exporter → platform (no gateway HTTP, no router rewrite).

## User-Visible Invariants
Same exporter delivery semantics; different entry control plane.

## Gaps
Which backends own which topics must be confirmed in infra/config.
