# Banner ads

Aliases: display ads, image ads, thumbnail ad, player pause ad

## What It Is

Still images on a screen — player art, pause, home, library, and similar — not a mid-roll and not watch-to-unlock. Distinct from promo strips (banners).

## Actors

Listener. The server decides whether that screen gets a display ad and which creative.

## Journey

1. App asks for display setup, then for an image on a named placement.
2. Server applies eligibility and returns setup and/or a creative.
3. Nothing is written on the listener for a fetch.

## User-Visible Invariants

- Which placements are on is server-owned. Do not assume every screen has a banner.
- First week of account/device age: no. Newer accounts in GDPR locales (first 30 days): no, unless an enable-ads test already enrolled them.
- Subscribers: no (standard path).
- Disney titles and subscription-exclusive titles: no.
- Low-end devices: no.
- Ad-free usually no; a test can still show display ads to ad-free listeners — do not assume ad-free means a blank player chrome.
- Guests can still see display ads if the other gates pass.
- A first-party promo strip can ride with the player display ad. That is not a network fill.
- “No banner” is a successful empty setup, not an error.

## Client Behavior

Needs network. Fetch only — do not persist another listener’s display setup across logout.

## Gaps

Exact live placements per platform and app vintage are not recorded here.
