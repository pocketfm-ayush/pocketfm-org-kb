<!-- After tests — evidence required. -->
# Skill: Harness test recheck

**When:** After claiming tests/evals passed, or before opening a draft PR.

## Require

- Exact command(s) run (e.g. `python -m pytest v3/content/latam_modules/test_views.py -q`)
- Exit code / summary counts (`N passed` / failures)
- Failures addressed (no skip/xfail without approval)
- Correct suite:
  - Co-located `test_*.py` for the changed module (Radioly), **not** only a
    distant parent `tests/` folder chosen by impacted-tests heuristics
  - Pack `test_command` / `test_paths` when applicable
  - Diff-cover awareness: new production lines must execute (≥80% on Radioly CI)

`TEST_RECHECK: PASS | FAIL`.

Never mark PASS from Phantom enqueue, Slack prose, or “tests look fine”.
