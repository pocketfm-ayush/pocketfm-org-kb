# Coin-pack checkout

Aliases: checkout, billing, payment options, pay, web checkout

## What It Is

How a listener **pays** for a pack the shop or lock sheet already
offered. Not the shop. Not the lock sheet. Not “am I subscribed?”

## Actors

Logged-in listener. Store / billing gateway reports success, fail,
or refund. The app does not credit coins on its own.

## Journey

1. Listener has a plan the server already listed.
2. Some servings ask **how to pay**: site (default, may promise extra
   coins) or in-app. Both choices are always offered. Extra-coin
   percent is server-owned.
3. Server starts an order and returns the pay methods for this
   market (India: UPI / net banking / card; elsewhere: store billing
   first).
4. Listener pays. App asks the server to confirm.
5. Confirm credits the pack (coins, and sometimes a pass or no-ads
   days). Then a success chrome can show — not the lock-sheet
   “what you unlocked.”

## User-Visible Invariants

- Do not invent a plan, a price, or an extra-coin percent.
- Pay methods are market-owned. Do not show India methods everywhere.
- An order already paid fails visibly. A second confirm of the same
  pay can look like success but must not double-credit.
- A collision can show **refund started**. That is not a credit.
- Closing the how-to-pay sheet without paying leaves the balance
  unchanged.

## Client Behavior

Needs network and a login. A pay that never confirms is no credit.

## Event Meaning

Start-pay is not credit. Confirm is. Used for billing and analytics
— not for inventing the pack.

## Security / PII / Compliance

Account-scoped. Site checkout carries a short-lived login so they
do not sign in again. Treat as sensitive.

## Gaps

Live extra-coin percent, which gateway is preferred, and pending-pay
banner behavior are not recorded here.
