# Stage tab

Aliases: Stage, UGC originals, originals tab, Studio tab label

## What It Is

A **separate tab** of free listener originals (and, for some people,
writer tools). Not For You. Not Home’s UGC-row (that **replaces**
Home in some locales).

## Actors

Listener (guest or logged-in) when the tab is on. Writers can see
Studio / continue-writing on the same tab. LiveOps / editorial fill
rails.

## Journey

1. App asks which tabs to show. Stage is experiment- and
   vintage-gated.
2. Some writer states rename Write to **Studio** and may default-land
   there. Studio is not a third tab.
3. Stage stack: rising / editor / contests / picks / genres. Newer
   apps can add continue-writing, contests, and writer spotlights.
4. A short “find your next binge” tour can show, then stop.

## User-Visible Invariants

- Do not assemble Stage from Home rails.
- Home UGC-row locales are still Home, not this tab.
- A Home “originals” rail (when present) is Home, not Stage.
- Disabled / hidden titles must not stay on a rail.

## Client Behavior

Needs network. Empty Stage is a quiet catalog, not a failed Home.
Logout must not keep another person’s writer stack.

## Gaps

Which locales / languages / vintages have the tab, and which Stage
stack is live, are not recorded here.

## Writer bridge

Writer achievements / profile-state may load via [ugc-backend-writer](ugc-backend-writer.md).
Studio is a Write-tab rename under Stage V2 — not a separate app package.
