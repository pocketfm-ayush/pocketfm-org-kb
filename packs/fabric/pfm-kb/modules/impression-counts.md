# Impression Tracking

## What It Is
Platform source of aggregated view/interaction counts used for frequency capping and experimentation.

## Actors
Impression Kafka consumer; Go/Python query clients; Radioly and peers that cap surfaces.

## Journey
Client/Relay emits impression → Fabric consumer stores buckets → callers query counts by feature/asset/scope.

## Product Source Of Truth
Fabric Scylla impression tables via clients — not Radioly local counters.

## Gaps
Which Radioly surfaces call Fabric vs local logic must be confirmed per feature.
