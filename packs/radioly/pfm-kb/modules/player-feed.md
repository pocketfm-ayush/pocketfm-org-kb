# Player feed

Aliases: player feed, player rails, episode page feed, next series, new releases, new on pocketfm

## What It Is

Rails on the **player / episode page**, not Home: queue, must-listen,
rising, collections, mood, and “explore more.” The app asks the server.

Older and newer player-feed URLs are the same product. Do not treat them
as two players.

## Actors

Listener (guest or logged-in). A test can add an extra player-page stack.

## Journey

1. App opens the player.
2. Server builds player rails for this listener and title.
3. Same visibility and one-of-pair rules as Home.
4. Testers on the extra stack: first page is the main rails; later pages
   are “explore more.” Everyone else gets an empty extra stack — that is
   success, not a missing Home.

## User-Visible Invariants

- Player rails are not For You. Debugging Home will not explain a wrong
  player row.
- An empty extra stack for non-testers is expected.
- A title the listener must not see must not remain after assembly.
- Fetching one rail later is an empty row on miss, not a failed player.
- New Releases / Next Series uses the brand “Pocket FM” (two words). The one-word form “PocketFM” is the wrong title.
- The app shows the server’s title. Title-casing on the device does not own the brand wording, so the fix ships with the server, not an app release.

## Product Source Of Truth

The FM consumer service (Radioly) writes these rail titles. The catalog service and the Go relay are other products. They do not supply this rail’s name.

## Client Behavior

Needs network. Logout must not keep another person’s player rails.

## Gaps

Exact rail order and which extra-stack test is live are not recorded here.
