# TikTok S2S Export

## What It Is
Server-side delivery of selected product events to TikTok for ads attribution.

## Actors
TikTok exporter workers; growth marketing.

## Client Behavior
Listeners never talk to TikTok from this path; delivery is server-side.

## Gaps
Whitelisted event set is config/code — verify whitelistmgr + provider.
