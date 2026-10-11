# App-open ads

Aliases: app-open interstitial, launch interstitial, app-open ad,
app-launch ad, full-screen open ad

## What It Is

A **full-screen network ad** at cold launch or when the listener
returns from background. One product, two setups the server may attach
on launch config.

This is **not** a launch overlay (popup / nudge / slider), not a
mid-roll, and not watch-to-unlock.

## Actors

Listener opening or returning to the app. The server owns eligibility,
which setup is attached, and how many are left today.

## Journey

1. Launch (or return-from-background) asks for ads config.
2. Server may attach a launch interstitial, a return interstitial, both,
   or neither.
3. On iOS, if the return interstitial is attached, the launch one is
   removed — they do not both show.
4. The app shows the ad only after the background-time and gap rules
   pass, and not on top of a mid-roll.
5. A play report spends the daily cap. Config without a play is not a
   view.

## User-Visible Invariants

- Empty config is success (no interstitial), not an error.
- Do not build this from the overlay picker, and do not treat an
  overlay miss as “show an ad instead.”
- Tablets, TV, and car: no.
- Newer accounts and higher-spend listeners generally do not see this.
  Exact age / spend / market gates are live state.
- Some free-app tests hide **all** ads, including this.
- A daily cap exists. Hitting it is “no interstitial,” not a retry.
- Return-from-background needs a real background gap and a quiet
  window after the last interstitial. Do not invent the timings.
- Ad-free does **not** automatically mean this is off — do not assume
  that unless the live test says so.

## Client Behavior

Needs network for the config. A show without a play report can appear
again the same day. Closing the ad does not unlock, credit coins, or
ack an overlay.

## Event Meaning

The play report is the cap event. “Eligible / attached” is not a view.
A failed impression read must not show the ad.

## Product Source Of Truth

Server. The app does not choose launch vs return.

## Gaps

- Which setup is live, daily cap, background gap, and market gates.
- Whether ad-free or a no-ad pack turns this off.
