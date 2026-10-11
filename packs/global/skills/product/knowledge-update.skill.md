<!-- Default skill. Packs may override at <pack>/skills/knowledge-update.skill.md -->
# Skill: Knowledge Update

**Stage:** green tests/checks → `READY_FOR_PR` → `refresh-mind`  
**Inputs:** accepted PRD, evals, applied diff, command results, old managed block, repo mind,
knowledge-base, graph/current source, repair reasoning if any  
**Output:** managed Markdown block; optional proposed learnings entry; human accept/discard

## Standard

Document implemented reality, not intended design. Update only facts proven by the applied
diff, current source, tests, and accepted PRD. Do not copy speculative PRD language into the
repo mind.

Use `CONTEXT_BUILDER.md`, but scope it to changed symbols and public/cross-feature behavior.
Graph evidence may identify affected callers; verify INFERRED edges in source before
documenting them.

## Entry gate

Do not propose an update unless:

- required tests and checks are green;
- final applied diff is available;
- implementation is inside allowed paths;
- the old managed block is well-formed with exactly one BEGIN/END marker pair.

If these conditions fail, return the existing block unchanged.

## Update procedure

1. Read the old block and preserve its useful structure.
2. Compare old claims to current source and tests for changed symbols.
3. Determine whether the diff changes durable contract:
   - endpoint, method, parameter, validation, default, response, error
   - routing or eligibility
   - ranking/filtering/personalization semantics or order
   - cache ownership, key/version, invalidation, hit/miss behavior
   - external dependency/fallback
   - compatibility or intentional divergence
   - new/retired core service
4. Update only affected statements. Remove claims made false by the change.
5. Preserve unchanged API rows and intentional divergences.
6. Use precise present tense. Name symbols and behavior; avoid implementation narration.
7. Do not include ticket history, rollout progress, test details, temporary flags, TODOs, or
   future proposals unless they are durable API behavior.
8. If feature knowledge also needs revision, do not edit it here; the managed block may link
   to its slug, and the orchestrator should create a separate reviewed knowledge update.

## Verification checklist

- Every new/changed claim has source or test evidence.
- Current endpoint paths and handlers are exact.
- Cache and personalization claims match both hit and miss paths.
- v2/v3 relationship is accurate.
- Known divergences are still true.
- No secrets, internal credentials, user data, unstable line numbers, or dates.
- No architecture/convention/DoD text outside the managed block is changed.

## Hard rules

- Output the complete managed block, including markers; a learnings entry, when warranted, is
  the only other permitted artifact and lives under `knowledge-base/notes/solutions/`.
- Never edit `contract.json` in this stage.
- Never broaden allowed paths or weaken Definition of Done.
- Do not claim an API was removed merely because it was absent from the diff.
- If public behavior is unchanged, return the old block byte-for-byte.
- Human acceptance is mandatory; this skill only proposes.

## Output shape

```markdown
<!-- BEGIN MANAGED: CURRENT_API -->
## Current API / behavior

### Endpoints

| Version | Path | Handler |
|---|---|---|
| ... | ... | ... |

### Routing
...

### Orchestration and invariants
...

### Core services
...

### Known intentional divergences
...
<!-- END MANAGED: CURRENT_API -->
```

## Compound the learning (return arrow)

The managed block records *what the API is now*. This step records *what was learned* so the
next PRD analysis, eval pass, and repair start smarter — the loop that makes each unit of work
easier than the last.

Propose a learnings entry **only** when the work produced a non-trivial, reusable insight:
a root cause that took real investigation (mine the repair `causal_chain`, `assumptions`, and
`failed_predictions`), a wrong assumption about a shared dependency, or a pattern future work
should follow. Skip trivial fixes, mechanical edits, and one-off incidents.

Follow `knowledge-base/notes/solutions/README.md`:

1. Pick the track — **bug** (Symptoms → What Didn't Work → Root Cause → Solution → Why This
   Works → Prevention) or **knowledge** (Context → Guidance → Why This Matters → When to
   Apply → Examples).
2. **Overlap check.** Search the store first. If an existing entry covers the same root cause
   or guidance (matching feature, symbols, problem), propose an *update* with fresher context
   and a bumped `last_updated` — do not create a near-duplicate that will drift.
3. **Grounding.** Every claim reads a current source line before assertion; cite PR over SHA;
   set `verified_against`. Unverifiable claim → drop it, do not soften it.
4. This is a *separate* proposed artifact from the managed block, and separately accepted by a
   human. Never write it silently, and never let it edit the managed block, `contract.json`,
   or protected paths.

Proposed entry:

```text
=== LEARNING: knowledge-base/notes/solutions/<category>/<slug>.md ===
<complete Markdown file with frontmatter, following the store README>
=== END LEARNING ===
```

If the work yielded no reusable learning, state `No learning to compound.` and emit only the
managed block.
