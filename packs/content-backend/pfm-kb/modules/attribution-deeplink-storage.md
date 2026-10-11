# AppsFlyer GCD Deeplink Storage

## What It Is
Temporary device-keyed deeplink attribution storage for AppsFlyer GCD flows.

## Actors
Attribution/install pipelines; experience callers.

## Journey
Write deeplink for device → later read/patch within freshness window.

## Security / PII / Compliance
Device-linked marketing identifiers — treat as sensitive.

## Gaps
Who writes vs who consumes across services must be confirmed.
