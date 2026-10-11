# Purchase to entitlement and attribution

## Journey
1. Payment succeeds on request path (Radioly/clients).
2. Wallet/recon/coins workers credit balances and heal mismatches.
3. Unlock/battle-pass workers materialize entitlements.
4. S2S workers fan payment events to AppsFlyer/Meta/Firebase/Google/MoEngage.

## Modules
- [wallet-coins-and-recon](../modules/wallet-coins-and-recon.md)
- [show-unlocks-and-battle-pass](../modules/show-unlocks-and-battle-pass.md)
- [subscription-lifecycle](../modules/subscription-lifecycle.md)
- [s2s-attribution-and-moengage](../modules/s2s-attribution-and-moengage.md)

## Failure modes
- Coin credit lag → unlock UI fails until refresh.
- S2S drop while wallet succeeded → ads under-report.
- Wrong owner (Relay vs these workers) delays the real fix.
