# Notification inbox

Aliases: in-app notification center, notification feed

## What It Is
Server-backed notification content and dispatch that powers in-app notification
experiences and related push fan-out. Separate from the OS permission prompt.

## Actors
Listener. CRM/push pipelines. Radioly notification services.

## Journey
1. An event qualifies for a notification.
2. Server stores/dispatches according to channel rules and rate limits.
3. Listener sees it in-app and/or as a push.

## Client Behavior
Inbox UI may be client-owned; empty states and badges depend on fetch APIs.

## Gaps
- Exact inbox screen IA varies by client shell — confirm before screenshot claims.
