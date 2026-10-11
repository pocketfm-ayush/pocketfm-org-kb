<!-- Default skill. Packs may override at <pack>/skills/explain-flow.skill.md -->
# Skill: Explain / debug a service flow

**When:** `@groot` asks how a service works, how to reduce/debug an endpoint, or what a
flow does. Not a PRD analysis. Not a live 5xx incident (that is Sherlock).

**Inputs:** pack `CONTRACT.md`, matching `features/*/overview.md`, matching
`<pack>/pfm-kb/` module/flow when present, `data/tables.md` for DB asks,
this skill, optional Sherlock note, codebase URL.

**Output:** Slack-readable walkthrough. Facts only from those inputs.
Skills are procedure — never invent architecture from this skill alone.

## Slack format (required)

Write for Slack mrkdwn — *short bullets a coworker will actually read*:

- Bold with *single* asterisks: `*Handler.build_response*`
- Never use `**double asterisks**` or `---` rules
- Shape: *Verdict* (1 line) → *Details* (3–7 `•` bullets) → *Flow* only if
  asked → *Questions* (0–3) → *Next step* (optional)
- *Flow*: numbered steps or `A → B → C` — never mermaid, never ASCII boxes,
  never markdown tables (`| a | b |`). Tables become `• *col* — value`
- Backticks for files, symbols, endpoints
- One idea per bullet. Blank line between sections
- Answer only what was asked — no pack catalogs, experiment dumps, checklists,
  tool dumps, model names, sandbox paths, or "Steps & commands"
- Target ≤15 short lines. Operator metadata only with `raw_metadata=true`

## Grounding

1. Resolve the service pack(s) for this ask (`radioly` vs `search` vs …).
2. Read **each attached** pack’s `CONTRACT.md` Current API / architecture map first.
3. Read the matching feature overview(s) and `pfm-kb` module/flow if attached.
4. For table asks, read that pack’s `data/tables.md` (+ catalogs) — never invent columns.
5. Use only names that appear in those files or in `# CODEBASE` for **that** repo.
6. If a name is not there, do not invent it. Say `unknown` and name the file to open.
7. Do not invent Java packages, Android services, `/v3/user/search`,
   `PocketSearchServer`, `MultiStepReducer`, or voice-search unless **this** pack says so.
8. Do not import symbols from another pack (feed code ≠ search code; kafka ≠ HTTP).
9. If `# MULTI-REPO CONTEXT` is attached, compare labeled sections and say which
   layer/repo owns the issue (or both / unclear). Do not ask “which service?”
   just to stall when evidence is already labeled.
10. If `# PRODUCT BUG CHECKLIST` is attached, walk experiments → DB/Redis (Argus
    after uid+device_id) → blast radius → deploy → curl → behaviour → different
    responses, plus multi-pod traps (stale Redis, schema drift, token races,
    retry storms, pagination, timezone, flag drift, N+1, deploy-order, swallowed
    partials). Ask for uid/device_id before DB claims; never invent rows.
11. If two packs could own the ask and multi-repo context is **not** attached,
    ask which service — do not blend answers.

## Screenshots / UI screens (when attached)

If the ask includes a screenshot, image URL, or screen description:

1. Use `# API TO SCREEN` / `architecture/api-to-screen.md` when present —
   map **screen → API path → feature** before inventing handlers.
2. Name the screen and primary path in *Verdict* / Details.
3. Never paste JWTs, uids, or full Confluence curls — paths + query keys only.
4. If the image is ambiguous across two surfaces, ask which tab/screen.

## Question the ask (required)

Do not accept the user's premise. Explicitly answer:

- What did they mean? (latency vs payload vs QPS cost vs result count)
- Is there evidence the problem exists? If Sherlock said no signal, say so.
- Which path? cache-hit vs cache-miss vs empty-query vs genre vs text
- What would break if we "reduce" the wrong step? (cache key, personalization order, v2/v3)

## Clarify before concluding (required)

Incomplete Slack asks are normal. Do **not** invent a finished answer when
critical context is missing.

1. If repo, env (prod/QA/canary), API/endpoint, uid/show, or symptom scope is
   still unclear after pack/CODE SEARCH/DESCRIBE/Sherlock — ask **1–3 sharp
   cross-questions** and stop.
2. Label guesses as **Assumption:** … and ask what would confirm them.
3. Prefer partial evidence + questions over a confident wrong RCA.
4. Do not ask filler questions for facts already in the thread or tool output.
5. When warehouse ids are already present, execute — do not stall on dates.

## Procedure

1. Entry: HTTP view / handler from the pack.
2. Routing: how the request is classified.
3. Cache: key contents, hit vs miss, what is stored.
4. Retrieval / filters / personalization *in pack order*.
5. Response shape.
6. If they asked to reduce/debug: list *candidate* levers from the pack, each with
   the risk. Mark any lever that needs a live metric as unverified.
7. Unknowns last — never fill them with a plausible architecture.

## Pack loading

Groot loads this skill from content-knowledge-base. Never ask the user to paste
or attach a pack.

- If `# KNOWLEDGE BASE` is attached, use it first.
- If `# REPO SOURCE` is attached, the hosted pack was missing — use those repo
  files the same way (names only from those files).
- If `# KNOWLEDGE BASE` says load failed, say that and stop. Do not invent.

## Forbidden

- Asking for a PRD, a repo link, or a knowledge pack
- A 6-bullet sketch that skips cache or personalization
- Treating "reduce X" as proof that X is slow
