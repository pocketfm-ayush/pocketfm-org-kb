# Continue Playing Candidates

## What It Is
Builds the Continue Playing candidate list from shared play/onboarding state.

## Actors
Home/experience services; listeners via BFF.

## Journey
Load onboarding + recent play snapshot → filter geo/removed → rank active then stale.

## Client Behavior
Apps display CP from BFF; this service supplies ranked candidates.

## Gaps
Upstream writers of playtime/onboarding state may live outside this repo.
