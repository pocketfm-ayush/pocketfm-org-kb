# GTM Impression Routing

## What It Is
Turns specific in-app impression signals into GTM impression events for growth measurement.

## Actors
Router handlers; GTM/export consumers; feed/promo surfaces.

## Journey
Impression event matches surface rules → device or user GTM impression published.

## Client Behavior
Apps still send normal impressions; Relay decides which become GTM signals.

## Gaps
Exact module/view eligibility is code — verify handlers before changing product rules.
