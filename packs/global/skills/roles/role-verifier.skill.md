# Skill: Role — Verifier

**When:** Prove a claim (tests, deploy health, evals, confidence) before “done”.
**Borrowed from:** obra verification-before-completion; Deep Agents rubric freeze.

## Process

1. Freeze the checklist (rubric) on first pass.
2. For each criterion: gather **new** evidence (command, MCP tool, file read).
3. Incomplete grading → force revision (do not drop criteria).
4. Cap iterations; if exhausted → `VERIFY: FAILED` with unmet list.

## Typical rubrics

- Unit/integration: command + exit code (`run_repo_tests` / pytest)  
- Draft PR: sandbox pytest must PASS; reviewer must not be `REQUEST_CHANGES`  
- Radioly: co-located tests + diff-cover awareness  
- Deploy: `monitoring-deploy` layers  
- PRD/evals: id/requirement/expected coverage  
- Confidence: formula inputs present  

`VERIFY: PASSED | FAILED | NEEDS_REVISION`.
