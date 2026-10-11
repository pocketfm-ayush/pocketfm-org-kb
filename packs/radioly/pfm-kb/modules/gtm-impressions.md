# GTM impressions (publish)

Aliases: impression publish, GTM frequency events

## What It Is
Radioly publishes impression events when promotional/GTM surfaces are shown so
platform impression counts can drive frequency caps later.

## Actors
Listener (sees the surface). Radioly publishers. Fabric impression store.

## Journey
1. A GTM/promo surface is shown.
2. Radioly publishes an impression event.
3. Later eligibility checks read aggregated counts (via Fabric clients).

## User-Visible Invariants
- Over-publishing or under-publishing skews how often promos reappear.

## Gaps
- Cap thresholds live in callers — verify per surface; do not invent numbers.
