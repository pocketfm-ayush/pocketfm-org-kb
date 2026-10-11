# User Attribution Capture

## What It Is
Persists browser/app attribution identifiers so later server-side ads events can still attribute correctly.

## Actors
Clients on login/attribution capture; Meta exporter readers.

## Journey
Client stores attribution → later purchase/registration export may resolve missing cookies from store.

## Security / PII / Compliance
Attribution ids are marketing identifiers; treat as sensitive linkage data.

## Gaps
Durable fallback on store outage is incomplete in source.
