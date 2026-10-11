# Open Discover

Participating modules: discover-tab, home-feed, library,
onboarding-show-pick, visibility-filters, ai-pgc-show-selection.

## Journey

1. Launch / Home asks which tab is first.
2. Discover default-land only on the first session today, and only
   if the primary-title rule hits — then daily + 7-day caps.
3. First week on a new or reinstalled device: force Home as first tab;
   Discover stays in the bar.
4. Opening Discover: personalized recs may own the top; else
   onboarding seeds, LiveOps, then a shared short may pin.
5. Same hide / pair rules as Home.

## User-Visible Invariants

- Default-land is not “Discover is on.” The tab can exist without
  being first.
- A share deep link that points at a hidden promo must not pin it.

## Failure modes

- Language not English/Hindi/German → reject, do not show Home
  rails in Discover.
- Personalized recs down → fall through to the editorial / cycle
  stack, do not blank the tab.
