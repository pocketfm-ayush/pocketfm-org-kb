# New-user coin grant

Aliases: Germany coin reward, new user free coins, DE coin grant

## What It Is

A **one-time** coin grant for a new account (Germany campaign).
Not follow-for-coins. Not daily check-in.

## Actors

Logged-in listener. Server owns eligibility and the amount.

## Journey

1. App asks for the grant.
2. New account, never granted → coins land in the coin wallet.
3. Already an existing account, or already granted → success-shaped
   “not eligible” copy. No second credit.

## User-Visible Invariants

- Follow-for-coins is gone. Do not rebuild it as this.
- Amount is server-owned. Do not invent it.
- “Already registered” is not an error. Do not retry as a miss.

## Client Behavior

Needs network and a login. Closing the success copy does not
remove a real credit.

## Gaps

Whether the campaign is still promoted in-app (vs only the grant
path existing) is not recorded here.
