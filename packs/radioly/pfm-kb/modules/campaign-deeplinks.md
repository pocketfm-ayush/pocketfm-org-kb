# Campaign deeplinks

Aliases: ad deeplink, install deeplink, open from campaign,
direct play from ad

## What It Is

A campaign / ad / install link that **resolves to a title or episode
and opens it playing**. This is not trailer-code, not a launch overlay
deeplink, and not a Discover share pin.

## Actors

Listener arriving from an ad or install. Campaign ops map the ad to a
show or episode. Only those two entity kinds resolve.

## Journey

1. App sends the campaign / ad identifier.
2. Hit: open that title or episode and start playback.
3. Miss: no destination — do not invent Home or a fallback title.
4. Show-open then applies hidden / pair / unavailable rules. Resolve
   does **not** strip those titles first.
5. A real show link skips the first-run **picker**. It does not skip
   language, name, or ATT.

## User-Visible Invariants

- Unknown or unmapped campaign id is a miss, not an outage.
- A hidden, campaign-only, or otherwise suppressed title can still
  resolve. The show page owns “unavailable,” not this resolver.
- Do not apply Home visibility filters at resolve time.
- Some mapped titles force a content language. Do not ignore that.
- Launch-overlay “open subscription” deeplinks are launch-overlays,
  not this product.

## Client Behavior

Needs network to resolve. A miss stays on the current screen / Home.
Direct-play failure should open the show (or unavailable), not retry
as a different title.

## Gaps

- Live ad-set → title map, and which install sources may land a link.
