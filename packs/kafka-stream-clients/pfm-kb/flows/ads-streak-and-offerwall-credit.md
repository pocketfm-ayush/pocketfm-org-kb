# Ads streak and offerwall credit

## Journey
1. Ad playtime / RV events arrive.
2. Streak retain and RV key workers update streak state.
3. Partner webhooks (Tapjoy/Digital Turbine) credit rewards.
4. PAM workers record revenue signals.

## Modules
- [ads-playtime-streaks-and-offerwall](../modules/ads-playtime-streaks-and-offerwall.md)
- [wallet-coins-and-recon](../modules/wallet-coins-and-recon.md)

## Failure modes
- Webhook replay double-credits without idempotency.
- Streak reset worker clears progress unexpectedly.
