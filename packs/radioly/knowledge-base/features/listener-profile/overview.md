# Listener profile

Aliases: profile, listener profile, user profile

Product context: `radioly/pfm-kb/modules/listener-profile.md`

## What it is

Public/private listener profile surfaces (not writer profile).

## Graph anchors

CODE SEARCH profile views under `v2/user_api/` / `v3/`. Distinct from `writer-profile`.


## Key product notes

The **person page**: name, photo, language, gender, bio, and (when
opened) that person’s titles. Edit is the same facts after first-run.

Not multi-profile (family slots), not community posts (community-updates),
not first-run name/gender/language screens (onboarding-first-run).

## Risks

- Mixing listener profile with writer/author profile.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "listener profile" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

