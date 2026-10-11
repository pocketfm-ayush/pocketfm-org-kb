# Launch config

Aliases: launch_config, fetch_config, refresh-config, cold start config

## What It Is
The bootstrap payload the app fetches on launch/refresh so it knows which
features, experiments, and promotional surfaces to enable before home settles.

## Actors
Listener (indirect). iOS/Android clients. Radioly feed/launch builders.

## Journey
1. App opens or resumes and requests launch config.
2. Server assembles platform-specific config (flags, experiment hooks, promos).
3. App applies config, then loads home and other surfaces.

## User-Visible Invariants
- Misconfigured launch payload can hide or over-show promos across the session.
- Config refresh may change behavior without reinstalling the app.

## Client Behavior
Needs network on cold start for full config; cached/last-known behavior is
client-specific — do not invent offline rules here.

## Gaps
- Exact flag catalog is large and changes often — verify in source for a named flag.

## Related bootstrap hooks

Launch may attach LiveOps splash/popup/bottom slider and Episode Zero
allocation ([liveops-tentpole](liveops-tentpole.md)), experiment bucketing
([experiments-allocation](experiments-allocation.md)), and promo hooks such as
Budget Booster ([budget-booster](budget-booster.md)).
