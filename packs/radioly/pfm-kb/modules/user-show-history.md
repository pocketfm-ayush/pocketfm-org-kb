# User show history

Aliases: show history, listening history, last listened shows

## What It Is
API that returns the listener’s recently listened shows for history / continue
surfaces. Distinct from full library subscriptions.

## Actors
Listener. History UI. Radioly history API.

## Journey
1. Client requests show history for the signed-in (or device) context.
2. Server reads recent play progress and enriches show cards.
3. Client renders a short recent list (default server cap is small — verify
   current `max_records` in source; do not invent a different number).

## User-Visible Invariants
- History is progress-based, not the same as “subscribed in library.”
- Related: [listening-progress](listening-progress.md), [library](library.md).

## Client Behavior
Needs network for authoritative history; offline may show a local subset only
if the client implements it.
