# Experiments allocation

Aliases: A/B tests, experiment bucketing, variants

## What It Is
How listeners are placed into experiment variants that change UX, feed, ads, or
monetization. Allocation is server-driven; clients usually receive outcomes via
launch config or feature payloads.

## Actors
Listener. Experiment owners. Radioly allocation code.

## Journey
1. Eligible request hits an experiment gate (often at launch or feature entry).
2. Server allocates or reuses a sticky variant.
3. Downstream surfaces render the variant experience.

## User-Visible Invariants
- Sticky variants should not flicker across a session without product intent.
- Guests vs logged-in users may allocate differently.

## Gaps
- **Do not store live percentages, winners, or ramp state in this KB.**
