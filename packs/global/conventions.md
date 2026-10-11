# Groot conventions (all packs)

How Groot talks. Product truth lives in `<pack>/knowledge-base/`, not here.

## Skills vs pack facts

**Pack facts win over skills.** Load in this order for answers:

1. `<pack>/knowledge-base/CONTRACT.md`
2. Matching `features/*/overview.md` (+ `slug-map.yaml` for product aliases)
3. `<pack>/pfm-kb/modules|flows` for user-visible meaning
4. `<pack>/knowledge-base/data/` for tables
5. Skills (`global/skills/**` then pack overlay) — **procedure only**, never a substitute for missing pack facts
6. Graphify — discovery only; verify in source. Do not treat `graph.json` / cache as knowledge.

## Skills


Load `global/skills/**/<name>.skill.md` (segregated under `agents-md/`, `harness/`,
`roles/`, `engineering/`, `stack/`, `ai/`, `product/`), then overlay
`<pack>/skills/**/<name>.skill.md` if that stem exists. Search context loading is
`search/skills/CONTEXT_BUILDER.md` only. Lookup is by skill **name**, not folder.

## Hard rules

- Never invent product defaults when a P0 decision is missing. Ask, then stop.
- Never merge to `main`. Draft PRs only.
- Writes only under that pack’s `allowed_edit_paths`.
- Repair budget is the pack’s `max_repair_iterations` (cap 3).
- Graphify is discovery. `INFERRED` edges are hypotheses until verified in source.
- One Graphify server, one graph **per pack**. Never query Search and Radioly as one graph.

## Eval shape

Each eval has `id`, `requirement`, `expected`, and a mutation that can fail. Evals are
immutable during repair.

## After a run

Proven facts go into that pack’s `CONTRACT.md` / `contract.json`. Reusable learnings go into
that pack’s `knowledge-base/notes/solutions/`. Do not put Search cache lore (or Radioly feed
lore) in `global/`.
