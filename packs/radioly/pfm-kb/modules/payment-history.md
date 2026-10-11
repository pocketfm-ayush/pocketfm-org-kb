# Payment history

Aliases: history, coins history, purchase history, transaction receipt,
free episode history

## What It Is

The **History** screen on wallet: Coins and Purchases. Receipts and a
separate free-episode grant list. Not the paywall and not the coin store.

## Actors

Logged-in listener. India and US on newer apps. Support via contact /
FAQ on the lists.

## Journey

1. App opens History. Ineligible listeners get a blank success, not an
   error.
2. Tabs: Coins (added / spent) and Purchases (success / pending / failed /
   refunded). Free-episode grants are a separate list, not a tab.
3. Tap a purchase → receipt. Pending can be refreshed; the server may
   refuse a rapid second refresh.
4. Incomplete checkouts that never reached pay are hidden.

## User-Visible Invariants

- Login required. You cannot open someone else’s receipt by guessing
   an order id.
- Ineligible (other markets / older apps) → empty, not “history is down.”
- “Placed” and “pending” both look pending. Cancelled looks failed.
  Only one refund label: refunded / refund issued.
- Created or abandoned sessions must not appear.

## Security / PII / Compliance

Account-scoped. Receipts are that login’s orders only.

## Client Behavior

Needs network and a login. History lives on the account, not only on
the device.

## Gaps

Exact refresh cool-off, pending-payment banner behavior, and whether
History will open outside India/US later are not recorded here.
