# Airtel Premium claim

Aliases: Airtel free subscription, carrier Premium, Airtel promotion

## What It Is

A **carrier-granted** Pocket Premium window. Airtel starts an order;
the listener claims it on a Pocket FM web page. This is not a store
buy and not Reward Club.

The window is **90 days**. Lifetime: one successful claim per login.

## Actors

Listener (claim needs a login). Airtel creates and can cancel the
order. Unauthenticated visitors only see the marketing page.

## Journey

1. Airtel sends them to the Pocket FM claim page with that order.
2. Not logged in: marketing page (extra daily unlock time, ad-free,
   Premium FAQ). Claim is not offered yet.
3. Logged in and ineligible (already claimed, order not claimable,
   missing order): one “not eligible” state. Reasons are not listed
   on screen.
4. Logged in and eligible: they claim.
5. No pass yet → a new 90-day Premium. Already on a pass → that
   pass is extended 90 days and store billing is deferred for the
   window.
6. Success: Premium unlocked, end date, “download the app.”

## User-Visible Invariants

- One claim per login, ever. A second order on the same login is
  ineligible.
- Do not invent Premium prices. The page ships its own FAQ.
- Membership history for this pass shows **Expiry date**, not Next
  billing date.
- Ineligible and claim failure use the same envelope. Do not invent
  a distinct error per reason.
- Cancel of an unclaimed order is Airtel-side. The listener does
  not cancel from this page.

## Client Behavior

Needs network. Claim needs a login. Benefits are in the app, not
on the web page.

## Event Meaning

Claim success is “Premium started or extended,” not a paid
checkout.

## Product Source Of Truth

Server. The app must not mark them Premium from the page alone.

## Security / PII / Compliance

**Sensitive.** Carrier order, login, and claim outcome.

- Do not invent retention or what Airtel may store.
- Do not echo the order id in product copy beyond the page they
  landed on.

## Gaps

Whether the promo is live now, and which app vintages can use the
benefits in-app, are not recorded here.
