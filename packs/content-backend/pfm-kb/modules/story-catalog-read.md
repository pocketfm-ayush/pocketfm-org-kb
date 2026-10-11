# Story Catalog Read

## What It Is
Episode/story catalog for a show after product rules (release gates, branching, experiments).

## Actors
Show page / player callers; catalog domain features.

## Journey
Request stories → load approved set → apply domain features → return ordered list.

## User-Visible Invariants
Listeners may see fewer or reordered episodes based on FastPass, branching, or experiment caps.

## Gaps
Exact show allowlists for special rules live in code — do not invent here.
