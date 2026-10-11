# Paywall to unlock

## Journey
1. Listener hits paid gate.
2. Store / purchase funnel / premium options appear.
3. Payment succeeds; unlock applies; playback resumes.

## Modules
- [coin-store](../modules/coin-store.md)
- [purchase-and-unlock](../modules/purchase-and-unlock.md)
- [payments-and-premium](../modules/payments-and-premium.md)
- [premium-manage](../modules/premium-manage.md)

## Failure modes
- StoreKit success without backend wallet credit.
- WebView checkout abandoned mid-flow.
