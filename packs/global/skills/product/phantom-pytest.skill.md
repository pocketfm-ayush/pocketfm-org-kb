<!-- Phantom repo (Pocket-Fm/phantom) pytest — write + validate. Not Groot's tests. -->
# Skill: Phantom pytest — write and validate tests

**When:** Adding or fixing tests in the **Phantom** Python repo (`src/` + `tests/`).
**Not for:** Groot engine tests, target-service repo tests (pocket_search, radioly, …) —
those use each pack's `test_command` via the `phantom-tests` routing skill.

## Phantom architecture (what you test)

```
src/core/          ReAct agent, LLM, tools, prompts, truncation
src/agents/        Agent configs + toolset lists (writing, execution, phantom_assistant)
src/workflows/     LangGraph graphs (analysis, execution)
src/runners/       CLI, FastAPI, Slack bot, Redis queue, runtime
src/plugins/       Jinja2 prompts + REST/MCP toolsets (argus, jira, confluence, …)
src/config/        Settings (PHANTOM_* env prefix)
```

Entry points: `phantom analyze`, `phantom serve`, `python -m src.runners.slack_bot`,
`runtime_poc/*.py` for live manual runs.

## Validate before finishing

From Phantom repo root (requires [uv](https://docs.astral.sh/uv/)):

```bash
uv sync --extra dev --group dev
uv run ruff check src tests
uv run pytest -q
uv run pytest --cov=src          # optional coverage
```

**Scoped runs** (after editing an area):

| Area | Command |
|------|---------|
| Input matrix (mandatory after matrix changes) | `uv run pytest tests/test_integration/test_input_matrix.py -v` |
| Phantom assistant / toolsets | `uv run pytest tests/test_integration/test_phantom_assistant.py -v` |
| One toolset | `uv run pytest tests/test_plugins/test_toolsets/test_<name>.py -v` |
| Core agent loop | `uv run pytest tests/test_core/test_base_agent.py -v` |

Do not mark work complete until `uv run pytest -q` passes.

## Test layout (mirror `src/`)

| Layer | Directory | Examples |
|-------|-----------|----------|
| Unit | `tests/test_unit/` | Slack handlers, Redis, budget, experiment confirm |
| Core | `tests/test_core/` | `ToolCallingAgent`, LLM, tools, truncation |
| Plugins | `tests/test_plugins/` | Toolset init, mocked HTTP, prompt render |
| Workflows | `tests/test_workflows/` | Graph wiring, guards, retry |
| Integration | `tests/test_integration/` | Agent loop + toolsets + prompt markers |
| Runners | `tests/test_runners/` | CLI, server |
| Config | `tests/test_config/` | Settings validation |
| E2E | `tests/test_e2e/` | Placeholder — no live E2E yet |

New module `src/foo/bar.py` → `tests/test_foo/test_bar.py` (or the matching layer dir).

## Environment isolation (mandatory)

`tests/conftest.py` autouse fixture `_clean_env`:
- Strips all `PHANTOM_*` env vars
- `chdir("/tmp")` so pydantic-settings never reads `.env`

In tests use:

```python
from src.config.settings import Settings, get_settings

s = Settings(_env_file=None)
s = get_settings(argus_base_url="https://argus.pocketfm.org", argus_token="sk-x")
```

Or the `env_factory` fixture with `monkeypatch`. Never rely on a developer `.env` during tests.

## Mocking rules

| Do mock | Do not |
|---------|--------|
| LLM (`MagicMock` → `AIMessage` with optional `tool_calls`) | Real Madeye / OpenAI / Bedrock |
| httpx on toolset client (`patch.object(tool._client, "get/post")`) | Live Argus, Jira, Confluence, Slack |
| `httpx.MockTransport` for REST toolsets | Real Redis (use `fakeredis` where needed) |
| Slack `WebClient` | Network in unit/integration tests |

Assert on **`StructuredToolResult`**: `.status` (`ToolResultStatus.SUCCESS` / `ERROR`), `.data`, `.error` — not ad-hoc dicts.

## Patterns by change type

### Toolset (REST — e.g. Argus, Jira)

Follow `src/plugins/toolsets/CLAUDE.md` checklist:

1. **Init** — tool names, `llm_instructions` contains expected KB names
2. **Instructions** — Jinja2 renders without missing vars
3. **Invocation** — mock HTTP, assert request body + `StructuredToolResult`
4. **Loader** — `load_toolset_by_name("argus", settings)` returns `None` when unconfigured

Argus example (`tests/test_integration/test_phantom_assistant.py`):

```python
with patch.object(tool._client, "post", return_value=_resp(200, fake)) as mock_post:
    r = tool._invoke({"question": "Q", "kbs": "pfm_product_flows"})
body = mock_post.call_args.kwargs["json"]
assert body["model"] == "claude-opus-4.7"
assert body["files"] == [{"type": "collection", "id": "d9eba661-..."}]
```

For **DB / table / schema** questions in prompts or tools, attach or reference
`fm_product_analytics` KB (same UUIDs as `KNOWN_KBS` in `argus_toolset.py`).

### Agent ReAct loop

Mock LLM returns tool calls → tools execute → results return → final answer.
Test `ToolCallingAgent.call()` path in `tests/test_core/test_base_agent.py` style —
not each component in isolation only.

### Prompt templates

Assert **marker strings** in rendered Jinja2 output (discipline phrases, tool names,
"Do NOT use Argus …"). Do not snapshot full LLM output or assert prose quality.

### Workflow / LangGraph

Test state transitions: node receives state X → produces state Y.
Use mocked agent nodes; assert status keys, errors list, metadata timing.

### Bug fix (regression — mandatory)

Per `CLAUDE.md` §Testing:

1. Test **fails without the fix**, passes with it
2. Cover the **wiring path** that broke (integration), not only the isolated function
3. Same commit as the fix

## Input matrix

`tests/test_integration/test_input_matrix.py` — parametrized over platform/combo cells.
**Run after any input-matrix or tc_generator prompt change.**

## Argus-specific tests

| File | Covers |
|------|--------|
| `test_phantom_assistant.py` → `TestArgusToolset` | init, KB UUID resolve, list_kbs slim, reason_with_kb `files` attach |
| `test_unit/test_experiment_lookup.py` | `ExperimentKB` with fake file cache |
| `test_unit/test_score_collision.py` | Pure collision math |
| `test_integration/test_experiment_analysis_render.py` | Argus markers in prompts |

Consult `docs/assistant/reference/argus_reference.md` before changing Argus behavior or tests.

## Anti-patterns

- Importing pytest without `uv sync --extra dev --group dev` (wrong Python env)
- Shared secrets / real `PHANTOM_*` tokens in tests
- Testing LLM-generated paragraph text
- Unit test only when the bug was integration wiring
- Second MCP construction path (use `create_mcp_toolsets_from_config` only)
- `@pytest.mark.skip` / xfail to green CI without user approval

## Related skills

- **`phantom-tests`** — Groot routes "write tests on branch/PR" to Phantom jobs (target repos)
- **`argus-kb`** — Argus Knowledge Collection names for KB-grounded reasoning

## References (Phantom repo)

- `CLAUDE.md` §Testing — hybrid approach, regression + integration mandates
- `TDD.md` §11 — test layer breakdown
- `src/plugins/toolsets/CLAUDE.md` — toolset test checklist
- `README.md` — `uv run pytest`, coverage
