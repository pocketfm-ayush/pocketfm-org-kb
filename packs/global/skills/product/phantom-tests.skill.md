<!-- Slack @groot "write tests" / Phantom. Not eval-writer. -->
# Skill: Tests and Phantom

**When:** User asks to write tests, unit tests, BDD, or to call Phantom on a
branch / PR — or the implement pipeline reaches the **tester** role.  
**Inputs:** Repo id, PR or branch, pack `test_command` / `test_paths`, this skill.  
**Output:** Pytest evidence (required) and optionally a Phantom job. No production-only edits without tests.

## Two different test jobs

| Job | Skill | Who |
|---|---|---|
| Acceptance contract from an approved PRD | `eval-writer` | `/groot` evals stage → later encoded as tests in `implementation` |
| Tests on an existing branch or PR / sandbox edits | this skill | `@groot` tester + **sandbox pytest** (+ optional Phantom) |

If they have a PRD and no branch, do not call Phantom. Point them at evals.
If they have a PR/branch and no PRD, this skill applies.

## Hard gate (Groot)

Before claiming `TEST: PASSED` or allowing a draft PR:

1. Discover targets: co-located `test_*.py` next to changed modules **first**,
   then nearest `tests/` dir. Radioly modules like
   `v3/content/latam_modules/` use `test_views.py` beside `views.py` —
   parent `v3/content/tests` alone is **wrong** and will fail diff-cover.
2. Run `python -m pytest <targets> -q --tb=short` on the sandbox edits.
3. Record command + exit code (`harness-test-recheck`). No invented passes.
4. Radioly CI also requires ≥80% diff-cover on changed production files.

Phantom enqueue **does not** satisfy this gate.

## Phantom (optional extra writer)

Phantom is the GitHub-MCP coworker for generating additional tests. Groot may
still write/fix tests in the sandbox. Enqueue:

```
v=1, source=groot, kind=write_tests, repo_id, prompt, extra
```

Reachability: `PHANTOM_API_URL` `/v1/jobs`, else `PHANTOM_REDIS_URL` LPUSH
`PHANTOM_QUEUE`. Socket Mode Slack Phantom is not an HTTP API Groot can scrape.

If Phantom is not configured, say so and still run sandbox pytest.

## What the job must contain

- `repo_id` from the onboarded pack
- PR URL or branch name (ask once if missing) when calling Phantom
- What to cover, in pack language (endpoints/handlers from CONTRACT only)
- `test_command` and `test_paths` from `contract.json`
- Fixture/stub rule from the pack (`mocking_rules`)
- Explicit paths of co-located tests to run

## Hard rules (pass through to Phantom + sandbox)

- Follow the pack's `test_command`, `test_paths`, and the runner already used
  under those paths (pytest, XCTest, Gradle, `go test`, unittest). Do not
  introduce a new runner.
- No live MySQL, Redis, Scylla, ES, Kafka, or HTTP in unit tests.
- `force_authenticate` does not work on Radioly — pack mocking_rules win.
- Do not weaken assertions, add skip/xfail, or lower coverage gates.
- Do not edit production code on a "write tests" ask unless the user also said implement.
- Allowed paths only. Never write knowledge-base, graphify, or env files.
- Cover new branches (validation errors, duplicates, cache invalidate, null defaults).

## Slack

Say which pytest command ran and the exit summary. If Phantom was also asked,
say so — but never imply Phantom alone validated the PR.

## Phantom repo itself

If the work is **inside Pocket-Fm/phantom** (toolsets, agents, workflows, runners),
follow **`phantom-pytest`** (`global/skills/phantom-pytest.skill.md`):

- `uv run pytest -q` before done
- Mirror `src/` under `tests/`
- Mock LLM + httpx; no live Argus/Jira/Slack
- Bug fixes need regression tests on the wiring path
