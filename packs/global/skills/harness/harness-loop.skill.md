<!-- Meta harness — question everything; re-check every level before promotion. -->
# Skill: Harness loop

**When:** Any multi-step Groot/PFM task (PRD, implement, deploy, incident, research).
**Not for:** Bare greetings.

Borrowed from Deep Agents (plan→act→rubric), obra/superpowers verification-before-completion,
and Codex planner/plan-checker. **No stage advances without evidence.**

## Stages (must run in order; fail → re-enter)

| # | Stage | Role / skill | Exit gate |
|---|-------|--------------|-----------|
| 0 | Intake | `harness-intake` | Assumptions listed; blocking Qs asked or deferred |
| 1 | Research | `role-researcher` / `role-scout` | Claims have paths/URLs/tool output or INFERRED |
| 2 | Plan | `role-planner` | Atomic tasks + acceptance + validation commands |
| 3 | Critique | `harness-plan-critique` | Plan-checker + adversary OK or plan revised |
| 4 | Act | `role-implementer` / domain skill | Diff matches plan; allowed paths only |
| 5 | Verify | `role-verifier` + `harness-test-recheck` | Commands + exit codes recorded |
| 6 | Review | `role-reviewer` + `harness-review-recheck` | No open Blockers |
| 7 | Deploy-check | `harness-deploy-recheck` / `monitoring-deploy` | Every data plane OK/WARN/FAIL/SKIPPED |

## Every turn

Run **`harness-response-recheck`** on the draft answer before sending:

```
CLAIMS: …
EVIDENCE: … (tool/file/URL or INFERRED)
OPEN QUESTIONS: …
CONFIDENCE: high|medium|low
RECHECK: what could be wrong? what was not verified?
```

If confidence is low or OPEN QUESTIONS are blocking → do not claim done.

## Absolute rules

1. Question every assumption — if unsure, ask or mark ASSUMPTION.
2. Re-check after each stage using a **fresh pass** (do not reuse the same
   paragraph as proof).
3. Truncated / errored tools = failed evidence, not success.
4. Memory/AGENTS.md/KB lose to live tool output when they conflict.
5. Max one silent skip: none. Use SKIPPED(reason).

## Output when finishing a stage

`STAGE <n> <name>: PASS | FAIL | BLOCKED`  
`EVIDENCE: …`  
`NEXT: <stage or human gate>`
