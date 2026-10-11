<!-- Author a PRD in prd-format from a ticket, notes, or thread. -->
# Skill: Write PRD

**When:** User asks to write / draft / author a PRD from a Jira, notes, or chat.  
**Inputs:** Ticket or notes, optional pack.  
**Output:** One markdown document that matches `prd-format.skill.md`.

## Standard

You are drafting for Groot, not shipping a vision doc. The draft must be
analysable: atomic MUSTs, explicit unknowns, no invented architecture.

## Procedure

1. Emit `prd-format` headings in order.
2. Problem / Goal: only what the ticket or user stated. If the ticket is a
   one-liner, write that one-liner and add Open questions for evidence and
   measurable goal.
3. Current behavior: pack names only. If no pack, `unknown — say the repo`.
4. Required behavior: turn each requested change into one `MUST-*`. If the
   user said "improve X" without an observable, write a MUST that restates
   their words and an Open question for the acceptance test.
5. API / ranking / cache / dependencies: leave `unknown` unless the pack or
   the user named them.
6. Rollout and metrics: `unknown` unless the ticket has them. Do not invent
   experiment IDs or percentages.
7. End with Open questions for every `unknown` that would block `prd-analysis`.

## Ask at most once

If repo or Jira is missing and you cannot draft even a Problem line, ask for
that one thing. Do not ask a questionnaire.

## Forbidden

- Filling Current behavior from memory of Pocket FM.
- Inventing handler names, cache keys, or v2/v3 paths.
- Skipping Open questions so the draft looks finished.
- JSON analysis output (that is `prd-analysis`).
- Code or evals.
