# Skill: AGENTS — Testing requirements

Groot engine: `pytest -q` for Groot itself; `kb_root`, `reset_settings`, mock httpx.
Target repos: sandbox `run_repo_tests` / pack `test_command` with **real exit evidence**.
Radioly: co-located `test_*.py` + ≥80% diff-cover on changed production files.
Phantom enqueue ≠ tests passed. Never claim pass without command + exit
(`harness-test-recheck`). Draft PR is blocked when sandbox tests fail or cannot run.
