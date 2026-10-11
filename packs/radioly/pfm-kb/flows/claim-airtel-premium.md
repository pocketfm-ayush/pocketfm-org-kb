# Claim Airtel Premium

Participating modules: airtel-premium, otp-login, subscriptions.

## Journey

1. Airtel opens the Pocket FM claim page with an order.
2. Guest sees marketing only. They log in (otp-login) to claim.
3. Server accepts or returns the single ineligible state.
4. Success: they now have Premium (new or +90 days). Store billing
   on an existing pass is deferred for that window.
5. They download / open the app to use the pass (subscriptions).

## User-Visible Invariants

- This is not a My Store checkout and not Reward Club.
- One claim per login.
- “Not eligible” is not a paywall failure.

## Failure modes

- No login → no claim.
- Already claimed, dead order, or missing order → ineligible, not
  a second Premium.
