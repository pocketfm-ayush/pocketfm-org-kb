# User survey

Aliases: NPS, in-app survey, player minimise survey

## What It Is

A short in-app feedback survey. Typical trigger: they minimise the
player. One survey at a time; a newer form replaces the older one on
newer apps.

## Actors

Logged-in listener who is at least a day old, on a supported app, with
impressions left.

## Journey

1. Eligible minimise (or other trigger) shows the survey.
2. Questions: pick one, pick many, free text, or rate several aspects
   at once.
3. High aspect ratings can skip the follow-up for that aspect. Skip
   list survives if they drop and come back.
4. If nothing is left to ask, it completes. Thank-you, then back to
   listening.

## User-Visible Invariants

- They see at most one of the two NPS forms.
- Resume must not re-ask skipped or already-answered questions.
- Question text lives in the survey catalog — do not invent it here.

## Client Behavior

Needs network and a login. Closing mid-survey should resume, not reset,
while they are still in the window.

## Security / PII / Compliance

Answers are feedback tied to the login. Do not invent retention or
sharing rules.

## Gaps

- Live question list and which trigger besides player minimise is used.
