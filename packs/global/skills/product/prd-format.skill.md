<!-- Canonical PRD contract. Other PRD skills must emit or consume this shape. -->
# Skill: PRD format

**When:** Any stage that reads or writes a PRD.  
**Output:** Markdown in the sections below. No JSON. No code.

This is the only PRD shape Groot and the knowledge base accept as *normalized*.
Free-form Confluence / Google Docs / Slack dumps are raw input. Convert them with
`prd-normalize` before analysis. Author new ones with `prd-writer`.

## Required sections (in this order)

```markdown
# <Feature title>

## Problem
Who has what problem? What evidence shows it exists? Do not invent metrics.

## Goal
One measurable user or business outcome.

## Non-goals
Explicit exclusions. If none are known, write `unknown` — do not invent.

## Users and eligibility
Platforms, locales, app versions, auth state, cohorts, experiments.
Name only what the source states.

## Current behavior
What happens today, including defaults and fallbacks. Cite pack `CONTRACT.md`
or `features/*/overview.md` names when a pack is attached. If unknown, say so.

## Required behavior
- MUST-1: Atomic, observable requirement
- MUST-2: ...
- SHOULD-1: optional, still atomic

## User journeys
Happy path plus important alternatives. One journey per bullet.

## API / data contract
Inputs, validation, defaults, response fields, errors, ordering, compatibility.
Use pack endpoint/handler names only. Do not invent paths.

## Ranking / filtering / personalization
Rules, precedence, tie-breaking, exclusions, cache behavior. Keep this heading.
If the pack and PRD both say it does not apply, write `not_applicable: <reason>`.
Otherwise fill it or write `unknown`.

## External dependencies
Redis, ES, Scylla, MySQL, Kafka, S3, HTTP APIs; failure and timeout behavior.

## Rollout
Experiment, eligibility, kill switch, metrics, rollback.

## Acceptance metrics
Success target and guardrails. Numbers only if the source has them.

## Open questions
Unresolved decisions. Each item is a later P0/P1 question, not a guess.
```

## Rules

- Every `MUST-*` / `SHOULD-*` is one observable sentence. Split compounds.
- Never renumber an ID once emitted. Add `MUST-3`; do not reuse `MUST-1`.
- Missing section: keep the heading and write `unknown`. Do not drop headings.
  If a required section does not apply, keep the heading and write
  `not_applicable: <reason>`.
- Do not fill gaps with plausible product defaults.
- Slack mrkdwn if posting to Slack: `*bold*`, no `**`, no `---`.
- Knowledge-base names only from `# KNOWLEDGE BASE` / `# CODEBASE`. If a name
  is not there, write `unknown` and the file to open.
