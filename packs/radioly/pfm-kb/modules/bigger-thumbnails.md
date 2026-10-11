# Bigger thumbnails

Aliases: bigger thumbnails, large home art, editorial BT

## What It Is

A **Home rail with larger art** for one promoted title. Editorial or a
campaign can pick it. Not the per-device cover stamp, and not the
retired ops dashboard.

## Actors

Listener on a new-enough phone. Editorial / campaign can assign the
title. Testers may see a stitch / cross-promo title here instead.

## Journey

1. Home is assembling rails.
2. If this listener is eligible, server picks one title for the large
   rail (campaign, then editorial, then the older test).
3. After enough looks without a listen, the rail cools down or swaps.

## User-Visible Invariants

- This is not “device-specific cover art.” That stamp can still run
  on other cards.
- Missing rail = not eligible or in cooldown — not a broken Home.
- The retired dashboard is not how art is chosen anymore.

## Client Behavior

Server-side. The app renders the large card it is given.

## Gaps

Impression cap, cooldown length, and which campaign is live are not
recorded here.
