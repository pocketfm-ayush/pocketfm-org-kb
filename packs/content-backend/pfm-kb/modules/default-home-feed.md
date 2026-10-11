# Default Home Feed Shows

## What It Is
Catalog-backed default home show ranking for onboarding/home bootstrap callers.

## Actors
Experience/home services; new listeners.

## Journey
Caller sends audience headers → service loads configured onboarding feed → ranked shows.

## Client Behavior
Listeners see default modules via BFF, not this private route directly.

## Gaps
How CMS authors `onb_feed_v2_*` contents is outside this pack unless documented elsewhere.
