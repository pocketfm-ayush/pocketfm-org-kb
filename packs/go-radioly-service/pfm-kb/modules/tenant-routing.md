# Tenant Routing

## What It Is
Routes accepted events to the right product tenant bus and may rewrite or fan out specialized signals for GTM/S2S.

## Actors
Router workers; downstream exporters; product analytics.

## Journey
Gateway topic → match tenant + handlers → publish to destination topics or drop unmatched.

## User-Visible Invariants
Unmatched events do not surface to listeners; growth may simply never see them.

## Gaps
Per-tenant destination topic map is config — verify in source/config before changing.
