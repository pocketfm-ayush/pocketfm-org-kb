# Open points — agent harness (from deepagents / awesome-agent-skills / codex-skills)

Track these so the harness does not lose failure modes.

## Evidence & completeness
- [ ] Success from one tool/layer
- [ ] Truncated MCP/tool output treated as complete
- [ ] Rubric criteria silently dropped on later passes
- [ ] “Done” when last AI prose looks good but verifier FAILED

## Stale / conflicting knowledge
- [ ] AGENTS.md/KB contradicts tools — agent obeys memory
- [ ] Skill metadata loaded but full body never read
- [ ] Wrong pack overlay (name collision last-wins)

## Planning / loop
- [ ] Tasks without validation commands
- [ ] Plan critique skipped
- [ ] Implement without PLAN_CRITIQUE PASS
- [ ] Todos left pending without reason

## Tool / env
- [ ] VPN/SSO/Safari preflight skipped (monitoring-mcp)
- [ ] Wrong env (pilot vs main, QA vs prod)
- [ ] Writes without MCP_ALLOW_WRITES / HITL

## Groot / KB specific
- [ ] Invented pack names / tables / metrics
- [ ] Deploy claimed from CodePipeline alone
- [x] Tests claimed without exit codes → fixed: sandbox pytest gate before draft PR + `run_repo_tests`
- [ ] No durable log of what was checked
- [x] Draft PR without running co-located module tests (radioly #32947 / diff-cover) → discover + gate

## Process
On every multi-step task: `harness-loop` + per-stage gate + `harness-response-recheck`.
Spawn `role-adversary` when confidence is not high.
