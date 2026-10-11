# App Shell and Navigation

## What It Is
App chrome and route-based navigation that hosts all Pocket FM iOS screens.

## Actors
Listeners; app bootstrap.

## Journey
Launch → landing/auth gates → tab/route stack for features.

## Client Behavior
Navigation is path-array driven; back stack is AppState-owned.

## Gaps
Exact tab composition may vary by experiment/config.
