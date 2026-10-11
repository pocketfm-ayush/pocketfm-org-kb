# Interactive story

Aliases: choice story, tap to choose, branching story

## What It Is

A choose-your-path story, not a normal episode list. Home can show a
banner; tap starts or **resumes**. Ending is “to be continued,” with
Notify Me — not a finished catalog title.

## Actors

Logged-in listener in the test. Default gate: iOS, US, and they must
already have listened far into a designated title. Guests can start;
progress is saved on the login.

## Journey

1. Eligible Home (or deep link) shows the banner. Whole banner is
   tappable; no separate CTA.
2. Start resumes where they left off, or the first node.
3. Each choice is recorded; the next node is served.
4. Restart wipes the path and returns to the start.
5. Ending: hold copy plus notify. Some listeners get a tap-to-end
   treatment (experiment).

## User-Visible Invariants

- The next beat is server-owned. The app must not invent a branch.
- Hesitation tooltip: the app can auto-pick; they can cancel and
  choose. Undo exists when enabled.
- This is not onboarding show-pick and not story-evolution cards.

## Client Behavior

Needs network. Resume needs a login. Restart needs a login to stick.

## Gaps

- Which title and listen-depth product uses as the gate.
- Whether tap-to-end is shipped meaning or only a test.
