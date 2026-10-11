# Show referral

Aliases: gift and earn, invite friends, series gift, referral code

## What It Is

Gift a **specific series** to a friend (Gift & Earn). Referrer shares a
code; referee enters it (Profile → Enter Referral Code). Rewards are
coins for progress on **that** gifted series, not the whole catalog.

**New invite codes and new redemptions are turned off.** Do not build
this as a live invite program unless product turns it back on. Existing
invite tracking may still load.

## Actors

Referrer (logged-in, typically Android, India or US). Referee (friend).
Web can hold a code before the app.

## Journey

1. Referrer opens Gift & Earn on a series and shares a code plus link.
2. Friend: web signup (India: phone; US: email) gets a short free
   listen; then install the app, log in with the **same** identity, and
   enter the code for a few days of free access to that series.
3. Profile → Gift & Earn → Track Your Invites shows who joined and
   progress.
4. Coins land after the friend hits listen or unlock milestones on the
   gifted series, inside a time window.

## User-Visible Invariants

- One code is tied to one series. The gifted series cannot change
  after the friend joins.
- Rewards only if the friend listens to / unlocks **that** series.
- Two reward shapes (experiment): listen-to-episode levels, or coin-back
  when the friend unlocks. Do not invent which is live or the amounts.
- Some variants gift only new listeners; others allow existing ones.
- This is not a generic “invite anyone for coins” program.

## Client Behavior

Needs network and a login to create or redeem. Gift & Earn entry and
explainer sheets are server-built. Closing a sheet without redeeming
leaves the friend ungifted.

## Security / PII / Compliance

Invite lists can show a friend’s name, phone, or email to the referrer.
Treat as PII. Do not invent sharing or retention rules.

## Gaps

- Whether leftover Gift & Earn UI should still show for old invites.
- FAQ “invite as many as you want” vs a hard cap in source.
- Live reward amounts and which variant is shipped.
