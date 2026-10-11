# Launch the app

Participating modules: onboarding-first-run, discover-tab,
daily-checkin, streaks, launch-overlays, app-open-ads, sleep-mode,
home-feed.

## Journey

1. If first-run screens are still due, that flow runs first
   (language / name / ATT). This flow does not replace it.
2. Server returns the tab bar and which tab is first.
3. Discover default-land only under discover-tab rules (first
   session today, primary-title / no heavy title, daily + 7-day
   caps). First week on a new or reinstalled device: tab can exist,
   first tab is forced Home.
4. Right after the genre picker, first tab can be Discover if that
   tab is in the bar. Right after interactive onboarding, first tab
   is Home. Those two beat other default-land tests.
5. Same launch chooses **check-in or listen streak**, not both.
   Enrollment is not redone mid-session. A later streak ask only
   reads that choice and the next-due countdown.
6. Same launch may attach overlays (popup, top nudge, tooltip,
   slider) — at most one per surface. Which campaign wins is a gap
   (launch-overlays).
7. Same launch may attach a full-screen **app-open / launch ad**
   (app-open-ads). That is not an overlay. Overlay miss must not
   invent an interstitial.
8. If they are in Unwind, launch can also flip “Unwind is on” so
   Home / profile / nudges may show it in the evening. The Unwind
   **catalog** is not time-gated.
9. Home rail assembly is open-home, after the first tab is chosen.
10. A later refresh can update Discover / profile / Unwind flags
    without serving a new overlay.

## User-Visible Invariants

- Default-land is not “Discover is on.”
- Check-in vs streak is a launch choice. Opening Home does not
  claim the day.
- Overlay ack is not overlay serving.
- Do not invent which LiveOps / writer / other default-tab test
  wins when the onboarding forces above do not apply.

## Failure modes

- Overlay picker miss → no popup / nudge / slider. Still launch.
  Do not invent a fallback campaign or an app-open ad.
- Check-in / streak miss → do not invent a track. Guest is not
  told to track streak.
- Refresh miss → keep last launch flags; do not drop the tab bar.
- First-run already finished → do not re-show language / ATT here.
