# Rewarded ads

Aliases: rewarded video, watch-an-ad, watch to unlock, earn coins, rewards screen

## What It Is

The listener watches a video to get a reward. Two rewards, one product:

- **Watch-to-unlock** — from show page, player, or the lock sheet: finish a pack of ads, then a pack of episodes opens on that series.
- **Earn coins** — from rewards / store / home / earn-coins banner: coins, often behind a streak.

This is not the lock sheet (that is paywall) and not a mid-roll.
A brand-sponsored session sheet is sponsored-ads, not this pack.

## Actors

Listener (guest or logged-in). The server owns the offer, the pack size, the caps, and the credit.

## Journey

1. App asks for the current offer for a title and an entry point.
2. Server allows or refuses (install age, coin-economy market, title type, login, tests that strip ads).
3. Listener watches.
4. App reports that watch with a one-time proof.
5. Server credits coins, or — for watch-to-unlock — opens the episode pack only when that pack’s ads are done.
6. Caps, streak, and warning/success sheets come back on that same completion.

## User-Visible Invariants

- Watching is not credit. The completion report is.
- Watch-to-unlock does not pay coins. Earn-coins does not open episodes.
- No title on the request → no offer.
- Audiobooks, Disney titles, and subscription-exclusive titles never offer this.
- Listeners still in their first days after install generally do not see it.
- Only coin-economy listeners.
- Guests only from a short allow-list of entry points (store / masthead-style). Other guest taps must not invent an offer.
- Some subscription titles hide this. Some free-app tests hide **all** ads, including this.
- Buying ad-free does **not** hide this.
- Daily and hourly caps exist. Hitting them is “come back later,” not a silent empty player.
- The first pack of the day on a title can be smaller than later packs.
- Episodes opened this way are durable unlock (same meaning as show-open unlock — do not treat as a session cache).
- A new earn-coins / rewards-screen entry must be treated as a rewards-screen entry. If it is not, the listener watches and gets no streak, warning, or success sheet.
- After a rewarded watch, some listeners get a **premium slider**.
  That is not the launch bottom slider (launch-overlays).

## Client Behavior

Needs network for the offer and again for credit. A watch that never reports completion is no reward. Closing the lock sheet without finishing the pack leaves the episode locked.

## Event Meaning

The completion report is the credit event. Fetching an offer is not. A failed or never-started watch must not credit. The same proof reused must not double-credit (listener may still see a success-shaped sheet).

## Security / PII / Compliance

Credit requires a matching one-time proof. A bad proof is unauthorized — do not credit and retry as a soft miss.

## Gaps

Live daily/hourly caps per spend segment, which sale or offerwall is on, and coin amounts are not recorded here.
