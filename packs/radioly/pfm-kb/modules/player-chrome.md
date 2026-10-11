# Player chrome

Aliases: player config, playback speed, sleep timer, player tabs,
autoplay from playlist, reel player

## What It Is

Player **controls and layout**: speeds, sleep timer, tabs, comments,
autoplay-from-playlist, and reel / background-play rules. Not the
paywall and not the player rails.

## Actors

Listener on the player. Server decides what this vintage may show.

## Journey

1. App opens the player and asks for chrome.
2. Server returns speeds, sleep, tabs, and whether background play is
   allowed. Some reel titles restrict background play.
3. Auto-debit onboarding can appear here. CarPlay bits can appear on iOS.

## User-Visible Invariants

- The app must not invent tabs, speeds, or “background play is fine.”
- Restricting background play on a reel title is not a global player outage.
- Shorts / reels as a product are still a gap; this is only player chrome.

## Client Behavior

Needs network for the first chrome. Changing speed or sleep is local
after that.

## Gaps

Which tab set or speed list is live now is not recorded here.
