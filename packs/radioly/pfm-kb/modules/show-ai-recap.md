# Show AI recap

Aliases: daily recap, saga so far, show recap, AI recap

## What It Is

A skippable audio recap before the next episode — either yesterday’s
episode or a multi-episode “saga so far.” The listener is in **one**
of those two, not both.

This is not the per-episode recap card (episode-recap).

## Actors

Listener already in the recap test, on an allowlisted title, not brand
new on the device, and they have already listened to an allowlisted title.

## Journey

1. Player asks for a recap for this episode.
2. Server finds the latest earlier episode they finished far enough.
   If that is older than two episodes back, use two-back.
3. Daily recap: last listen was about a day ago (roughly 12–48 hours).
   Saga: last listen was more than 48 hours ago **and** they have at
   least six episodes in. Otherwise saga falls back to a daily recap.
4. Skip three times in a row → hide recaps for 7 days.
5. Replay is offered for 24 hours.

## User-Visible Invariants

- No recap if they have not listened recently enough, or the recap
  audio is missing.
- Copy is “Episode N Recap” or “Episodes X–Y Recap” (saga window is
  up to 10 episodes ending at the target).
- Skip and complete are separate analytics events.

## Client Behavior

Needs network. Skip must not play the recap. A missing recap is not an
error sheet — continue into the episode.

## Gaps

Which titles are allowlisted now, and which platform/locale split is
live, are not recorded here.
