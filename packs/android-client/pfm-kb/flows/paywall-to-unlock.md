# Paywall to unlock

## Journey
1. Listener hits a paid gate on show/player.
2. Payment UI offers coins/subscription/autodebit options.
3. Orchestrator sequences deduct/unlock.
4. Content becomes playable.

## Modules
- [payments-and-premium](../modules/payments-and-premium.md)
- [autodebit](../modules/autodebit.md)
- [orchestrator](../modules/orchestrator.md)
- [player](../modules/player.md)

## Failure modes
- Gateway success without wallet credit ack.
- Double deduct if orchestration retried unsafely.
