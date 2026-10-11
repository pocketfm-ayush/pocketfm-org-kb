# Watch to unlock

Participating modules: rewarded-ads, show-details-and-unlock,
paywall.

## Journey

1. Listener hits a lock (show page, player, or lock sheet).
2. Server builds the sheet and, if allowed, a watch-to-unlock
   offer for that title and entry. The app does not choose the
   journey type.
3. They either watch the required ads, or pay (coins / pass) on
   the same lock family.
4. Watching is not credit. The app reports each finished watch
   with a one-time proof.
5. When that pack’s ads are done, the episode pack opens as
   durable unlock — same meaning as show-open unlock. No coins.
6. If they pay instead: after-pay is unlock confirmation, not a
   new price. Watch-to-unlock does not run.
7. Closing the sheet or abandoning the pack leaves the episode
   locked.

## User-Visible Invariants

- Watch-to-unlock does not pay coins. Earn-coins (rewards /
  store) does not open episodes.
- Ad-free does not hide this. Audiobooks, Disney, and
  subscription-exclusive titles never offer it. First-days-after
  install generally do not.
- Daily / hourly cap is “come back later,” not a silent empty
  player.
- The first pack of the day on a title can be smaller than later
  packs. Do not invent pack size or which ads they must finish.

## Failure modes

- Offer refused → no watch CTA. Fall through to paywall items
  the server already chose. Do not invent an offer.
- Bad or reused proof → no unlock. Do not retry as a soft miss.
- Unlock service dark → same durable-unlock fallback as
  open-show. Do not tell them “unlock is down.”
