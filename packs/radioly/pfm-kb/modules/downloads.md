# Downloads

Aliases: download episode, listen offline, offline, bulk download,
save offline

## What It Is

Saving an episode **on this device** to play without network. Library
has a Downloads tab; the player has a download control. This is not
unlock, not the saved / subscribed list, and not a mid-roll skip.

## Actors

Listener. The server says whether this episode may be saved. The files
live on the device.

## Journey

1. Show page / player marks each episode downloadable or not.
2. Listener saves one episode or a bulk set (bulk can be off).
3. Offline play uses the device copy. Unlock and lock still follow
   the account.
4. While a subscription is active, eligible episodes may be saved.
   After it ends: already-listened copies can stay; unlistened ones
   lock and leave downloads.

## User-Visible Invariants

- Download is not unlock. A locked episode must not become playable
  because it was saved.
- Battle-pass / time-boxed “free with pass” episodes can be open in
  the player and still **not** downloadable. Do not treat “unlocked”
  as “saveable.”
- Missing bulk save is a test or title rule — not a broken download.
- Offline autoplay of the next unlistened episode is a playback
  setting, not a new download.
- Files do not follow the login to a new phone.

## Client Behavior

Needs network to learn eligibility. Already-saved play can work
offline. Logout does not delete another account’s unlock; it also
does not move these files to the next login.

## Gaps

- Whether a coin “paid download” charge still exists as its own
  product, vs a history label only.
- Live bulk-download tests and which titles disable bulk.
