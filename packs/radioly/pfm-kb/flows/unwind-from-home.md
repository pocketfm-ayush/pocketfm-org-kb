# Unwind from Home

Participating modules: sleep-mode, home-feed, launch-overlays.

## Journey

1. Listener is already in the Unwind test (iOS; US or India
   English). Hindi is rejected — not an empty English catalog.
2. Local evening (about 8pm–7am): Home feed can insert an Unwind
   banner (feed module, not the overlay picker). Profile can show
   Unwind. A top nudge or “you were in Unwind” relaunch popup can
   also fire in the same window — which of those wins versus other
   overlays is a gap.
3. Tap / Explore opens Unwind. The catalog itself is not
   time-gated.
4. Fixed stack: premier, four mood cards (classics, relaxing,
   history, calm your mind), popular, soundscapes, explore-all,
   quote.
5. Titles in this catalog are treated as free.
6. Close returns to Home.

## User-Visible Invariants

- Home banner ≠ launch top nudge ≠ relaunch popup ≠ Unwind
  catalog.
- Demo devices can bypass the clock. Everyone else must be in
  the evening window for Home / profile / nudges.
- Do not assemble Unwind from Home rails.

## Failure modes

- Not in test, or outside the evening window → omit banner /
  nudge / profile entry. Do not show a daytime Unwind strip.
- Wrong language → reject. Do not serve English Unwind as a
  fallback.
- Overlay picker gives a different campaign the top nudge → omit
  Unwind there; the Home banner can still show.
