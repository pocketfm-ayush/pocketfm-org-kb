# Onboarding first-run

Aliases: language screen, name screen, gender screen, ATT, notification
permission, first-run profile

## What It Is

The first-run screens **before or around** the title picker: name (and
often age), gender, language, notification permission, and on iOS
tracking / personalization (ATT).

The title picker itself is **onboarding-show-pick**. Trailer-code is a
separate “remember the code” prompt. Do not fold those into this
module.

## Actors

New listener. Screens hide when that fact is already on the account
(name+age, gender, language).

## Journey

1. Launch asks the server which screens to show and in what order.
2. Typical stack: name/age → gender → language → title picker →
   notification / ATT (iOS).
3. Variants (do not invent which is live): one combined info screen;
   language+gender on one screen; name/age dropped; extra genre/trope
   or trailer-grid screens inserted **before** the picker.

## User-Visible Invariants

- Language is hidden if they already have one.
- ATT / tracking sits with notifications and is iOS. Do not invent
  Android ATT.
- A real show deep link still skips the **picker** (see
  onboarding-show-pick); it does not automatically skip language or
  permissions.
- Server owns order and visibility. The app must not invent a stack.

## Client Behavior

Needs network for the screen list and language options. Answers persist
on the account so the same screen does not return every launch.

## Security / PII / Compliance

Name, age, gender, language, and tracking consent are profile /
device facts. Mark ATT as consent. Do not invent legal copy or what
tracking is used for.

## Gaps

- Which stack is live per market and app version.
- Whether Android shows a notification screen outside tests.
