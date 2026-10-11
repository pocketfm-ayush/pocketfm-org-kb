# Purchase communications

Aliases: purchase WhatsApp, transaction email, payment receipt message

## What It Is
Messages sent after a successful purchase (and related transactional emails).
Not the in-app notification center.

## Actors
Listener (inbox / WhatsApp). Payments success path. Comms vendors.

## Journey
1. Purchase succeeds.
2. Server enqueues email and/or locale-gated WhatsApp confirmation.
3. Listener receives receipt-style confirmation outside the app shell.

## User-Visible Invariants
- WhatsApp purchase success is market-gated (India path in source).
- Related: [checkout](checkout.md), [payment-history](payment-history.md),
  [notification-inbox](notification-inbox.md) (different channel).
